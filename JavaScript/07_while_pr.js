console.log('1부터 10000까지 13배수 구하기');
for (let i = 1; i <= 10000; i++) {
    if (1 % 13 === 0 && i % 2 === 1) {
        // i % 13 === 0 => 13의 배수
        // i % 2 === 1 => 홀수
        console.log(i);
    }
}

// 아래처럼도 작성 가능
// for (let i = 13; i < 10000; i +=13) {}
let num = Number(prompt('숫자를 입력해주세요'));
for (let i = 1; i <= num; i++) {
    if (1 % 13 === 0 && i % 2 === 1) {
        console.log(i);
    }
}