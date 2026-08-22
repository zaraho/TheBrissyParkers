from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError, GeocoderTimedOut


geolocator = Nominatim(
    user_agent="TheBrissyParkers/1.0"
)


def geocode_address(address):
    """
    Convert an address into latitude and longitude.
    """

    try:
        location = geolocator.geocode(
            address,
            country_codes="au",
            exactly_one=True,
            timeout=10,
        )

        if location is None:
            return None

        return {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "display_name": location.address,
        }

    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print("Geocoding error:", e)
        return None
    
def search_addresses(query):
    if not query or len(query) < 3:
        return []

    search_query = f"{query}, Brisbane, Queensland, Australia"

    locations = geolocator.geocode(
        search_query,
        country_codes="au",
        exactly_one=False,
        limit=5,
        timeout=10,
    )

    if not locations:
        return []

    return [
        {
            "display_name": location.address,
            "latitude": location.latitude,
            "longitude": location.longitude,
        }
        for location in locations
    ]