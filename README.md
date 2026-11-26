# Twitter (X) Zero-Cookie Scraper & Solana / Pump.fun Crypto X-Intel SDK (Apify Cloud)

[![Run on Apify Store](https://img.shields.io/badge/Apify%20Store-Run%20Twitter%20Scraper-00C853?style=for-the-badge&logo=apify)](https://apify.com/jistudio/twitter-scraper)
[![Apify Hosted MCP](https://img.shields.io/badge/Hosted%20MCP-mcp.apify.com-7C3AED?style=for-the-badge)](https://mcp.apify.com/?actors=jistudio/twitter-scraper)
[![All JiStudio Actors](https://img.shields.io/badge/Apify%20Store-JiStudio%20Portfolio-06B6D4?style=for-the-badge&logo=apify)](https://apify.com/jistudio)

Official Python & Node.js client examples for **[JiStudio Twitter (X) Scraper & Crypto X-Intel on Apify Store](https://apify.com/jistudio/twitter-scraper)** — a lightweight, zero-cookie cloud scraper for extracting public **X (Twitter) Tweets, 1080p HD MP4 Videos, User Profiles, Multi-KOL Timelines, 25x Batch Tweets, Chronological Thread Unrolls**, and **Solana / Base / Pump.fun & DexScreener Token X-Intel**.

- **[Run Live on Apify Store (Zero Setup, No 50-Tweet Minimum)](https://apify.com/jistudio/twitter-scraper)**
- **[Connect Hosted Remote MCP (`mcp.apify.com`)](https://mcp.apify.com/?actors=jistudio/twitter-scraper)**
- **[Get Your Free Apify API Token](https://console.apify.com/account/integrations)**

---

## Why Developers Use `jistudio/twitter-scraper` Instead of the $5,000/mo Official X API

| Feature | Official X API Pro | Cookie-Based Scrapers | **JiStudio on Apify Store** |
| :--- | :---: | :---: | :---: |
| **Pricing** | `$200 - $5,000 / mo` | `$20 - $50 / mo` | **Pay-Per-Event (Free Apify tier included)** |
| **X Login Cookies Required?** | OAuth App Review | Yes (Accounts get suspended) | **Zero Cookies / Zero Account Risk** |
| **Minimum Tweet Charge** | Monthly flat fee | Often 50-tweet minimum | **No minimum — extract 1 to 5,000 items** |
| **25x Batch Tweet Lookup** | Paid per post | Usually unsupported | **Up to 25 Tweets in 1 batch action** |
| **Solana / Base Crypto X-Intel** | No | No | **Built-in Token CA -> Official X + Market Intel** |
| **Native MCP for AI Agents** | Manual wrapper | No | **1-click via `mcp.apify.com`** |

---

## Quick Start (30 Seconds)

1. Open **[Twitter Scraper on Apify Store](https://apify.com/jistudio/twitter-scraper)** to test directly in your browser.
2. Or grab your free `APIFY_TOKEN` from [Apify Account Integrations](https://console.apify.com/account/integrations) and run via Python, Node.js, cURL, or MCP.

### Python Example (`x_crypto_client.py`)

```python
import requests

APIFY_TOKEN = "YOUR_APIFY_TOKEN"
ENDPOINT = f"https://api.apify.com/v2/acts/jistudio~twitter-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}&clean=true"

# 1. Single Tweet Detail + HD MP4 Video
tweet = requests.post(ENDPOINT, json={
    "action": "tweet",
    "tweetIdOrUrl": "https://x.com/solana/status/2125078025377378634",
}, timeout=90).json()
print("Tweet:", tweet[:1])

# 2. KOL / User Latest Timeline Tweets
timeline = requests.post(ENDPOINT, json={
    "action": "timeline",
    "username": "solana",
    "maxItems": 15,
}, timeout=90).json()
print("Timeline count:", len(timeline))

# 3. Solana / Base Token Contract -> Official X Handle, Price & Tweets
token_intel = requests.post(ENDPOINT, json={
    "action": "token_x_intel",
    "contractAddress": "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263",
}, timeout=90).json()
print("Token X-Intel:", token_intel[:1])
```

### Node.js Example (`example_node.js`)

```javascript
const APIFY_TOKEN = process.env.APIFY_TOKEN || "YOUR_APIFY_TOKEN";
const ENDPOINT = `https://api.apify.com/v2/acts/jistudio~twitter-scraper/run-sync-get-dataset-items?token=${encodeURIComponent(APIFY_TOKEN)}&clean=true`;

async function runDemo() {
  const res = await fetch(ENDPOINT, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      action: "batch_tweets",
      batchTweetIds: "2125078025377378634,1812258574049157405,20",
    }),
  });
  console.log(JSON.stringify(await res.json(), null, 2));
}

runDemo();
```

### Hosted MCP for Claude Desktop / Cursor / Antigravity
Connect directly to Apify's managed Streamable HTTP MCP Server:
```text
https://mcp.apify.com/?actors=jistudio/twitter-scraper
```
Header: `Authorization: Bearer YOUR_APIFY_TOKEN`

---

## All 11 Supported Modes (`action`)

1. **`auto_start_urls`**: Paste any mix of X Tweet URLs, Profile URLs, or Solana/Base Contract Addresses — auto-detected automatically.
2. **`timeline`**: Fetch latest public timeline tweets from one or multiple KOL handles (`twitterHandles`).
3. **`tweet`**: Single tweet metrics (views, likes, retweets, quotes, bookmarks), media & HD MP4 video URLs.
4. **`batch_tweets`**: Hydrate up to 25 Tweet IDs in parallel in one run.
5. **`thread_unroll`**: Walk author self-reply chains to reconstruct full threads.
6. **`user`**: Profile bio, followers, following, tweet count, verification & banner.
7. **`token_x_intel`**: Map any Solana/Base/ETH/BSC Contract Address to official X handle, live price, liquidity & latest tweets.
8. **`meme_radar`**: Live surging meme token radar with linked official X accounts.
9. **`search_x_tokens`**: Search crypto tickers/narratives and auto-hydrate linked X profiles/tweets.
10. **`dex_boosts_live`**: Live feed of DexScreener boosted tokens + X socials.
11. **`new_token_profiles`**: Newly claimed DexScreener token profiles + X verification.

---

## Full Zero-Browser Cloud Scraper Ecosystem by JiStudio on Apify Store

| Platform | Apify Store Actor | Key Capabilities |
| :--- | :--- | :--- |
| **Twitter (X) & Crypto** | [**Twitter Scraper**](https://apify.com/jistudio/twitter-scraper) | Tweets, timelines, threads, HD MP4 videos & Solana / DexScreener X-Intel |
| **TikTok & TikTok Shop** | [**TikTok Shop Scraper**](https://apify.com/jistudio/tiktok-shop-scraper) | Products, SKUs, seller ratings, KOL affiliates, HD no-watermark MP4 & VTT transcripts |
| **TikTok Transcripts** | [**TikTok Transcript Scraper**](https://apify.com/jistudio/tiktok-transcript-scraper) | Fast bulk voiceover `.vtt` subtitles & plaintext script extraction |
| **TikTok Trends** | [**TikTok Trends Scraper**](https://apify.com/jistudio/tiktok-trends-scraper) | Regional For-You viral feeds & Top 30 music charts |
| **Shopee (8 Countries)** | [**Shopee Scraper**](https://apify.com/jistudio/shopee-scraper) | VN/ID/TH/PH/MY/SG/TW/BR product search, exact sold counts, shops & live |
| **1688 China Wholesale** | [**1688 Wholesale Scraper**](https://apify.com/jistudio/1688-wholesale-scraper) | Factory supplier pricing tiers, SKUs, MOQ & wholesale catalog extraction |
| **AliExpress Global** | [**AliExpress Scraper**](https://apify.com/jistudio/aliexpress-scraper) | Global keyword search, SKU variants, verified reviews & shipping ETA |
| **Lazada (6 SEA Markets)** | [**Lazada Scraper**](https://apify.com/jistudio/lazada-scraper) | SEA marketplace product search, prices, ratings & seller catalogs |
| **Goofish / Xianyu** | [**Goofish Xianyu Scraper**](https://apify.com/jistudio/goofish-xianyu-scraper) | Secondhand search, item details & seller listings |
| **Full Store Portfolio** | [**Browse All Actors (`JiStudio`)**](https://apify.com/jistudio) | Complete suite of lightweight pay-per-event cloud scrapers |

---

## Enterprise & Custom APIs
Need dedicated high-volume endpoints or custom scrapers?
- **Telegram**: [@WinJ_sui](https://t.me/WinJ_sui)
- **Apify Store Profile**: [https://apify.com/jistudio](https://apify.com/jistudio)
