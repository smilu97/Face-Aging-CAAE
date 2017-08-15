# -*- coding: utf8 -*-

# 기본 인코딩을 UTF8로 변경합니다
import imp, sys
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except: pass

GOOGLE_APPLICATION_CREDENTIALS = 'credential.json'
from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()

# 플라스크 모듈을 설정합니다
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)  # CORS 헤더들을 자동으로 추가해주도록 합니다

# 플라스크 라우팅 함수들을 연결해줍니다
from route import register_all_blueprints

register_all_blueprints(app)