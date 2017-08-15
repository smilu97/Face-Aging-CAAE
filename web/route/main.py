# -*- coding: utf8 -*-

from flask import Blueprint, jsonify, request

app = Blueprint('main', __name__)

from ..service.faceaging import predict as predict_face
from ..service.http import wget, upload_cloud


@app.route('/', methods=['GET'])
def get_home():
	'''
		헬로 월드!
	'''
	return 'Hello World'


'''
Sample Request
{
	“user_key” : ”-KrMoTYXieZCGXvDSUXR”,
	“orig_image_url” : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_PN3ZFNxCcqO6bZpsl9DqCbBKvrFXt6BxYcyNkPgIgSI4AMAtgQ”,
	“missing-time” : 960994800000,
        "age" : 8
}
'''

@app.route('/predict', methods=['POST'])
def post_predict():
	'''
		description:
			인물 사진을 받아서 특징을 분석해낸 후에,
			만약 연령, 성별이 이랬다면 어땠을지 예측한 사진을
			클라우드에 업로드합니다.
		parameters:
			orig_image_url:
				이미지를 받을 수 있는 주소
			user_key: 
				클라우드에 올릴 장소
			age:
				예측할 연령
			gender:
				예측할 성별
				'male'이라면 남성으로, 그렇지 않다면 여성으로 처리합니다
	'''
	body = request.get_json()

	# 필수 파라미터 존재 여부 확인
	parameters = ['user_key', 'orig_image_url', 'age', 'gender']
	for param in parameters:
		if body.get(param) is None:
			return jsonify({'success': 0, 'message': '{} 파라미터가 없습니다'.format(param)})

	# 파라미터 추출
	user_key      = body['user_key']
	orig_image_url        = body['orig_image_url']
	age              = body['age']
	gender           = body['gender']

	rand_number = random.randint(1, 1000000000)
	cache_file_path = './cache/{}_{}_{}'.format(age, gender, rand_number)

	# 웹에서 원본이미지 다운로드
	wget(orig_image_url, cache_file_path + '.in')

	predict_face(
		image_in_path=cache_file_path + '.in',
		image_out_path=cache_file_path + '.out',
		age=age,
		gender=gender
	)

	upload_path = '{}/{}'.format(user_key, rand_number)

	public_url = upload_cloud(upload_path, cache_file_path + '.out')

	return jsonify({'success': 1, 'afterUrl': public_url})
