import logging
from agents.research_agent import research_ads
from agents.analysis_agent import analyze_ads
from agents.script_agent import generate_script
from agents.video_agent import create_video

logging.basicConfig(level=logging.INFO)

def run_pipeline():
    try:
        logging.info("Step 1: Research Ads")
        ads = research_ads()

        logging.info("Step 2: Analyze Ads")
        insights = analyze_ads(ads)

        logging.info("Step 3: Generate Script")
        script = generate_script(insights)

        logging.info("Step 4: Create Video")
        create_video(script)

        logging.info("Pipeline Completed Successfully!")

    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    run_pipeline()
