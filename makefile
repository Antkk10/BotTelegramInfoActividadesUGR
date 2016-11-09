install:
	pip install -r requirements.txt
	sudo apt install postgresql

test:
	cd ActividadesUGRBot && python test.py

ejecutar:
	cd ActividadesUGRBot && python actividadesUGR_bot.py
