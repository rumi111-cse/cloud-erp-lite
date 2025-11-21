from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_org():
    return {"msg": "organization ok"}
