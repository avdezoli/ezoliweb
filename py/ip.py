import requests # type: ignore
import socket
import subprocess
import os

logo = \
"""


███████╗███████╗ ██████╗ ██╗     ██╗        ██╗██████╗         ████████╗███████╗███████╗████████╗███████╗██████╗ 
██╔════╝╚══███╔╝██╔═══██╗██║     ██║        ██║██╔══██╗        ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
█████╗    ███╔╝ ██║   ██║██║     ██║        ██║██████╔╝           ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝
██╔══╝   ███╔╝  ██║   ██║██║     ██║        ██║██╔═══╝            ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗
███████╗███████╗╚██████╔╝███████╗██║        ██║██║                ██║   ███████╗███████║   ██║   ███████╗██║  ██║
╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝        ╚═╝╚═╝                ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   


"""


cevap = input(" ")

def al_public_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        ip_address = response.json()["ip"]
        print("IP :", ip_address)
    except requests.RequestException as e:
        print("Error:", e)

def al_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip



def local_ip_tarama():
    local_ip = al_local_ip()
    network = '.'.join(local_ip.split('.')[:-1]) + '.'

    print(f"Scanning network: {network}\n")
    
    for i in range(1, 255):
        ip = network + str(i)
        result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode()
        if result.returncode == 0 and "TTL=" in output:
            print(f"Device found: {ip}")
        else:
            print(f"Scaning: {ip}")

def özel_ip_tarama():
    print ("\n")
    network2 = "192.168.1"
    network2 = network2.strip() + '.'
    
    print(f"Scanning network: {network2}xxx\n")
    
    for i in range(1, 255):
        ip2 = network2 + str(i)
        result2 = subprocess.run(['ping', '-c', '1', '-W', '1', ip2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output2 = result2.stdout.decode()
        if result2.returncode == 0 and "TTL=" in output2:
            print(f"Device found: {ip2}")
        else:
            print(f"Scaning: {ip2}")

if cevap == '1':
    al_public_ip()
if cevap == '2':
    local_ip_tarama()
if cevap == '3':
    özel_ip_tarama()