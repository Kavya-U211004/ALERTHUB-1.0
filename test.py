'''c=("google.com","yahoo.com")
s=('68.180.206.184','98.170.216.167')
n=str(input())
for i in range(len(c)):
    if c[i]==n:
        print('Connected to',s[i])
        break
else:
    print("NO IP")'''

import socket

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.error as err:
        print(f"Error: {err}")

url = "facebook.com"
ip = get_ip_address(url)
print(f"The IP address of {url} is {ip}")