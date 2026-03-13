# EduSustain AI: Dropout Prediction & Counseling System

EduSustain AI is a comprehensive web-based platform designed to identify students at risk of dropping out and provide them with personalized AI-driven counseling recommendations. Built with Python, Flask, and Scikit-learn, it offers a data-driven approach to educational retention.

## 🚀 Key Features

*   **AI Dropout Risk Prediction**: Uses a machine learning model to categorize student risk into Low, Medium, or High based on factors like attendance, marks, stress levels, and socio-economic indicators.
*   **Interactive Analytics Dashboard**: A sleek, real-time interface with visualizations for risk distribution, attendance trends, and feature importance.
*   **AI Counseling Chatbot**: A Virtual assistant that provides immediate academic and emotional support to students.
*   **Administrative Management**:
    *   Secure Admin Login & Management.
    *   Bulk student data processing via CSV upload.
    *   Automated PDF Summary Reports for individual students.
    *   Detailed Audit Logs for system transparency.
*   **Automated Alerts**: Email notification system for "High Risk" student identification.

## 🛠️ Technology Stack

*   **Backend**: Python, Flask
*   **Database**: SQLite
*   **Machine Learning**: Scikit-Learn (Random Forest/Gradien Boosting)
*   **Frontend**: HTML5, Vanilla CSS, Bootstrap 5, Chart.js
*   **PDF Generation**: ReportLab

## 📋 Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd ai_dropout_counseling_system
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

4. **Default Admin Login**:
   *   **Username**: `admin`
   *   **Password**: `Admin@123`

## 📊 Sample Data
You can use the included `seed_db.py` script to populate the dashboard with sample data for demonstration purposes:
```bash
python seed_db.py
```

---
*Created as a college project to demonstrate the application of AI in Educational Support Systems.*