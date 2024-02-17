import requests
import zipfile
from io import BytesIO

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception("Error al descargar la imagen")

def save_image(content, filename):
    with open(filename, 'wb') as f:
        f.write(content)

def zip_image(image_filename, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(image_filename)

def unzip_image(zip_filename, extract_path):
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        zipf.extractall(extract_path)

def main():
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    image_content = download_image(url)
    image_filename = "downloaded_image.jpg"
    save_image(image_content, image_filename)

    zip_filename = "image_zip.zip"
    zip_image(image_filename, zip_filename)

    extract_path = "unzipped_images"
    unzip_image(zip_filename, extract_path)

    print("Imagen descargada y almacenada como archivo zip, y luego descomprimida con éxito.")

if __name__ == "__main__":
    main()
