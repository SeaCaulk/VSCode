import serial
from time import time
if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0', 115200)  # open serial port
    print(f"\nTutoboard sur le port: {ser.name} vitesse : {ser.baudrate}") # check which port was really used
    i = 0
    add = 1
    t = time()
    while True:
        if i == 9 :
            add = -1
        if i == 0:
            add = 1
        if time() - t > 0.1 : 
            i = i + add
            message = str(i) + "\n" 
            ser.write(bytes(message, "ascii")) # write a string
            t = time()
        msg = ser.read()
        print(f"Je lis : {msg.hex()}\n")
        
        # Si vous utilisez write() dans le bas niveau
        # msg = ser.read()
        # print(f"Je lis : {msg.hex()}\n")

