from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# Генерация ключей
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Создание подписи
data = "Здраствуй мир!".encode('utf-8')
signature = private_key.sign(
    data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Для ", data.decode('utf-8'))

# Проверка подписи
try:
    public_key.verify(
        signature,
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Подпись верна!")
except Exception as e:
    print("Подпись недействительна:", e)

# Изменение данных для проверки недействительной подписи
data = "Здраствуй мир!!!".encode('utf-8')
print("Для ", data.decode('utf-8'))

# Проверка подписи
try:
    public_key.verify(
        signature,
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Подпись верна!")
except Exception as e:
    print("Подпись недействительна:", e)
