from fastapi import APIRouter

from .views.user import *

router = APIRouter()
router.add_api_route("/user/sign/in", user_sign_in, methods=["POST"])
router.add_api_route("/user/sign/out", user_sign_out, methods=["GET"])
