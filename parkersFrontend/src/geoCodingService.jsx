// GeocodingService.js
// Encapsulates all Nominatim API access behind one class (single responsibility).
// Public policy note: nominatim.openstreetmap.org is rate-limited (~1 req/sec)
// and not meant for embedding at scale — self-host or proxy for production.
// https://nominatim.org/release-docs/latest/

const NOMINATIM_URL = "https://nominatim.openstreetmap.org/search";
const BRISBANE_VIEWBOX = "152.6,-27.1,153.3,-27.8"; // left,top,right,bottom — bias only

class GeocodingService {
  // Building/POI names often fail without geographic context, so if the raw
  // query returns nothing, retry once with the city appended.
  async search(query, { signal } = {}) {
    const results = await this.#fetchResults(query, signal);
    if (results.length > 0) return results;
    return this.#fetchResults(`${query}, Brisbane, Australia`, signal);
  }

  async #fetchResults(query, signal) {
    const params = new URLSearchParams({
      format: "json",
      q: query,
      addressdetails: "1",
      limit: "6",
      viewbox: BRISBANE_VIEWBOX,
      bounded: "0",
    });
    const response = await fetch(`${NOMINATIM_URL}?${params.toString()}`, {
      signal,
      headers: { Accept: "application/json" },
    });
    if (!response.ok) throw new Error(`Geocoding failed (${response.status})`);
    return response.json();
  }
}

// Shared singleton — one instance, reused everywhere it's imported.
export default new GeocodingService();