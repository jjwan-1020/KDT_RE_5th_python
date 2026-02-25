int swich1 = 12;
int LED_Blue = 4;
int swtich2 = 11;
int LED_Green = 5;

void setup() {
  Serial.begin(9600);
  pinMode(12, INPUT_PULLUP);
  pinMode(4, OUTPUT);
  pinMode(11, INPUT_PULLUP); 
  pinMode(5, OUTPUT);
}

void loop() {
  int SW1 = digitalRead(12);
  int SW2 = digitalRead(11);

  digitalWrite(LED_Blue, LOW);
  digitalWrite(LED_Green, LOW);

  if(SW1 == LOW) {
    Serial.println("SWitch : Blue");
    digitalWrite(LED_Blue, HIGH);
  }
  if(SW2 == LOW) {
    Serial.println("Swtich : Green");
    digitalWrite(LED_Green, HIGH);
  }
  delay(100);
}
