Vagrant.configure('2') do |config|
  config.vm.box = 'azure' # Indicamos donde estará la caja
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box' # Caja vacía
  config.vm.hostname = 'localhost'
  config.vm.network "public_network"
  config.vm.network "private_network",ip: "192.168.50.4", virtualbox__intnet: "vboxnet0" #Ip privada
  config.vm.network "forwarded_port", guest: 80, host: 80 # puerto de escucha.
  # ssh
  config.ssh.username = 'vagrant'
  config.ssh.private_key_path = File.expand_path('~/.ssh/id_rsa')

  config.vm.provider :azure do |azure|
    # Indicamos el SO en azure.
    azure.vm_image_urn = 'canonical:ubuntuserver:16.04.0-LTS:16.04.201606270'
    azure.location = 'westeurope' # Localización
    azure.vm_name = 'BotActividadesUGR'
    azure.vm_size = 'Standard_A0'
    azure.tcp_endpoints = '80:80'
    azure.vm_password = 'pass'

    # each of the below values will default to use the env vars named as below if not specified explicitly
    azure.tenant_id = ENV['TENANT_AZURE']
    azure.client_id = ENV['CLIENT_AZURE']
    azure.client_secret = ENV['CLIENT_SECRET_AZURE']
    azure.subscription_id = ENV['SUBSCRIPTION_AZURE']
  end

  #Provisionamiento
  config.vm.provision "ansible" do |ansible|
        ansible.sudo = true
        ansible.playbook = "playbock.yml"
        ansible.verbose = "v"
        ansible.host_key_checking = false
  end
end
