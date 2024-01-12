import serial
ser = serial.Serial("COM2", 9600)
while True:
     cc=str(ser.readline())
     print(cc[2:][:-5])