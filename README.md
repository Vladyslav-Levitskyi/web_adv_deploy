Django Web Application

Description:

    This project is a Django-based web application with five main applications:

    web_adv_deploy: Initializes the project and includes all required server settings. It also contains the root urls.py file, necessary for all HTML templates to function correctly.

    core_app: Handles static files such as CSS, images, and JavaScript. Additionally, core_app includes its own templates, including layout.html, which serves as the main layout template.

    register: Manages user registration and login functionalities, utilizing Django’s UserCreationForm in register/views.py.

    weather: Provides weather information for any city in the world using the OpenWeatherMap API. This app retrieves current weather data to enhance the user experience.

    chat: Integrates an AI chatbot with memory of previous messages, powered by the Groq API and utilizing the Llama 70b model to enable conversational interaction with users.

Features:

    Template Management: All HTML templates are managed within web_adv_deploy for a streamlined structure.
    Static Files: The core_app organizes static assets and includes a layout template for consistency across pages.
    User Registration: register app provides user registration and login features.
    Weather Data: The weather app integrates with OpenWeatherMap API to provide up-to-date weather information.
    AI Chatbot: The chat app uses an AI model with message memory to create an interactive, conversational experience for users.



License MIT
© 11-2024 Vladyslav Levytskyi

