import serial
import time

def send_data_via_bluetooth(port, baudrate, data):
    # 블루투스 시리얼 연결 생성
    bluetooth = serial.Serial(port, baudrate)

    # 데이터 전송
    bluetooth.write(data.encode())  # 데이터를 바이트로 인코딩하여 전송합니다.
   
    # 시리얼 연결 종료
    bluetooth.close()

# 사용 예제:
port_name = "COM4"  # Windows의 경우, 예: "COM5". macOS의 경우, 예: "/dev/tty.HC-05-DevB" # COM4 ?
baud_rate = 9600
data_to_send = "YEAH!"

send_data_via_bluetooth(port_name, baud_rate, data_to_send)
