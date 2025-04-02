import geocoder
import datetime
import time
import random
import cv2
import pickle
import os
import temple
#sys contains command line arguments
from sys import argv
from pyperclip import paste
def main():
    current_time = datetime.datetime.now()
    hr=current_time.hour
    mi=current_time.minute
    sec=current_time.second
    print(hr,mi,sec)
    hour=[]
    minute=[]
    second=[]

    for i in range(3):
        hr_r=random.randint(hr,24)
        mi_r=random.randint(mi,60)
        sec_r=random.randint(sec,60)
        hour.append(hr_r)
        minute.append(mi_r)
        second.append(sec_r)
    print("hr",hour,"min",minute,"sec",second)
    y=0
    from webbrowser import open
    while True:
        p=0
        current_time = datetime.datetime.now()
        hr=current_time.hour
        mi=current_time.minute
        sec=current_time.second
        print(hr,mi,sec)
        time.sleep(1)
        if True or (hour[0]==hr and minute[0]==mi and second[0]==sec) or (hour[1]==hr and minute[1]==mi and second[1]==sec) or (hour[2]==hr and minute[2]==mi and second[2]==sec):
            y=y+1
            g = geocoder.ip('me')
            address=g.latlng
            k=""
            for i in range(len(address)):
                address[i]=str(address[i])
                if i==len(address)-1:
                    k=k+address[i]
                else:
                    k=k+address[i]+","
            print("location:",k)
            open("http://www.google.com/maps/place/"+k)
            time.sleep(5)
            if k=="13.0878,80.2785":
                print("--LOCATION MATCHED--")
                temple.main()
                time.sleep(3)
            else:
                print("--LOCATION NOT MATCHED--")
            if y==3:
                break
if __name__=="__main__":
    main()

