import os
import logging
from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

def fetch_ads(keyword="crowdwisdomtrading trading", max_items=20):
    try:
        logger.info(f"Fetching Meta Ads for keyword: {keyword}")
        
        run = client.actor("vdrmota/meta-ads-library-scraper").call(
            run_input={
                "searchTerms": [keyword],
                "country": "ALL",
                "activeStatus": "ACTIVE",
                "maxItems": max_items
            }
        )
        
        items = client.dataset(run["defaultDatasetId"]).list_items().items
        logger.info(f"Successfully fetched {len(items)} ads")
        return items
    except Exception as e:
        logger.error(f"Error fetching ads: {e}")
        # Return fallback data if Apify fails
        return [
            {
                "ad_archive_id": "fallback-1",
                "ad_snapshot_url": "https://example.com",
                "text": "Stop losing money in trading! Get AI-powered signals that actually work.",
                "cta_text": "Learn More",
                "landing_page_url": "https://crowdwisdomtrading.com"
            },
            {
                "ad_archive_id": "fallback-2",
                "ad_snapshot_url": "https://example.com",
                "text": "Tired of spending hours on chart analysis? Let our AI do the work for you.",
                "cta_text": "Get Started",
                "landing_page_url": "https://crowdwisdomtrading.com"
            }
        ]
