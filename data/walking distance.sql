SELECT
    meter_no,
    street,
    suburb,
    max_stay_hrs,
    tar_rate_weekday AS price,
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
AND max_stay_hrs IN ('4','8','12')
ORDER BY walking_distance_m;