# -*- coding: utf8 -*-

from ..secret import *
import urllib

def wget(remote_path, save_path):
	urllib.urlretrieve(remote_path, save_path)

# Google Firebase Storage 관련 인스턴스들을 생성합니다
from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket(FIREBASE_BUCKET)

def upload_cloud(blobname, filename):
	blobname = bucket.get_blob(blob)
	blob.upload_from_filename(filename=filename)