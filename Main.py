import Easy.EasyMain
import Medium.MediumMain
import Hard.HardMain

if __name__=='__main__':
    print("Hello Player and welcome to the puzzle game!!")
    while True:
        print("Choose a difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        # print (choice)
        if choice==1:
            em = Easy.EasyMain.EasyMain
            em.EasyStart()
        if choice==2:
            mm = Medium.MediumMain.MediumMain
            mm.MediumStart()  
        if choice==3:
            hm = Hard.HardMain.HardMain
            hm.HardStart()  
        if choice >= 4:
            break