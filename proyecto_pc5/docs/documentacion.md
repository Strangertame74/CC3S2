# Ejercicio 1

- Con el comando 'vagrant ssh' accedemos a la terminal de la vm desde la maquina host y verificamos que exista el usuario devuser:

![](./assets/1.png)

- Y que el sistema esté actualizado:
![](./assets/4.png)

- También verificamos el grupo admin:
![](./assets/2.png)

- Y la zona horaria:
![](./assets/3.png)

# Ejercicio 2
- Mostramos la fecha del certificado
![](./assets/5.png)
- Mostramos el certificado y sus metadatos:
![](./assets/6.png)
- Con el comando ```curl -k https://localhost``` mostramos lo que el servidor manda cuando nos conectamos a esa dirección y realizamos la solicitud.

![](./assets/7.png)

Vemos que salía 403 forbidden y era porque Nginx no podia servir lo que salía del directorio /var/www/html cuando nos conectábamos a la dirección del localhost, ya que teníamos esto:

```
location / {
        root /var/www/html;
        index index.html index.htm;
    }
```

Sin tener un index.html, pero al agregar el archivo que sí teníamos, osea indez.nginx-debian.html, ahora sí salió y pudo servir bien.

```
index index.html index.htm index.nginx-debian.html;
```

Al usar de nuevo el comando ```curl -k https://localhost``` :
![](./assets/8.png)