l script [superscan.sh](scriptbash.sh):

#!/bin/bash: Esto es la línea shebang y especifica que el script será interpretado por el intérprete de comandos bash.

El bucle while true; do inicia un bucle infinito para que el menú se mantenga mostrando hasta que se seleccione la opción de salida.

clear limpia la pantalla antes de mostrar el menú.

Las siguientes líneas imprimen el título del menú y las opciones disponibles.

read -p "Seleccione una opción [1-4]: " opcion muestra un mensaje y espera a que el usuario introduzca una opción. La opción ingresada se guarda en la variable opcion.

El case $opcion in inicia una estructura de control basada en la opción seleccionada.

Cada caso (1, 2, 3, 4) corresponde a una opción del menú y ejecuta el comando o script correspondiente.

En el caso 1, se ejecuta el script $HOME/netdiscover.sh. $HOME representa la variable de entorno que contiene la ruta al directorio de inicio del usuario.
En el caso 2, se muestra el nombre de usuario actual utilizando el comando whoami.
En el caso 3, se muestra el nombre del host utilizando el comando hostname.
En el caso 4, se muestra un mensaje de despedida y se sale del script con el comando exit 0.
El ;; marca el final de cada caso en la estructura case.

Después del case, se muestra un mensaje para presionar Enter y continuar.

El bucle done cierra el bucle infinito del menú.
