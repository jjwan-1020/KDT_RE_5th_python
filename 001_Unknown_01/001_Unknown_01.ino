#include <DHT.h>
#define DHTPIN 3
#define DHTTYPE DHT22
#define GAS_DO 2
#define GAS_AO A0


DHT myDHT(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  myDHT.begin();
  pinMode(GAS_AO, INPUT);
  pinMode(GAS_DO, INPUT);
  Serial.println("가열 시작");
  delay(1000);
  Serial.println("동작 시작");
}

void loop() {
  delay(2000);
  float h = myDHT.readHumidity();
  float c = myDHT.readTemperature();
  float sensorValue = analogRead(GAS_AO);
  int sensorDValue = digitalRead(GAS_DO);

  Serial.print("온도: ");
  Serial.print(c);
  Serial.print("습도: ");
  Serial.print(h);
  Serial.println();
  Serial.print("아날로그 센서: ");
  Serial.print(sensorValue);
  Serial.print(" | ");
  Serial.print("디지털 센서: ");
  Serial.print(sensorDValue);
  Serial.println();

  delay(1000);
}

