from fastapi import APIRouter

router = APIRouter()


@router.get("/v1/health")
def route_v1_health():
    return {"status": "OK"}
