from fastapi import APIRouter
from controllers.post_controller import PostController
from models.marp import Marp

router = APIRouter()
post_controller = PostController()

@router.post("/share/{uuid}")
def create_post(uuid: str, marp: Marp):
    return post_controller.create_post(uuid, marp)

@router.get("/share/{uuid}")
def get_post(uuid: str):
    return post_controller.get_post(uuid)