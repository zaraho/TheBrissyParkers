BEST_PARKING_QUERY = """
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
                ST_MakePoint(%s,%s),
                4326
            )::geography
        )::numeric,
        0
    ) AS walking_distance_m
FROM parking_spots
WHERE ST_DWithin(
    location,
    ST_SetSRID(
        ST_MakePoint(%s,%s),
        4326
    )::geography,
    %s
)
ORDER BY walking_distance_m;
"""
