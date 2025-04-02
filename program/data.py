import mysql.connector
import serial
def main():
    arduino = serial.Serial('COM4',9600)
    mydb = mysql.connector.connect(host='localhost',user='root', passwd='balaji',
                                   database="testdatabase")
    mycursor=mydb.cursor()
    num=int(input())
    datalist=["PersonID -","name     -","age      -","adhar_no -","phone_no -","RFDI_pin -"]
    arr=[]
    drugs_data=["dolo650","paracetamol","dog40","digene"]
    med_data=["PersonID    -","name        -","hospital    -","doctor      -","Appointment -"]
    if num==1:
        print("enter name")
        str1=input()
        print("enter age")
        num1=int(input())
        print("enter adhar number")
        num2=int(input())
        print("phone number")
        num3=int(input())
        
        print("register your tag")
        for i in range(2):
            data = arduino.readline()[0:-2]
            data=str(data)[2:-1]
        data=data.replace(" ","")
        print(data)
        mycursor.execute("INSERT INTO patient(name,age,adhar_no,phone_no,RFID_pin) VALUES(%s,%s,%s,%s,%s)",(str1,num1,num2,num3,data))
        mydb.commit()
        print("updated successfully")
        sql = ("SELECT * FROM patient WHERE RFID_pin='%s'"%data)
        result = mycursor.execute(sql)
        for i in mycursor:
            i=list(i)
        for j in range(len(i)):
            print(datalist[j],i[j])
        
    if num==2:
        print("enter ID")
        num1=int(input())
        mycursor.execute("DELETE FROM patient WHERE personID=%d"%(num1))
        mydb.commit()
        print("deleted successfully")
    if num==3:
        print("place your reg tag -",end="")
        for i in range(2):
            data = arduino.readline()[0:-2]
            data=str(data)[2:-1]
        data=data.replace(" ","")
        print(data)
        sql = ("SELECT * FROM patient\
               WHERE RFID_pin='%s'"%data)
        data=data.replace(" ","")
        result = mycursor.execute(sql)
        for i in mycursor:
            i=list(i)
            print(i)
        for j in range(len(i)):
            print(datalist[j],i[j])
    if num==4:
        print("place your reg tag -",end="")
        for i in range(2):
            data = arduino.readline()[0:-2]
            
            data=str(data)[2:-1]
        data=data.replace(" ","")
        print(data)
        mycursor.execute("SELECT patient.PersonID,name,hospital,doctor,Appointment\
                        FROM patient JOIN med ON patient.PersonID=med.id \
                        WHERE RFID_pin='%s'"%data)
        myresult = mycursor.fetchall()
        for i in myresult:
            print(i)
            i=list(i)
        for j in range(len(i)):
            print(med_data[j],i[j])
    if num==5:
        print("place your reg tag -",end="")
        for i in range(2):
            data = arduino.readline()[0:-2]
            
            data=str(data)[2:-1]
        data=data.replace(" ","")
        print(data)
        mycursor.execute("SELECT patient.PersonID,name,dolo650,paracetamol,dog40,digene\
                        FROM patient JOIN drugs ON patient.PersonID=drugs.id \
                        WHERE RFID_pin=%s"%data)
        myresult = mycursor.fetchall()
        for i in myresult:
            i=list(i)
        print("name -",i[1])
        print("drugs:")
        for j in range(2,len(i)):
            if i[j]!=None:
                print(i[j],"x",drugs_data[j-2])
if __name__=="__main__":
    main()
