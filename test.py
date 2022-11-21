from os import system
from time import sleep
from googleTrans import hypertranslate # (text: str = "None", deph: int = 10, final_dest: str = "pt")

chars = ['/', '-', '\\', '|']

while True:
  for char in chars:
    print(char)
    sleep(0.2)
    system("cls")