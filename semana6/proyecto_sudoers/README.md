# Implementar y automatizar la configuración de una Flask App Web en una VM utilizando Vagrant y Ansible.

1. Crearemos la carpeta proyecto_sudoers
2. Crearemos el archivo Vagrantfile con el comando ```vagrant init ubuntu/focal64```
3. Creamos un playbook de Ansible llamado site.yml donde definimos los task que se importaran desde la carpeta tasks.
4. Creamos la carpeta task que contendrá los tareas.
- La primera tarea estará en archivo user_and_group.yml, aquí crearemos el grupo desarrolladores y también el usuario bender el cuál pertenecerá al grupo desarrolladores.
- En el archivo web_applications.yml automatizaremos la instalación de flask, giunicorn y nginx. También crearemos el directorio para la aplicacion, que estará en ingeneering.
 Copiaremos una aplicación de muestra para greetings.py y wsgi.py (por el loop).
 También copiamos el greeting.service y luego lo iniciamos.
5. Creamos una carpeta templates y crearemos el archivo developers.j2 y actualizamos site.yml agregando: 
 ```
 vars_files:
    - templates/developers.j2
 ```
6. Levantamos la máquina virtual.
7. Nos conectamos como el usuario bender


