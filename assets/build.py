"""Generates the profile README's header and project cards as SVGs.

Edit CARDS or the header text below, then run:  python3 assets/build.py
The images are dark by design, so they read the same on GitHub's light and
dark themes (theme-switching <picture> tags break side-by-side widths).
Phones get header-mobile.svg and the *-mobile.svg cards through <picture>; the cards and the wide header
also switch to a compact layout by themselves when drawn small.
"""

import math
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

THEME = {
    "bg": "#0d1117", "panel": "#161b22", "line": "#30363d",
    "text": "#e6edf3", "muted": "#8b949e", "accent": "#f5a524", "accent2": "#ff7a45",
}

CARDS = [
    {
        "file": "card-clinicdesk",
        "kicker": "VOICE AGENT",
        "name": "ClinicDesk",
        "line": "A Hindi voice receptionist for Indian clinics",
        "tiles": [
            ("~650ms", "p50 voice-to-voice"),
            ("520+", "backend tests"),
            ("44", "Playwright browser tests"),
            ("0", "audio recordings stored"),
        ],
        "proof": "Books only after the caller says yes, and the code enforces it, not the prompt.",
        "stack": "LiveKit · FastAPI · Postgres · Next.js",
    },
    {
        "file": "card-evident",
        "kicker": "RAG",
        "name": "Evident AI",
        "line": "Answers over PDFs that cite the page they came from",
        "tiles": [
            ("0.975", "faithfulness (RAGAS)"),
            ("46/50", "questions with grounded citations"),
            ("0.900", "context recall"),
            ("0.865", "composite; CI gate is 0.80"),
        ],
        "proof": "Every claim cites its page, and CI fails any build below 0.80. Scored on a 50-question golden set.",
        "stack": "Qdrant · BM25 + dense · RAGAS",
    },
]


ANIMATION = """
    .bar { transform-box: fill-box; transform-origin: center; animation: talk 1.4s ease-in-out infinite; }
    @keyframes talk { 0%, 100% { transform: scaleY(1); } 50% { transform: scaleY(0.35); } }
    .cursor { animation: blink 1.1s steps(1) infinite; }
    @keyframes blink { 50% { opacity: 0; } }
    @media (prefers-reduced-motion: reduce) { .bar, .cursor { animation: none; } }"""

# An SVG's media queries measure the size the image is drawn at, not the
# screen. Below this width (in CSS px) the header switches to a compact
# layout with less text, set larger.
HEADER_COMPACT_BELOW = 560


def waveform(t: dict, n: int, x0: float, gap: float, w: float, cy: float, amp: float) -> str:
    """Animated bars with a speech-like envelope: louder in the middle, uneven bar to bar."""
    bars = []
    for i in range(n):
        env = math.sin(math.pi * (i + 0.5) / n)
        h = amp * 0.2 + amp * env * (0.55 + 0.45 * abs(math.sin(i * 1.7)))
        delay = (i * 0.07) % 1.4
        color = t["accent"] if i % 7 else t["accent2"]
        bars.append(
            f'<rect class="bar" x="{x0 + i * gap:.1f}" y="{cy - h / 2:.1f}" width="{w}" height="{h:.1f}" rx="{w / 2}" '
            f'fill="{color}" style="animation-delay:-{delay:.2f}s"/>'
        )
    return "".join(bars)


def tagline_end(t: dict) -> str:
    accent = t["accent"]
    return f'I build the system around them<tspan fill="{accent}">.</tspan><tspan class="cursor" fill="{accent}"> ▍</tspan>'


def header(t: dict) -> str:
    """1000x260 banner: an animated voice waveform beside the name.

    When drawn narrower than HEADER_COMPACT_BELOW px it drops the waveform and
    sets the name and tagline larger, across the full width."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="260" viewBox="0 0 1000 260" role="img" aria-label="Harsh Dharnidharka, Applied AI Engineer. Prompts are a draft. I build the system around them.">
  <style>{ANIMATION}
    .compact {{ display: none; }}
    @media (max-width: {HEADER_COMPACT_BELOW}px) {{ .full {{ display: none; }} .compact {{ display: inline; }} }}
  </style>
  <rect x="0.5" y="0.5" width="999" height="259" rx="16" fill="{t['bg']}" stroke="{t['line']}"/>
  <g class="full">
    {waveform(t, 30, 64, 10, 5, 130, 90)}
    <line x1="390" y1="56" x2="390" y2="204" stroke="{t['line']}"/>
    <text x="426" y="78" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{t['muted']}">APPLIED AI ENGINEER · MUMBAI</text>
    <text x="424" y="132" font-family="{SANS}" font-size="46" font-weight="700" fill="{t['text']}">Harsh Dharnidharka</text>
    <text x="426" y="172" font-family="{SANS}" font-size="20" fill="{t['muted']}">Prompts are a draft.</text>
    <text x="426" y="200" font-family="{SANS}" font-size="20" fill="{t['muted']}">{tagline_end(t)}</text>
  </g>
  <g class="compact">
    {waveform(t, 16, 60, 14, 7, 52, 34)}
    <text x="58" y="138" font-family="{SANS}" font-size="78" font-weight="700" fill="{t['text']}">Harsh Dharnidharka</text>
    <text x="60" y="190" font-family="{SANS}" font-size="38" fill="{t['muted']}">Prompts are a draft.</text>
    <text x="60" y="234" font-family="{SANS}" font-size="38" fill="{t['muted']}">{tagline_end(t)}</text>
  </g>
</svg>
"""


def header_mobile(t: dict) -> str:
    """600x440 stacked banner, served to phones through <picture>."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="600" height="440" viewBox="0 0 600 440" role="img" aria-label="Harsh Dharnidharka, Applied AI Engineer. Prompts are a draft. I build the system around them.">
  <style>{ANIMATION}</style>
  <rect x="0.5" y="0.5" width="599" height="439" rx="20" fill="{t['bg']}" stroke="{t['line']}"/>
  {waveform(t, 30, 52, 17, 8, 112, 120)}
  <text x="50" y="236" font-family="{MONO}" font-size="18" letter-spacing="3.5" fill="{t['muted']}">APPLIED AI ENGINEER · MUMBAI</text>
  <text x="48" y="296" font-family="{SANS}" font-size="48" font-weight="700" fill="{t['text']}">Harsh Dharnidharka</text>
  <text x="50" y="350" font-family="{SANS}" font-size="30" fill="{t['muted']}">Prompts are a draft.</text>
  <text x="50" y="390" font-family="{SANS}" font-size="30" fill="{t['muted']}">{tagline_end(t)}</text>
</svg>
"""


def card(c: dict, t: dict) -> str:
    """1000x350 full-width project card: name, four numbers, the one fact that proves it."""
    tiles = []
    for i, (big, label) in enumerate(c["tiles"]):
        x = 32 + i * 236
        rows = "".join(
            f'<text x="{x}" y="{256 + j * 20}" font-family="{MONO}" font-size="14" fill="{t["muted"]}">{escape(part)}</text>'
            for j, part in enumerate(textwrap.wrap(label, 24))
        )
        divider = f'<line x1="{x - 24}" y1="178" x2="{x - 24}" y2="278" stroke="{t["line"]}"/>' if i else ""
        tiles.append(
            f'{divider}<text x="{x}" y="226" font-family="{SANS}" font-size="52" font-weight="700" fill="{t["accent"]}">{escape(big)}</text>{rows}'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="350" viewBox="0 0 1000 350" role="img" aria-label="{escape(c['name'])}: {escape(c['line'])}">
  <rect x="0.5" y="0.5" width="999" height="349" rx="16" fill="{t['panel']}" stroke="{t['line']}"/>
  <circle cx="38" cy="44" r="4" fill="{t['accent']}"/>
  <text x="52" y="49" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{t['accent']}">{escape(c['kicker'])}</text>
  <text x="968" y="49" text-anchor="end" font-family="{MONO}" font-size="13" fill="{t['muted']}">{escape(c['stack'])}</text>
  <text x="32" y="102" font-family="{SANS}" font-size="40" font-weight="700" fill="{t['text']}">{escape(c['name'])}</text>
  <text x="32" y="134" font-family="{SANS}" font-size="19" fill="{t['muted']}">{escape(c['line'])}</text>
  <line x1="32" y1="158" x2="968" y2="158" stroke="{t['line']}"/>
  {"".join(tiles)}
  <line x1="32" y1="298" x2="968" y2="298" stroke="{t['line']}"/>
  <text x="32" y="329" font-family="{SANS}" font-size="16" fill="{t['text']}">{escape(c['proof'])}</text>
</svg>
"""


def card_mobile(c: dict, t: dict) -> str:
    """600-wide portrait card for phones, served through <picture>: same content,
    numbers in a stacked list and text sized to stay readable at ~60% scale."""

    def lines(text: str, width: int, x: int, y: int, step: int, size: int, fill: str, family: str = SANS) -> str:
        return "".join(
            f'<text x="{x}" y="{y + i * step}" font-family="{family}" font-size="{size}" fill="{fill}">{escape(part)}</text>'
            for i, part in enumerate(textwrap.wrap(text, width))
        )

    tiles = []
    for i, (big, label) in enumerate(c["tiles"]):
        top = 244 + i * 104
        label_rows = textwrap.wrap(label, 20)
        first = top + 54 - (len(label_rows) - 1) * 14
        tiles.append(
            f'<line x1="36" y1="{top}" x2="564" y2="{top}" stroke="{t["line"]}"/>'
            f'<text x="34" y="{top + 72}" font-family="{SANS}" font-size="64" font-weight="700" fill="{t["accent"]}">{escape(big)}</text>'
            + lines(label, 20, 300, first, 28, 22, t["muted"], MONO)
        )
    proof_rows = textwrap.wrap(c["proof"], 38)
    proof_y = 712
    stack_y = proof_y + len(proof_rows) * 34 + 18
    height = stack_y + 40
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="600" height="{height}" viewBox="0 0 600 {height}" role="img" aria-label="{escape(c['name'])}: {escape(c['line'])}">
  <rect x="1" y="1" width="598" height="{height - 2}" rx="24" fill="{t['panel']}" stroke="{t['line']}" stroke-width="2"/>
  <circle cx="44" cy="54" r="7" fill="{t['accent']}"/>
  <text x="62" y="62" font-family="{MONO}" font-size="22" letter-spacing="3" fill="{t['accent']}">{escape(c['kicker'])}</text>
  <text x="34" y="132" font-family="{SANS}" font-size="60" font-weight="700" fill="{t['text']}">{escape(c['name'])}</text>
  {lines(c['line'], 34, 36, 176, 34, 26, t['muted'])}
  <line x1="36" y1="244" x2="564" y2="244" stroke="{t['line']}" stroke-width="2"/>
  {"".join(tiles)}
  <line x1="36" y1="660" x2="564" y2="660" stroke="{t['line']}" stroke-width="2"/>
  {lines(c['proof'], 38, 36, proof_y, 34, 26, t['text'])}
  <text x="36" y="{stack_y}" font-family="{MONO}" font-size="20" fill="{t['muted']}">{escape(c['stack'])}</text>
</svg>
"""


if __name__ == "__main__":
    (OUT / "header.svg").write_text(header(THEME), encoding="utf-8")
    (OUT / "header-mobile.svg").write_text(header_mobile(THEME), encoding="utf-8")
    for c in CARDS:
        (OUT / f"{c['file']}.svg").write_text(card(c, THEME), encoding="utf-8")
        (OUT / f"{c['file']}-mobile.svg").write_text(card_mobile(c, THEME), encoding="utf-8")
    print(f"wrote {2 + 2 * len(CARDS)} SVGs to {OUT}")
