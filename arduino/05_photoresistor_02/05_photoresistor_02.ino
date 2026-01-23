void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT); //LED

}

void loop() {
  int photoresistor = analogRead(A0);
  Serial.println(photoresistor);

  if (photoresistor > 900)
    digitalWrite(13, HIGH);
  else
    digitalWrite(13, LOW);

}
