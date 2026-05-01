# CrowdWisdomTrading AI Ads Agent

## Overview
AI agents pipeline to research, analyze, and generate animated video ads for CrowdWisdomTrading.

## Project Structure
```
crowdwisdom-ai-agent/
├── agents/                # AI agent implementations
│   ├── research_agent.py   # Researches ads via Apify
│   ├── analysis_agent.py   # Analyzes ads for insights
│   ├── script_agent.py     # Generates ad scripts
│   └── video_agent.py      # Creates Remotion video project
├── tools/                 # Helper tools
│   ├── apify_tool.py       # Apify integration
│   ├── gdrive_tool.py      # GDrive data fetching (simulated)
│   └── llm.py              # OpenRouter LLM integration
├── remotion/              # Remotion video project
│   └── src/
├── outputs/               # Generated files
│   ├── ads.json
│   ├── insights.txt
│   ├── script.txt
│   └── final_video.txt
├── requirements.txt       # Python dependencies
└── main.py                # Main pipeline
```

## Setup
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. (Optional) Set up environment variables in `.env`:
   ```
   OPENROUTER_API_KEY=your_key_here
   APIFY_API_TOKEN=your_token_here
   ```

## Run
1. Run the AI pipeline:
   ```bash
   python main.py
   ```

2. Run Remotion video project:
   ```bash
   cd remotion
   npm install
   npx remotion studio src/index.tsx
   ```

## Features
- **Research Agent**: Fetches Meta Ads via Apify (with fallback data)
- **Analysis Agent**: Extracts pain points, hooks, and CTAs from ads
- **Script Agent**: Generates 60-second ad scripts
- **Video Agent**: Creates complete Remotion video project
- **Animated Ad**: Fade-in, scale-in animations, gradient backgrounds, and glow effects
- **Clear Structure**: Hook → Pain → Solution → CTA
- **Error Handling**: Graceful degradation with fallback data

## Ad Features (Remotion)
- 🎬 Animated sections with fade-in and scale-in effects
- 🌈 Gradient background with pulsing glow effects
- 📊 Clear 4-part structure: Hook → Pain → Solution → CTA
- 🎨 Professional styling with glowing text and buttons

## Notes
- The current .env includes test API keys (may need to be replaced for production use)
- Remotion project requires Node.js and npm to run
- To add voiceover: Use ElevenLabs to generate audio, place in remotion/public/, and use <Audio> component
