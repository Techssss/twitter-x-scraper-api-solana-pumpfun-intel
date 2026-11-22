"""
Official Python SDK Client for Twitter (X) Real-Time Data & Crypto X-Intel API
Get your Free API Key at: https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel
"""

import json
import os
import urllib.parse
import urllib.request

RAPIDAPI_HOST = "twitter-x-real-time-data-crypto-x-intel.p.rapidapi.com"


class XCryptoIntelClient:
    def __init__(self, rapidapi_key: str):
        self.api_key = rapidapi_key
        self.base_url = f"https://{RAPIDAPI_HOST}"

    def _get(self, path: str, params: dict) -> dict:
        qs = urllib.parse.urlencode(params)
        url = f"{self.base_url}{path}?{qs}"
        req = urllib.request.Request(
            url,
            headers={
                "x-rapidapi-key": self.api_key,
                "x-rapidapi-host": RAPIDAPI_HOST,
                "Accept": "application/json",
            },
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))

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
    key = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY_HERE")
    print("Get your API key at: https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel")
    client = XCryptoIntelClient(key)
    if key != "YOUR_RAPIDAPI_KEY_HERE":
        print(json.dumps(client.get_user("lookonchain"), indent=2))
