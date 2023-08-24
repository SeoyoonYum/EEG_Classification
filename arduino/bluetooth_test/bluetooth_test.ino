#include <SoftwareSerial.h> //시리얼통신 라이브러리 호출
 
int blueTx=2;   //Tx (보내는핀 설정)at
int blueRx=3;   //Rx (받는핀 설정)
SoftwareSerial mySerial(blueTx, blueRx);  //시리얼 통신을 위한 객체선언
 
void setup()
{
  Serial.begin(9600);   //시리얼모니터
  mySerial.begin(9600); //블루투스 시리얼
}
void loop()
{
  if (mySerial.available()) {      
    Serial.write(mySerial.read());  //블루투스측 내용을 시리얼모니터에 출력
  }
  String data = mySerial.read();
  if (data == "open"){
    //code for opening hand
  }
  else if (data == "grip"){
    //code for gripping hand
  }
  else if (data == "pinch"){
    //code for pinching hand
  }
}
