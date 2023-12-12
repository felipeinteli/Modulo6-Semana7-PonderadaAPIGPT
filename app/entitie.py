from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
)

# Criação do banco de dados
Base = declarative_base()


class HistoryEntity(Base):
    __tablename__ = 'historys_tb'

    id = Column(Integer, primary_key=True, autoincrement=True)
    prompt = Column(String(200), nullable=True)
    resposta = Column(String(50000), nullable=True)
