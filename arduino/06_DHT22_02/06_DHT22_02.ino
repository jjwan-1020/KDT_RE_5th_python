#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT22

DHT myDHT(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  myDHT.begin();
}

void loop() {
  delay(2000);
  float h = myDHT.readHumidity(); 
  float c = myDHT.readTemperature(); 
  float f = myDHT.readTemperature(true); 

  
if (isnan(h) || isnan(c) || isnan(f)) {
  Serial.println("값을 읽어오지 못했습니다.");
  return; 
  }

  Serial.print("습도: ");
  Serial.print(h);
  Serial.print(" | 섭씨 온도: ");
  Serial.print(c);
  Serial.print(" | 화씨 온도: ");
  Serial.print(f);
  Serial.println();
}
