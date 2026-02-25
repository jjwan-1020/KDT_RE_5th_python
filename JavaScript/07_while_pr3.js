let sum = 0; // 합계
let i = 0; // for 문에서 i 역할 (반복 횟수)
while (i <= 101) {
    if (i % 2 === 0 || i % 5 === 0) {
        sum += i;
    }
    i++;
}
console.log("합계: ", sum);