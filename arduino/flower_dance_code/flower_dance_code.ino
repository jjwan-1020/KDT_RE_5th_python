

#define BUZZER 8

#define NOTE_C4  262
#define NOTE_D4  294
#define NOTE_E4  330
#define NOTE_F4  349
#define NOTE_G4  392
#define NOTE_A4  440
#define NOTE_B4  494
#define NOTE_C5  523
#define NOTE_D5  587
#define NOTE_E5  659
#define NOTE_G5  784

int melody[] = {
  NOTE_E5, NOTE_D5, NOTE_C5, NOTE_D5,
  NOTE_E5, NOTE_G5, NOTE_E5,
  NOTE_D5, NOTE_C5, NOTE_A4,
  NOTE_C5, NOTE_D5, NOTE_E5,
  NOTE_D5, NOTE_C5
};

int noteDurations[] = {
  8, 8, 8, 8,
  4, 4, 4,
  8, 8, 4,
  8, 8, 4,
  4, 2
};

void setup() {
  pinMode(BUZZER, OUTPUT);
}

void loop() {
  for (int i = 0; i < 15; i++) {
    int duration = 1000 / noteDurations[i];
    tone(BUZZER, melody[i], duration);

    delay(duration * 1.3);  
    noTone(BUZZER);
  }

  delay(3000); 
}
