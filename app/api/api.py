from fastapi import APIRouter

from app.api.routers import channel, guild

api_router = APIRouter()

api_router.include_router(guild.router, prefix="/guild", tags=["guild"])
api_router.include_router(channel.router, prefix="/channel", tags=["channel"])
