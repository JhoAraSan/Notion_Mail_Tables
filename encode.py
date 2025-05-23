from cryptography.fernet import Fernet #pip install 
from tkinter import filedialog
#este codigo genera una clave de encriptacion en un archivo llamado secret.key, solo se debe ejecutar una vez.
def gen_key():
    output_path = filedialog.asksaveasfilename(
        title="Guardar archivo PDF combinado",
        defaultextension=".key",
        filetypes=[("Claves de Seguridad", "*.key")]  # Opcional: Filtra por tipo de archivo
    )
    key = Fernet.generate_key()
    with open(output_path, "wb") as key_file:
        key_file.write(key)
    print(f"🔑 Clave generada y guardada en '{output_path}'")

#este codigo encripta una contraseña y la imprime en la consola, se debe ejecutar cada vez que se quiera encriptar una nueva contraseña.
def enc_data(value):
    input_path = filedialog.askopenfilename(
        title="Seleccione la llave de encriptación",
        filetypes=[("Claves de Seguridad", "*.key")]
    )
    if not input_path:
        return

    with open(input_path, "rb") as key_file:
        key = key_file.read()

    fernet = Fernet(key)

    password = value
    encrypted = fernet.encrypt(password.encode())

    print("Contraseña encriptada:")
    print(encrypted.decode())

def dec_data(value):
    input_path = filedialog.askopenfilename(
        title="Seleccione la llave de encriptación",
        filetypes=[("Claves de Seguridad", "*.key")]
    )
    if not input_path:
        return

    with open(input_path, "rb") as key_file:
        key = key_file.read()

    fernet = Fernet(key)

    password = value
    decrypted = fernet.decrypt(password.encode())

    print("Contraseña desencriptada:")
    print(decrypted.decode())

if __name__ == "__main__":
    value=input("seleccione una opción:\n1. Desencriptar\n2. Encriptar\n3. Generar clave\n")
    # value=input("Contraseña a encriptar o desencriptar:\n")
    if value=="3":
        print("Gen Key")
        gen_key()
    elif value=="1":
        value=input("Contraseña a desencriptar:\n")
        dec_data(value)
    elif value=="2":
        value=input("Contraseña a encriptar:\n")
        enc_data(value)
    else:
        print("Opción no válida")
