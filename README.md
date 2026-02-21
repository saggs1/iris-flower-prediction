# Iris Flower Prediction – End-to-End Machine Learning Project

This project is an end-to-end Machine Learning application that predicts the species of an Iris flower based on user-provided measurements of sepals and petals.
It includes model training, a backend API, and a frontend interface, making it suitable for academic, demo, and beginner-to-intermediate ML projects.

# Project Overview

The Iris dataset is a classic dataset in machine learning used for multi-class classification.
This application predicts one of the following species: Iris-setosa, Iris-versicolor, Iris-virginica

**Input Features:** Sepal Length (cm) | Sepal Width (cm) | Petal Length (cm) | Petal Width (cm)

**Tech Stack :** 
Machine Learning : Python, NumPy, Pandas, Scikit-learn
Backend : FastAPI, Uvicorn, Joblib
Frontend : HTML, CSS, JavaScript 

**📁 Project Structure**

IRIS-FLOWER-PROJECT/
│
├── backend/
│   ├── __pycache__/          # Python cache (auto-generated)
│   └── app.py                # FastAPI backend application
│
├── frontend/
│   ├── index.html            # Frontend UI
│   ├── script.js             # JavaScript for API calls
│   └── style.css             # Styling
│
├── model/
│   ├── model.pkl             # Trained ML model
│   └── scaler.pkl            # Scaler used during training
│
├── venv/                     # Virtual environment (project-scoped)
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
│
├── .gitignore                # Ignore venv, cache files, etc.
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation

# Installation & Setup :

Step1: Clone the Repository
git clone https://github.com/saggs1/iris-flower-prediction.git
cd iris-flower-prediction

Step2: Create & Activate Virtual Environment
venv\Scripts\activate

Step3: Install Dependencies 
pip install -r requirements.txt

# Running the Project

1) Start the Backend (FastAPI)
cd backend
uvicorn main:app --reload
Backend will run at: http://localhost:8000
Swagger API Docs: http://localhost:8000/docs

2) Run the Frontend
Open frontend/index.html directly in your browser

3)API Usage
Endpoint : POST /predict
Sample Request:
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
Sample Response:
{
  "prediction": "Iris-setosa"
}

# NOTE : This project is open-source and free to use for educational purposes.



