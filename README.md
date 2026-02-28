 Smart FAQ Chatbot (FastAPI + NLP)
An intelligent web-based chatbot that answers user queries using Natural Language Processing and Machine Learning.

This project demonstrates how to integrate an ML model with a web application using FastAPI and deploy it as an interactive chatbot.

🚀 Features
Intent-based NLP understanding using Scikit-learn
FastAPI backend for real-time communication
Interactive web UI (HTML, CSS, JavaScript)
Trained using custom dataset (intents.json)
REST API powered chatbot architecture
Lightweight and easy to extend
Resume-ready ML + Web integration project
🧠 Tech Stack
Layer	Technology Used
Frontend	HTML, CSS, JavaScript
Backend	FastAPI
Machine Learning	Scikit-learn (Logistic Regression)
Text Processing	CountVectorizer (BoW Model)
Language	Python
📂 Project Structure
chatbot_project/ │ ├── app.py # FastAPI server ├── train.py # Model training script ├── intents.json # Training dataset │ ├── templates/ │ └── index.html # Chat UI │ └── static/ └── style.css # Styling

⚙️ How It Works
User sends a message through the web interface.
FastAPI receives the request via /chat endpoint.
Message is transformed using CountVectorizer.
Logistic Regression model predicts the intent.
A response is selected from the dataset.
Reply is returned instantly to the browser.
🏃‍♂️ Run Locally
