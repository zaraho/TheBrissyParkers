# TheBrissyParkers

Find smarter parking in Brisbane.

Bris Parker is a hackathon web application that helps drivers find suitable parking near their destination. A user enters a destination, arrival and departure times, and preferred walking distance. The application searches Brisbane parking data and recommends options based on price, walking distance, and maximum permitted stay.

## The Problem

Finding parking in Brisbane can be confusing and time-consuming. Parking restrictions, prices, maximum stay limits, and distance from a destination are often spread across different signs and services.

Bris Parker brings this information together and presents the most useful options on an interactive map.

## Key Features

- Search parking by address or destination
- Choose arrival and departure times
- Set a preferred walking distance or search radius
- View parking locations on an interactive map
- Compare price, walking distance, and maximum stay
- Rank results by Best Choice, Least Walking, or Lowest Cost
- Display relevant parking restrictions and sign information

## User Story

As a driver, I want to search for parking near my destination based on walking distance, price, and maximum stay so that I can quickly choose the most suitable parking option.

Acceptance Criteria

The user can enter a valid destination and parking preferences.

The system converts the destination into geographic coordinates.

The system returns parking spots within the selected radius.

Each suggestion displays its price, walking distance, and maximum stay.

The suggested parking locations appear on an interactive map.

The user can sort or filter the returned options.

## Tech Stack

| Technology | Purpose |
|---|---|
| **Django** | Backend | Ila |
| **PostgreSQL + PostGIS** | Database & spatial queries | Suha |
| **HTMX** | Dynamic page updates | Rizwan |
| **Leaflet.js** | Interactive map | Dhruti/Zara |
| **OpenStreetMap** | Map data | Dhruti/Zara |
| **Mapbox** | Address geocoding | Dhruti/Zara |
| **Brisbane City Council Open Data** | Parking data | Dhruti/Zara 

## Architecture

Bris Parker uses Django's Model–Template–View architecture with a spatial database and external map services.

flowchart TD
    A["User search form"] --> B["Django view"]
    B --> C["Geocoding service"]
    C --> B
    B --> D["Search and ranking service"]
    D --> E["PostgreSQL + PostGIS"]
    E --> D
    D --> F["Django template / HTMX partial"]
    F --> G["Leaflet + OpenStreetMap"]
    G --> H["Ranked parking suggestions"]

Request Flow

The user submits a destination, arrival time, departure time, and walking-distance preference.

Django validates the form input.

The geocoding service converts the destination into latitude and longitude.

PostGIS finds parking locations within the selected radius.

Django filters invalid options by time restrictions and maximum stay.

The ranking logic scores the remaining options by distance, cost, and suitability.

Django returns an HTML template or HTMX partial.

Leaflet plots the recommended locations on the OpenStreetMap map.

Suggested Project Structure

TheBrissyParkers/
├── manage.py
├── requirements.txt
├── .env.example
├── bris_parker/              # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── parking/                  # Main Django application
│   ├── migrations/
│   ├── services/
│   │   ├── geocoding.py
│   │   └── parking_search.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── templates/
│   └── parking/
├── static/
│   ├── css/
│   └── js/
└── data/                     # Imported or processed open datasets

Data Model

A parking record can contain:

id

latitude and longitude

location as a PostGIS point

street_name

parking_type

price_per_hour

maximum_stay_minutes

restriction_start and restriction_end

valid_days

sign_description

Ranking Approach

For the hackathon prototype, each valid parking option can receive a weighted suitability score:

score = distance_score + price_score + stay_score

The weighting changes with the user's selected preference:

Best Choice: balances walking distance, cost, and stay suitability.

Least Walking: gives the greatest weight to distance.

Lowest Cost: gives the greatest weight to free or low-cost parking.

Getting Started

Prerequisites

Python 3.11 or later

PostgreSQL

PostGIS extension

Git

A Mapbox access token, if Mapbox is used for geocoding

Installation

Clone the repository:

git clone https://github.com/zaraho/TheBrissyParkers.git
cd TheBrissyParkers

Create and activate a virtual environment:

Windows PowerShell

py -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS/Linux

python3 -m venv .venv
source .venv/bin/activate

Install the dependencies:

pip install -r requirements.txt

Create a .env file from .env.example and configure the database and geocoding values:

SECRET_KEY=replace-with-a-local-secret
DEBUG=True
DB_NAME=bris_parker
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
MAPBOX_ACCESS_TOKEN=your-mapbox-token

Enable PostGIS in the project database:

CREATE EXTENSION postgis;

Apply the Django migrations:

python manage.py migrate

Import the parking dataset using the project's import command, when available:

python manage.py import_parking_data

Start the development server:

python manage.py runserver

Open http://127.0.0.1:8000/ in a browser.

Hackathon MVP

The minimum viable product focuses on:

One destination search form

Geocoding the entered address

Radius-based parking queries

Three ranking modes

Parking markers and result cards

Price, distance, and maximum-stay information

Future Improvements

Real-time parking availability

Live traffic and event information

Accessible parking filters

EV charging and motorcycle parking filters

Turn-by-turn walking directions

Saved locations and recent searches

User reports for incorrect or outdated restrictions

Predictive parking availability based on historical demand

Data and API Notes

Parking rules should always be verified against the physical street signs.

Brisbane City Council data may change, so the application should track dataset update dates.

OpenStreetMap attribution must remain visible on the map.

API keys and database passwords must be stored in environment variables and never committed to Git.

Authors

Ila — Django backend

Rizwan —  frontend

Suha — PostgreSQL and PostGIS

Zara/Dhruti — mapping, geocoding