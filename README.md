# 🎯 Intelligent Career Guidance Expert System

## 📌 Overview

The **Intelligent Career Guidance Expert System** is a web-based application that helps students choose the most suitable career path based on their interests, skills, personality, and work style.

The system uses a **rule-based expert system + intelligent scoring algorithm** to provide accurate career recommendations along with confidence scores and learning roadmaps.

It also includes an **AI chatbot** that provides real-time career guidance.

---

## 🚀 Features

* 🎯 Personalized career recommendations
* 📊 Confidence-based scoring system
* 🧠 Rule-based Expert System
* 🤖 AI-powered chatbot for career queries
* 📈 Career insights (salary, demand, roadmap)
* 🌐 Interactive multi-step assessment form
* 💡 Clean and modern UI

---

## 🛠️ Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Logic:** Rule-Based Expert System
* **AI Component:** Chatbot (NLP using regex patterns)

---

## 📂 Project Structure

```id="code1"
career-guidance-system/
│
├── app.py                  # Flask backend server
├── chatbot.py             # AI chatbot logic
├── expert_system.py       # Career prediction engine
├── rules.py               # Rule-based logic (optional/backup)
│
├── templates/
│   ├── index.html         # Home page
│   ├── form.html          # Assessment form
│   └── result.html        # Results page
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## ⚙️ How to Run This Project

### 🔹 Step 1: Install Python

Make sure Python is installed (version 3.7 or above)

---

### 🔹 Step 2: Install Required Libraries

Open terminal / command prompt and run:

```bash id="code2"
pip install flask
```

---

### 🔹 Step 3: Run the Application

Navigate to project folder and run:

```bash id="code3"
python app.py
```

---

### 🔹 Step 4: Open in Browser

Go to:

```id="code4"
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

* User fills assessment form (education, interests, skills, personality) 
* Data is sent to backend via Flask API 
* Expert system calculates match score for multiple careers 
* Top 3 careers are returned with confidence percentage
* Results displayed dynamically on results page 
* Chatbot provides additional guidance interactively 

---

## 📸 Screens

* 🏠 Home Page → 
* 📋 Assessment Form → 
* 📊 Result Page → 

---

## 🎯 Objective

To help students make better career decisions using intelligent systems and data-driven recommendations.

---

## 🔮 Future Enhancements

* 🤖 Machine Learning based prediction
* 🔐 User login system
* 📊 Dashboard analytics
* 🌍 Deployment on cloud (AWS / Render)
* 📱 Mobile responsive improvements

---

## 👨‍💻 Author

**Vedant Chavan**

---

## 📄 License

This project is open-source and available under the MIT License.
