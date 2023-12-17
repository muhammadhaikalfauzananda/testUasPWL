from sqlalchemy import (
    Column,
    BigInteger,
    String,
    TIMESTAMP
)
from sqlalchemy.orm import relationship

from .meta import Base


class Pengguna(Base):
    __tablename__ = 'pengguna'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nama = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, index=True)
    gambar_user = Column(String(255), nullable=True)
    no_telepon = Column(String(255), nullable=True)
    password = Column(String(255), nullable=False)
    roles_id = Column(BigInteger, nullable=True, default=99, index=True)
    remember_token = Column(String(100), nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nama": self.nama,
            "email": self.email,
            "gambar_user": self.gambar_user,
            "no_telepon": self.no_telepon,
            "password": self.password,
            "roles_id": self.roles_id,
            "remember_token": self.remember_token,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
