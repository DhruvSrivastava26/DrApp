# 🩺 DR-APP – Machine Learning Enabled Healthcare Platform

DR-APP is a full-stack healthcare platform that simplifies online doctor appointment booking while leveraging Machine Learning for early disease risk prediction. The platform provides dedicated dashboards for Patients, Doctors, and Administrators with secure authentication, appointment management, payment integration, and predictive healthcare features.

---

## 🚀 Features

### 👤 Patient Module
- User Registration & Login (JWT Authentication)
- Browse doctors by specialty
- Search doctors
- Book doctor appointments
- View appointment history
- Online payment integration using Razorpay
- Update personal profile
- Diabetes Risk Prediction using Machine Learning
- Heart Disease Risk Prediction using Machine Learning

---

### 👨‍⚕️ Doctor Module
- Secure Doctor Login
- Dashboard with appointment statistics
- Manage appointments
- Update doctor profile
- View patient details
- Track earnings

---

### 👨‍💼 Admin Module
- Secure Admin Authentication
- Add New Doctors
- Manage Doctor Profiles
- View All Appointments
- Dashboard Analytics
- Manage Users

---

### 🤖 Machine Learning Module

Integrated ML models help users assess their health risks.

#### Diabetes Prediction
- Algorithm: Support Vector Machine (SVM)

#### Heart Disease Prediction
- Algorithm: Logistic Regression

The ML models are served using a Flask microservice and communicate with the MERN backend via REST APIs.

---

## 🛠️ Tech Stack

### Frontend
- React.js
- Tailwind CSS
- Axios
- React Router

### Backend
- Node.js
- Express.js
- JWT Authentication
- REST APIs

### Database
- MongoDB Atlas

### Machine Learning
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Cloud Services
- Cloudinary
- Razorpay

---

## 📂 Project Structure

```
DR-APP
│
├── frontend          # Patient Web Application
├── admin             # Admin & Doctor Dashboard
├── backend           # Express Backend APIs
├── ml-service        # Flask Machine Learning Service
└── README.md
```

---

## 🔐 Authentication

- JWT Authentication
- Protected Routes
- Role-Based Access Control

Users are authenticated based on their role:

- Patient
- Doctor
- Admin

---

## 💳 Payment Gateway

Integrated with Razorpay for secure online appointment booking payments.

---

## ☁️ Cloud Storage

Doctor images and related media are securely stored using Cloudinary.

---

## 🧠 Machine Learning Workflow

```
Patient Input
        │
        ▼
React Frontend
        │
        ▼
Express Backend
        │
        ▼
Flask ML Service
        │
        ▼
Prediction Model
        │
        ▼
Prediction Result
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/DhruvSrivastava26/DrApp.git
```

Move into the project directory

```bash
cd DrApp
```

---

## Install Dependencies

### Frontend

```bash
cd frontend
npm install
```

### Admin

```bash
cd ../admin
npm install
```

### Backend

```bash
cd ../backend
npm install
```

### ML Service

```bash
cd ../ml-service
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside the backend folder.

```
MONGODB_URI=Your MongoDB URI

JWT_SECRET=Your JWT Secret

CLOUDINARY_NAME=Your Cloudinary Name

CLOUDINARY_API_KEY=Your API Key

CLOUDINARY_SECRET_KEY=Your API Secret

RAZORPAY_KEY_ID=Your Razorpay Key

RAZORPAY_KEY_SECRET=Your Razorpay Secret

ML_SERVICE_URL=http://localhost:5001
```

---

## Running the Project

### Start Backend

```bash
cd backend
npm run server
```

### Start Frontend

```bash
cd frontend
npm run dev
```

### Start Admin Panel

```bash
cd admin
npm run dev
```

### Start ML Service

```bash
cd ml-service
python app.py
```

---

## Future Enhancements

- AI Chatbot for Medical Assistance
- Online Video Consultation
- Electronic Health Records (EHR)
- Email & SMS Notifications
- Doctor Availability Calendar
- Medical Report Upload
- Prescription Management
- Health Analytics Dashboard

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
