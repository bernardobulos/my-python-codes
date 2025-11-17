# Este código gera um QR Code a partir de um texto ou URL fornecido pelo usuário, salva o arquivo como PNG em uma pasta específica e garante que o nome do arquivo seja válido removendo caracteres proibidos. 🇧🇷
# This code generates a QR Code from a user-provided text or URL, saves the file as a PNG in a designated folder, and ensures the file name is valid by removing forbidden characters. 🇺🇸
# Este código genera un código QR a partir de un texto o una URL proporcionado por el usuario, guarda la imagen como PNG en una carpeta específica y garantiza que el nombre del archivo sea válido eliminando caracteres no permitidos. 🇪🇸
# Ce code génère un QR Code à partir d’un texte ou d’une URL fourni par l’utilisateur, enregistre l’image en PNG dans un dossier spécifique et garantit que le nom du fichier est valide en supprimant les caractères interdits. 🇫🇷

import qrcode
import os
import re

def generate_qrcode(url, file_path):
    qr = qrcode.QRCode()
    qr.add_data(url)
    img = qr.make_image()
    img.save(file_path)

url = input("Enter the URL or text: ").strip()
file_name = input("Enter the file name (without extension): ").strip()

file_name = re.sub(r'[<>:\"/\\|?*]', "", file_name)
if not file_name:
    file_name = "qrcode"

folder = os.path.join(os.path.expanduser("~"), "Desktop", "qrcode_files")
os.makedirs(folder, exist_ok=True)

file_path = os.path.join(folder + file_name + ".png")

generate_qrcode(url, file_path)

print(f"QR Code saved as: {file_name}.png.")
