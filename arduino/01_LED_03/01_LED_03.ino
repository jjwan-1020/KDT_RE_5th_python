/* ctrl + n : 아두이노 새 스케치 열기

새로운 스케치를 열면 새로운 창이 열림

아두이노 IDE에서는 탭 방식이 아닌 여러 창을 사용하는 방식이기 떄문

스케치 = 하나의 폴더
폴더 = 하나의 독립 프로젝트
그렇기 떄문에 프로젝트마다 별도의 창이 생기고 사용하는 것
---

폴더 = 하나의 독립 프로젝트
그래서 .ino 파일은 새로운 폴더 안에 생김

아두인노는 폴더 이름과 동일한 .ino 파일을 "메인 파일"로 간주
같은 폴더 안의 .ino 파일은 하나의 코드처럼 합쳐서 컴파일

즉 하나의 스케치 폴더 안에는 .ino 파일이 여러개 있으면 하나의 큰 코드로 인식
하나의 스케치 폴더 안에는 setup(), loop()가 단 하나씩만 존재해야함.
*/

int RED_LED = 10;
int GREEN_LED = 11;
int BLUE_LED = 12;

void setup() {
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop() {
  digitalWrite(10, HIGH);
  delay(500);
  digitalWrite(10, LOW);
  delay(500);
  digitalWrite(11, HIGH);
  delay(500);
  digitalWrite(11, LOW);
  delay(500);
  digitalWrite(12, HIGH);
  delay(500);
  digitalWrite(12, LOW);
  delay(500);
}