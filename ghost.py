#Librerias 
import os
import subprocess
#banner
banner = """
  ____ _   _  ___  ____ _____ 
 / ___| | | |/ _ \/ ___|_   _|
| |  _| |_| | | | \___ \ | |  
| |_| |  _  | |_| |___) || |  
 \____|_| |_|\___/|____/ |_|  
                              
"""
os.system('clear')
print(banner)
print("1 --> Instagram ")
print("2 --> TIKT0K ")
print("3 --> Facebook")
opt_menu = input("--> ")
if opt_menu == "1":
    user = input("Inserta Username --> ")
    web = subprocess.getoutput('firefox www.instagram.com/' + str(user))
elif opt_menu == "2":
    user = input("Inserta Username --> ")
    web = subprocess.getoutput('firefox www.tiktok.com/@' + str(user) )
if opt_menu == "3":
    user = input("Inserta Username --> ")
    web = subprocess.getoutput('firefox www.facebook.com/' + str(user) )
