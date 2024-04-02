from datetime import datetime

from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, false, text
from sqlmodel import Field, Relationship, SQLModel

###
# Base models
###


class GuildBase(SQLModel):
    name: str
    description: str | None = None
    icon_url: str | None = None


class ChannelBase(SQLModel):
    name: str
    enabled: bool = Field(default=False, sa_column=Column(Boolean, server_default=false(), nullable=False))
    deleted: bool = Field(default=False, sa_column=Column(Boolean, server_default=false(), nullable=False))


class MessageBase(SQLModel):
    image_url: str


class ReactionBase(SQLModel):
    count: int = Field(default=0, sa_column=Column(Integer, server_default="0"))


class UserBase(SQLModel):
    name: str


class UserGuildInfoBase(SQLModel):
    pseudo: str = Field(nullable=True)
    exp: int = Field(default=0, sa_column=Column(Integer, server_default="0"))
    level: int = Field(default=0, sa_column=Column(Integer, server_default="0"))


###
# Database models
###


class UserGuildInfoDB(UserGuildInfoBase, table=True):
    __tablename__ = "user_guild_info"

    id: int | None = Field(default=None, primary_key=True)

    user_id: int = Field(default=None, foreign_key="user.id", primary_key=True)

    guild_id: int = Field(default=None, foreign_key="guild.id", primary_key=True)


class GuildDB(GuildBase, table=True):
    __tablename__ = "guild"

    id: int | None = Field(default=None, primary_key=True)

    channels: list["ChannelDB"] = Relationship(back_populates="guild")

    users: list["UserDB"] = Relationship(back_populates="guilds", link_model=UserGuildInfoDB)


class ChannelDB(ChannelBase, table=True):
    __tablename__ = "channel"

    id: int | None = Field(default=None, primary_key=True)

    guild_id: int = Field(default=None, foreign_key="guild.id")
    guild: "GuildDB" = Relationship(back_populates="channels")


class MessageDB(MessageBase, table=True):
    __tablename__ = "message"

    id: int | None = Field(default=None, primary_key=True)
    insert_at: datetime = Field(
        sa_column=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    )
    send_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
        )
    )

    user_id: int = Field(default=None, foreign_key="user.id")
    user: "UserDB" = Relationship(back_populates=None)

    channel_id: int = Field(default=None, foreign_key="channel.id")
    channel: "ChannelDB" = Relationship(back_populates=None)

    reaction: list["ReactionDB"] = Relationship(back_populates="message")


class ReactionDB(ReactionBase, table=True):
    __tablename__ = "reaction"

    id: int | None = Field(default=None, primary_key=True)

    channel_id: int = Field(default=None, foreign_key="channel.id")
    channel: "ChannelDB" = Relationship(back_populates=None)

    message_id: int = Field(default=None, foreign_key="message.id")
    message: "MessageDB" = Relationship(back_populates="reaction")

    user_id: int = Field(default=None, foreign_key="user.id")
    user: "UserDB" = Relationship(back_populates=None)


class UserDB(UserBase, table=True):
    __tablename__ = "user"

    id: int | None = Field(default=None, primary_key=True)

    guilds: list["GuildDB"] = Relationship(back_populates="users", link_model=UserGuildInfoDB)


###
# Create models
###


class GuildCreate(GuildBase):
    pass


class ChannelCreate(ChannelBase):
    guild_id: int = Field(foreign_key="guild.id")


###
# Read models
###


class GuildRead(GuildBase):
    id: int


class GuildWithChannelsRead(GuildRead):
    channels: list["ChannelRead"] = []

    users: list["UserRead"] = []


class ChannelRead(ChannelBase):
    id: int
    guild_id: int


class ChannelWithGuildRead(ChannelRead):
    guild: "GuildRead" = None


class UserRead(UserBase):
    id: int


###
# Update models
###


class GuildUpdate(GuildBase):
    pass


class ChannelUpdate(ChannelBase):
    pass
