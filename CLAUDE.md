# Ironbark Advisory

Static HTML site for an independent international education advisory in Dubai.
Served by GitHub Pages from `main` at ironbarkadvisory.ae.

## Writing in Aqeeb's voice

Derived from his edits to draft copy. When a rule here conflicts with a
general instinct about good prose, this file wins.

**Name the mechanism, never reach for a metaphor.** "The most common
prerequisite", not "the most common hard gate". "Subject choices in Year 10
decide the degree choices you have", not "the decision that closes the door".
Doors, gates, forks and arcs all get cut.

**Never end on a flourish.** A neat inversion or a well turned closing line
gets deleted and replaced with the consequence spelled out. Draft: "Same
subject, same student, entirely different answer, and in most handbooks those
two words sit a line apart." His: "Same subject, same student, but different
outcomes." Explain what happens to the student instead of landing a line.

**Spell out the consequence.** Where a draft says a course "is closed", he
adds "and a student will be unable to apply if they have not studied this
subject previously". Where it says a subject will "be harder", he adds "to
understand the concepts and catch up to the rest of the class". Assume the
reader wants the mechanics, not the summary.

**Repeat the noun rather than use a pronoun.** "frequently require Chemistry
as a prerequisite", not "frequently require it outright". "the standard
mathematics does not substitute", not "the standard course". "open at another
university", not "open at another".

**Constructive, never accusatory.** He does not blame schools, counsellors or
parents. Draft: "nobody flags it at the time". His: "it is important to make
an informed choice". He works with these institutions; the copy never scores
points off them.

**End a section on what to do.** He replaces comparative judgements with
actions. Draft: "The hardest of the four to reverse, and the one taken
earliest." His: "It is almost impossible to reverse the decision once made
and important to understand the university requirements as early as Year 10."

**No emphatic fragments.** "Not a summary site, the university handbook." was
cut. Write it as a sentence or leave it out.

**Cut intensifiers.** "actually", "precisely", "genuinely", "entirely" mostly
come out.

**Year groups, not ages.** "after Year 9", not "at around fourteen". Write
them in full: Year 10, not Y10.

**Adds substance where a draft adds shape.** He deleted "Less of a single
fork, more of a slow narrowing" and added the SAT as an alternative entry
route. If a sentence is carrying rhythm rather than information, it goes.

### Habits to avoid, flagged in his own words as reading "very AI like"

- Mechanical triads. Three items because three scans well.
- Sentences engineered to land on a reversal.
- Uniformly even paragraph lengths.
- Abstractions where the concrete noun was available.
- A register more formal than he would use across a table from a parent.

### House conventions

Settled once, so they do not get relitigated:

- **prerequisite**, never pre-requisite.
- **Bengaluru**, not Bangalore. It is the official name.
- **Consuls-General** is the plural, not Consul-Generals.
- **alternative**, not alternate, when the meaning is "a different option".
- **program**, not programme. Applied across the whole site.
- **Founder**, not Founder & CEO. Ironbark is founder led and deliberately
  small, and CEO of a practice of one reads against that.
- **Sentence case** for labels, card titles and lists. Not Title Case.
- Currency is **AUD 2,500**, not AUD $2,500. The code already names the
  currency, so the dollar sign repeats it.
- Numbers under a hundred are **spelled out**: twelve years, not 12 years.
  Where the same figure recurs on a page, vary the sentence rather than
  repeat it identically.

### Do not write about commissions

Nothing on the site says how Ironbark is or is not paid. No "no provider
commissions", no "none of them pay me", no claim that the advice is
unshaped by who pays. The business model may change and the copy should
not have to be retracted. Independence can be shown by what the advice
actually does, not asserted as a payment arrangement.

### Standing accuracy rule

Entry requirements vary by university and by state and change between
intakes. Never state a requirement for a named university as settled fact.
Frame with "commonly", "frequently", "at many universities", and keep the
instruction to check the current handbook for the specific course and intake.

Case studies are composites drawn from several families. The words
"composite, illustrative" stay on them.

### Figures that expire

The student visa application charge in `insights-cost-to-graduation.html`
is set by the Department of Home Affairs and reviewed annually. It is the
only hard government figure on the site and it goes stale on a schedule.
`immi.homeaffairs.gov.au` and `studyaustralia.gov.au` are both blocked by
the network policy in Claude sessions, so the figure cannot be verified
from here. Aqeeb supplies it.

### Search indexing is settled

The site is fully indexed. Sixteen of eighteen pages were in within about
three weeks of the sitemap going live, including all eight city pages.
Slow indexing on this domain has been a queue every single time, never a
fault. Do not diagnose it as a content or linking problem again.

The constraint now is inbound links, of which there are none, and content
that targets queries families actually type. Technical SEO work has no
remaining return.

## Images

Photographs arrive as full size JPEGs uploaded through the GitHub web
interface. Convert them with Pillow, never ship the originals:

- Inline article images: 3:2, 1200 wide, WebP quality 80, into `img/dest/`
- News index feature card: 4:5, 900x1124. Where a piece covers several
  countries, build a two by two quad from the four so no single image
  implies one country
- Social card: 1200x630, JPEG rather than WebP, because scraper support
  for WebP is inconsistent

Every image carries explicit width and height plus `loading="lazy"`, so
nothing shifts while the page loads. Delete the source JPEGs from the
working tree once converted.

## Adding a page

Drop the `.html` file in the repository root and link to it. `sitemap.xml`
rebuilds itself on push to `main`, so there is nothing to update by hand.

While a page is still rough, keep it out of Google:

    <meta name="robots" content="noindex, follow">

The sitemap skips any page carrying that tag. Swap it for the indexable
version once the content is finished:

    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">

Every page needs exactly one doctype and one `<html lang="en">` element, plus
a `<title>`, a `<meta name="description">` and a `<link rel="canonical">`
pointing at its own URL. New pages are assembled from the shared chrome in an
existing page; that chrome already opens the document, so do not add a second
doctype.

To rebuild the sitemap locally: `python3 scripts/build-sitemap.py`
