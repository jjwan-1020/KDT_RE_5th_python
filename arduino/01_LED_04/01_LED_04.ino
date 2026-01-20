int LEDS[]= {10,11,12};
int count = 3; // 배열 요소의 수가 달라져도 해당 변수값만 수정하면 됨

void setup() {
 for (int i = 0; i < 3; i++){
  pinMode(LEDS[i], OUTPUT);
  delay(500);
  }
 }

void turnOnALL() {
 for (int i = 0; i < 3; i++){
  pinMode(LEDS[i], OUTPUT);
  delay(500);
  }
 }

void turnOffALL() {
 for (int i = 0; i < 3; i++){
  pinMode(LEDS[i], OUTPUT);
  delay(500);
  }
 }
void loop() {
  turnOnALL();
delay(500)

  turnOffALL();
}
