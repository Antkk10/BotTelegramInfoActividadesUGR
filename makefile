install:
	sudo apt-get update
	sudo apt-get install postgresql
	pip install -r requirements.txt

test:
	cd ActividadesUGRBot && python test.py

ejecutar:

	cd ActividadesUGRBot && python actividadesprueba.py && python actividadesUGR_bot.py
