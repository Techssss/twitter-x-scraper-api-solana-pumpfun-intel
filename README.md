# ⚡ Twitter (X) Real-Time Data & Solana Pump.fun Crypto X-Intel API (Python & Node.js SDK)

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Get%20Free%20API%20Key-0055FF?style=for-the-badge&logo=rapid)](https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel)
[![Uptime](https://img.shields.io/badge/Service%20Level-100%25-brightgreen?style=for-the-badge)](https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel)
[![Latency](https://img.shields.io/badge/Edge%20Latency-%3C300ms-00f0ff?style=for-the-badge)](https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel)

Official Python & Node.js client examples for the **[Twitter (X) Real-Time Data & Crypto X-Intel API](https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel)** — an ultra-fast (`<300ms`), zero-cookie REST API for scraping public **X (Twitter) Tweets, User Profiles, Timelines, 25x Batch Tweets**, and unlocking **hidden on-chain Twitter/X metadata + RugCheck forensics for 1-minute-old Solana & Pump.fun tokens**.

👉 **[Get Your Instant Free API Key on RapidAPI Here](https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel)** *(No Twitter/X account, cookies, or OAuth required!)*

---

## 🔥 Why Developers Use This Instead of the $5,000/mo Official X API

| Feature | Official X API Pro | Cookie-Based Scrapers | **This API ([RapidAPI Hub](https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel))** |
| :--- | :---: | :---: | :---: |
| **Starting Price** | `$200 - $5,000 / mo` | `$20 - $50 / mo` | **`$0 Free Tier` / `$6.99 Pro`** |
| **X Login Cookies Required?** | OAuth App Review | Yes (Accounts get banned) | **Zero Cookies / Zero Ban Risk** |
| **Average Response Latency** | `400ms` | `1,800ms+` (Residential proxies) | **`~270ms` (Cloudflare Global Edge)** |
| **25x Batch Tweet Lookup** | Paid per post | ❌ Not supported | **✅ 25 Tweets in 1 API Request** |
| **Solana RPC Hidden X Unlock + RugCheck Audit** | ❌ No | ❌ No | **✅ Built-in 4-in-1 Endpoint** |

---

## 🚀 Quick Start (Get Your API Key in 30 Seconds)

1. Go to **[Twitter (X) Real-Time Data & Crypto X-Intel on RapidAPI](https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel)**.
2. Click **Subscribe to Test** and select the **Basic ($0.00 / Free)** or **Pro ($6.99/mo)** plan.
3. Copy your `X-RapidAPI-Key` and run any of the examples below!

---

## 🐍 Python Examples (`x_crypto_client.py`)

```python
import requests

RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY_HERE"
RAPIDAPI_HOST = "twitter-x-real-time-data-crypto-x-intel.p.rapidapi.com"

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": RAPIDAPI_HOST,
}

# 1. Get Full Tweet Details & Real-Time Metrics (Views, Likes, Retweets, Media, Quote)
resp = requests.get(
    f"https://{RAPIDAPI_HOST}/api/v1/x/tweet",
    headers=HEADERS,
    params={"id": "https://x.com/WatcherGuru/status/2124323299639296287"},
)
print("Tweet Metrics:", resp.json())

# 2. Get X User Profile & Follower Count (<270ms)
user = requests.get(
    f"https://{RAPIDAPI_HOST}/api/v1/x/user",
    headers=HEADERS,
    params={"username": "lookonchain"},
)
print("User Profile:", user.json())

# 3. Get Latest Timeline Posts from Any KOL or News Account
timeline = requests.get(
    f"https://{RAPIDAPI_HOST}/api/v1/x/timeline",
    headers=HEADERS,
    params={"username": "WatcherGuru", "limit": 10},
)
print("Latest Tweets:", timeline.json())

# 4. 4-in-1 Solana / Pump.fun On-Chain Hidden X Unlock + RugCheck Forensics + X Hydration
token_intel = requests.get(
    f"https://{RAPIDAPI_HOST}/api/v1/crypto/token-x-intel",
    headers=HEADERS,
    params={"ca": "EEULtyiNJLcSxfrFnB92Tk9jcaRM8UbRhKfJFKxvuaN1"},
)
print("Solana Token X-Intel & RugCheck Verdict:", token_intel.json())
```

---

## 🟢 Node.js / TypeScript Example (`example_node.js`)

```javascript
const RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY_HERE";
const RAPIDAPI_HOST = "twitter-x-real-time-data-crypto-x-intel.p.rapidapi.com";

async function runDemo() {
  // Batch hydrate multiple tweets in a single call
  const res = await fetch(
    `https://${RAPIDAPI_HOST}/api/v1/x/batch-tweets?ids=20,2124323299639296287`,
    {
      headers: {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST,
      },
    }
  );
  const data = await res.json();
  console.log(JSON.stringify(data, null, 2));
}

runDemo();
```

---

## 📡 All 7 Endpoints Reference

1. **`GET /api/v1/x/tweet?id={tweet_id_or_url}`**
   Extracts full tweet text, author profile, real-time views, likes, retweets, replies, bookmarks, HD photos/videos, and quoted tweet.
2. **`GET /api/v1/x/user?username={handle}`**
   Instant lookup of any X account's followers, following, tweet count, bio, joined date, avatar, and banner.
3. **`GET /api/v1/x/timeline?username={handle}&limit=20`**
   Fetches the latest public timeline tweets of any user or KOL sorted newest-first.
4. **`GET /api/v1/x/batch-tweets?ids={id1,id2,...}`**
   Hydrates up to **25 tweets in parallel in 1 API request** (saves up to 96% quota).
5. **`GET /api/v1/crypto/token-x-intel?ca={contract_address}`**
   **4-in-1 Web3 Sniper Audit**: Concurrently fetches DexScreener 5m/1h orderflow acceleration + unlocks hidden on-chain Twitter/X links via **Solana Mainnet RPC `getAsset` & IPFS** + checks **RugCheck** dev serial-rugger history & whale concentration + hydrates the linked X Tweet/Profile engagement.
6. **`GET /api/v1/crypto/meme-radar?chain={all|solana|base}&limit=10`**
   Live surging meme coin orderflow radar ranked by 5m buy pressure, volume acceleration (`vol_accel_ratio`), and average ticket size.
7. **`GET /api/v1/crypto/search-x-tokens?q={keyword}&limit=5`**
   Search tokens by narrative/ticker and auto-hydrate their linked X Tweet or User Profile in one call.

---

🔗 **Subscribe & Test Live in Your Browser:** [https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel](https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel)
