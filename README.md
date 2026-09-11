<div align="center">
  <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/heart-pulse.svg" width="80" alt="Dr. ML Logo">
  
  <h1>🩺 Dr. ML</h1>
  <p><strong>Intelligent Multi-Disease Predictive Diagnostics</strong></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
    <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="scikit-learn" />
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit" />
    <img src="https://img.shields.io/badge/Vanilla_JS-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="Vanilla JS" />
  </p>
</div>

---

## 📖 About the Project

**Dr. ML** is an end-to-end Machine Learning ecosystem designed to assess patient vitals and cardiological data to predict the likelihood of **Diabetes** and **Heart Disease**. 

By bridging the gap between raw data science and usable software, this project serves robust predictive models (like `SVC` and `RandomForest`) through a lightning-fast API, presenting the results on beautiful, responsive user interfaces.

### ✨ Key Features
- **Dual Prediction Models:** Hyperparameter-tuned models tailored for specific diseases.
- **FastAPI Backend:** A highly scalable, decoupled REST API architecture.
- **Two Beautiful Frontends:** Choose between a rapid-prototyped Streamlit dashboard or a premium, split-screen Vanilla Web UI.
- **Data Integrity:** Strict input validation using Pydantic schemas.

---

## 🏗️ Architecture & Structure

The repository is modularly designed to separate concerns between data science, backend services, and frontend interfaces.

```text
Dr.ML/
├── dataset/                  # 📊 Raw and processed CSV datasets
├── model_dir/                # 🧠 Serialized, ready-to-use models (.joblib)
├── src/
│   ├── backend/              # ⚙️ FastAPI Application
│   │   ├── api/              # Route handlers and endpoints
│   │   ├── schemas/          # Pydantic data validation
│   │   └── services/         # ML inference and prediction logic
│   │
│   ├── frontend/             # 🎨 Streamlit Interface
│   │   ├── pages/            # Multi-page routing
│   │   └── app.py            # Streamlit entry point
│   │
│   ├── prod_frontend/        # 💎 Premium Production UI
│   │   ├── css/              # Monochrome aesthetic styling
│   │   ├── js/               # Asynchronous API integration
│   │   └── index.html        # 50/50 split-layout interface
│   │
│   └── training/             # 🛠️ Model training pipelines
│
├── .env                      # 🔐 Environment variables (Git-ignored)
└── requirements.txt          # 📦 Python dependencies
```

---

## 🚀 Getting Started

Follow these instructions to get a local copy of the project up and running.

### 1. Prerequisites
Ensure you have the following installed:
- **Python 3.10** or higher
- **Git**

### 2. Installation
Clone the repository and set up a secure virtual environment:

```bash
# Clone the repository
git clone https://github.com/sazybuilds/Dr.ML.git
cd Dr.ML

# Create a virtual environment
python -m venv .venv

# Activate the environment (Windows)
source .venv/Scripts/activate
# Activate the environment (Mac/Linux)
# source .venv/bin/activate

# Install all required libraries
pip install -r requirements.txt
```

### 3. Environment Configuration
The backend and frontend rely on environment variables to communicate. 

1. Create a `.env` file in the root directory.
2. Add the required variables (like the API endpoint).
   
```env
# .env
API_URL=http://127.0.0.1:8000/api/predict
# Add any other required model paths or database URIs here
```

3. **Load the variables into your terminal** using the command sandwich below. You must do this before running the application:
```bash
set -a
source .env
set +a
```

---

## 💻 Running the Application

### Step 1: Start the Backend Server
The core of Dr. ML is the API. You **must** have this running for the interfaces to work.
```bash
uvicorn src.backend.main:app --reload
```
> 💡 **Tip:** Once running, visit `http://127.0.0.1:8000/docs` to interact with the auto-generated Swagger API documentation!

### Step 2: Choose Your Frontend
With the backend running, open a **new terminal**, activate your environment (`source .venv/Scripts/activate`), and launch a UI:

#### Option A: Streamlit Prototyping UI
A Python-driven dashboard perfect for rapid testing.
```bash
streamlit run src/frontend/app.py
```

#### Option B: Premium Production UI
A sleek, responsive web interface built with pure web technologies.
- Simply navigate to `src/prod_frontend/` in your file explorer.
- Double-click `index.html` to open it in any web browser. 

---

<div align="center">
  <b>Built with ❤️ by <a href="https://github.com/sazybuilds">Sazybuilds</a></b>
</div>
