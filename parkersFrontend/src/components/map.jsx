import { useState, useEffect, useRef, useCallback } from "react";
import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import geocodingService from "../geoCodingService";
import "../css/map.css";

const DEFAULT_LOCATION = { position: [-27.47, 153.02], label: "Brisbane asset" };

function FlyToLocation({ position, zoom = 16 }) {
  const map = useMap();
  useEffect(() => {
    if (position) map.flyTo(position, zoom, { duration: 1 });
  }, [position, zoom, map]);
  return null;
}

function Map() {
  const [selected, setSelected] = useState(DEFAULT_LOCATION);
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [activeIndex, setActiveIndex] = useState(-1);
  const [isLoading, setIsLoading] = useState(false);
  const containerRef = useRef(null);

  // Debounced search: waits 500ms after typing stops before calling Nominatim.
  useEffect(() => {
    const trimmed = query.trim();
    if (trimmed.length < 3) {
      setResults([]);
      return;
    }
    const controller = new AbortController();
    const timer = setTimeout(() => {
      setIsLoading(true);
      geocodingService
        .search(trimmed, { signal: controller.signal })
        .then((data) => {
          setResults(data);
          setActiveIndex(-1);
        })
        .catch((err) => {
          if (err.name !== "AbortError") setResults([]);
        })
        .finally(() => setIsLoading(false));
    }, 500);
    return () => {
      clearTimeout(timer);
      controller.abort();
    };
  }, [query]);

  useEffect(() => {
    function handleClickOutside(e) {
      if (containerRef.current && !containerRef.current.contains(e.target)) setResults([]);
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const selectResult = useCallback((result) => {
    setQuery(result.display_name);
    setResults([]);
    setSelected({
      position: [parseFloat(result.lat), parseFloat(result.lon)],
      label: result.display_name,
    });
  }, []);

  const runSearch = useCallback(() => {
    const chosen = results[activeIndex] ?? results[0];
    if (chosen) selectResult(chosen);
  }, [results, activeIndex, selectResult]);

  function handleKeyDown(e) {
    if (results.length === 0) return;
    if (e.key === "ArrowDown") {
      e.preventDefault();
      setActiveIndex((i) => Math.min(i + 1, results.length - 1));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setActiveIndex((i) => Math.max(i - 1, 0));
    } else if (e.key === "Enter") {
      e.preventDefault();
      runSearch();
    }
  }

  return (
    <div className="map-page">
      <div className="search-bar" ref={containerRef}>
        <div className="search-bar__row">
          <input
            className="search-bar__input"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Search an address or building..."
            aria-label="Search for a location"
          />
          <button
            className="search-bar__button"
            onClick={runSearch}
            disabled={isLoading || results.length === 0}
          >
            {isLoading ? "..." : "Search"}
          </button>
        </div>

        {results.length > 0 && (
          <ul className="suggestions-list">
            {results.map((result, index) => (
              <li
                key={result.place_id}
                className={
                  index === activeIndex
                    ? "suggestions-list__item suggestions-list__item--active"
                    : "suggestions-list__item"
                }
                onMouseDown={() => selectResult(result)}
                onMouseEnter={() => setActiveIndex(index)}
              >
                {result.display_name}
              </li>
            ))}
          </ul>
        )}
      </div>

      <MapContainer center={selected.position} zoom={12} className="map-page__map">
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
        <Marker position={selected.position}>
          <Popup>{selected.label}</Popup>
        </Marker>
        <FlyToLocation position={selected.position} />
      </MapContainer>
    </div>
  );
}

export default Map;