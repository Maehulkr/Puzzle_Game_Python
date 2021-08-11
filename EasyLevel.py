class EasyLevel:
    def getDirection(self, pos, dir):
        try:
            file = open("Direction.txt")
            for s in file:
                if s[0]==pos[0] and s[1]==pos[1] and s[3]==dir[0]:
                    return s[6:len(s)-1]
        except:
            print("Error occured in EasyLevel getDirection")
        finally:
            file.close()
        return None 

    def getDescription(self, s):
        try:
            file=open("Description.txt")
            for st in file:
                if st[0]==s[0] and st[1]==s[1] and s!="Null" and s!="Exit":
                    return st[3:]
                elif (s=="Null" or s=="Exit") and st[0]==s[0]:
                    return st[5:] 
        except:
            print("Error occured in EasyLevel getDescription")
        finally:
            file.close()
        return None