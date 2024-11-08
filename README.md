# Django Web Application

## Description:

This project is a Django-based web application with five main applications:

1. **web_adv_deploy**: Initializes the project and includes all required server settings. It also contains the root `urls.py` file, necessary for all HTML templates to function correctly.

2. **core_app**: Handles static files such as CSS, images, and JavaScript. Additionally, `core_app` includes its own templates, including `layout.html`, which serves as the main layout template.

3. **register**: Manages user registration and login functionalities, utilizing Django’s `UserCreationForm` in `register/views.py`.

4. **weather**: Provides weather information for any city in the world using the OpenWeatherMap API. This app retrieves current weather data to enhance the user experience.

5. **chat**: Integrates an AI chatbot with memory of previous messages, powered by the Groq API and utilizing the Llama 70b model to enable conversational interaction with users.

## Features:

- **Template Management**: All HTML templates are managed within `web_adv_deploy` for a streamlined structure.
- **Static Files**: The `core_app` organizes static assets and includes a layout template for consistency across pages.
- **User Registration**: `register` app provides user registration and login features.
- **Weather Data**: The `weather` app integrates with the OpenWeatherMap API to provide up-to-date weather information.
- **AI Chatbot**: The `chat` app uses an AI model with message memory to create an interactive, conversational experience for users.

## Getting Started:

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    ```
    Navigate to the project directory:

cd <project_directory>

## Set up a virtual environment (recommended):
```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
## Install dependencies:
```
pip install -r requirements.txt
```
## Set up environment variables:

Create a .env file in the project root.
Define your API keys, database configurations, and other environment-specific settings.

## Run database migrations:
```
python manage.py migrate
```
## Start the development server:
```
python manage.py runserver
```
## Dependencies

    Django: Web framework for Python.
    OpenWeatherMap API: For weather data integration.
    Groq API: For AI chatbot functionality.
    Llama 70b Model: Used in the chatbot for advanced AI conversation.

## License
MIT

## Copyright
© 11-2024 Vladyslav Levytskyi