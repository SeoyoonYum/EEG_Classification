import serial

bluetooth_port = '/dev/tty.Bluetooth-Incoming-Port'  # Replace with the correct Bluetooth serial port on your system
ser = serial.Serial(bluetooth_port, baudrate=9600, timeout=1)

def send(data):
    try:
        
        data_to_send = data
        ser.write(data_to_send.encode())
    except KeyboardInterrupt:
        ser.close()