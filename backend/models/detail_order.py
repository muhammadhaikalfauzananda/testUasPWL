from sqlalchemy import Column, BigInteger, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Transaksi(Base):
    __tablename__ = 'detail_order'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    list_id = Column(BigInteger, nullable=True, index=True)
    opsi_pengiriman = Column(String(255), nullable=True)
    pembayaran = Column(String(255), nullable=True)
    foto_pembayaran = Column(String(255), nullable=True)
    no_rekening = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "list_id": self.list_id,
            "opsi_pengiriman": self.opsi_pengiriman,
            "pembayaran": self.pembayaran,
            "foto_pembayaran": self.foto_pembayaran,
            "no_rekening": self.no_rekening,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
