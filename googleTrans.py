from googletrans import Translator, LANGUAGES
from colorama import Fore

def hypertranslate(text="None", deph=10, final_dest="pt"):
  temp = text

  langs = list(LANGUAGES)

  if(deph > len(langs) or (deph < 1)):
    return None

  else:
    translator = Translator()

    index = 0
    while(index != deph):
      text = translator.translate(text, dest=langs[index]).text
      print(index)
      print(temp)
      print(Fore.RED + translator.translate(text, dest=final_dest).text + Fore.WHITE)
      print("===")

      index += 1

    return translator.translate(text, dest=final_dest).text

if __name__ == "__main__":
  text = input("Insira o texto a ser destruído: ")
  print(hypertranslate(text=text, deph=30, final_dest="pt")) #18, 19, 20, 23