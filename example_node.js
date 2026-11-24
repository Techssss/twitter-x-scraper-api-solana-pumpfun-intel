/**
 * Official Node.js Client Example for Twitter (X) Real-Time Data & Crypto X-Intel API
 * - Get FREE Production API Key: https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel
 * - Run Bulk on Apify Store:     https://apify.com/nghianguyen2/twitter-x-tweet-scraper-solana-crypto
 */

const RAPIDAPI_KEY = (process.env.RAPIDAPI_KEY || "").trim();
const IS_TRIAL = !RAPIDAPI_KEY || RAPIDAPI_KEY.startsWith("YOUR_");
const RAPIDAPI_HOST = "twitter-x-real-time-data-crypto-x-intel.p.rapidapi.com";
const RAPIDAPI_URL = "https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel";
const APIFY_URL = "https://apify.com/nghianguyen2/twitter-x-tweet-scraper-solana-crypto";

async function callApi(endpoint, params = {}) {
  const notice = `⚡ FREE DEMO PREVIEW (1 item) — Get your FREE Production Key for all 10 X & Crypto X-Intel endpoints at ${RAPIDAPI_URL} or run on Apify: ${APIFY_URL}`;
  if (IS_TRIAL) {
    if (endpoint.includes("token-x-intel")) {
      const ca = params.ca || "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263";
      const res = await fetch(`https://api.dexscreener.com/latest/dex/tokens/${ca}`);
      const dex = await res.json();
      const pair = (dex.pairs || [])[0] || {};
      const tw = (pair.info?.socials || []).find((s) => s.type === "twitter")?.url || null;
      return {
        ok: true,
        _trial_notice: notice,
        symbol: pair.baseToken?.symbol,
        price_usd: pair.priceUsd,
        market_cap: pair.marketCap || pair.fdv,
        official_twitter_url: tw,
      };
    }
    const uname = params.username || "solana";
    const res = await fetch(`https://api.fxtwitter.com/${uname}`, {
      headers: { "User-Agent": "TelegramBot (like TwitterBot)" },
    });
    const fx = await res.json();
    return {
      ok: true,
      _trial_notice: notice,
      username: fx.user?.screen_name || uname,
      followers: fx.user?.followers,
      tweets_count: fx.user?.tweets,
    };
  }
  const qs = new URLSearchParams(params).toString();
  const res = await fetch(`https://${RAPIDAPI_HOST}${endpoint}?${qs}`, {
    headers: {
      "x-rapidapi-key": RAPIDAPI_KEY,
      "x-rapidapi-host": RAPIDAPI_HOST,
      Accept: "application/json",
    },
  });
  return res.json();
}

async function main() {
  console.log("=".repeat(78));
  console.log("🚀 Twitter (X) Real-Time Data & Crypto X-Intel API — Live Zero-Config Demo");
  console.log(`🔑 Get FREE API Key (RapidAPI):   ${RAPIDAPI_URL}`);
  console.log(`🕷️ Run Bulk Scraper (Apify Store): ${APIFY_URL}`);
  console.log("=".repeat(78));

  const profile = await callApi("/api/v1/x/user", { username: "solana" });
  console.log("\n1. Live @solana X Profile:", profile);

  const tokenAudit = await callApi("/api/v1/crypto/token-x-intel", {
    ca: "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263",
  });
  console.log("\n2. Live 4-in-1 Solana Token X-Intel (BONK):", tokenAudit);

  console.log(`\n✅ Live Demo Succeeded! Subscribe for FREE at ${RAPIDAPI_URL} to unlock all 10 endpoints.`);
}

main().catch(console.error);
