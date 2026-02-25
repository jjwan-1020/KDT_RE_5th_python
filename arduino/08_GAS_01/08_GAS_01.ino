#define GAS_AO A0
#define GAS_DO 8
void setup() {
  Serial.begin(9600);
  pinMode(GAS_AO, INPUT);
  pinMode(GAS_DO, INPUT);
  Serial.println("히터 가열 시작");
  delay(1000);
  Serial.println("히터 가열 종료 동작 시작");


}

void loop() {
  float sensorValue = analogRead(GAS_AO);
  int sensorDValue = digitalRead(GAS_DO);

  Serial.print("아날로그 센서 입력: ");
  Serial.print(sensorValue);

  Serial.print(" | ");
  Serial.print("디지털 센서 입력: ");
  Serial.print(sensorDValue);
  Serial.println();
  
  if (sensorValue > 100) {
    Serial.println("가스 누출 확인");
  }


  delay(1000);
}
