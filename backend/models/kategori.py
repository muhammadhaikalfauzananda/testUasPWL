from sqlalchemy import Column, BigInteger, String, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Kategori(Base):
    __tablename__ = 'kategori'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    gambar_kategori = Column(String(255), nullable=True)
    nama_kategori = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "gambar_kategori": self.gambar_kategori,
            "nama_kategori": self.nama_kategori,
        }
