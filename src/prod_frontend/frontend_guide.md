# Dr. ML Frontend Guide

Welcome! If you're a backend developer or someone just getting started with modern frontend development, this guide will explain exactly how the `prod_frontend` is built. 

We built this using **Vanilla Web Technologies**—meaning pure HTML, CSS, and JavaScript with no frameworks like React or Vue. This is the best way to understand how the web actually works under the hood!

---

## 1. The Structure (HTML)
**File:** `index.html`

HTML (HyperText Markup Language) is the skeleton of our application. It defines *what* is on the page, but not *how* it looks.

### The Head
In the `<head>` tag, we link external resources:
- We import the **Inter** font from Google Fonts.
- We link our stylesheet `<link rel="stylesheet" href="css/style.css">`.

### The Split Layout
To achieve the 50/50 black and white design, we wrap everything in a master container called `<div class="split-layout">`. 
Inside it, there are two distinct halves:
1. `<section class="left-panel">`: The black side containing the branding and navigation buttons.
2. `<section class="right-panel">`: The white side containing the actual prediction forms.

### The Forms
Inside the right panel, we have two `<form>` elements (one for Diabetes, one for Heart Disease). By default, we use CSS classes (`active-form` and `hidden-form`) to control which one is visible.

---

## 2. The Aesthetics (CSS)
**File:** `css/style.css`

CSS (Cascading Style Sheets) is the paint and interior design. It makes the HTML look beautiful.

### CSS Variables (The Theme)
At the very top of the CSS file, you'll see `:root`. Here, we define **CSS Variables** (like `--black: #0f1115;`). This is incredibly useful. Instead of typing `#0f1115` everywhere, we just type `var(--black)`. If we ever want to change our black to a dark blue, we only change it in one place!

### Flexbox (The Layout Engine)
To make the 50/50 split work flawlessly, we use **Flexbox**:
```css
.split-layout {
    display: flex;
    height: 100vh; /* 100% of the Viewport Height */
    width: 100vw;  /* 100% of the Viewport Width */
}
```
Flexbox allows elements to sit side-by-side. By giving `.left-panel` and `.right-panel` a `width: 50%`, they perfectly divide the screen in half.

### The Grid (Form Layout)
For the form inputs (Age, Glucose, etc.), we don't want a single massive vertical list. We want them in a neat 2-column grid. We use **CSS Grid** for this:
```css
.form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr; /* Two columns of equal width (1 fraction each) */
    gap: 1.5rem; /* Space between inputs */
}
```

---

## 3. The Logic (JavaScript)
**File:** `js/app.js`

JavaScript is the brain. It handles user interaction (clicking buttons) and talking to your Python backend (FastAPI).

### Step 1: Grabbing Elements from HTML
Before JS can do anything, it needs to know what it's working with. We use `document.getElementById` and `document.querySelectorAll` to grab HTML elements and store them in variables.
```javascript
const diabetesForm = document.getElementById('diabetes-form');
```

### Step 2: Tab Navigation
When you click "Diabetes Risk" or "Heart Disease" on the left panel, the page doesn't reload. Instead, JavaScript simply hides one form and shows the other.
It does this by adding and removing CSS classes (specifically the `active-form` class which sets `display: block;`).

### Step 3: Submitting Data to FastAPI
This is the most critical part. When a user clicks "Predict", we don't want the browser's default behavior (which is to refresh the page). 

1. **`e.preventDefault()`**: This stops the page from reloading.
2. **Gathering Data**: We read the `.value` of every input box.
3. **The `fetch` API**: We send a "POST" request to your FastAPI server. We convert our Javascript object into JSON text using `JSON.stringify()`.
```javascript
const response = await fetch("http://127.0.0.1:8000/api/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
});
```
4. **Updating the UI**: Finally, we read the JSON response from your Python code, figure out if the prediction was positive or negative, and inject HTML into the `result-card` to show the user the result!

---

## Summary
1. **HTML** defines the buttons and input boxes.
2. **CSS** puts them on a 50/50 black-and-white grid and makes them look premium.
3. **JavaScript** listens for clicks, sends the data to FastAPI, and updates the screen with the results!
