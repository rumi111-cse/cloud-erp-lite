from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_product():
    return {"msg": "product ok"}
