SELECT
    meter_no,
    street,
    suburb,
    tar_rate_weekday AS price,
    max_stay_hrs,
    ROUND(
        ST_Distance(
            location,
            ST_SetSRID(
                ST_MakePoint(153.0260,-27.4705),
                4326
            )::geography
        )::numeric,
        0
    ) AS walking_distance_m
FROM parking_spots
WHERE ST_DWithin(
    location,
    ST_SetSRID(
        ST_MakePoint(153.0260,-27.4705),
        4326
    )::geography,
    500
)
ORDER BY price, walking_distance_m;