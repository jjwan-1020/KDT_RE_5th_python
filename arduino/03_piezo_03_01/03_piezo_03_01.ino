const int piezo_pin = 8;
const int BTN = 2;

void setup() {
  Serial.begin(9600);
  pinMode(piezo_pin, OUTPUT);
  pinMOde(BTN, INPUT_PULLUP);
}

void loop() {
  int BTNState = digitalRead(BTN);
  digitalWrite(piezo_pin, LOW);

  if (BTNState == LOW) {
    Serial.println("부저 ON");
    digitalWrite(piezo_pin, HIGH);
  }
  else {
    Serial.println("부저 OFF");
  }
  delay(100);
}
