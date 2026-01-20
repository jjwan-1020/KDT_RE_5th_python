int RED_LED = 10;
int Green_LED = 11;
int Blue_LED = 12;

void setup() {
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop() {
  digitalWrite(10, HIGH);
  delay(500);
  digitalWrite(10, HIGH);
  delay(500);
  digitalWrite(11, HIGH);
  delay(500);
  digitalWrite(11, LOW);
  delay(500);
  digitalWrite(12, LOW);
  delay(500);
  digitalWrite(12, LOW);
  delay(500);
}