# Weather Application with Django and Python

This project is a web-based weather application built using Python and the Django framework. It fetches current weather information for a user-specified city and displays it along with an image of the city.

## Features

* Fetch and display current temperature, weather conditions, and weather icons.
* Display an image of the queried city.
* Handle invalid city names with error messages.
* Simple and intuitive user interface.

## Technologies Used

* Python
* Django
* OpenWeatherMap API (for weather data)
* Google Custom Search JSON API (for city images)
* HTML
* CSS (basic styling, full code available on GitHub)

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt # Assuming you have a requirements.txt file
    ```
    If you don't have a `requirements.txt`, you'll need to install Django and any other libraries used manually:
    ```bash
    pip install django requests # requests is likely needed for API calls
    ```
4.  **Set up API keys:**
    * Obtain an API key from OpenWeatherMap.
    * Obtain an API key and set up a Custom Search Engine in Google Cloud Console for the Google Custom Search JSON API.
    * Store your API keys securely, preferably using environment variables or a `.env` file. You'll need to configure your Django settings to access these keys.

5.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
