# 🍽️ Food Recommendation System with Ranking Optimization

## 📌 Overview
Built a hybrid recommendation system combining collaborative filtering (ALS) and content-based filtering to improve food recommendations.

---

## 🚀 Features
- Hybrid recommendation system (Collaborative + Content-based)
- Feature engineering (cuisine, price bucket, popularity)
- Ranking optimization for better recommendation ordering
- Evaluation using precision@k and recall@k
- Flask API for real-time recommendations

---

## 🧠 Tech Stack
- Python, Pandas, NumPy
- Scikit-learn
- ALS (implicit library)
- PySpark (basic usage)
- Flask API

---

## ⚙️ Pipeline
Data → Preprocessing → Feature Engineering → Model → Ranking → Evaluation → API

---

## 📊 Evaluation Metrics
- Precision@K
- Recall@K

---

## ▶️ Run the Project

```bash
pip install -r requirements.txt
python src/api.py
