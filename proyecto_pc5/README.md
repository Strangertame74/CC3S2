En esta carpeta del repositorio CC3S2, llamada proyecto_pc5, se encuentra la resolución de los ejercicios para la PC5, que es una pequeña parte de todo un proyecto que incluye a la PC3, PC4 y PC5.

----
### Requisitos 
----
Requisitos previos para poder correr los archivos:
- Tener instalado Vagrant
- Tener instalado Ansible
- Tener instalado Virtualbox

### Levantar la VM
----
Si queremos levantar las vm debemos ubicarnos en el directorio ```proyecto_pc/vagrant``` y utilizar el comando ```vagrant up```

### Contenido
-----
Este README.md contendrá el resumen de los pasos de cada ejercicio.

### Documentación adicional
----
Existe un archivo markdown llamado ```documentacion.md```, ubicado en ```docs/``` donde están las capturas de pantalla con los resultados importantes de cada ejercicio e información adicional.

-----

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

Para el ejercicio 2 tenemos los archivos: 
- site.yml (actualizado): Actualizado con vars (variables), handlers (manejador para el restart de nginx), importar el task para el ejercicio 2(main.yml)
- ejercicio2/main.yml : Tasks para instalar nginx, generar certificado SSL autofirmado, configurar nginx para utilizar SSL, config SSL, config firewall UFW para https.
- handlers/main.yml: Task para reiniciar gninx (con notify le decimos qué task agarrar)
- templates/nginx_https.conf.j2: Configuración de Nginx para HTTPS.

### Dentro de ejercicio2/main.yml:
Tenemos el siguiente flujo:
1. Instalar nginx
2. Instalar las dependencias de openSSL
3. Crear un directorio para el certificado SSL
4. Crear una clave privada RSA
5. Crear certificado SSL autofirmado
6. Configurar Nginx para HTTPS
7. Crear enlace para habilitar el sitio por defecto
8. Habilitar UFW para permitir tráfico HTTPS
9. Probar configuración de Nginx

### Dentro de templates/nginx_https.conf.j2
Tenemos la configuración configuración de Nginx para habilitar HTTPS en un servidor web.

# Ejercicio 3: Despliegue de aplicación web con balanceador de carga

Para el ejercicio 3, los siguientes archivos fueron añadidos o actualizados:
- site.yml (actualizado): Se importó los task del ejercicio 3, además de las variables, que están señaladas y separadas por un comentario(se pueden ver dentro del archivo).
- templates/nginx_https.conf.j2 (actualizado): Escalando la configuración del ejercicio 2, aquí se cambió en location los archivos que podía buscar(index.html y index.nginx-debian.html) y ahora que vamos a trabajar con una aplicación de flask, tenemos el proxy_pass el cuál va a redirigir las solicitudes que lleguen a alguno de los servidores de los bloques que hemos definido (A esto se le llama balancear).
- templates/gunicorn.service.j2: Aquí irá la configuración de gunicorn, es un archivo de unidad de sysmtemd, con esto gestionaremos este servicio.
- ejercicio3/main.yml: Aquí irán los tasks para instalar las dependencias de python, instalar flask y unicorn, y el resto de tareas para este ejercicio.
- templates/nginx_load_balancer.conf.j2: En este archivo se especifican los servidores gunicorn que van a recibir la solicitud del nginx en el puerto 443 (Luego en otro commit lo cambié porque había un conflicto con el ejercicio 2 y no me permitía seguir, y al final uní dos templates y borré este directorio).
- templates/app.py: Pequeña app creada con flask para que se copie a la VM.
- handlers/main.yml(actualizado): Se agregó un manejador para recargar systemd.

### Dentro de ejercicio3/main.yml:
Tenemos el siguiente flujo:
1. Instalar dependencias de python
2. Instalar Flask y Gunicorn
3. Crear un ddirectorio para la aplicación
4. Crear la aplicación de Flask
5. Crear servicios systemd para gunicorn
6. Iniciar y habilitar servicios Gunicorn
7. Configurar archivo de Nginx para balanceo de carga
8. Habilitar configuración de Nginx

# Ejercicio 4: Monitoreo y alertas

Para este ejercicio 4, los siguientes archivos fueron añadidos o actualizados:
- site.yml(actualizado): Se importó el task del ejercicio 4.
- templates/prometheus.service.j2: Archivo para gestionar el servicio de prometheus
- templates/prometheus.yml.j2: Configuración de prometheus
- templates/node_exporter.service.j2: Configuración de node_exporter
- templates/grafana.service.j2: Archivo para gestionar el servicio de grafana
- templates/alerts.yml.j2: Aquí estaba la configuración para las alertas
- ejercicio4/main.yml: Aquí estarán los tasks para el ejercicio 4.
- handlers/main.yml (actualizado): Reiniciar prometheus.
- templates/app.py: Métricas para grafana y prometheus

### Dentro de ejercicio4/main.yml:
Tenemos el siguiente flujo:
1. Descargar binarios de Prometheus desde GitHub
2. Crear directorio para Prometheus
2. Descargar Prometheus
3. Extraer Prometheus
4. Crear usuario para Prometheus
5. Configurar Prometheus
6. Configurar alertas en Prometheus
7. Crear directorio de almacenamiento para Prometheus
8. Dar permisos a Prometheus para el directorio de almacenamiento
9. Crear servicio para Prometheus
10. Descargar Node Exporter
11. Extraer Node Exporter
12. Eliminar el directorio de Node Exporter si existe
13. Mover Node Exporter
14. Crear servicio para Node Exporter
15. Iniciar y habilitar Prometheus
16. Iniciar y habilitar Node Exporter
17. Configurar Prometheus
18. Agregar clave GPG de Grafana
19. Agregar repositorio de Grafana
20. Actualizar la caché de paquetes
21. Instalar Grafana
22. Habilitar e iniciar el servicio de Grafana

# Ejercicio 5: Implementación de alta disponibilidad y recuperación de desastres:

Para este ejercicio 5, los siguientes archivos fueron añadidos o actualizados:
- site.yml(actualizado): Se importó el task del ejercicio 5.
- templates/postgresql-primary.conf.j2: Config para servidor primario
- templates/postgresql-replica.conf.j2: Config para el entorno de replicaión
- templates/pg_backup.sh: Backup de una base de datos postgre.

### Dentro de ejercicio5/main.yml:
Tenemos el siguiente flujo:
1. Agregar el repositorio de PostgreSQL
2. Instalar la clave GPG del repositorio de PostgreSQL
3. Actualizar el caché de APT
4. Instalar PostgreSQL y sus dependencias
5. Fijar la versión de las dependencias de PostgreSQL (libpq-dev)
6. Configurar PostgreSQL. Establecer listen_addresses
7. Configurar PostgreSQL. Establecer max_connections
8. Configurar PostgreSQL. Deshabilitar SSL
9. Configurar PostgreSQL. Habilitar autovacuum
10. Configurar PostgreSQL. Establecer hosts en pg_hba.conf
11. Instalar psycopg2
12. Crear la base de datos PostgreSQL
13. Crear usuario de base de datos y otorgar acceso
14. Configurar PostgreSQL como primario
15. Configurar PostgreSQL como réplica
16. Reiniciar PostgreSQL17. 
17. Crear directorio de backups
18. Copiar script de backup
19. Configurar tarea cron para backups
20. Instalar Keepalived
21. Configurar Keepalived
22. Habilitar y reiniciar Keepalived

Un problema que tuve para este ejercicio fue que después de levantar nuevamente con vagrant up, el postgresql no se podía instalar, al parece por la url.

