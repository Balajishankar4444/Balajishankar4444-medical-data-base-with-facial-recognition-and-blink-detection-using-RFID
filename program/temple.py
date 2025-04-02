import time
import cv2
import pickle
import smtplib
import time
import datetime
def main():
    now = datetime.datetime.now()
    day=now.day
    day=30-day
    s=day
    a=day*2
    d=day//2
    sender_email = "raspberryserver00@gmail.com"
    rec_email = "prabavathishankar0@gmail.com"
    password = "tempmail007"
    time1=str(now.strftime("%d-%m-%Y   %H:%M:%S"))
    sub=time1
    text1 = "Your presence is recorded, thanks for your patiences\r\n"+"medicine left:\r\n"+"Ibuprofen - %s med/mon\r\n"%s+"Acetaminophen - %a med/mon\r\n"%a+"Dextromethorphan - %d med/mon\r\n"%d
    text2 = "your failed to be in quarantine"
    video = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Loaading the face recogniser and the trained data into the program
    recognise = cv2.face.LBPHFaceRecognizer_create()
    recognise.read("trainner.yml")

    labels = {} # dictionary
    # Opening labels.pickle file and creating a dictionary containing the label ID
    # and the name
    with open("labels.pickle", 'rb') as f:##
        og_label = pickle.load(f)##
        labels = {v:k for k,v in og_label.items()}##
        print(labels)
    t=0
    l=0

    while t!=10:
        ID=0
        l=l+1
        if l==200:
            break
        check,frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
        #print(face)

        for x,y,w,h in face:
            face_save = gray[y:y+h, x:x+w]
            
            # Predicting the face identified
            ID, conf = recognise.predict(face_save)
            #print(ID,conf)
            if conf >= 20 and conf <= 115:
                t=t+1
                cv2.putText(frame,labels[ID],(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX ,1, (18,5,255), 2, cv2.LINE_AA )
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,255),4)

        cv2.imshow("Video",frame)
        key = cv2.waitKey(1)
        if(key == ord('q')):
            break
    video.release()
    cv2.destroyAllWindows()
    print("name    :",labels[ID])
    if ID==2:
        print("----FACE MATCHED----")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login success")
        message1 = 'Subject: {}\n\n{}'.format(sub, text1)
        server.sendmail(sender_email, rec_email, message1)
        print("Email has been sent to ", rec_email)
        print(message1)
    else:
        print("----NOT MATCHED----")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login success")
        message2 = 'Subject: {}\n\n{}'.format(sub, text2)
        server.sendmail(sender_email, rec_email, message2)
        print("Email has been sent to ", rec_email)
        print(message2)
if __name__ == "__main__":
     main()
