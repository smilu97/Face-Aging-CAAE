# -*- coding: utf8 -*-

import sys
sys.path.insert(0, '../..')

from FaceAging import FaceAging
import tensorflow as tf

config = tf.ConfigProto()
session = tf.Session(config=config)
model = FaceAging(
	session,
	is_training = False,
	save_dir = './save',
	dataset_name = 'UTKFace'
)

if model.load_checkpoint():
	print 'Success!'
else:
	print 'Failed..'
	exit(0)

def predict(image_in_path, image_out_path, age, gender):
	'''
		description:
			이미지를 읽어서 나이, 성별을 바꾼 모습을 예측합니다
		parameters:
			image_in_path:
				원본 사진의 로컬 경로
			image_out_path:
				예측한 사진이 저장될 로컬경로
			age:
				예측할 나이
			gender:
				예측할 성별
				'male'이면 남자, 그렇지 않으면 여자
	'''
	model.predict(image_in_path, image_out_path, age, gender)