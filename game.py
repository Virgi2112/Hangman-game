import random
import os

def run():
    images = [ '''
  +---+
  | |
      |
      |
      |
      |
=========''' , '''
  +---+
  | |
  O |
      |
      |
      |
=========''' , '''
  +---+
  | |
  O |
  | |
      |
      |
=========''' , '''
  +---+
  | |
  O |
/| |
      |
      |
=========''' , '''
  +---+
  | |
  O |
/|\ |
      |
      |
=========''' , '''
  +---+
  | |
  O |
/|\ |
/ |
      |
=========''' , '''
  +---+
  | |
  O |
/|\ |
/\ |
      |
=========''' ]
    
    DB = [
        "C",
        "PYTHON",
        "JAVASCRIPT",
        "PHP",
        "C++",
        "C#",
        "SQL",
        "JAVA",
        "RUST",
        "PERL",
        "SWIFT",
        "PASCAL",
        "WINDOWS",
        "LINUX",
        "IOS"
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6

    while True:
        os.system("cls")
        for character in spaces:
            print(character, end=" ")
        print(images[attemps])
        letter = input("Elige una letra").upper()
        
        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
                
        if not found:
            attemps -= 1
            
        if "_" not in spaces:
            os.system("cls")
            print("Ganaste")
            break
            input()
            
        if attemps == 0:
            os.system("cls")
            print("Perdiste")
            break
            input()
        
if __name__ == '__main__':
    run()