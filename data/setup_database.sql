-- Creates PostGIS-enabled parking table
CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE parking_spots AS
SELECT
    meter_no,
    category,
    street,
    suburb,
    max_stay_hrs,
    restrictions,
    operational_day,
    operational_time,
    tar_zone,
    tar_rate_weekday,
    tar_rate_ah_we,
    loc_desc,
    longitude,
    latitude
FROM parking_raw;

ALTER TABLE parking_spots
ADD COLUMN location GEOGRAPHY(Point,4326);

UPDATE parking_spots
SET location =
    ST_SetSRID(
        ST_MakePoint(
            longitude::DOUBLE PRECISION,
            latitude::DOUBLE PRECISION
        ),
        4326
    )::geography;

CREATE INDEX parking_location_idx
ON parking_spots
USING GIST(location);
-- Finds parking within walking distance threshold