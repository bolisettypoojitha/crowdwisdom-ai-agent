import json
from tools.apify_tool import fetch_ads

def research_ads():
    ads = fetch_ads("trading strategy")
    with open("outputs/ads.json", "w") as f:
        json.dump(ads, f, indent=2)
    return ads
