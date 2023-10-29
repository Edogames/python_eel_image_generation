def Check():
	import os
	try:
		import requests
		print("Модуль 'requests' установлен")
	except ModuleNotFoundError:
		print("Модуль 'requests' не установлен! Устанавливаем...")
		os.system("pip install requests")
	try:
		import eel
		print("Модуль 'eel' установлен")
	except ModuleNotFoundError:
		print("Модуль 'eel' не установлен! Устанавливаем...")
		os.system("pip install eel")
	try:
		import json
		print("Модуль 'json' установлен")
	except ModuleNotFoundError:
		print("Модуль 'json' не установлен! Устанавливаем...")
		os.system("pip install json")
	try:
		import base64
		print("Модуль 'base64' установлен")
	except ModuleNotFoundError:
		print("Модуль 'base64' не установлен! Устанавливаем...")
		os.system("pip install base64")
	try:
		import glob
		print("Модуль 'glob' установлен")
	except ModuleNotFoundError:
		print("Модуль 'glob' не установлен! Устанавливаем...")
		os.system("pip install glob")
	
	print("Проверка модулей прошла успешно!")
