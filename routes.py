from fastapi import APIRouter
from controllers.prediction_controllers import router as ml_router

router = APIRouter()

router.include_router(ml_router)
