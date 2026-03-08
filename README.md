AI Prediction Hub - Backend (FastAPI)

ระบบหลังบ้าน (Backend) สำหรับให้บริการโมเดล Machine Learning ผ่าน REST API โดยใช้ FastAPI Framework

🚀 ฟีเจอร์หลัก

Flight Price Prediction: ทำนายราคาตั๋วเครื่องบินด้วย Scikit-learn

Depression Screening: ประเมินความเสี่ยงภาวะซึมเศร้าด้วย Deep Learning

Animal Classification: จำแนกประเภทสัตว์จากรูปภาพด้วย Convolutional Neural Network (CNN)

Movie Recommendation: ระบบแนะนำหนังที่ใกล้เคียงโดยใช้ Similarity Search

🛠 เทคโนโลยีที่ใช้

Framework: FastAPI

Server: Uvicorn (ASGI)

ML Libraries: TensorFlow, Scikit-learn, Pandas, NumPy, Joblib

Data Validation: Pydantic

📦 การติดตั้งและรันระบบ

สร้างและเปิดใช้งาน Virtual Environment:

python -m venv venv
venv\Scripts\activate


ติดตั้งไลบรารีที่จำเป็น:

pip install -r requirements.txt


รันเซิร์ฟเวอร์:

uvicorn app.main:app --reload


หมายเหตุ: ระบบจะทำงานอยู่ที่ http://127.0.0.1:8000

📖 API Documentation

คุณสามารถเข้าดูและทดสอบ API ผ่านหน้า Swagger UI ได้ที่:

http://127.0.0.1:8000/docs

