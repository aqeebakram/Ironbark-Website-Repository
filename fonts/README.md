# Self-hosted fonts

Copied unchanged from Google Fonts, Latin subset only (the `/* latin */` files that
`fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900` served on
22 October 2026, and `family=Poppins:wght@400;500;600` on 30 October 2026).
Self-hosted so first paint does not wait on a stylesheet from another domain. The
`@font-face` rules are inline in the `<head>` of every page, and Archivo and
Poppins 400 are preloaded.

| File | Family | Axes / weight |
|---|---|---|
| archivo-var-latin.woff2 | Archivo | wdth 62–125, wght 100–900 |
| poppins-400-latin.woff2 | Poppins | 400 |
| poppins-500-latin.woff2 | Poppins | 500 |
| poppins-600-latin.woff2 | Poppins | 600 |

Archivo sets headings and the wordmark. Poppins sets everything else: body text,
buttons, the menu, labels, captions, forms. Inter and IBM Plex Mono were retired on
30 October 2026; `--f-mono` now points at the body font, so old rules still resolve.
A request for weight 700 in Poppins falls to 600, which is the heaviest face shipped.

Both families are under the SIL Open Font License 1.1, which allows self-hosting.
Characters outside the Latin range (the → ← ↗ arrows) are not in these subsets and
come from system fonts.

New pages: copy the font block (preloads plus the inline `@font-face` style) from an existing page.
