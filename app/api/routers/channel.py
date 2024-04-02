from fastapi import APIRouter, HTTPException, status

from app.api.deps import SessionDep
from app.crud.channel import crud_channel
from app.models.models import ChannelCreate, ChannelWithGuildRead

router = APIRouter()


@router.get("/{channel_id}", response_model=ChannelWithGuildRead, status_code=status.HTTP_200_OK)
async def get_channel(session: SessionDep, channel_id: int):
    channel = crud_channel.get(session, channel_id)
    if not channel or not channel.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    print(channel.dict())

    return channel


@router.post("/", response_model=ChannelWithGuildRead, status_code=status.HTTP_200_OK)
async def create_channel(session: SessionDep, channel_in: ChannelCreate):
    channel = crud_channel.create(session, channel_in)

    return channel
