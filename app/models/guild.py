# from typing import TYPE_CHECKING
# from sqlmodel import SQLModel, Field, Relationship
#
# # if TYPE_CHECKING:
# from app.models.channel import Channel, ChannelRead
#
#
# class GuildBase(SQLModel):
#     name: str
#     description: str | None = None
#     icon_url: str | None = None
#
#
# class Guild(GuildBase, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#
#     channels: list["Channel"] = Relationship(back_populates="guild")
#
#
# class GuildCreate(GuildBase):
#     pass
#
#
# class GuildUpdate(GuildBase):
#     pass
#
#
# class GuildRead(GuildBase):
#     id: int
#
#     channels: list["ChannelRead"]
