-- Enable PostGIS
CREATE EXTENSION IF NOT EXISTS postgis;


-- Raw table matching the Brisbane parking CSV
DROP TABLE IF EXISTS parking_raw;

CREATE TABLE parking_raw (
    meter_no TEXT,
    category TEXT,
    street TEXT,
    suburb TEXT,
    max_stay_hrs TEXT,
    restrictions TEXT,
    operational_day TEXT,
    operational_time TEXT,
    tar_zone TEXT,
    tar_rate_weekday TEXT,
    tar_rate_ah_we TEXT,
    loc_desc TEXT,
    veh_bays TEXT,
    mc_bays TEXT,
    mc_rate TEXT,
    longitude TEXT,
    latitude TEXT,
    mobile_zone TEXT,
    max_cap_chg TEXT,
    objectid TEXT,
    geo_shape TEXT,
    geo_point_2d TEXT,
    veh_bays_int TEXT
);


-- Clean table used by Django/PostGIS
DROP TABLE IF EXISTS parking_spots;

CREATE TABLE parking_spots (
    meter_no INTEGER PRIMARY KEY,
    category TEXT,
    street TEXT,
    suburb TEXT,

    -- Numeric because Django needs to compare:
    -- max_stay_hrs >= required_stay
    max_stay_hrs NUMERIC,

    restrictions TEXT,
    operational_day TEXT,
    operational_time TEXT,
    tar_zone TEXT,

    tar_rate_weekday NUMERIC,
    tar_rate_ah_we NUMERIC,

    loc_desc TEXT,
    veh_bays INTEGER,

    longitude DOUBLE PRECISION,
    latitude DOUBLE PRECISION,

    -- PostGIS geographic point
    location GEOGRAPHY(POINT, 4326)
);