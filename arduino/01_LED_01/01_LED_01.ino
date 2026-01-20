int LEDS[]= {10,11,12};
int count = 3; // 배열 요소의 수가 달라져도 해당 변수값만 수정하면 됨

void setup() {
 for (int i = 0; i < 3; i++){
  pinMode(LEDS[i], OUTPUT);
  }
 }


void loop() {
   for (int i = 0; i < 3; i++) {
    digitalWrite(LEDS[i], HIGH);
    delay(500);
   }
   // delay(500); //여기에 써도 괜찮음. 그냥 동작 방식이 달라지는 것
    for (int i = 0; i < 3; i++){
    pinMode(LEDS[i], LOW;);
    }
}
