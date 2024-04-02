# from sqlalchemy import Column, Boolean, false
# from sqlmodel import SQLModel, Field, Relationship
#
#
# from typing import TYPE_CHECKING
#
# if TYPE_CHECKING:
#   from app.models.guild import Guild, GuildRead
#
#
# class ChannelBase(SQLModel):
#     name: str
#     enabled: bool = Field(default=False, sa_column=Column(Boolean, server_default=false(), nullable=False))
#     deleted: bool = Field(default=False, sa_column=Column(Boolean, server_default=false(), nullable=False))
#
#
# class Channel(ChannelBase, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#
#     guild_id: int = Field(default=None, foreign_key="guild.id")
#     guild: "Guild" = Relationship(back_populates="channels")
#
#
# class ChannelRead(ChannelBase):
#     id: int
#
#     guild_id: int
#
#     guild: "Guild" = Relationship(back_populates="channels")
#
#
# class ChannelCreate(ChannelBase):
#     guild_id: int = Field(foreign_key="guild.id")
#
#
# class ChannelUpdate(ChannelBase):
#     pass
