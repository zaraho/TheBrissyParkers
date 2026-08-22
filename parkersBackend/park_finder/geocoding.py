from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError, GeocoderTimedOut


geolocator = Nominatim(
    user_agent="TheBrissyParkers/1.0"
)


def geocode_address(address):
    """
    Converts a user's address into latitude and longitude.
    """

    try:
        search_address = f"{address}, Brisbane, Queensland, Australia"

        location = geolocator.geocode(
            search_address,
            country_codes="au",
            exactly_one=True,
            timeout=10
        )

        if location is None:
            return None

        return {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "display_name": location.address
        }

    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print("Geocoding error:", e)
        return None