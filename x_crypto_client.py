"""
Python Client for JiStudio Twitter (X) Scraper & Crypto X-Intel on Apify Store
Actor: https://apify.com/jistudio/twitter-scraper
Get free token: https://console.apify.com/account/integrations
"""

import os
import requests

APIFY_TOKEN = os.environ.get("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ACTOR_SLUG = "jistudio~twitter-scraper"


def run_twitter_actor(payload: dict):
    url = f"https://api.apify.com/v2/acts/{ACTOR_SLUG}/run-sync-get-dataset-items"
    resp = requests.post(
        url,
        params={"token": APIFY_TOKEN, "clean": "true"},
        json=payload,
        timeout=90,
    )
    resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    # 1. Single Tweet Detail & HD Video
    tweet = run_twitter_actor({
        "action": "tweet",
        "tweetIdOrUrl": "https://x.com/solana/status/2125078025377378634",
    })
    print("Tweet:", tweet[:1])

    # 2. Latest KOL Timeline
    timeline = run_twitter_actor({
        "action": "timeline",
        "username": "solana",
        "maxItems": 10,
    })
    print("Timeline items:", len(timeline))

    # 3. Solana Token Contract -> Official X Intel
    intel = run_twitter_actor({
        "action": "token_x_intel",
        "contractAddress": "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263",
    })
    print("Token X-Intel:", intel[:1])
