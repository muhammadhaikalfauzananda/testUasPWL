from cornice import Service
import json
from pyramid.response import Response

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models import Pengguna
import bcrypt
import jwt
import datetime

engine = create_engine('mysql+pymysql://root:@localhost:3306/belanjainaja')
Session = sessionmaker(bind=engine)
session = Session()


def create_response(jenis_pesan, isi_pesan, status):
    response_json = {
        jenis_pesan: isi_pesan
    }
    response = Response(
        json.dumps(response_json),
        content_type='application/json; charset=utf-8',
        status=status
    )
    return response


login = Service(
    name='login',
    path='/login',
    cors_origins=("*",),
)


def hash_password(password):
    # Membuat salt
    salt = bcrypt.gensalt()

    # Membuat hash dari password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


secret_key = "tubespwl"


def create_jwt_token(id_pengguna, email, expiration_hours=1):
    # Data yang ingin dimasukkan ke dalam token (payload)
    payload = {
        "id_pengguna": id_pengguna,
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=expiration_hours)
    }

    # Membuat token
    token = jwt.encode(payload, secret_key, algorithm='HS256')

    return token


@login.post()
def login_post(request):
    data = request.json_body
    # Deklarasi sesi di database
    session = request.dbsession
    # Mendapatkan data pengguna dari database
    all_accounts = session.query(Pengguna).all()
    # Membuat list data dari semua pengguna
    pengguna_list = [account.to_dict() for account in all_accounts]

    # Inisialisasi variabel untuk menyimpan hasil autentikasi
    authentication_result = None
    # Mencocokan user dengan data di server
    for existing_account in pengguna_list:
        if data["email"] == existing_account["email"]:
            # Menggunakan bcrypt untuk memeriksa kecocokan password
            if bcrypt.checkpw(data["password"].encode('utf-8'), existing_account["password"].encode('utf-8')):
                authentication_result = create_response(
                    "respon", create_jwt_token(existing_account["id"], existing_account["email"]), 200)
            else:
                authentication_result = create_response(
                    "error", "Password salah", 400)
            break

    # Jika tidak ada kecocokan akun, maka email belum terdaftar
    if authentication_result is None:
        authentication_result = create_response(
            "error", "Email belum terdaftar", 400)

    return authentication_result


register = Service(
    name='register',
    path='/register',
    cors_origins=("*",),
)


@register.post()
def register_post(request):
    data = request.json_body
    # Deklarasi sesi di database
    session = request.dbsession
    # Mendapatkan data pengguna dari database
    all_accounts = session.query(Pengguna).all()
    # Membuat list data dari semua pengguna
    pengguna_list = [account.to_dict() for account in all_accounts]

    # Mencoocokan user dengan data di server
    for existing_account in pengguna_list:
        if data["email"] == existing_account["email"]:
            return create_response("error", "Email sudah terdaftar dalam sistem.", 409)
    # Jika email belum terdaftar, tambahkan pengguna baru
    required_fields = ('email', 'password', 'nama')
    if all(data.get(field) for field in required_fields) and all(data.get(field) != "" for field in required_fields):
        pengguna = Pengguna(
            nama=data.get('nama'),
            email=data.get('email'),
            no_telepon=data.get('no_telepon'),
            password=hash_password(data.get('password')),
            roles_id=data.get('roles_id')
        )
        session.add(pengguna)
        session.flush()
        return create_response("success", "Berhasil membuat akun data", 200)
    else:
        return create_response("error", "Gagal mengirimkan data login", 400)
