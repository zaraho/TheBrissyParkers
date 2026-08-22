from django.db import connection


BEST_PARKING_QUERY = """
SELECT
    meter_no,
    street,
    suburb,
    max_stay_hrs,
    tar_rate_weekday AS price,
    longitude,
    latitude,   

    ROUND(
        ST_Distance(
            location,
            ST_SetSRID(
                ST_MakePoint(%s, %s),
                4326
            )::geography
        )::numeric,
        0
    ) AS distance_m

FROM parking_spots

WHERE ST_DWithin(
    location,
    ST_SetSRID(
        ST_MakePoint(%s, %s),
        4326
    )::geography,
    %s
)

AND max_stay_hrs >= %s

ORDER BY price ASC, distance_m ASC;
"""


def find_carpark(
    latitude,
    longitude,
    max_distance,
    required_stay,
):
    params = [
        longitude,
        latitude,
        longitude,
        latitude,
        max_distance,
        required_stay,
    ]

    with connection.cursor() as cursor:
        cursor.execute(
            BEST_PARKING_QUERY,
            params,
        )

        columns = [
            column[0]
            for column in cursor.description
        ]

        results = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    return results