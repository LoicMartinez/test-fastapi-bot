from fastapi import APIRouter, HTTPException, status

from app.api.deps import SessionDep
from app.crud.guild import crud_guild
from app.models.models import GuildCreate, GuildDB, GuildWithChannelsRead

router = APIRouter()


@router.get("/{guild_id}", response_model=GuildWithChannelsRead, status_code=status.HTTP_200_OK)
async def get_guild(session: SessionDep, guild_id: int):
    guild = session.get(GuildDB, guild_id)
    if not guild or not guild.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    print(guild.dict())
    print(guild.channels)
    return guild


@router.post("/", response_model=GuildWithChannelsRead, status_code=status.HTTP_200_OK)
async def create_guild(session: SessionDep, guild_in: GuildCreate):
    guild = crud_guild.create(session, guild_in)

    return guild
