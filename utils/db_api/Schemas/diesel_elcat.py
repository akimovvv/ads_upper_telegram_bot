from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, sql
from .user import User
from utils.db_api.db_gino import TimedBaseModel


class Diesel_data(TimedBaseModel):
    __tablename__ = 'diesel_login_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100))
    password = Column(String(100))
    user_id = Column(BigInteger, ForeignKey(User.id))

    query: sql.Select