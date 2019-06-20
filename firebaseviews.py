from firebase import firebase
from firebase_admin import storage
from firebase_admin import credentials
import firebase_admin
import os
from . import settings


firebaseConfig = {
    "apiKey": "AIzaSyDdlIsZVaGEzRWTKOR_n0KDf-TTnVqNjh8",
    "authDomain": "concrete-zephyr-244112.firebaseapp.com",
    "databaseURL": "https://concrete-zephyr-244112.firebaseio.com",
    "projectId": "concrete-zephyr-244112",
    "storageBucket": "",
    "messagingSenderId": "803790513672",
    "appId": "1:803790513672:web:1f1dfb169bfd6802"
  }
firebaseview = firebase.initialize_app(firebaseConfig)
base_dir = settings.BASE_DIR
cert_dir = os.path.join(BASE_DIR, 'gd-mimic-11b6d082299b.json')

credentialss = credentials.Certificate(cert_dir)
firebase_admin.initialize_app(credentialss, {
    'storageBucket': 'gd-mimic.appspot.com'
})

bucket = storage.bucket()

source_file_name = os.path.join(BASE_DIR, "media")

def upload_files(MyDrive, source_file_name, files):
    """file upload """
    storage_client = storage.Client()
    buck = storage_client.get_bucket('MyDrive')
    load = buck.load(files)

    load.upload_from_filename(source_file_name)
