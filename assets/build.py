"""Generates the profile README's header and project cards as SVGs.

Edit CARDS or the header text below, then run:  python3 assets/build.py
The images are dark by design, so they read the same on GitHub's light and
dark themes (theme-switching <picture> tags break side-by-side widths).
"""

import math
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
        "proof": ("Books only after the caller says yes,", "and the code enforces it, not the prompt."),
        "metric": ("520+", "backend tests"),
        "stack": "LiveKit · FastAPI · Postgres · Next.js",
    },
    {
        "file": "card-evident",
        "kicker": "RAG",
        "name": "Evident AI",
        "line": "Answers over PDFs that cite the page they came from",
        "proof": ("Every claim cites its page; CI fails", "any build that scores below 0.80."),
        "metric": ("0.975", "faithfulness"),
        "stack": "Qdrant · BM25 + dense · RAGAS",
    },
    {
        "file": "card-phoenix",
        "kicker": "MULTI-AGENT",
        "name": "Phoenix AI",
        "line": "Describe an app in English, get a project that runs",
        "proof": ("Writes, runs, critiques, fixes,", "in a network-less Docker sandbox."),
        "metric": ("5×", "self-repair loops"),
        "stack": "LangGraph · Docker · FastAPI",
    },
    {
        "file": "card-payment",
        "kicker": "CONVERSATIONAL AI",
        "name": "Payment Agent",
        "line": "Collects a payment end to end, in conversation",
        "proof": ("The LLM understands the customer;", "a state machine makes every decision."),
        "metric": ("9", "eval scenarios"),
        "stack": "OpenAI Structured Outputs · Python",
    },
]


def header(t: dict) -> str:
    """1000x260 banner: an animated voice waveform beside the name."""
    bars = []
    n, x0, gap, w = 30, 64, 10, 5
    for i in range(n):
        # A speech-like envelope: louder in the middle, uneven from bar to bar.
        env = math.sin(math.pi * (i + 0.5) / n)
        h = 18 + 90 * env * (0.55 + 0.45 * abs(math.sin(i * 1.7)))
        x = x0 + i * gap
        delay = (i * 0.07) % 1.4
        color = t["accent"] if i % 7 else t["accent2"]
        bars.append(
            f'<rect class="bar" x="{x}" y="{130 - h / 2:.1f}" width="{w}" height="{h:.1f}" rx="2.5" '
            f'fill="{color}" style="animation-delay:-{delay:.2f}s"/>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="260" viewBox="0 0 1000 260" role="img" aria-label="Harsh Dharnidharka, Applied AI Engineer">
  <style>
    .bar {{ transform-box: fill-box; transform-origin: center; animation: talk 1.4s ease-in-out infinite; }}
    @keyframes talk {{ 0%, 100% {{ transform: scaleY(1); }} 50% {{ transform: scaleY(0.35); }} }}
    .cursor {{ animation: blink 1.1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .bar, .cursor {{ animation: none; }} }}
  </style>
  <rect x="0.5" y="0.5" width="999" height="259" rx="16" fill="{t['bg']}" stroke="{t['line']}"/>
  {''.join(bars)}
  <line x1="390" y1="56" x2="390" y2="204" stroke="{t['line']}"/>
  <text x="426" y="78" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{t['muted']}">APPLIED AI ENGINEER · MUMBAI</text>
  <text x="424" y="132" font-family="{SANS}" font-size="46" font-weight="700" fill="{t['text']}">Harsh Dharnidharka</text>
  <text x="426" y="172" font-family="{SANS}" font-size="20" fill="{t['muted']}">Prompts are a draft.</text>
  <text x="426" y="200" font-family="{SANS}" font-size="20" fill="{t['muted']}">I build the system around them<tspan fill="{t['accent']}">.</tspan><tspan class="cursor" fill="{t['accent']}"> ▍</tspan></text>
</svg>
"""


def card(c: dict, t: dict) -> str:
    """480x230 project card: what it is, the one fact that proves it, the stack."""
    big, small = c["metric"]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="480" height="230" viewBox="0 0 480 230" role="img" aria-label="{escape(c['name'])}: {escape(c['line'])}">
  <rect x="0.5" y="0.5" width="479" height="229" rx="14" fill="{t['panel']}" stroke="{t['line']}"/>
  <circle cx="32" cy="36" r="3.5" fill="{t['accent']}"/>
  <text x="44" y="40" font-family="{MONO}" font-size="11" letter-spacing="2.5" fill="{t['accent']}">{escape(c['kicker'])}</text>
  <text x="28" y="72" font-family="{SANS}" font-size="26" font-weight="700" fill="{t['text']}">{escape(c['name'])}</text>
  <text x="28" y="100" font-family="{SANS}" font-size="15" fill="{t['muted']}">{escape(c['line'])}</text>
  <line x1="28" y1="122" x2="452" y2="122" stroke="{t['line']}"/>
  <text x="28" y="162" font-family="{SANS}" font-size="30" font-weight="700" fill="{t['text']}">{escape(big)}</text>
  <text x="28" y="182" font-family="{MONO}" font-size="11" fill="{t['muted']}">{escape(small)}</text>
  <text x="168" y="158" font-family="{SANS}" font-size="14" fill="{t['text']}">{escape(c['proof'][0])}</text>
  <text x="168" y="178" font-family="{SANS}" font-size="14" fill="{t['muted']}">{escape(c['proof'][1])}</text>
  <text x="28" y="212" font-family="{MONO}" font-size="11.5" fill="{t['muted']}">{escape(c['stack'])}</text>
</svg>
"""


if __name__ == "__main__":
    (OUT / "header.svg").write_text(header(THEME), encoding="utf-8")
    for c in CARDS:
        (OUT / f"{c['file']}.svg").write_text(card(c, THEME), encoding="utf-8")
    print(f"wrote {1 + len(CARDS)} SVGs to {OUT}")
