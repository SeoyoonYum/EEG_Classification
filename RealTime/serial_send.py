import serial
import time

def send(data):
    
    port = "COM4"
    baudrate = 9600
    # 블루투스 시리얼 연결 생성
    bluetooth = serial.Serial(port, baudrate)
    if data == 1:
        data = "ebma" # eye blink movement A
    elif data == 2:
        data = "ebmb" # eye blink movement B
    elif data == 3:
        data = "ebmc" # eye blink movement C
    
    # 데이터 전송
    bluetooth.write(data.encode())  # 데이터를 바이트로 인코딩하여 전송합니다.
   
    # 시리얼 연결 종료
    bluetooth.close()


