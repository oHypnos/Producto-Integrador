#Fernando Javier Marin Salas
#1679139
import nmap

def udp_scan(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-p U:137,T:138')
    return scanner[target]['udp']

def full_scan(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-p 1-65535')
    return scanner[target]['tcp']

def os_detection(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-O')
    return scanner[target]['osmatch']

def network_scan(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-sn')
    return scanner.all_hosts()

def display_menu():
    print("=== Menú de opciones ===")
    print("1. Escaneo UDP")
    print("2. Escaneo completo")
    print("3. Detección de sistema operativo")
    print("4. Escaneo de red con ping")
    print("5. Salir")

def main():
    target = input("Ingrese la dirección IP o el rango de IP a escanear: ")
    while True:
        display_menu()
        option = input("Seleccione una opción: ")

        if option == '1':
            result = udp_scan(target)
            print("Resultados del escaneo UDP:")
            print(result)
        elif option == '2':
            result = full_scan(target)
            print("Resultados del escaneo completo:")
            print(result)
        elif option == '3':
            result = os_detection(target)
            print("Resultados de la detección de sistema operativo:")
            print(result)
        elif option == '4':
            result = network_scan(target)
            print("Direcciones IP activas en la red:")
            for ip in result:
                print(ip)
        elif option == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == '__main__':
    main()
