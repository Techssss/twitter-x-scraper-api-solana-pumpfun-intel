"""
Official Python SDK Client for Twitter (X) Real-Time Data & Crypto X-Intel API
==============================================================================
- Get your FREE Production API Key: https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel
- Run No-Code / Bulk on Apify Store: https://apify.com/nghianguyen2/twitter-x-tweet-scraper-solana-crypto
"""

import json
import os
import sys
import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAPIDAPI_HOST = "twitter-x-real-time-data-crypto-x-intel.p.rapidapi.com"
RAPIDAPI_URL = "https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel"
APIFY_URL = "https://apify.com/nghianguyen2/twitter-x-tweet-scraper-solana-crypto"


class XCryptoIntelClient:
    def __init__(self, rapidapi_key: str = ""):
        raw_key = (rapidapi_key or os.environ.get("RAPIDAPI_KEY", "")).strip()
        self.is_trial = (not raw_key) or raw_key.startswith("YOUR_")
        self.api_key = "" if self.is_trial else raw_key
        self.base_url = f"https://{RAPIDAPI_HOST}"

    def _fetch_json(self, url: str) -> dict:
        r = requests.get(
            url,
            headers={
                "Accept": "application/json",
                "User-Agent": "TelegramBot (like TwitterBot)",
            },
            timeout=12,
        )
        return r.json()

    def _trial_preview(self, path: str, params: dict) -> dict:
        notice = f"⚡ FREE DEMO PREVIEW (1 item) — Get your FREE Production Key for all 10 X & Crypto X-Intel endpoints at {RAPIDAPI_URL} or run on Apify: {APIFY_URL}"
        if "token-x-intel" in path or "crypto" in path:
            ca = params.get("ca") or "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263"
            dex = self._fetch_json(f"https://api.dexscreener.com/latest/dex/tokens/{ca}")
            pair = (dex.get("pairs") or [{}])[0]
            socials = (pair.get("info") or {}).get("socials") or []
            tw_url = next((s.get("url") for s in socials if s.get("type") == "twitter"), None)
            return {
                "ok": True,
                "_trial_notice": notice,
                "token": pair.get("baseToken"),
                "price_usd": pair.get("priceUsd"),
                "market_cap": pair.get("marketCap") or pair.get("fdv"),
                "official_twitter_url": tw_url,
            }
        uname = params.get("username") or "solana"
        fx = self._fetch_json(f"https://api.fxtwitter.com/{uname}")
        u = fx.get("user") or {}
        return {
            "ok": True,
            "_trial_notice": notice,
            "data": {
                "username": u.get("screen_name") or uname,
                "name": u.get("name"),
                "followers": u.get("followers"),
                "following": u.get("following"),
                "tweets_count": u.get("tweets"),
                "joined": u.get("joined"),
            },
        }

    def _get(self, path: str, params: dict) -> dict:
        if self.is_trial:
            return self._trial_preview(path, params)
        r = requests.get(
            f"{self.base_url}{path}",
            params=params,
            headers={
                "x-rapidapi-key": self.api_key,
                "x-rapidapi-host": RAPIDAPI_HOST,
                "Accept": "application/json",
            },
            timeout=15,
        )
        return r.json()

    def get_tweet(self, tweet_id_or_url: str) -> dict:
        return self._get("/api/v1/x/tweet", {"id": tweet_id_or_url})

    def get_user(self, username: str) -> dict:
        return self._get("/api/v1/x/user", {"username": username})

    def get_timeline(self, username: str, limit: int = 20) -> dict:
        return self._get("/api/v1/x/timeline", {"username": username, "limit": limit})

    def get_batch_tweets(self, tweet_ids: list) -> dict:
        return self._get("/api/v1/x/batch-tweets", {"ids": ",".join(str(x) for x in tweet_ids)})

    def get_token_x_intel(self, contract_address: str) -> dict:
        return self._get("/api/v1/crypto/token-x-intel", {"ca": contract_address})

    def get_meme_radar(self, chain: str = "solana", limit: int = 10) -> dict:
        return self._get("/api/v1/crypto/meme-radar", {"chain": chain, "limit": limit})

    def search_x_tokens(self, query: str, limit: int = 5) -> dict:
        return self._get("/api/v1/crypto/search-x-tokens", {"q": query, "limit": limit})

    def get_thread_unroll(self, tweet_id_or_url: str, max_depth: int = 8) -> dict:
        return self._get("/api/v1/x/thread-unroll", {"id": tweet_id_or_url, "max_depth": max_depth})

    def get_dex_boosts_live(self, chain: str = "solana", limit: int = 10) -> dict:
        return self._get("/api/v1/crypto/dex-boosts-live", {"chain": chain, "limit": limit})

    def get_new_token_profiles(self, chain: str = "all", limit: int = 10) -> dict:
        return self._get("/api/v1/crypto/new-token-profiles", {"chain": chain, "limit": limit})


if __name__ == "__main__":
    print("=" * 78)
    print("🚀 Twitter (X) Real-Time Data & Crypto X-Intel API — Live Zero-Config Demo")
    print(f"🔑 Get FREE API Key (RapidAPI):   {RAPIDAPI_URL}")
    print(f"🕷️ Run Bulk Scraper (Apify Store): {APIFY_URL}")
    print("=" * 78)

    client = XCryptoIntelClient(os.environ.get("RAPIDAPI_KEY", ""))
    profile = client.get_user("solana")
    print("\n1. Live @solana Profile Telemetry:")
    print(json.dumps(profile, indent=2, ensure_ascii=False))

    bonk = client.get_token_x_intel("DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263")
    print("\n2. Live 4-in-1 Solana Token X-Intel (BONK Contract -> Official X + Market Cap):")
    print(json.dumps(bonk, indent=2, ensure_ascii=False))
    print(f"\n✅ Live Demo Succeeded! Subscribe for FREE at {RAPIDAPI_URL} to unlock full production quota.")
