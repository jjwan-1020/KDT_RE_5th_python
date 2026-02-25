let num = [];
for (let i = 1; i <= 100; i++) {
    num.push(i);
}
console.log('배열은:', num);
console.log("========")
let sumnum = 0;
for (let i = 0; i < num.length; i++) {
    sumnum += num[i];
}
console.log('for문 합:', sumnum);
console.log("========")
let ofnum = 0;
for (let number of num) {
    ofnum += number;
}
console.log('forof문합:', ofnum);
console.log("========")
let chnum = 0;
num.forEach(numbers => {
    chnum += numbers;
})
console.log('forEach문합:', chnum);

// reduce
// let sum4 = num.reduce((acc, cur) => acc + cur);

console.log("========")

let fr1 = ['사과', '딸기', '파인애플', '수박', '참외', '오렌지', '자두', '망고']
let fr2 = ['수박', '사과', '참외', '오렌지', '파인애플', '망고']

let same = fr1.filter((fr) => fr2.includes(fr))
console.log('same배열 출력:', same);

let diff = fr1.filter((fr) => !fr2.includes(fr))
console.log('diff배열 출력', diff);

// 평일/주말 구분
// JS에 내장된 Date 객체 활용
// Date.getDay(): 요일별로 0~6(일~토)로 숫자 반환
let now = new Date();
console.log(now.getDay()); // 금요일 기준 5가 출력
console.log("===============")

let now2 = new Date();
let day = now2.getDate();
if (day === 0 || day === 6) {
    console.log('오늘은 주말입니다');
} else {
    console.log('오늘은 평일입니다');
}

console.log("===============")

let rnum = Math.floor(Math.random() * 11);
console.log('랜덤 숫자:', rnum);

// switch문 활용
switch (nowDay) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        console.log('평일');
        break;
    case 0:
    case 6:
        console.log('주말');
        break;
    default:
        console.log('조건에 맞지 않습니다');
        break;
}

// 삼항연산자
let today = nowDay === 0 || 6 ? '주말' : '평일'
console.log(today);






// 4. 0~10사이의 랜덤 숫자 출력
// Math.random(): 0이상 1미만의 난수 생성
// Math.floor(x): 양수 기준으로는 소숫점 버림, 음수 기준으로는 더 작은 음수로 소숫점 사라짐
// Math.floor(3.2984676) -> 3 -> 소숫점 버림
// Math.floor(3.2984676) -> 4 -> floor 즉, 바닥으로 내린다는 것은 값을 줄인다 그래서 음수에서는 더 작은 음수 값으로 반환

console.log(Math.floor(Math.random()))

// 0.2 * 10 = 2
// 0.6354 * 10 = 6.354
// 즉, Math.random() * 10의 결과는 10미만 결과 출력
// 하지만 실습 조건은 10을 포함해야함
// 0 * 11 = 0
// 0.966 * 11 = 10.626
// 0.9999999 * 11 = 10.9999999
// 무조건 11 미만 숫자가 나옴
// 그리고 그 결과를 Math.floor()하면 0~10 사이 숫자가 반환됨
