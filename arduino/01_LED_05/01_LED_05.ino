// 함수 매개변수 활용//

int LEDS[]= {10,11,12};
int count = 3; // 배열 요소의 수가 달라져도 해당 변수값만 수정하면 됨

/* state ? HIGH : LOW => 
조건 ? true일때 반환할 값 : false일때 반환할 값
삼항연산자 => if문을 아주 짧게 줄어놓은 것
state가 true인지 false
if state == true
  return HIGH
else:
  return LOW

*/
void blinkALL(bool state) {
 for (int i = 0; i < count; i++){
  pinMode(LEDS[i], state ? HIGH : LOW);
  delay(500);
  }
 }
void setup() {
 for (int i = 0; i < 3; i++){
  pinMode(LEDS[i], OUTPUT);
  }
 }

 void loop() {
  blinkALL(true);
  blinkALL(false);
 }
