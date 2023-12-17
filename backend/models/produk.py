from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Text,
    Integer,
    TIMESTAMP
)
from sqlalchemy.orm import relationship

from .meta import Base


class Produk(Base):
    __tablename__ = 'produk'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    kategori_id = Column(BigInteger, nullable=True, index=True)
    gambar_produk = Column(String(255), nullable=True)
    nama_produk = Column(String(255), nullable=False)
    deskripsi_produk = Column(Text, nullable=False)
    stok_produk = Column(Integer, nullable=False)
    harga_produk = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "kategori_id": self.kategori_id,
            "gambar_produk": self.gambar_produk,
            "nama_produk": self.nama_produk,
            "deskripsi_produk": self.deskripsi_produk,
            "stok_produk": self.stok_produk,
            "harga_produk": self.harga_produk,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
