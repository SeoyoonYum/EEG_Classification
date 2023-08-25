#include <SoftwareSerial.h>

SoftwareSerial bluetooth(1, 0); // RX, TX

const int testmotorDelay = 200; const int halfmotorDelay = 1000; const int fullmotorDelay = 2000;

char command[5]; // 4 command characters + 1 null terminator

void setup() {
  bluetooth.begin(9600);
 
  int pins[] = {2, 3, 4, 5, 6, 7, 8, 9, A0, A1, A2, A3, A4, A5};
  for(int pin : pins) {
    pinMode(pin, OUTPUT); digitalWrite(pin, LOW);
  }
}

void testextend(int pin1, int pin2) {
  digitalWrite(pin1, LOW); digitalWrite(pin2, HIGH); delay(testmotorDelay); digitalWrite(pin2, LOW);
}
void testflex(int pin1, int pin2) {
  digitalWrite(pin2, LOW); digitalWrite(pin1, HIGH); delay(testmotorDelay); digitalWrite(pin1, LOW);
}

void halfextend(int pin1, int pin2) {
  digitalWrite(pin1, LOW); digitalWrite(pin2, HIGH); delay(halfmotorDelay); digitalWrite(pin2, LOW);
}
void halfflex(int pin1, int pin2) {
  digitalWrite(pin2, LOW); digitalWrite(pin1, HIGH); delay(halfmotorDelay); digitalWrite(pin1, LOW);
}

void fullextend(int pin1, int pin2) {
  digitalWrite(pin1, LOW); digitalWrite(pin2, HIGH); delay(fullmotorDelay); digitalWrite(pin2, LOW);
}
void fullflex(int pin1, int pin2) {
  digitalWrite(pin2, LOW); digitalWrite(pin1, HIGH); delay(fullmotorDelay); digitalWrite(pin1, LOW);
}

void fullextend2(int pin1, int pin2, int pin3, int pin4) {
  digitalWrite(pin1, LOW); digitalWrite(pin3, LOW);
  digitalWrite(pin2, HIGH); digitalWrite(pin4, HIGH);
  delay(fullmotorDelay);
  digitalWrite(pin2, LOW); digitalWrite(pin4, LOW);
}
void fullflex2(int pin1, int pin2, int pin3, int pin4) {
  digitalWrite(pin2, LOW); digitalWrite(pin4, LOW);
  digitalWrite(pin1, HIGH); digitalWrite(pin3, HIGH);
  delay(fullmotorDelay);
  digitalWrite(pin1, LOW); digitalWrite(pin3, LOW);
}

void fullextend3(int pin1, int pin2, int pin3, int pin4, int pin5, int pin6) {
  digitalWrite(pin1, LOW); digitalWrite(pin3, LOW); digitalWrite(pin5, LOW);
  digitalWrite(pin2, HIGH); digitalWrite(pin4, HIGH); digitalWrite(pin6, HIGH);
  delay(fullmotorDelay);
  digitalWrite(pin2, LOW); digitalWrite(pin4, LOW); digitalWrite(pin6, LOW);
}
void fullflex3(int pin1, int pin2, int pin3, int pin4, int pin5, int pin6) {
  digitalWrite(pin2, LOW); digitalWrite(pin4, LOW); digitalWrite(pin6, LOW);
  digitalWrite(pin1, HIGH); digitalWrite(pin3, HIGH); digitalWrite(pin5, HIGH);
  delay(fullmotorDelay);
  digitalWrite(pin1, LOW); digitalWrite(pin3, LOW); digitalWrite(pin5, LOW);
}

void fullextend4(int pin1, int pin2, int pin3, int pin4, int pin5, int pin6, int pin7, int pin8) {
  digitalWrite(pin1, LOW); digitalWrite(pin3, LOW); digitalWrite(pin5, LOW); digitalWrite(pin7, LOW);
  digitalWrite(pin2, HIGH); digitalWrite(pin4, HIGH); digitalWrite(pin6, HIGH); digitalWrite(pin8, HIGH);
  delay(fullmotorDelay);
  digitalWrite(pin2, LOW); digitalWrite(pin4, LOW); digitalWrite(pin6, LOW); digitalWrite(pin8, LOW);
}
void fullflex4(int pin1, int pin2, int pin3, int pin4, int pin5, int pin6, int pin7, int pin8) {
  digitalWrite(pin2, LOW); digitalWrite(pin4, LOW); digitalWrite(pin6, LOW); digitalWrite(pin8, LOW);
  digitalWrite(pin1, HIGH); digitalWrite(pin3, HIGH); digitalWrite(pin5, HIGH); digitalWrite(pin7, HIGH);
  delay(fullmotorDelay);
  digitalWrite(pin1, LOW); digitalWrite(pin3, LOW); digitalWrite(pin5, LOW); digitalWrite(pin7, LOW);
}

void fullextendall() {
  digitalWrite(2, LOW); digitalWrite(4, LOW); digitalWrite(6, LOW); digitalWrite(8, LOW); digitalWrite(A0, LOW);
  digitalWrite(3, HIGH); digitalWrite(5, HIGH); digitalWrite(7, HIGH); digitalWrite(9, HIGH); digitalWrite(A1, HIGH);
  delay(fullmotorDelay);
  digitalWrite(3, LOW); digitalWrite(5, LOW); digitalWrite(7, LOW); digitalWrite(9, LOW); digitalWrite(A1, LOW);
}
void fullflexall() {
  digitalWrite(3, LOW); digitalWrite(5, LOW); digitalWrite(7, LOW); digitalWrite(9, LOW); digitalWrite(A1, LOW);
  digitalWrite(2, HIGH); digitalWrite(4, HIGH); digitalWrite(6, HIGH); digitalWrite(8, HIGH); digitalWrite(A0, HIGH);
  delay(fullmotorDelay);
  digitalWrite(2, LOW); digitalWrite(4, LOW); digitalWrite(6, LOW); digitalWrite(8, LOW); digitalWrite(A0, LOW);
}

void wristbalance() {
  while (((analogRead(A6)>180)||(analogRead(A7)>180))||((analogRead(A6)<170)||(analogRead(A7)<170))) {
    if (analogRead(A6)>180) { digitalWrite(A2, LOW); digitalWrite(A3, HIGH); }
    else if (analogRead(A6)<170) { digitalWrite(A2, HIGH); digitalWrite(A3, LOW); }
    else if (analogRead(A7)>180) { digitalWrite(A4, LOW); digitalWrite(A5, HIGH); }
    else if (analogRead(A7)<170) { digitalWrite(A4, HIGH); digitalWrite(A5, LOW); }
  }
  digitalWrite(A2, LOW); digitalWrite(A3, LOW); digitalWrite(A4, LOW); digitalWrite(A5, LOW);
}

void wristtwistCW() {
  while (analogRead(A7) - analogRead(A6) < 100) {
    digitalWrite(A2, LOW); digitalWrite(A5, LOW); digitalWrite(A3, HIGH); digitalWrite(A4, HIGH);
  }
  digitalWrite(A3, LOW); digitalWrite(A4, LOW);
}
void wristtwistCCW() {
  while (analogRead(A6) - analogRead(A7) < 150) {
    digitalWrite(A3, LOW); digitalWrite(A4, LOW); digitalWrite(A2, HIGH); digitalWrite(A5, HIGH);
  }
  digitalWrite(A2, LOW); digitalWrite(A5, LOW);
}

void wristextend() {
  while (((analogRead(A6)>80)||(analogRead(A7)>80))||((analogRead(A6)<70)||(analogRead(A7)<70))) {
    if (analogRead(A6)>80) { digitalWrite(A2, LOW); digitalWrite(A3, HIGH); }
    else if (analogRead(A6)<70) { digitalWrite(A2, HIGH); digitalWrite(A3, LOW); }
    else if (analogRead(A7)>80) { digitalWrite(A4, LOW); digitalWrite(A5, HIGH); }
    else if (analogRead(A7)<70) { digitalWrite(A4, HIGH); digitalWrite(A5, LOW); }
  }
  digitalWrite(A2, LOW); digitalWrite(A3, LOW); digitalWrite(A4, LOW); digitalWrite(A5, LOW);
}
void wristflex() {
  while (((analogRead(A6)>230)||(analogRead(A7)>230))||((analogRead(A6)<220)||(analogRead(A7)<220))) {
    if (analogRead(A6)>230) { digitalWrite(A2, LOW); digitalWrite(A3, HIGH); }
    else if (analogRead(A6)<220) { digitalWrite(A2, HIGH); digitalWrite(A3, LOW); }
    else if (analogRead(A7)>230) { digitalWrite(A4, LOW); digitalWrite(A5, HIGH); }
    else if (analogRead(A7)<220) { digitalWrite(A4, HIGH); digitalWrite(A5, LOW); }
  }
  digitalWrite(A2, LOW); digitalWrite(A3, LOW); digitalWrite(A4, LOW); digitalWrite(A5, LOW);
}

void processCommand() {
  // Finger ABCDE Full Extend/Flex
  if (strcmp(command, "fafe") == 0) fullextend(2, 3); else if (strcmp(command, "faff") == 0) fullflex(2, 3);
  else if (strcmp(command, "fbfe") == 0) fullextend(4, 5); else if (strcmp(command, "fbff") == 0) fullflex(4, 5);
  else if (strcmp(command, "fcfe") == 0) fullextend(6, 7); else if (strcmp(command, "fcff") == 0) fullflex(6, 7);
  else if (strcmp(command, "fdfe") == 0) fullextend(8, 9); else if (strcmp(command, "fdff") == 0) fullflex(8, 9);
  else if (strcmp(command, "fefe") == 0) fullextend(A0, A1); else if (strcmp(command, "feff") == 0) fullflex(A0, A1);

  // Finger BC Full Extend/Flex
  else if (strcmp(command, "bcfe") == 0) fullextend2(4, 5, 6, 7); else if (strcmp(command, "bcff") == 0) fullflex2(4, 5, 6, 7);

  // Finger BE Full Extend/Flex
  else if (strcmp(command, "befe") == 0) fullextend2(4, 5, A0, A1); else if (strcmp(command, "beff") == 0) fullflex2(4, 5, A0, A1);

  // Wrist Full Movement Balance
  else if (strcmp(command, "wfmb") == 0) wristbalance();

  // Wrist Full Movement Extend/Flex
  else if (strcmp(command, "wfme") == 0) fullextend2(A2, A3, A4, A5); else if (strcmp(command, "wfmf") == 0) fullflex2(A2, A3, A4, A5);

  // Wrist Rotation External/Internal
  else if (strcmp(command, "whre") == 0) wristtwistCW(); else if (strcmp(command, "whri") == 0) wristtwistCCW();

  // All Finger Full Extend/Flex
  else if (strcmp(command, "affe") == 0) fullextendall(); else if (strcmp(command, "afff") == 0) fullflexall();

  // Special Show-off Mission Alpha
  else if (strcmp(command, "ssma") == 0) {
    wristbalance();
    fullextend(2, 3); fullextend(4, 5); fullextend(6, 7); fullextend(8, 9); fullextend(A0, A1);
    delay(500);
    fullflex(A0, A1); fullflex(8, 9); fullflex(6, 7); fullflex(4, 5); fullflex(2, 3);
    wristbalance();
  }

  // Special Show-off Mission Beta
  else if (strcmp(command, "ssmb") == 0) {
    wristbalance();
    fullextend(4, 5); fullextend(A0, A1);
    wristtwistCW(); wristtwistCCW(); wristtwistCW(); wristtwistCCW();
    wristbalance();
    wristflex(); wristextend(); wristflex(); wristextend();
    wristbalance();
    fullflex(4, 5); fullflex(A0, A1);
  }

  // Special Show-off Mission Gamma
  else if (strcmp(command, "ssmc") == 0) {
    wristbalance();
    fullextend(4, 5); fullextend(A0, A1);
    for (int i=0; i<10; i++) { wristtwistCW(); wristtwistCCW(); wristtwistCW(); wristtwistCCW(); }
    wristbalance();
    fullflex(4, 5); fullflex(A0, A1);
  }

  // Eye Blink Motion Alpha (Grip)
  else if (strcmp(command, "ebma") == 0) {
    wristbalance();
    fullflex(2, 3); fullflex(4, 5); fullflex(6, 7); fullflex(8, 9); fullflex(A0, A1);
  }
  // Eye Blink Motion Alpha (Grip Lose)
  else if (strcmp(command, "ebmb") == 0) {
    wristbalance();
    fullextend(2, 3); fullextend(4, 5); fullextend(6, 7); fullextend(8, 9); fullextend(A0, A1);
  }

  // Eye Blink Motion Alpha (Pinch)
  else if (strcmp(command, "ebmc") == 0) {
    wristbalance();
    fullflex(4, 5); fullflex(2, 3);
  }
  // Eye Blink Motion Alpha (Pinch Lose)
  else if (strcmp(command, "ebmd") == 0) {
    wristbalance();
    fullextend(2, 3); fullextend(4, 5);
  }

  // Finger ABCDE Test Extend/Flex
  else if (strcmp(command, "fate") == 0) testextend(2, 3); else if (strcmp(command, "fatf") == 0) testflex(2, 3);
  else if (strcmp(command, "fbte") == 0) testextend(4, 5); else if (strcmp(command, "fbtf") == 0) testflex(4, 5);
  else if (strcmp(command, "fcte") == 0) testextend(6, 7); else if (strcmp(command, "fctf") == 0) testflex(6, 7);
  else if (strcmp(command, "fdte") == 0) testextend(8, 9); else if (strcmp(command, "fdtf") == 0) testflex(8, 9);
  else if (strcmp(command, "fete") == 0) testextend(A0, A1); else if (strcmp(command, "fetf") == 0) testflex(A0, A1);

  // Finger ABCDE Half Extend/Flex
  else if (strcmp(command, "fahe") == 0) halfextend(2, 3); else if (strcmp(command, "fahf") == 0) halfflex(2, 3);
  else if (strcmp(command, "fbhe") == 0) halfextend(4, 5); else if (strcmp(command, "fbhf") == 0) halfflex(4, 5);
  else if (strcmp(command, "fche") == 0) halfextend(6, 7); else if (strcmp(command, "fchf") == 0) halfflex(6, 7);
  else if (strcmp(command, "fdhe") == 0) halfextend(8, 9); else if (strcmp(command, "fdhf") == 0) halfflex(8, 9);
  else if (strcmp(command, "fehe") == 0) halfextend(A0, A1); else if (strcmp(command, "fehf") == 0) halfflex(A0, A1);
}

void loop() {
  if (bluetooth.available() >= 4) {  // If at least 2 characters are available
    command[0] = bluetooth.read();  // Read the first character
    command[1] = bluetooth.read();  // Read the second character
    command[2] = bluetooth.read();  // Read the third character
    command[3] = bluetooth.read();  // Read the fourth character
    command[4] = '\0';  // Null terminate the string

    processCommand();
  }
}