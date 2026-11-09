# Brand → Flutter theme

Sources: W3C DTCG format 2025.10 (stable 28 Oct 2025), Flutter API docs (ColorScheme.fromSeed, DynamicSchemeVariant), Flutter blog 9 Sep 2026 (material_ui / cupertino_ui decoupling), WCAG 2.2, Apple HIG app icons, Android adaptive icons, Linear UI redesign. Full research report: `docs/research.md`.

## 1. Tokens (DTCG format)

Store the identity's constants once, as `brand.tokens.json` — vendor-neutral, importable by Figma plugins / Style Dictionary, readable by a small Dart codegen.

```json
{
  "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
  "color": {
    "brand": {
      "seed":   { "$type": "color", "$value": { "colorSpace": "srgb", "components": [0.0549, 0.4863, 0.4], "hex": "#0E7C66" } },
      "exact":  { "$type": "color", "$value": "{color.brand.seed}", "$description": "Use where the exact brand hex is mandatory" },
      "accent": { "$type": "color", "$value": { "colorSpace": "srgb", "components": [0.949, 0.702, 0.2392], "hex": "#F2B33D" } }
    },
    "neutral": {
      "900": { "$type": "color", "$value": { "colorSpace": "srgb", "components": [0.0706, 0.0863, 0.0784], "hex": "#121614" } },
      "50":  { "$type": "color", "$value": { "colorSpace": "srgb", "components": [0.9647, 0.9725, 0.9686], "hex": "#F6F8F7" } }
    }
  },
  "font": {
    "display": { "$type": "fontFamily", "$value": ["Space Grotesk", "sans-serif"] },
    "text":    { "$type": "fontFamily", "$value": ["Inter", "sans-serif"] }
  },
  "space":  { "1": { "$type": "dimension", "$value": { "value": 4, "unit": "px" } },
              "2": { "$type": "dimension", "$value": { "value": 8, "unit": "px" } } },
  "radius": { "brand": { "$type": "dimension", "$value": { "value": 12, "unit": "px" } } },
  "motion": { "standard": { "$type": "duration", "$value": { "value": 220, "unit": "ms" } } },
  "button": { "primary": { "bg": { "$type": "color", "$value": "{color.brand.exact}" } } }
}
```

Rules (DTCG Format + Color Modules 2025.10):
- every token has `$value` + `$type`; aliases use `{group.token}`;
- **colour values are objects**, not hex strings: `colorSpace` + `components` (0–1 for srgb), optional `alpha` (0–1) and `hex` (fallback for tools). Compute components as channel/255, 4 decimals;
- dimensions/durations are objects: `{ "value": 4, "unit": "px" }`, `{ "value": 220, "unit": "ms" }`;
- keep a separate `exact` token because the seed may not survive scheme generation.
Mirror the tokens in Dart as a `BrandTokens` class of `static const` values (use the hex for `Color(0xFF……)`).

## 2. ColorScheme

```dart
// Prefer package:material_ui (Material moved out of the framework, Sep 2026; `dart fix` migrates).
ColorScheme brandScheme(Brightness b, {double contrast = 0.0}) =>
    ColorScheme.fromSeed(
      seedColor: BrandTokens.seed,
      brightness: b,
      dynamicSchemeVariant: DynamicSchemeVariant.fidelity,
      contrastLevel: contrast, // -1.0..1.0; 1.0 = high-contrast theme
    ); // .copyWith(primary: BrandTokens.exact) only if the exact hex is mandatory — then re-check contrast of onPrimary

ThemeData brandTheme(Brightness b, {double contrast = 0}) {
  final scheme = brandScheme(b, contrast: contrast);
  return ThemeData(
    colorScheme: scheme,
    textTheme: /* display + text families from tokens */,
    // shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(BrandTokens.radius)) in component themes
  );
}
```

### Variant = brand decision

| Personality (from sliders) | Variant | Effect |
|---|---|---|
| Bold, loud, brand-colour-led | `fidelity` or `content` | stays close to the seed |
| Playful, energetic | `vibrant` | max chroma |
| Calm, trustworthy, utility | `tonalSpot` (default) | low-chroma pastels — washes out bold brands |
| Experimental | `expressive` | shifts hue away from seed |
| Minimal / editorial | `monochrome` / `neutral` | near-greyscale |

Linear's lesson: aim for **few inputs** (base, accent, contrast) generating the whole theme, not 98 hand-tuned colours.

### After generating — fix what the generator gets wrong

- **Tinted surfaces:** `fromSeed` tints `surface`, `surfaceContainer*` and `background` with the seed hue (a yellow seed gives cream). If the brand wants clean neutrals, `copyWith` those roles from the neutral tokens.
- **Very light / very saturated brand colours** (yellow, lime, cyan, light orange): they fail as text on white (e.g. #FFC300 on white = 1.6:1). Use them as **fills with dark ink on top** (primary button, FAB, selected indicator). In light mode, make the *text/line-level* primary dark (ink or a deep shade of the hue, e.g. amber #7A5900), and put the bright colour in `primaryContainer`/a `BrandColors` ThemeExtension. In dark mode the bright colour can be `primary` directly.
- **When to hand-build roles instead of `fromSeed`:** if after `fidelity` + overrides you're replacing most roles anyway, build the `ColorScheme(...)` explicitly from tokens — it's clearer. Either is fine; what matters is the verified result.
- **Semantic clashes:** if the brand is yellow/orange, make warning a clearly different hue; if green, keep success distinct (or reserve brand green for "verified").

Provide: light, dark, and high-contrast (contrastLevel 1.0) themes. Wire `ThemeMode.system` and an in-app override.

## 3. Contrast checks

Run `python3 scripts/contrast_check.py` on the real role pairs for **both** brightnesses:
- body text: `onSurface/surface`, `onPrimary/primary`, `onPrimaryContainer/primaryContainer`, `onSecondary/secondary`, `onError/error`
- ≥ **4.5:1** normal text, ≥ **3:1** large text (≥18.66 px bold / 24 px), UI components, icons, focus rings.
- Logos are exempt; the UI around them isn't. APCA is not a current standard — don't use it as the compliance bar.

Check the **generated** scheme, not only the brand hexes — `fromSeed` output differs from the seed. When Flutter is available:

1. Create a scratch project outside the user's repo (`flutter create --empty /path/to/scratchpad/theme_check`), drop the theme files in `lib/`.
2. Add a contrast test that walks the real role pairs for every theme (light, dark, high-contrast):

```dart
double _lum(Color c) {
  double ch(double v) => v <= 0.04045 ? v / 12.92 : math.pow((v + 0.055) / 1.055, 2.4).toDouble();
  return 0.2126 * ch(c.r) + 0.7152 * ch(c.g) + 0.0722 * ch(c.b);
}
double ratio(Color a, Color b) {
  final l1 = _lum(a), l2 = _lum(b);
  return (math.max(l1, l2) + 0.05) / (math.min(l1, l2) + 0.05);
}
// for each theme: expect(ratio(s.onPrimary, s.primary), greaterThanOrEqualTo(4.5)); … onSurface/surface,
// onPrimaryContainer/primaryContainer, onSecondary/secondary, onError/error, primary/surface (3.0 for UI)
```

3. Run `flutter analyze` and `flutter test`; report results and the 2–3 tightest ratios.

Without Flutter, print colours from reasoning only as a last resort and say they're unverified; `scripts/contrast_check.py` still covers the brand-level pairs.

## 4. Typography

- `google_fonts` package is convenient but fetches at runtime by default — bundle the font files as assets for production/offline (and ask before adding the dependency).
- Urdu/Arabic UI: use Noto Nastaliq Urdu (display/reading) or Noto Naskh Arabic (UI density); increase line height (~1.6–1.8) and test RTL layouts.

## 5. App icon

- **iOS:** layered artwork (1024×1024 background + foreground layers) built in **Icon Composer**; six appearances — default, dark, clear light, clear dark, tinted light, tinted dark. Prefer vector layers; avoid thin lines and baked-in shadows/gloss (the system adds Liquid Glass effects).
- **Android adaptive:** 108 dp foreground, background and **monochrome** layers; keep the logo inside the central **66 dp** safe zone. Since Android 16 QPR2 the system auto-themes icons that lack a monochrome layer — supply your own.
- Start from the one-colour silhouette of the mark; that single asset feeds monochrome, tinted, notification icon (Android: white-on-transparent) and favicon.
- `flutter_launcher_icons` can generate platform sets (new dependency → ask first); Icon Composer output is added in Xcode.
- Test the icon at real size on light, dark and busy wallpapers next to competitors' icons.
