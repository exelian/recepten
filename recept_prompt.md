Zet de bovenstaande conversatie om in een praktisch kookrecept.

Geef uitsluitend de ruwe Markdown-broncode van het recept, zodat ik die direct kan kopiëren naar een `.md`-bestand.

BELANGRIJK:
- Zet het volledige recept in één Markdown-codeblok met taalmarkering `markdown`.
- Render de Markdown niet buiten het codeblok.
- Voeg geen inleiding, toelichting of tekst buiten het codeblok toe.
- De inhoud van het codeblok moet direct bruikbare, geldige Markdown zijn.
- Het recept moet beginnen met de onderstaande YAML frontmatter.
- Neem de frontmatter exact over. Als informatie voor een veld niet uit de conversatie blijkt, laat de waarde leeg.
- Baseer je uitsluitend op de bovenstaande conversatie. Vul niets zelf in.

Vereiste structuur:

---
bereidingstijd: [waarde of leeg]
porties: [waarde of leeg]
categorieën: [waarde of leeg]
---

# [Naam van het recept]

## Ingrediënten
- [exacte hoeveelheid in metrische eenheid] [ingrediënt]
- [exacte hoeveelheid in metrische eenheid] [ingrediënt]

## Bereiding
1. [Concrete bereidingsstap.]
2. [Concrete bereidingsstap.]
3. [Concrete bereidingsstap.]

## Optioneel
### Alternatieven
- [Alleen indien logisch en gebaseerd op de conversatie.]

### Tips
- [Alleen praktisch relevante tips uit de conversatie.]

### Regels voor Ingrediënten
- De sectie `## Ingrediënten` bevat uitsluitend een lijst van ingrediënten met hun hoeveelheden.
- Gebruik altijd de volgorde: `<hoeveelheid> <ingrediënt>`.
- Voorbeelden:
  - `2 el olijfolie`
  - `250 g aubergine`
  - `1 rode ui`
  - `½ tl chilivlokken`
- Beschrijf in deze sectie nooit hoe een ingrediënt moet worden bereid, gesneden, geraspt, gehakt, gekookt, gebakken, gemengd, etc.
- Bereidingsinstructies voor ingrediënten mogen uitsluitend in de sectie `## Bereiding` staan.
- Schrijf bijvoorbeeld `10 g peterselie`, niet `10 g fijngehakte peterselie`.
- Vermeld een hoeveelheid alleen als die uit de conversatie blijkt.
- Gebruik metrische eenheden

### Regels voor Bereiding
- De bereiding is concreet, chronologisch en genummerd.
- Iedere stap beschrijft één duidelijke handeling of een logisch samenhangend groepje handelingen.
- Combineer geen ongerelateerde handelingen in één stap.
- Handelingen die hetzelfde doel hebben mogen wel worden gecombineerd.
- Goed: `Snijd de peterselie en munt fijn.`
- Niet goed: `Snijd de munt en verwarm de oven voor.`
- Houd voorbereidende handelingen en kookhandelingen als afzonderlijke stappen wanneer ze niet direct bij elkaar horen.
- Verwerk alle instructies voor het bereiden van ingrediënten hier, en nergens anders.

### Vetgedrukte waarden in Bereiding
Maak in de sectie `## Bereiding` de volgende elementen altijd vetgedrukt:
- Tijden: bijvoorbeeld `**10 minuten**`, `**5 min**`
- Gewichten: bijvoorbeeld `**250 g**`, `**1 kg**`
- Hoeveelheden: bijvoorbeeld `**2 el**`, `**1 tl**`, `**½ liter**`, `**3 stuks**`

Maak alleen de betreffende waarde vetgedrukt, niet automatisch de volledige zin.

### Algemene regels
- Neem uitsluitend informatie over die uit de bovenstaande conversatie blijkt.
- Voeg geen ingrediënten, hoeveelheden, bereidingswijzen, tijden, temperaturen, porties, categorieën, alternatieven, tips of andere details toe die niet uit de conversatie blijken.
- Als informatie voor de frontmatter niet bekend is, laat het betreffende veld leeg.
- Als een receptnaam niet expliciet bekend is maar wel ondubbelzinnig uit de conversatie blijkt, gebruik die naam.
- Als informatie niet bekend is en niet noodzakelijk is voor de structuur, hoef je niet te vermelden dat deze ontbreekt.
- Taal: Nederlands.
- Geen tekst buiten het Markdown-codeblok.