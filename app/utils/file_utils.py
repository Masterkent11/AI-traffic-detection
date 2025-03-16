import os
from werkzeug.utils import secure_filename
from app.config import Config


def save_uploaded_file(file):
    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)

    except Exception as e:
        print(f'Error saving file: {e}')
        return None