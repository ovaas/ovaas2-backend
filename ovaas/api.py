from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Demo
from ninja import Schema

router = Router()


class DemoOut(Schema):
    id: str
    name_ja: str
    name_en: str
    description_ja: str
    description_en: str
    endpoint_url: str
    thumbnail_uri: str
    gui_type: str


@router.get(
    "/demo/{demo_id}",
    response=DemoOut,
    tags=["Demo"],
)
def get_demo(request, demo_id: int):
    demo = get_object_or_404(Demo, id=demo_id)
    return demo


@router.get(
    "/demo",
    response=List[DemoOut],
    tags=["Demo"],
)
def list_demo_list(request):
    demos = get_list_or_404(Demo)
    return demos
