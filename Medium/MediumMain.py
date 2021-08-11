from Medium import MediumLevel
import random

class MediumMain:
    def MediumStart():
        ml = MediumLevel.MediumLevel()
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
        print("Hello Player!!")
        print("Welcome to Medium Mode")
        print("You have only 6 directions of traversing as N, E, W, S, NE, SW")
        begin = input("Do you want to start? (y/n): ")
        if begin.upper()=="Y":
            print(ml.getDescription(pos))
            while pos!="Exit" and pos1!="Exit" and pos2!="Exit" and pos3!="Exit" and pos4!="Exit":
                dir=input("Enter a valid direction: ")
                dir=dir.upper();
                if dir=="N" or dir=="E" or dir=="W" or dir=="S" or dir=="NE" or dir=="SW":
                    try:
                        if pos=="Null" and pos1!="Null":
                            pos1 = ml.getDirection(pos1,dir)
                            s=ml.getDescription(pos1)
                            print(s)
                            pos=pos1
                        elif pos1=="Null" and pos2!="Null":
                            pos2 = ml.getDirection(pos2,dir)
                            s=ml.getDescription(pos2)
                            print(s)
                            pos=pos2
                        elif pos2=="Null" and pos3!="Null":
                            pos3 = ml.getDirection(pos3,dir)
                            s=ml.getDescription(pos3)
                            print(s)
                            pos=pos3
                        elif pos3=="Null" and pos4!="Null":
                            pos4 = ml.getDirection(pos4,dir)
                            s=ml.getDescription(pos4)
                            print(s)
                            pos=pos4
                        else:
                            pos1=pos
                            pos2=pos
                            pos3=pos
                            pos4=pos
                            pos = ml.getDirection(pos,dir)
                            s=ml.getDescription(pos)
                            print(s)
                    except:
                        print("Error occured in EasyMain");
                else:
                    continue    
            print("You found a way out of maze\n Game Over")