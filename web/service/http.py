# -*- coding: utf8 -*-

from ..secret import *
import urllib
from datetime import datetime, timedelta

def wget(remote_path, save_path):
	urllib.urlretrieve(remote_path, save_path)

# Google Firebase Storage 관련 인스턴스들을 생성합니다
from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket(FIREBASE_BUCKET)

def upload_cloud(blobname, filename):
	blob = bucket.blob(blobname)
	blob.upload_from_filename(filename=filename)
	return blob.generate_signed_url(datetime.now() + timedelta(365))