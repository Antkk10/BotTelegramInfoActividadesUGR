despliegue:
	vagrant up --provider=azure
	vagrant provision

install:
	fab -H vagrant@40.68.201.43 InstalaAplicacion

test:
	fab -H vagrant@40.68.201.43 TestApp

ejecutar:
	fab -H vagrant@40.68.201.43 EjecutarApp

parar:
	fab -H vagrant@40.68.201.43 StopApp

provision:
	vagrant provision
