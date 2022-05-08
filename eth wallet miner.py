import time
import hashlib
import random
import time
from colorama import Fore
import os
os.system("")



print(f'''
      
{Fore.CYAN}███████╗████████╗██╗  ██╗     {Fore.LIGHTRED_EX}███╗   ███╗██╗███╗   ██╗███████╗██████╗ 
{Fore.CYAN}██╔════╝╚══██╔══╝██║  ██║     {Fore.LIGHTRED_EX}████╗ ████║██║████╗  ██║██╔════╝██╔══██╗
{Fore.CYAN}█████╗     ██║   ███████║     {Fore.LIGHTRED_EX}██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝
{Fore.CYAN}██╔══╝     ██║   ██╔══██║     {Fore.LIGHTRED_EX}██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗
{Fore.CYAN}███████╗   ██║   ██║  ██║     {Fore.LIGHTRED_EX}██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║
{Fore.CYAN}╚══════╝   ╚═╝   ╚═╝  ╚═╝     {Fore.LIGHTRED_EX}╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                    {Fore.LIGHTGREEN_EX}> Made By nok#1079
                     {Fore.LIGHTGREEN_EX}> YouTube - $Nks
''')

# q = Zmienna z odpowiedzią
q = input("want start mining eth?(Y/N)")
if q == "Y" or q == "y":
    pass
else:
    exit(1)

# Po ilu probach ma pokazać że udało się wykopać
proby = random.randint(100, 89300)
eth = random.randint(0, 500)  # Ile eth ma być wykopane

#szuka eth
for i in range(0, proby):
    print(
        f'''{Fore.RED}[-] [0x{hashlib.sha1(str(i).encode()).hexdigest()}] Mining...  Amount eth: 0.00ETH")''')

#znaleziono ETH
i = random.randint(0, 9999)
print(
    f'''{Fore.GREEN}[+] [0x{hashlib.sha1(str(i).encode()).hexdigest()}] HIT!!! Amount eth: {eth/100}ETH")''')

input()

