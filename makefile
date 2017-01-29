despliegue:
	vagrant up --provider=azure
	vagrant provision

install:
	sudo pip install -r requirements.txt

test:
	cd ActividadesUGRBot && python test.py

ejecutar:
	cd ActividadesUGRBot && python actividadesUGR_bot.py

parar:
	fab -H vagrant@40.68.201.43 StopApp

provision:
	vagrant provision
