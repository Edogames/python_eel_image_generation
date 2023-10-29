import os
import socket

def CheckConnection():
	try:
        # connect to the host -- tells us if the host is actually reachable
		socket.create_connection(("www.google.com", 80))
		return True
	except OSError:
		return False

def Clear():
	return os.system("cls" if os.name == 'nt' else "clear")

Clear()

if CheckConnection() == True:
	import sys
	import modules.moduleCheck as moduleCheck

	Clear()

	moduleCheck.Check()
	import requests
	import json
	import eel
	import base64
	import glob

	api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2OTg0MzcyMjQsInVzZXJfaWQiOiI2NTNjMTg2N2VjZDFjN2JkZTQ3YjQyNmYifQ.KigIVnnEOVKQ3tMgl3XkNVd67sW3_whOUdaF5hzK11s"

	diffusion_url = "https://api.wizmodel.com/sdapi/v1/txt2img"
	llama_url = "https://api.wizmodel.com/v1/predictions"

	eel.init("web")

	def convert_text_content_to_image_file(text_content, output_file_path):
		if len(glob.glob(f'./web/images/{output_file_path}*')) > 0:
			output_file_path = f"{output_file_path}_({len(glob.glob(f'./web/images/{output_file_path}*'))})"
		
		with open(f"./web/images/{output_file_path}.png", "wb") as fh:
			fh.write(base64.decodebytes(text_content.encode()))

		fh.close()

		print("Завершение работы...")
		if os.path.exists(f"./web/images/{output_file_path}.png"):
			print(f"Успешно создан файл web/images/{output_file_path}!")
			return {"status":True, "filename": output_file_path}
		else:
			print("Произошла ошибка!")
			return False

	@eel.expose
	def StableDiffusion(prompt: str):
		Clear()
		print("Начало работы Stable Diffusion...")
		payload = json.dumps({
			"prompt": prompt,
			"steps": 100
		})

		headers = {
			'Content-Type': 'application/json',
			'Authorization': 'Bearer '+api_key
		}

		response = requests.request("POST", diffusion_url, headers=headers, data=payload)

		if 'code' in response.json():
			return False

		text_content = response.json()["images"][0]

		home_directory = os.path.expanduser("~")

		# Return the path to the pictures folder
		output_file_path = prompt.replace(" ", "_")

		return convert_text_content_to_image_file(text_content, output_file_path)

	@eel.expose
	def GetImages():
		return glob.glob('./web/images/*.png')

	@eel.expose
	def ClearGallery():
		files = glob.glob('./web/images/*.png')
		for f in files:
			print(f"удаляем {f}...")
			os.remove(f)
		print("Галлерея теперь пуста!")
		return True

	@eel.expose
	def CheckNetwork():
		return CheckConnection()

	Clear()

	def CheckInput(text):
		if text.isdigit():
			return int(text)
		else:
			print("Не правельный ввод! Попробуйте ещё раз")
			print()
			return CheckInput(input())

	eel.start("index.html", size=(600, 525))
else:
	print("Прошу подключится к интернету, затем опять запустить программу, благодарю!")
