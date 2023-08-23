import serial

bluetooth_port = '/dev/tty.Bluetooth-Incoming-Port'  # Replace with the correct Bluetooth serial port on your system
with serial.Serial(bluetooth_port, baudrate=9600, timeout=1) as ser:
    def send(data):
        try:
            
            if data == 1:
                data_to_send = "open"
                ser.write(data_to_send.encode())
            if data == 2:
                data_to_send = "grip"
                ser.write(data_to_send.encode())
            if data == 3:
                data_to_send = "pinch"
                ser.write(data_to_send.encode())
        except KeyboardInterrupt:
            ser.close()