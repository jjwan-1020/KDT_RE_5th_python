/*
함수 매개변수 활용
*/

int LEDS[] = {10, 11, 12};
int count = 3;

/*
state ? HIGH : LOW
=> 조건 ? true일 때 반환할 값: false일 때 반환할 값
삼형연산자 > if문을 짧게 줄여놓은 것

if state:
  return HIGH
else:
  return LOW
*/

void blinkAll(bool state) {
  for (int i = 0; i < count; i++) {
    digitalWrite(LEDS[i], state ? HIGH : LOW);
    delay(500);
  }
}

void setup() {
  for (int i = 0; i < count; i++) {
    pinMode(LEDS[i], OUTPUT);
  }
}

void loop() {
  blinkAll(true);
  blinkAll(false);
}