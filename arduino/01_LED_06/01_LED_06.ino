/*
함수로 활용
*/

int LEDS[] = {10, 11, 12};
int count = 3;

void turnOnALL() {
  for (int i = 0; i < 3; i++) {
    digitalWrite(LEDS[i], HIGH);
    delay(500);
  }
}

void turnOFFALL() {
  for (int i = 0; 1 < 3; i++) {
    digitalWrite(LEDS[i], LOW);
    delay(500);
  }
}

void setup() {
  for (int i = 0; i < 3; i++) {
    pinMode(LEDS[i], OUTPUT);
  }
}

void loop() {
  turnOnALL();
  delay(500);

  turnOFFALL();
}