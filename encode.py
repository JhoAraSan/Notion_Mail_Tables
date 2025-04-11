from cryptography.fernet import Fernet

#este codigo genera una clave de encriptacion en un archivo llamado secret.key, solo se debe ejecutar una vez.
def gen_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("🔑 Clave generada y guardada en 'secret.key'")

#este codigo encripta una contraseña y la imprime en la consola, se debe ejecutar cada vez que se quiera encriptar una nueva contraseña.
def enc_data(value):
    with open("secret.key", "rb") as key_file:
        key = key_file.read()

    fernet = Fernet(key)

    password = value
    encrypted = fernet.encrypt(password.encode())

    print("Contraseña encriptada:")
    print(encrypted.decode())

if __name__ == "__main__":
    #gen_key()
    value=input("Introduce la contraseña a encriptar: ")
    enc_data(value)