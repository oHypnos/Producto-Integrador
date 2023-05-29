#!/bin/bash
#Fernando Javier Marin Salas
#1679139
while true; do
    clear
    echo "|---------------------------|"
    echo "|   Super Scan Menu         |"
    echo "|---------------------------|"
    echo "|1. Netdiscover"
    echo "|2. Portscanv1"
    echo "|3. Welcome"
    echo "|4. Exit"
    echo "|"
    read -p "Seleccione una opción [1-4]: " opcion

    case $opcion in
        1)
            $HOME/netdiscover.sh
            ;;
        2)
            chmod +x portscanv1.sh
            ./portscanv1.sh
            ;;
        3)
            ./welcome.sh
            ;;
        4)
            echo "¡Adiós!"
            exit 0
            ;;
        *)
            echo "Opción inválida. Intente nuevamente."
            ;;
    esac

    echo -e "\nPresione Enter para continuar..."
    read -r
done
