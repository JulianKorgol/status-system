from fastapi import APIRouter

from .views.general import *


router = APIRouter()
router.add_api_route("/is-alive", is_alive, methods=["GET"])
