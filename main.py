import requests
from colorama import Fore, Back, Style

def token_check(token):
  headers = { "Authorization": token }
  r = requests.get("https://discordapp.com/api/v9/auth/login", headers = headers)
  
  try:
    if r.status_code == 200:
      print(f"{Fore.GREEN}[ SUCCES ] {Fore.CYAN}Token is working!")
    else:
      print("[ FAILED ] Token is invalid!")
  except Exception:
      print(Fore.RESET)
      print(f"{Fore.RED}[ ERROR ]{Fore.CYAN} Internet is not working or Discord is down...")
def __init__():
  token = input("[ TOKEN ] Enter token: ")
  
  if token == "":
    print("[ ERROR ] ENTERED TOKEN IS INVALID!")
    print(Fore.RESET)
    __init__()
  else:
    token_check(token)
    
__init__()
