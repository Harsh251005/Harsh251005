# Hi, I'm Harsh 👋

**Applied AI Engineer.** I build voice agents, RAG pipelines and multi-agent
systems, and I measure them until I can prove they work.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/harsh-dharnidharka/)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:dharnidharkaharsh@gmail.com)

Most agents can produce an answer. I care about the harder part: retrieving
the right information, refusing to act before the user confirms, and failing
loudly instead of silently. Rules that matter live in code, not in the
prompt, and every claim in my READMEs comes from a real evaluation run.

## Featured

### 🩺 [ClinicDesk](https://github.com/Harsh251005/clinic-voice-agent): a Hindi voice receptionist for Indian clinics

Patients call in Hindi or English (Hinglish works too) and it books, moves
and cancels appointments from the clinic's own data. The front desk runs its
day from a dashboard, and an admin panel shows each call's timings, vendor
errors and cost in rupees.

- Real-time voice on LiveKit, with swappable STT, LLM and TTS vendors (Sarvam, ElevenLabs, OpenAI)
- Booking is confirm-then-book, enforced in code: in live runs the model booked before the caller confirmed in 3 of 4 runs, so the tool now refuses until the caller has spoken after the read-back
- Double booking is impossible at the database level, even with two callers in the same second
- 520+ backend tests and 44 Playwright browser tests in CI, plus live evals graded by an LLM judge

`LiveKit` `FastAPI` `Postgres` `Next.js` `TypeScript` `Docker`

<table>
<tr>
<td width="50%" valign="top">

### 🔍 [Evident AI](https://github.com/Harsh251005/Evident-AI)

RAG over PDFs where every answer cites the page it came from.

- Hybrid retrieval: BM25 + dense + RRF, then cross-encoder reranking
- RAGAS faithfulness **0.975**, citation coverage **46/50** on a 50-question benchmark
- CI quality gate fails any build scoring below 0.80
- Latency cut by over 80%, from 40s+ to ~4–5s per query

`LangChain` `Qdrant` `RAGAS` `LangSmith` `Streamlit`

</td>
<td width="50%" valign="top">

### 🔥 [Phoenix AI](https://github.com/Harsh251005/PhoenixAI)

Describe an app in plain English, get a project that runs.

- LangGraph loop: coder → writer → executor → critic
- Failed runs go back to the coder with the real error, up to 5 fix attempts
- Generated code runs in Docker: no network, read-only root, non-root user
- CLI and FastAPI server, traced in LangSmith

`LangGraph` `OpenAI` `Docker` `FastAPI` `Pydantic`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 💳 [Payment Agent](https://github.com/Harsh251005/payment-agent)

A conversational agent that collects payments end to end.

- LLM extracts details with Structured Outputs; a deterministic state machine owns verification and payment
- Handles out-of-order answers, corrections and drip-fed details
- Strict identity checks with lockout after failed attempts
- Automated evaluation suite for edge cases

`OpenAI` `Structured Outputs` `Python`

</td>
<td width="50%" valign="top">

### 🕵️ [TruthLens AI](https://github.com/Harsh251005/TruthLens-AI)

Deepfake image detection, as an API and a mobile app.

- Deep-learning classifier plus EXIF metadata analysis
- LLM-written explanation of each verdict
- Batch scans, a real-vs-fake challenge and a deepfake news feed
- FastAPI + MySQL backend, Flutter app

`TensorFlow` `FastAPI` `Flutter` `MySQL`

</td>
</tr>
</table>

### More

- [**ApplyTrack AI**](https://github.com/Harsh251005/applytrack-ai): keeps my job-application sheet in sync with Gmail and auto-fills application forms (OpenAI Agents SDK, Playwright)
- [**Tabula AI**](https://github.com/Harsh251005/Tabula-AI): a supervisor agent with discovery and formula sub-agents that edit Google Sheets from plain English
- [**InsightForge**](https://github.com/Harsh251005/InsightForge): a LangGraph research agent that turns a question into a cited report
- [**Research Assistant**](https://github.com/Harsh251005/research-assistant): cited answers from research papers (Qdrant, FlashRank, Groq)
- [**MarketLens**](https://github.com/Harsh251005/market-lens): live NSE prices synced into Google Sheets, one tab per sector
- [**DSA**](https://github.com/Harsh251005/data-structures-and-algorithms): my structured path to interview-ready DSA in Python, with a tracker that enforces tests and spaced re-solves

## Stack

**AI:** LangGraph · LangChain · OpenAI API and Agents SDK · LiveKit Agents · RAGAS · LangSmith<br>
**Retrieval:** Qdrant · BM25 / hybrid search · cross-encoder reranking · sentence-transformers<br>
**Backend:** Python · FastAPI · Pydantic · Postgres · SQLAlchemy · Docker<br>
**Frontend:** Next.js · TypeScript · Streamlit · Flutter

## About

- 🎓 BSc IT, University of Mumbai (CGPI 8.68)
- 🥋 Gold medallist, National Karate Championship, representing Maharashtra
- 🔭 Now: taking ClinicDesk to phone calls and a pilot with a real clinic

<sub>Open to Applied AI Engineer roles at early-stage startups. The fastest way to reach me is email.</sub>
