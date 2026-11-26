/**
 * Node.js Example for JiStudio Twitter (X) Scraper & Crypto X-Intel on Apify Store
 * Actor: https://apify.com/jistudio/twitter-scraper
 * Get free token: https://console.apify.com/account/integrations
 */

const APIFY_TOKEN = process.env.APIFY_TOKEN || "YOUR_APIFY_TOKEN";
const ACTOR_SLUG = "jistudio~twitter-scraper";

async function runTwitterActor(input) {
  const url = `https://api.apify.com/v2/acts/${ACTOR_SLUG}/run-sync-get-dataset-items?token=${encodeURIComponent(APIFY_TOKEN)}&clean=true`;
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(input),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
  return res.json();
}

async function main() {
  const items = await runTwitterActor({
    action: "batch_tweets",
    batchTweetIds: "2125078025377378634,1812258574049157405,20",
  });
  console.log(`Fetched ${items.length} tweets:`, JSON.stringify(items.slice(0, 2), null, 2));
}

main().catch(console.error);
