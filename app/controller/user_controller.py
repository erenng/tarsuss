from flask import jsonify, abort

from app.service import user_service

users = []


def validate_user_data(data):
    # Gerekli alanların mevcut olup olmadığını kontrol edin
    if 'name' not in data or 'surname' not in data or 'phone' not in data or 'email' not in data or 'password' not in data:
        return abort(400, 'Eksik bilgiler var...')

    if not isinstance(data['name'], str):
        return abort(400, "isim için yanlış karakter kullandınız!")

    if not isinstance(data['surname'], str):
        return abort(400, "soyisim için yanlış karakter kullandınız!")

    if not isinstance(data['phone'], str):
        return abort(400, "telefon için yanlış karakter kullandınız!")

    if not isinstance(data['email'], str):
        return abort(400, "email için yanlış karakter kullandınız!")

    if not isinstance(data['password'], str):
        return abort(400, "şifre için yanlış karakter kullandınız!")

    return True


def create_new_user_controller(request):
    data = request.get_json() or {}

    validate_user_data(data)

    if user_service.get_user_by_email_service(data['email']):
        return abort(400, "Üyelik bulunmaktadır")

    if user_service.create_user_service(data):
        return jsonify(message="Üyelik Başarılı")

    return jsonify(message="HATA!")


def login_controller(request):
    data = request.get_json() or {}

    if 'password' not in data or 'email' not in data:
        return abort(400, "Bilgileri eksiksiz gönderin")

    if user_service.auth_user_service(data['password'], data['email']):
        return jsonify("Giriş başarılı")

    return abort(401, "Email ve Şifre kontrol ediniz")