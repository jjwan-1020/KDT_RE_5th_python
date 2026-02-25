void setup() {
    pinMode(3, OUTPUT);
}

void loop() {
    digitalWrite(3, HIGH); // 3번 핀을 high (5볼트)로 출력 > LED 켜짐
    delay(1000); // LED가 켜진 상태로 1초 중지
    digitalWrite(3, LOW) // 3번 핀을 low (0볼트)로 출력 > LED꺼짐
    delay(1000); // LED가 꺼진 상태로 1초 중지
}