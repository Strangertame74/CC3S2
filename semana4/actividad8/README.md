# Actividad 8 : Gestión ágil de sprints con GitHub
## Parte 1: Creación de un plan de sprint
En esta parte simulamos con el equipo que, a partir del product backlog, vamos a poner 
- A partir del estado en el que se quedó la actividad 7, es decir con las historias de usuario puestas en las columnas correspondientes, creamos un nuevo `field` y le ponemos Sprint, donde su field type será `iteration`
![](/images/1.png)
- Luego entramos a la primera historia de usuario que sería Need a Service that has a counter y le ponemos un estimado de `8` puntos de historia.

![](/images/2.png)

- También en el campo sprint que creamos, seleccionamos el primer sprint que es desde la fecha actual hasta el 13 de octubre

![](/images/3.png)
- Agregamos estimaciones a unos cuántas historias más y le asignamos el sprint actual que le asignamos a la primera historia, ya que en grupo se decidió que podía caber.
![](/images/4.png)
- Dentro de la reunión nos alcanza para hacer estimaciones de dos historias más, pero no se agregarán al sprint actual.
![](/images/5.png)
## Parte 2: Flujo de trabajo, del sprint Backlog a otras columnas
En esta parte simularemos cómo se desarrolla el flujo de trabajo y cómo pasamos de la columna sprint backlog a las columnas `In progress`, `Revieq/QA` y `Done` y qué significa pasarla a cada una de ellas.

Ahora que ya tenemos seleccionado las historias que realizaremos en este sprint, lo siguiente es asignar quién será responsable de cada historia.
- En este caso me estoy asignado `Need a service that has a counter` con la opción `asign yourself`.
![](/images/6.png)

- Se debería ver mi nombre de usuario como en la imagen.
![](/images/7.png)

- Arrastramos la historia a la columna `In progress` para hacer saber al grupo que yo estoy trabajando en ello.
![](/images/8.png)

- Aquí, esta tarea ya está terminada y se arrastra a `Review/QA` para decir que está en revisión
![](/images/9.png)

- Mientras está en revisión podemos pasar a atender la siguiente historia, así que la arrastramos a `In progress`
![](/images/10.png)

- Luego cuadno terminó ser revisado y está bien solucionado el issue o bien implementado la historia, se arrastra a done, lo cual quiere decir que está hecho y cerrado.
![](/images/11.png)

- Seguimos el flujo y pasamos a la siguiente historia para que sea revisada ya que acabamos de hacer el código para esa funcionalidad.
![](/images/12.png)

- Luego pasará a `Done` cuando esté cerrado
![](/images/13.png)

- No nos alcanzó el tiempo para resolver el issue o implementar la última historia en el sprint, así que quedaría de esta forma...
![](/images/14.png)

## Parte 3: Configuración de un Burndonw Chart para mi Sprint plan

- Nos vamos al menú desplegble de backlog y ponemos en `Genereate chart`
![](/images/15.png)

- Nos saldrá una gráfica predeterminada de mi proyecto
![](/images/16.png)

- Si filtramos pon status:done nos saldrá la gráfica de la cuenta de historias ya finalizadas.
![](/images/17.png)

- Nos vamos a la parte de Configure chart y ponemos las siguientes opciones y guardamos.
![](/images/18.png)

- Si filtramos por sprint, ponemos nuestro sprint1 en el cuál trabajamos, nos saldrá la gráfica de cuántas actividades están en progreso y cuántas ya están hechas, lo que nos ayuda a llevar la cuenta de manera visual.
![](/images/19.png)

## Parte 4: Cierre del Sprint 
Preparar el backlog para el siguiente sprint.

- En la parte anterior, `deploy service to the cloud` no se pudo concretar en el sprint
![](/images/20.png)

- Por ello bajamos su estimación de 5 a 2

![](/images/21.png)


- Arrastramos a la columna Done ya con el esfuerzo cambiado a 2 para indicar que solo pudimos hacer esa cantidad.

![](/images/22.png)

- Creamos un nuevo issue con 3 story points que representan lo que faltó del último sprint y especificamos que esté dentro de product backlog.
![](/images/24.png)

- Nos aseguramos de que quede en el top de la columna y así finalizaría el cierre de este sprint.
![](/images/25.png)



