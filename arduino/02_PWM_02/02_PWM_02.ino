void setup() {
  pinMode(3, OUTPUT);

}

void loop() {
  analogWrite(3, 0);
  delay(500);
  analogWrite(3, 51);
  delay(500);
  analogWrite(3, 153);
  delay(500);
  analogWrite(3, 204);
  delay(500);
  analogWrite(3, 255);
  delay(500);
}
