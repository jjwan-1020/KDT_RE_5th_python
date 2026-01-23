#define GAS_AO A0
#define GAS_DO 8
#define PIEZO 12
#define LED 13

void setup() {
  pinMode(PIEZO, OUTPUT);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("히터 가열");
  delay(1000);
}

void loop() {
  digitalWrite(PIEZO, LOW);
  digitalWrite(LED, LOW);

  float sensorValue = analogRead(GAS_AO);
  float sensorDValue = digitalRead(GAS_DO);

  Serial.print("센서 확인: ");
  Serial.print(sensorValue);

  if (sensorValue > 100) {
    Serial.println("연기 감지");
    digitalWrite(PIEZO, HIGH);
    digitalWrite(LED, HIGH);
  }
  
  Serial.print("D-센서: ");
  Serial.print(sensorDValue);
  Serial.println();
  delay(1000);
}
