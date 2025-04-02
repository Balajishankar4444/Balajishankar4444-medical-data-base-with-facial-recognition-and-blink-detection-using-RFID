import date_loc
import data
print("------MEDICAL SERVER-----")
while True:
    print("1: quarantine monitor")
    print("2: Enter data base")
    print("3: exit")
    num=int(input())
    if num==1:
        date_loc.main()
    elif num==2:
        print("1: register in server")
        print("2: delete registered data")
        print("3: profile")
        print("4: medical background")
        print("5: drugs info")
        data.main()
    elif num==3:
        break
    else:
        print("invalid input")
