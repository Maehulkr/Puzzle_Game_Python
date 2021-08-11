from Easy import EasyLevel
import random

class EasyMain:
    def EasyStart():
        el = EasyLevel.EasyLevel()
        i = random.randrange(1,99)
        pos=""
        if i>=1 and i<=9:
            pos = "0"+str(i)
        else:
            pos = str(i)
        pos1=pos
        pos2=pos
        print("Hello Player!!")
        print("Welcome to Easy Mode")
        print("You have only 4 directions of traversing as N, E, W, S")
        begin = input("Do you want to start? (y/n): ")
        if begin.upper()=="Y":
            print(el.getDescription(pos))
            while pos!="Exit" and pos1!="Exit":
                dir=input("Enter a valid direction: ")
                dir=dir.upper();
                if dir=="N" or dir=="E" or dir=="W" or dir=="S":
                    try:
                        if pos=="Null" and pos1!="Null":
                            pos1 = el.getDirection(pos1,dir)
                            s=el.getDescription(pos1)
                            print(s)
                            pos=pos1
                        elif pos1=="Null":
                            pos2 = el.getDirection(pos2,dir)
                            s=el.getDescription(pos2)
                            print(s)
                            pos=pos2
                        else:
                            pos1=pos
                            pos2=pos
                            pos = el.getDirection(pos,dir)
                            s=el.getDescription(pos)
                            print(s)
                    except:
                        print("Error occured in EasyMain");
                else:
                    continue    
            print("You found a way out of maze\n Game Over")