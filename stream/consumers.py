import json
from channels.generic.websocket import WebsocketConsumer
import cv2, base64, numpy as np
from asgiref.sync import async_to_sync
from pyzbar import pyzbar as pb
from io import BytesIO
from PIL import Image

class Streamer(WebsocketConsumer):
	def connect(self):
		self.accept()

	def disconnect(self, code):
		pass

	def receive(self, text_data):
		imgframe = text_data
		ext = imgframe.split(',')[0]
		data = imgframe.split(',')[1]
		# async_to_sync(self.channel_layer.send)({'type': 'modify_picture', 'ext': ext, 'data': data})
		# image = ext + self.modify_picture(data)

		img = base64.b64decode(data)
		img = BytesIO(img)
		img = Image.open(img)

		Read = pb.decode(img)
		for ob in Read:
			readData = str(ob.data.rstrip().decode('utf-8'))
			print('readData', readData)

		self.send(text_data=imgframe)

