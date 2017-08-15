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

model.predict('./test/test2.jpg', './test/test2_output.jpg', 60, 'male')