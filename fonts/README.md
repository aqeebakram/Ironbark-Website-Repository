# Self-hosted fonts

Copied unchanged from Google Fonts on 22 October 2026, Latin subset only (the
`/* latin */` files that `fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@300..700`
served). Self-hosted so first paint does not wait on a stylesheet from another
domain. The `@font-face` rules are inline in the `<head>` of every page, and the
Archivo and Inter files are preloaded.

| File | Family | Axes / weight |
|---|---|---|
| archivo-var-latin.woff2 | Archivo | wdth 62–125, wght 100–900 |
| inter-var-latin.woff2 | Inter | wght 300–700 |
| ibm-plex-mono-400-latin.woff2 | IBM Plex Mono | 400 |
| ibm-plex-mono-500-latin.woff2 | IBM Plex Mono | 500 |

All three families are under the SIL Open Font License 1.1, which allows
self-hosting. Characters outside the Latin range (the → ← ↗ arrows) were never in
these subsets and come from system fonts, as they did before.

New pages: copy the font block (preloads plus the inline `@font-face` style) from an existing page.
