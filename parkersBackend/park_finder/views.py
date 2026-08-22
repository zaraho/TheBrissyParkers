from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def home(request):
    return render(
        request,
        "park_finder/index.html",
    )


@require_GET
def mock_search(request):
    destination = request.GET.get(
        "destination",
        "Queen Street Mall, Brisbane",
    )

    radius = request.GET.get(
        "radius",
        "500",
    )

    sort_by = request.GET.get(
        "sort_by",
        "best",
    )

    results = [
        {
            "meter_no": "4006",
            "category": "TICKETLESS METER MULTISPACE",
            "street": "FORTESCUE ST",
            "suburb": "SPRING HILL",
            "max_stay_hrs": 12,
            "restrictions": "NONE",
            "operational_day": "MON-FRI",
            "operational_time": "7AM-7PM",
            "price": 4.50,
            "loc_desc": (
                "Fortescue Street between York Parade "
                "and Laisby Drive"
            ),
            "longitude": 153.023612,
            "latitude": -27.458958,
            "walking_distance_m": 180,
        },
        {
            "meter_no": "4007",
            "category": "TICKETLESS METER MULTISPACE",
            "street": "ST PAULS TCE",
            "suburb": "SPRING HILL",
            "max_stay_hrs": 3,
            "restrictions": (
                "CLEARWAY 7AM-9AM, 4PM-7PM MON-FRI"
            ),
            "operational_day": "MON-FRI",
            "operational_time": "9AM-4PM",
            "price": 6.85,
            "loc_desc": (
                "St Pauls Terrace between Gloucester "
                "Street and Boundary Street"
            ),
            "longitude": 153.027436,
            "latitude": -27.460389,
            "walking_distance_m": 310,
        },
        {
            "meter_no": "4008",
            "category": "PAY BY MOBILE APP ONLY",
            "street": "GREGORY TCE",
            "suburb": "SPRING HILL",
            "max_stay_hrs": 12,
            "restrictions": "NONE",
            "operational_day": "MON-FRI",
            "operational_time": "7AM-7PM",
            "price": 4.50,
            "loc_desc": (
                "Gregory Terrace between Kalinga Avenue "
                "and Pool Entry"
            ),
            "longitude": 153.022179,
            "latitude": -27.458441,
            "walking_distance_m": 460,
        },
    ]

    if sort_by == "distance":
        results.sort(
            key=lambda parking: (
                parking["walking_distance_m"]
            )
        )

    elif sort_by == "price":
        results.sort(
            key=lambda parking: parking["price"]
        )

    elif sort_by == "stay":
        results.sort(
            key=lambda parking: (
                parking["max_stay_hrs"]
            ),
            reverse=True,
        )

    return render(
        request,
        "park_finder/partials/search_results.html",
        {
            "destination_name": destination,
            "destination_latitude": -27.4705,
            "destination_longitude": 153.0260,
            "radius": radius,
            "results": results,
        },
    )