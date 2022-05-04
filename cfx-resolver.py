import requests
import json
import colorama
import os
from colorama import Fore

os.system("cls && title Cfx-resolver")
print("")
print("   ██████╗███████╗██╗  ██╗     ██████╗ ███████╗███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗ ")
print("  ██╔════╝██╔════╝╚██╗██╔╝     ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗")
print("  ██║     █████╗   ╚███╔╝█████╗██████╔╝█████╗  ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝")
print("  ██║     ██╔══╝   ██╔██╗╚════╝██╔══██╗██╔══╝  ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗")
print("  ╚██████╗██║     ██╔╝ ██╗     ██║  ██║███████╗███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║")
print("   ╚═════╝╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝\n")
print(f"  Cfx resolver developed & made with <3 by mkay\n")
cfx = input(f"  [{Fore.YELLOW}>{Fore.RESET}] Cfx code: ")

headers={
         "Host": "servers-frontend.fivem.net",
         "Connection": "keep-alive",
         "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
         "Accept": "application/json, text/plain, */*",
         "sec-ch-ua-mobile": "?0",
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
         "sec-ch-ua-platform": "Windows",
         "Sec-Fetch-Site": "same-site",
         "Sec-Fetch-Mode": "cors",
         "Sec-Fetch-Dest": "empty",
         "Accept-Language": "fr-FR,fr;q=0.9",
         "Accept-Encoding": "gzip, deflate"
         }

response = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{cfx}", headers=headers).json()

os.system("cls && title Cfx-resolver")

print("")
print("   ██████╗███████╗██╗  ██╗     ██████╗ ███████╗███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗ ")
print("  ██╔════╝██╔════╝╚██╗██╔╝     ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗")
print("  ██║     █████╗   ╚███╔╝█████╗██████╔╝█████╗  ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝")
print("  ██║     ██╔══╝   ██╔██╗╚════╝██╔══██╗██╔══╝  ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗")
print("  ╚██████╗██║     ██╔╝ ██╗     ██║  ██║███████╗███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║")
print("   ╚═════╝╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝\n")
print(f"  Cfx resolver developed & made with <3 by mkay\n")

print(f"  Server title:    [{response['Data']['hostname']}]")
print(f"  Server owner:    [{response['Data']['ownerName']}]")
print(f"  Server owner id: [{response['Data']['ownerID']}]")
print(f"  Players online:  [{response['Data']['clients']}/{response['Data']['svMaxclients']}]")
print(f"  Server endpoint: [{response['Data']['connectEndPoints'][0]}]")
