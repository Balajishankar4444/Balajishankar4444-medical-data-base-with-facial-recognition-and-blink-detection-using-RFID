import serial
arduino = serial.Serial('COM4', 9600)
for i in range(2):
    data = arduino.readline()[0:-2] #the last bit gets rid of the new-line chars
data=str(data)[2:-1]
print(data)


