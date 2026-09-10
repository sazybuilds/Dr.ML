<div align="center">
  <h1>🩺 Dr.ML</h1>
  <p><strong>A Machine Learning powered diagnostic tool for predicting Diabetes and Heart Disease.</strong></p>

  <!-- Tech Stack Badges -->
  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn" />
    <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
    <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="Numpy" />
    <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic" />
    <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  </p>
</div>

---

## 📖 Overview
**Dr.ML** is an end-to-end Machine Learning project designed to predict the likelihood of a patient having Diabetes or Heart Disease based on medical attributes. It features robust data preprocessing, hyperparameter-tuned predictive models (SVC for Diabetes, RandomForest for Heart Disease), and a modular backend service architecture.

## 🏗️ Project Architecture
The codebase is structured following best practices for modularity, scalability, and separation of concerns.

```text
Dr.ML/
├── dataset/                  # Raw and processed datasets (diabetes.csv, heart.csv)
├── logs/                     # Application and training logs
├── model_dir/                # Serialized trained models (.joblib)
├── notebook_dir/             # Jupyter notebooks for EDA and experiments
├── src/
│   ├── backend/              # API and prediction services
│   │   ├── config/           # Backend configurations and settings
│   │   └── services/         # Core prediction logic (predictor.py)
│   ├── training/             # Model training pipelines
│   │   ├── config/           # Training hyperparameters and settings
│   │   ├── diabetes.py       # Diabetes model training script
│   │   └── heart_disease.py  # Heart Disease model training script
│   └── utils/                # Shared utilities (e.g., preprocessing functions)
├── .env                      # Environment variables configuration
├── check.py                  # Sanity checks/tests
└── requirements.txt          # Python dependencies
```

## 🚀 How to Start

### Prerequisites
- Python 3.10+
- `git`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sazybuilds/Dr.ML.git
   cd Dr.ML
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows (Git Bash)
   python -m venv .venv
   source .venv/Scripts/activate

   # Linux/macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup:**
   Create a `.env` file in the root directory and configure your paths (you can refer to `env_template.txt` for the required variables). 
   *Note: If you use Bash, ensure there are no spaces around the `=` sign.*

5. **Train the Models:**
   Run the training scripts as Python modules from the root directory to generate the `.joblib` models:
   ```bash
   python -m src.training.diabetes
   python -m src.training.heart_disease
   ```

## 🛣️ Roadmap & Remaining Processes

Currently, the data science, model training, and core prediction services are complete. The following phases are next:

- [ ] **API Creation:** Expose the `predictor.py` service via a robust and scalable REST API (using FastAPI).
- [ ] **Frontend Development:** Build an aesthetic, user-friendly web interface for patients/doctors to input medical data and receive instant predictions.
- [ ] **Deployment:** Containerize the application (Docker) and deploy both the frontend and backend to a cloud platform.

## 👨‍💻 Author
**Sazybuilds**  
[GitHub Profile](https://github.com/sazybuilds)

---
*Built with ❤️ and Python.*
