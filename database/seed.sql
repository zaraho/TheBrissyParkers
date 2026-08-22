-- Clear existing data so this script can be rerun
TRUNCATE TABLE parking_raw;
TRUNCATE TABLE parking_spots;


-- Import the Brisbane parking CSV
\copy parking_raw FROM 'data/brisbane-parking-meters.csv' WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ','
);


-- Convert raw CSV data into our application's parking table
INSERT INTO parking_spots (
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
    veh_bays,
    longitude,
    latitude,
    location
)

SELECT
    meter_no::INTEGER,
    category,
    street,
    suburb,

    -- CSV contains the strange value '4P-12P'.
    -- Treat non-numeric values as NULL.
    CASE
        WHEN max_stay_hrs ~ '^[0-9]+(\.[0-9]+)?$'
        THEN max_stay_hrs::NUMERIC
        ELSE NULL
    END,

    restrictions,
    operational_day,
    operational_time,
    tar_zone,

    NULLIF(tar_rate_weekday, '')::NUMERIC,
    NULLIF(tar_rate_ah_we, '')::NUMERIC,

    loc_desc,

    NULLIF(veh_bays, '')::INTEGER,

    longitude::DOUBLE PRECISION,
    latitude::DOUBLE PRECISION,

    ST_SetSRID(
        ST_MakePoint(
            longitude::DOUBLE PRECISION,
            latitude::DOUBLE PRECISION
        ),
        4326
    )::geography

FROM parking_raw

WHERE longitude <> ''
AND latitude <> '';


-- Show how many usable parking spots were imported
SELECT COUNT(*) AS imported_parking_spots
FROM parking_spots;