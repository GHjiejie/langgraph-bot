"""User API routes"""

from fastapi import APIRouter 

router=APIRouter(prefix="/user", tags=["User"])


@router.get("/")
async def get_user():
  """
  获取当前用户的信息
  """
  return {"message": "Get user information"}