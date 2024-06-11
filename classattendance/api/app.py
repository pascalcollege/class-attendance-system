"""
-- Created by: Ashok Kumar Pant
-- Email: asokpant@gmail.com
-- Created on: 11/06/2024
"""

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from classattendance.api.controller import face_detection, face_enrollment, face_attendance
from classattendance.entities.api_res import ApiResponse
from classattendance.utils.settings import Settings

app = FastAPI(title="Pascal Class Attendance System API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def hc():
    return ApiResponse(error=False, msg="Ok", result={"status": "OK"})


app.include_router(face_detection.router)
app.include_router(face_enrollment.router)
app.include_router(face_attendance.router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=Settings.API_PORT)
