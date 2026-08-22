from django.urls import path

from . import views


app_name = "park_finder"

urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),
    path(
        "mock-search/",
        views.mock_search,
        name="mock_search",
    ),
]