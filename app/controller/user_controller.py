from flask import Flask ,jsonify, request, abort

users = []

def validate_user_data(data):

    # Gerekli alanların mevcut olup olmadığını kontrol edin
    if 'name' not in data or 'surname' not in data or 'phone' not in data or 'email' not in data:
        abort(400, 'Eksik bilgiler var...')

    if not isinstance(data['name'], str):
        return jsonify("isim için yanlış karakter kullandınız!")

    if not isinstance(data['surname'], str):
        return jsonify("soyisim için yanlış karakter kullandınız!")

    return True

    def validate_user_data(data):
    def create_new_user_controller():


    name = data['name']
    surname = data['surname']
    phone = data['phone']
    email = data['email']


    user = {'name': name, 'surname': surname, 'phone': phone, 'email': email}

    # Kullanıcıyı veritabanına ekleyin
    users.append(user)

    return jsonify({'message': 'Kullanıcı oluşturuldu', 'user': user})
