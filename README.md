Website for my business.

Static HTML, served by GitHub Pages from `main` at ironbarkadvisory.ae.

## Adding a page

Drop the `.html` file in the repository root and link to it. `sitemap.xml`
rebuilds itself on push to `main`, so there is nothing to update by hand.

While a page is still rough, keep it out of Google:

    <meta name="robots" content="noindex, follow">

The sitemap skips any page carrying that tag. Swap it for the indexable
version once the content is finished:

    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">

Every page also needs a `<title>`, a `<meta name="description">` and a
`<link rel="canonical">` pointing at its own URL.

To rebuild the sitemap locally: `python3 scripts/build-sitemap.py`
