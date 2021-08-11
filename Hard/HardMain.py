from Hard import HardLevel
import random

class HardMain:
    def HardStart():
        hl = HardLevel.HardLevel()
        i = random.randrange(1,99)
        pos=""
        if i>=1 and i<=9:
            pos = "0"+str(i)
        else:
            pos = str(i)
        pos1=pos
        pos2=pos
        pos3=pos
        pos4=pos
        pos5=pos
        print("Hello Player!!")
        print("Welcome to Hard Mode")
        print("You have only 8 directions of traversing as N, E, W, S, NE, NW, SW, SE")
        begin = input("Do you want to start? (y/n): ")
        if begin.upper()=="Y":
            print(hl.getDescription(pos))
            while pos!="Exit" and pos1!="Exit" and pos2!="Exit" and pos3!="Exit" and pos4!="Exit" and pos5!="Exit":
                dir=input("Enter a valid direction: ")
                dir=dir.upper();
                if dir=="N" or dir=="E" or dir=="W" or dir=="S" or dir=="NE" or dir=="NW" or dir=="SE" or dir=="SW":
                    try:
                        if pos=="Null" and pos1!="Null":
                            pos1 = hl.getDirection(pos1,dir)
                            s=hl.getDescription(pos1)
                            print(s)
                            pos=pos1
                        elif pos1=="Null" and pos2!="Null":
                            pos2 = hl.getDirection(pos2,dir)
                            s=hl.getDescription(pos2)
                            print(s)
                            pos=pos2
                        elif pos2=="Null" and pos3!="Null":
                            pos3 = hl.getDirection(pos3,dir)
                            s=hl.getDescription(pos3)
                            print(s)
                            pos=pos3
                        elif pos3=="Null" and pos4!="Null":
                            pos4 = hl.getDirection(pos4,dir)
                            s=hl.getDescription(pos4)
                            print(s)
                            pos=pos4
                        elif pos4=="Null" and pos5!="Null":
                            pos5 = hl.getDirection(pos5,dir)
                            s=hl.getDescription(pos5)
                            print(s)
                            pos=pos5
                        else:
                            pos1=pos
                            pos2=pos
                            pos3=pos
                            pos4=pos
                            pos5=pos
                            pos = hl.getDirection(pos,dir)
                            s=hl.getDescription(pos)
                            print(s)
                    except:
                        print("Error occured in EasyMain");
                else:
                    continue    
            print("You found a way out of maze\n Game Over")