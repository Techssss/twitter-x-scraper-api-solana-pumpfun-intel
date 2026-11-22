/**
 * Official Node.js Client Example for Twitter (X) Real-Time Data & Crypto X-Intel API
 * Get your Free API Key at: https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel
 */

const RAPIDAPI_KEY = process.env.RAPIDAPI_KEY || "YOUR_RAPIDAPI_KEY_HERE";
const RAPIDAPI_HOST = "twitter-x-real-time-data-crypto-x-intel.p.rapidapi.com";

async function callApi(endpoint, params = {}) {
  const qs = new URLSearchParams(params).toString();
  const res = await fetch(`https://${RAPIDAPI_HOST}${endpoint}?${qs}`, {
    headers: {
      "x-rapidapi-key": RAPIDAPI_KEY,
      "x-rapidapi-host": RAPIDAPI_HOST,
    },
  });
  return await res.json();
}

async function main() {
  console.log("Get your free API key at: https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel");
  if (RAPIDAPI_KEY === "YOUR_RAPIDAPI_KEY_HERE") return;

  const profile = await callApi("/api/v1/x/user", { username: "WatcherGuru" });
  console.log("User Profile:", profile);

  const tokenAudit = await callApi("/api/v1/crypto/token-x-intel", {
    ca: "EEULtyiNJLcSxfrFnB92Tk9jcaRM8UbRhKfJFKxvuaN1",
  });
  console.log("4-in-1 Solana Token X-Intel:", tokenAudit);
}

main();
