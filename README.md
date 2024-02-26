# Pre-Assessment-Test-Server-Setup-API-Integration-and-Data-Analysis

Task 1: Server Setup (Virtual Environment)

Install Docker:
Download and install Docker Desktop for your operating system from the official Docker website: Docker Desktop.

Create Dockerfile:
Created a Dockerfile in the project directory to define the environment setup.

Create requirements.txt:
Created a requirements.txt file listing all the Python dependencies required for the project.

Create app.py:
Created a simple Flask application for testing purposes.

Build Docker Image:
Built the Docker image using the Dockerfile and requirements.txt.

Run Docker Container:
Ran the Docker container based on the built image, exposing necessary ports for development.

Task 2: API Integration to Pull Data
For this task, we'll choose the OpenWeatherMap API.

Steps Taken:

API Endpoint:
Chose the current weather data endpoint from the OpenWeatherMap API: https://api.openweathermap.org/data/2.5/weather.

Authentication:
Obtained a free API key from OpenWeatherMap to authenticate requests.

Script for Data Pulling:
Wrote a Python script using the requests library to pull current weather data from the API.

Task 3: Storing and Analyzing the Data

Storing Data:
Stored the data collected from the API in a SQLite database.

Analysis Script:
Developed a Python script to analyze the stored data, calculating average temperature and humidity.

Insights:
Identified trends in temperature and humidity over time.

Error Handling:
Implemented error handling for cases such as rate limits or API downtime.

Challenges Faced:
Handling API rate limits and ensuring continuous availability of data.
