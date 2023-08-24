import serial
import time

def send(data):
    
    port = "COM4"
    baudrate = 9600
    # 블루투스 시리얼 연결 생성
    bluetooth = serial.Serial(port, baudrate)
    if data == 1:
        data = "open"
    elif data == 2:
        data = "grip"
    elif data == 3:
        data = "pinch"
    
    # 데이터 전송
    bluetooth.write(data.encode())  # 데이터를 바이트로 인코딩하여 전송합니다.
   
    # 시리얼 연결 종료
    bluetooth.close()


