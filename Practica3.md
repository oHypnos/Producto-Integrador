El script es un programa en Python que utiliza el módulo python-nmap para realizar diferentes tipos de escaneo de red. 
[Script](EscanerdePuertos.py)
Proporciona un menú con las siguientes opciones:

Escaneo UDP: Realiza un escaneo de puertos UDP en un objetivo especificado por el usuario.
Escaneo completo: Realiza un escaneo completo de todos los puertos TCP en un objetivo especificado por el usuario.
Detección de sistema operativo: Realiza una detección del sistema operativo en un objetivo especificado por el usuario.
Escaneo de red con ping: Realiza un escaneo de red utilizando ping para determinar las direcciones IP activas en la red, en base a un objetivo especificado por el usuario.
Salir: Permite salir del programa.
El script utiliza el módulo nmap para realizar los escaneos. Cada opción del menú llama a una función correspondiente que utiliza el objeto nmap.PortScanner() para realizar el escaneo con los argumentos adecuados.

Después de cada escaneo, se muestra el resultado obtenido al usuario. El menú se muestra en un bucle infinito hasta que el usuario selecciona la opción para salir.
