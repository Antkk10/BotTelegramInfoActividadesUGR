install:
	#sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
	#echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
	sudo apt-get update
	sudo apt-get install -y mongodb
	pip install -r requirements.txt

test:
	cd ActividadesUGRBot && python test.py

ejecutar:

	cd ActividadesUGRBot && python actividadesprueba.py && python actividadesUGR_bot.py
