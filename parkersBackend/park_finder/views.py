from django.shortcuts import render
from django.views.decorators.http import require_GET

from .geocoding import geocode_address
from .queries import find_carpark


@require_GET
def home(request):
    return render(
        request,
        "park_finder/index.html",
    )


@require_GET
def search(request):
    destination = request.GET.get(
        "destination",
        "",
    )

    radius = request.GET.get(
        "radius",
        "1000",
    )

    required_stay = request.GET.get(
        "required_stay",
        "1",
    )

    sort_by = request.GET.get(
        "sort_by",
        "best",
    )

    # Convert form values into numbers
    try:
        radius = int(radius)
    except ValueError:
        radius = 1000

    try:
        required_stay = float(required_stay)
    except ValueError:
        required_stay = 1


    # -----------------------------
    # Geocode destination
    # -----------------------------

    coordinates = geocode_address(destination)

    if coordinates is None:
        return render(
            request,
            "park_finder/partials/search_results.html",
            {
                "error": "We couldn't find that destination.",
                "results": [],
            },
        )


    latitude = coordinates["latitude"]
    longitude = coordinates["longitude"]


    # -----------------------------
    # Query PostgreSQL + PostGIS
    # -----------------------------

    results = find_carpark(
        latitude=latitude,
        longitude=longitude,
        max_distance=radius,
        required_stay=required_stay,
    )


    # -----------------------------
    # Additional sorting
    # -----------------------------

    if sort_by == "distance":
        results.sort(
            key=lambda parking: parking["distance_m"]
        )

    elif sort_by == "price":
        results.sort(
            key=lambda parking: parking["price"]
        )

    elif sort_by == "stay":
        results.sort(
            key=lambda parking: parking["max_stay_hrs"],
            reverse=True,
        )

    # "best" keeps the SQL ordering:
    # price ASC, distance ASC


    return render(
        request,
        "park_finder/partials/search_results.html",
        {
            "destination_name": coordinates["display_name"],
            "destination_latitude": latitude,
            "destination_longitude": longitude,
            "radius": radius,
            "required_stay": required_stay,
            "results": results,
        },
    )