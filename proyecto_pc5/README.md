En esta carpeta del repositorio CC3S2 se encuentra la resolución de los ejercicios para la PC5, que es una pequeña parte de todo un proyecto que incluye a la PC3, PC4 y PC5.

Requisitos previos para poder correr los archivos:
- Tener instalado Vagrant
- Tener instalado Ansible
- Tener instalado Virtualbox

Si queremos levantar las vm debemos ubicarnos en el directorio ```proyecto_pc/vagrant``` y utilizar el comando ```vagrant up```

# Ejercicio 1: Configuración básica del sistema
Para este ejercicio se creo un Vagrantfile con vagrant init ubuntu/focal64 para tener una vm con el sistema operativo deseado. También pedían una ip estática, así que en vez de dhcp se puso un ip estático y se puso en vb.memory el valor de 2048 para usar 2gb de ram. Por último se creó el playbook de ansible llamado site.yml y se importó las tareas del ejercicio1 que está en main.yml.

```
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.network "private_network", ip: "192.168.56.2" # dando una ip estática en vez de dhcp
  config.vm.provider "virtualbox" do |vb| #Configuramos como proveedor a virtualbox
    vb.memory = "2048" # Usará 2gb de ram
    vb.name = "vm_1" # Nombre de la vm
  end
  config.vm.provision "ansible" do |ansible| #Configuramos ansible como provisionador
    ansible.playbook = "../site.yml" #leeremos el site.yml un playbook de ansible que crearemos
  end

end
```
# Ejercicio 2: Implementación de servicios web con seguridad básica



