// Configuration
// We use localhost:8000 since FastAPI runs there locally by default.
const API_URL = "http://127.0.0.1:8000/api/predict";

// DOM Elements - Navigation
const navBtns = document.querySelectorAll('.nav-btn');
const forms = document.querySelectorAll('.prediction-form');

// DOM Elements - Forms
const diabetesForm = document.getElementById('diabetes-form');
const heartForm = document.getElementById('heart-form');

// Navigation Logic
navBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        // 1. Remove 'active' class from all buttons
        navBtns.forEach(b => b.classList.remove('active'));
        // 2. Add 'active' class to clicked button
        btn.classList.add('active');
        
        // 3. Hide all forms
        forms.forEach(f => f.classList.remove('active-form'));
        
        // 4. Show the target form
        const targetId = btn.getAttribute('data-target');
        document.getElementById(targetId).classList.add('active-form');
    });
});

// Helper function to handle API calls and update UI
async function handlePrediction(e, disease, inputData, resultElementId) {
    e.preventDefault(); // Prevent page reload
    
    const submitBtn = e.target.querySelector('.submit-btn');
    const resultCard = document.getElementById(resultElementId);
    
    // UI Loading state
    submitBtn.textContent = "Processing...";
    submitBtn.disabled = true;
    resultCard.classList.add('hidden');
    
    // Construct payload matching backend schema
    const payload = {
        disease: disease,
        features: inputData
    };

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error("API request failed.");

        const data = await response.json();
        const prediction = parseInt(data.prediction);
        const probability = parseFloat(data.probability) * 100;

        // Display results
        resultCard.classList.remove('hidden', 'success', 'danger');
        
        if (prediction === 1) {
            resultCard.classList.add('danger');
            resultCard.innerHTML = `
                ⚠️ Model Prediction: Positive (${disease})
                <div class="probability">Probability: ${probability.toFixed(2)}%</div>
            `;
        } else {
            resultCard.classList.add('success');
            resultCard.innerHTML = `
                ✅ Model Prediction: Negative
                <div class="probability">Probability: ${probability.toFixed(2)}%</div>
            `;
        }
        
    } catch (error) {
        resultCard.classList.remove('hidden', 'success');
        resultCard.classList.add('danger');
        resultCard.innerHTML = `❌ Error: Unable to reach prediction service. Make sure FastAPI is running.`;
        console.error(error);
    } finally {
        // Restore button state
        submitBtn.textContent = `Predict ${disease === 'diabetes' ? 'Diabetes' : 'Heart Disease'}`;
        submitBtn.disabled = false;
    }
}

// Event Listeners for Form Submissions
diabetesForm.addEventListener('submit', (e) => {
    // Gather inputs
    const inputData = {
        Pregnancies: parseFloat(document.getElementById('d-pregnancies').value),
        Glucose: parseFloat(document.getElementById('d-glucose').value),
        BloodPressure: parseFloat(document.getElementById('d-bp').value),
        SkinThickness: parseFloat(document.getElementById('d-skin').value),
        Insulin: parseFloat(document.getElementById('d-insulin').value),
        BMI: parseFloat(document.getElementById('d-bmi').value),
        DiabetesPedigreeFunction: parseFloat(document.getElementById('d-dpf').value),
        Age: parseFloat(document.getElementById('d-age').value)
    };
    
    handlePrediction(e, 'diabetes', inputData, 'diabetes-result');
});

heartForm.addEventListener('submit', (e) => {
    // Gather inputs
    const inputData = {
        age: parseFloat(document.getElementById('h-age').value),
        sex: parseFloat(document.getElementById('h-sex').value),
        cp: parseFloat(document.getElementById('h-cp').value),
        trestbps: parseFloat(document.getElementById('h-trestbps').value),
        chol: parseFloat(document.getElementById('h-chol').value),
        fbs: parseFloat(document.getElementById('h-fbs').value),
        restecg: parseFloat(document.getElementById('h-restecg').value),
        thalach: parseFloat(document.getElementById('h-thalach').value),
        exang: parseFloat(document.getElementById('h-exang').value),
        oldpeak: parseFloat(document.getElementById('h-oldpeak').value),
        slope: parseFloat(document.getElementById('h-slope').value),
        ca: parseFloat(document.getElementById('h-ca').value),
        thal: parseFloat(document.getElementById('h-thal').value)
    };
    
    handlePrediction(e, 'heart_disease', inputData, 'heart-result');
});
