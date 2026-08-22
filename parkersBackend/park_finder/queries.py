from django.db import connection


def find_carpark(latitude, longitude, max_distance, required_stay):
    sql = """
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

    params = [
        longitude,
        latitude,
        longitude,
        latitude,
        max_distance,
        required_stay
    ]

    with connection.cursor() as cursor:
        cursor.execute(sql, params)

        columns = [column[0] for column in cursor.description]

        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]