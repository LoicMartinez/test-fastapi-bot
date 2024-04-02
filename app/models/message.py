# from typing import TYPE_CHECKING
# from sqlmodel import SQLModel, Field, Column, TIMESTAMP, text, Relationship
#
# from datetime import datetime
#
# if TYPE_CHECKING:
#     from app.models.channel import Channel
#     from app.models.reaction import Reaction
#     from app.models.user import User
#
#
# class MessageBase(SQLModel):
#     image_url: str
#
#
# class Message(MessageBase, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     insert_at: datetime = Field(sa_column=Column(
#         TIMESTAMP(timezone=True),
#         nullable=False,
#         server_default=text("CURRENT_TIMESTAMP")
#     ))
#     send_at: datetime = Field(sa_column=Column(
#         TIMESTAMP(timezone=True),
#         nullable=False,
#     ))
#
#     user_id: int = Field(default=None, foreign_key="user.id")
#     # user: "User" = Relationship(back_populates=None)
#
#     channel_id: int = Field(default=None, foreign_key="channel.id")
#     # channel: "Channel" = Relationship(back_populates=None)
#
#     # reaction: list["Reaction"] = Relationship(back_populates=None)
