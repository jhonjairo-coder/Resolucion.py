import socket, struct
from colorama import init, Fore, Back, Style


pool = input("ingrese pool: ")

ip,mask = pool.split('/')

mask = int(mask)

def main():
    def ip2long(ip):#convierte octetos a long
        return struct.unpack("!L", socket.inet_aton(ip))[0]

    def long2ip(ip):#convierte long en octetos
        return socket.inet_ntoa(struct.pack("!L",ip))

    def ipmask(bits):#crea un mascara de la cantidad bits en formato long
        return ((1<<(bits))-1)<<(32-bits)

    def iprange(ip,mask):#entrega una tupla con la primera y ultima ip del rango
       return [ip&ipmask(mask),ip|(ipmask(mask)^(1<<32)-1)]

    longIP = ip2long(ip)#creamos el long
    extremos = iprange(longIP,mask)#entregamos long y mascara
    rango = range(extremos[0],extremos[1]+1)#creamos un array

    lista = []

    for i in rango: #lo que sea
        lista.append(long2ip(i))
    cantidad = len(lista)
    print("\n"+"El Pool {} de mascara {} tiene {} ips ".format(pool,mask, cantidad)+"\n")

    print("A continuacion se evidencia el rDNS  "+"\n")
    for j in lista:
        name,_ , ip_dos = socket.gethostbyaddr(j)
        print(Fore.WHITE+Back.BLUE+name,"|",ip_dos[0]+Back.RESET)
    print("\n")

if __name__ == "__main__":
    main()
