from sqlalchemy import Column, BigInteger, String, Integer, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'  # Replace with your actual table name

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    token = Column(String(255), nullable=True, index=True)
    user_id = Column(BigInteger, nullable=True, index=True)
    user_order = Column(String(255), nullable=True)
    no_telepon = Column(String(255), nullable=True)
    produk = Column(String(255), nullable=True)
    jenis_transaksi = Column(String(255), nullable=False, default="pemasukan")
    jumlah_order = Column(Integer, nullable=True)
    alamat_order = Column(String(255), nullable=True)
    harga_order = Column(Integer, nullable=True)
    status_order = Column(String(255), nullable=False)
    pesan_order = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "token": self.token,
            "user_id": self.user_id,
            "user_order": self.user_order,
            "no_telepon": self.no_telepon,
            "produk": self.produk,
            "jenis_transaksi": self.jenis_transaksi,
            "jumlah_order": self.jumlah_order,
            "alamat_order": self.alamat_order,
            "harga_order": self.harga_order,
            "status_order": self.status_order,
            "pesan_order": self.pesan_order,
        }
