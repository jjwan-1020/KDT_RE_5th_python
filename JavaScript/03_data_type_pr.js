let person = {
    name: '이몽룡',
    age: 18,
    like: ['강아지', '고양이'],
    isMarried: true,
    girlfriend: {
        name: '성춘향',
        age: 16
    }
}

console.log(person);

let mathScore = '77';
let engScore = '88';

let avgScore = (parseFloat(mathScore) + parseFloat(engScore)) / 2;

console.log(mathScore.toString(), '점');
console.log(engScore.toString(), '점');
console.log(avgScore, '점');

// ==========================

// prompt를 사용한 수학/영어 평균 점수를 구하는 실습

let mathScore2 = prompt('수학점수 입력');
let engScore2 = prompt('영어점수 입력');
let avgScore2 = (parseFloat(mathScore2) + parseFloat(engScore2)) / 2;
console.log('평균 점수: ', (avgScore2));

// Leader
// let mathScore1 = prompt('수학 점수 입력'); // prompt로 입력받은 값은 string타입으로 변수에 저장
// let engScore1 = prompt('영어 점수 입력');
// console.log('수학 점수: ', mathScore1);
// console.log('영어 점수: ', engScore1);
// let avgScore1 = (mathScore1 + engScore1) / 2;
// console.log(avgScore1)

let mathScore1 = Number(prompt('수학 점수 입력')); // prompt로 입력받은 값은 string타입 값을 number로 형변환해서 저장
let engScore1 = Number(prompt('영어 점수 입력'));
console.log('수학 점수: ', mathScore1);
console.log('영어 점수: ', engScore1);
let avgScore1 = (mathScore1 + engScore1) / 2;
console.log(avgScore1)