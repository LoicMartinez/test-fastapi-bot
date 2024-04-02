# from typing import TYPE_CHECKING
# from sqlmodel import SQLModel, Field, Relationship
#
# if TYPE_CHECKING:
#     from app.models.channel import Channel
#     from app.models.message import Message
#     from app.models.user import User
#
#
# class ReactionBase(SQLModel):
#     count: int = Field(default=0)
#
#
# class Reaction(ReactionBase, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#
#     channel_id: int = Field(default=None, foreign_key="channel.id")
#     # channel: "Channel" = Relationship(back_populates=None)
#
#     message_id: int = Field(default=None, foreign_key="message.id")
#     # message: "Message" = Relationship(back_populates=None)
#
#     user_id: int = Field(default=None, foreign_key="user.id")
#     # user: "User" = Relationship(back_populates=None)
