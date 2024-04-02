# from sqlalchemy import Column, Integer
# from sqlmodel import SQLModel, Field
#
#
# class UserGuildInfoBase(SQLModel):
#     pseudo: str = Field(nullable=True)
#     exp: int = Field(default=0, sa_column=Column(Integer, server_default="0"))
#     level: int = Field(default=0)
#
#
# class UserGuildInfo(UserGuildInfoBase, table=True):
#     __tablename__ = "user_guild_info"
#
#     id: int | None = Field(default=None, primary_key=True)
#
#     user_id: int = Field(default=None, foreign_key="user.id")
#
#     guild_id: int = Field(default=None, foreign_key="guild.id")
