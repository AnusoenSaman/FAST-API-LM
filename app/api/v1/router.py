from fastapi import APIRouter

# นำเข้า router ทั้ง 4 หัวข้อของเพื่อนกลับมา
from .flight.route import router as flight_router
from .depression.route import router as depression_router
from .animal.route import router as animal_router
from .recommend.route import router as recommend_router

# สร้างปลั๊กพ่วงหลักชื่อ app_router (เพื่อให้ตรงกับที่ main.py เรียกหา)
app_router = APIRouter()

# เสียบปลั๊กทั้ง 4 หัวข้อเข้าด้วยกัน
app_router.include_router(flight_router, prefix='/flight', tags=['Flight Price Prediction'])
app_router.include_router(depression_router, prefix='/depression', tags=['Depression Classification'])
app_router.include_router(animal_router, prefix='/animal', tags=['Animal Image Classification'])
app_router.include_router(recommend_router, prefix='/recommend', tags=['Recommendations'])