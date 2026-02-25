// 원시 자료형

// 1.문자열 (string)
const str = '좋은 아침';
console.log(str);

// 문자열 연산
const str2 = '오늘도 화이팅😊'
console.log(str + str2);

const name = "jjwan";
const age = 27;
console.log("안녕하세요~저는 " + name + "이고, 나이는 " + age + "입니다");

//  템플릿 리터럴
//  변수화 문자열을 함께 쓸 수 있도록 하는 문법
console.log(`안녕하세요 저는 ${name}이고 나이는 ${age}살 입니다`);

console.log(`변수말고 코드 실행도 가능하다 ${4 + 6}`);

//===========
// 2. 숫자형(number)
//  정수와 실수를 구분하지 않음
const num = 100;
const num2 = 3.14;
console.log("숫자형", num, num2);

//===========
// 3. 불리언/논리형 (boolean)
//  참 or 거짓을 표현하는 true, false
const isTure = true;
const isFalse = false;
console.log("불리연", isTure, isFalse);

//===========
// 4. null(빈 값)
// 의도적으로 값을 비운 상태
// "값이 없음"을 명시
let isVar = null;
console.log(isVar);
isVar = "이렇게 이후 값이 할당될 수 있다";
console.log(isVar);

//===========
// 5. undefined
// 값이 정의(할당)되지 않은 상태
let x;
console.log(x); // undefined 출력 
// console.log(x2); 할당되지 않은 변수로 에러 발생

//===========

// [객체 자료형]

// 1. 배열 (array)
const fruits = ["청포도", "오랜지", "체리", "말랑복숭아", "망고스틴"]
console.log('배열', fruits);

// 인덱싱
console.log(fruits[3]);
console.log(fruits[-1]); // undefined 출력

// at 활용 시 음수 인덱싱 가능
console.log(fruits.at(2)); // 체리 출력
console.log(fruits.at(-1)); // 망고스틴 출력

fruits[3] = '딱복숭아';
console.log(fruits);

// 배열 안에 요소로 배열 넣을 수 있음
const korean = [
    ['가', '나', '다'],
    ['라', '마', '바'],
    ['사', '아', '자']
];

//변수 차제에 대한 재할당은 불가
//하지만 배열 내부의 요소는 수정가능

korean[2][2] = '하';
console.log(korean[2][2]);
console.log(korean);

//변수 차제에 대한 재할당은 불가
//하지만 배열 내부의 요소는 수정가능
// korean = [
//     [1,2,3],
//     [4,5,6],
//     [7,8,9]
// ]

korean[0] = [1, 2, 3];
console.log(korean);

//===========

// 2. 객체 (object)
// 키-값 쌍을 값으로 가짐
let cat = {
    name: "장화",
    age: 18,
    isCute: true,
    mew: function () {
        return '야옹';
    },
};

console.log('객체', cat);

// 객채의 값 초회
// 1. 점 표기법
// 키가 문자열인 경우만 가능
console.log(cat.name);
console.log(cat.age);
// console.log(cat.12); // 키가 숫자인 경우 접근 못함
// 2. 대괄호 표기법
console.log(cat[`name`]);
console.log(cat['age']);
// console.log(cat[12]); // 키가 숫자여도 접근 가능

cat.mew(); // '야옹'이라는 문자열이 리턴됨
console.log(cat.mew());
let catMew = cat.mew();
console.log(catMew);

let cat2 = {
    name: "장화",
    age: 18,
    isCute: true,
    mew: function () {
        // console.log('야옹22');
    },
};

cat2.mew(); // cat2라는 객체의 mew키 값을 실행시키는 코드

let cat3 = {
    name: "장화",
    age: 18,
    isCute: true,
    mew: function (str) {
        return str;
    },
};

cat3.mew('야옹야옹'); // 매개변수로 전달한 "야옹야옹"을 리턴됨
// alert(cat3.mew('야옹야옹'));
// alert(cat3.mew('멍멍'));

//===========

// 자료형 확인 (typeof)
console.log(typeof '문자'); // string
console.log(typeof 1000); // number
console.log(typeof 3.14); // number
console.log(typeof true); // boolean
console.log(typeof false); // boolean
console.log(typeof null); // object
console.log(typeof undefined); // undefined

// 배열은 object 하위의 array이고, array에는 메서드들이 자동으로 포함되어 typeof로 자료형 확인 시 object로 출력됨
console.log(typeof fruits); // object 
console.log(typeof cat); // object

//===================
// 실습
`
const mongryong = {
    name: '이몽룡',
    age: 18,
    like: ['강아지', '고양이'],
    isMarried: true,
    girlfriend: {
        name: '성춘향',
        age: 16
    }
}

console.log(mongryong);
`
//=============================

//  형변환
// 1. 암시적 형변환
console.log('암시적 형변환 (1)', '2' + 3);
// 기대치: 암시적 형번환 (1), 2(문자열) 3(문자열)
// 실제로 출력= 임시적 형번환 (1) 23

console.log('암시적 형변환 (2', typeof (100 + '1'));
// 기대: 에러
// 숫자 더하기 문자는 타입(자료형)을 알 수 없기 때문
// 결과 암시적 형변환 (2) string
// JS가 자기 마음대로 숫자를 문자로 변환해버림

// 2. 명시적 형변환
// 2-1. 문자열로 변환: string(), toString()
let string1 = 123;
let string2 = true;
let string3 = undefined;

// String() 사용
console.log(String(string1), typeof String(string1)); // 숫자 123은 문자열 "123"으로 변함
console.log(String(string2), typeof String(string2)); // "true"
console.log(String(string3), typeof String(string3)); // "undefined"

// .toString() 사용
console.log(String(string1), typeof string1.toString());
console.log(String(string2), typeof string2.toString());
// console.log(String(string3), typeof string3.toString()); // 변수 값이 없기 때문에 변환 불가해서 에러

// 2-2. 숫자로 변환: Number(), parseInt()
let number1 = '123';
let number2 = false;
let number3 = '진짜 문자열';
let number4 = 3.14;
let number5 = '3.14';

// Number() 사용
console.log('===')
console.log(Number(number1), typeof Number(number1)); // 123
console.log(Number(number2), typeof Number(number2)); // 0 -> false는 다르게 표현하면 0이기 때문에 숫자 변환시 0으로 변환됨
console.log(Number(number3), typeof Number(number3)); // NAN -> Not a Number의 약자
console.log(Number(number4), typeof Number(number4)); // 3.14
console.log(Number(number5), typeof Number(number5)); // 3.14

// 정의되지 않음 => 값이 아예 없는 것 => NAN
console.log(Number(undefined), typeof Number(undefined)); // NAN

//  값이 없음을 정의 => 값이 없다는 것을 표현하는 값만 0으로 변환
console.log(Number(null), typeof Number(null)); // 0

// parseInt() 사용 => 소수점 버리고 정수로 출력
console.log(parseInt(number1), typeof parseInt(number1)); // 123
console.log(parseInt(number4), typeof parseInt(number4)); // 3
console.log(parseInt(number5), typeof parseInt(number5)); // 3
console.log(parseInt(3.8), typeof parseInt(3.8)) // 3

// parseFloat() 사용
console.log('===parseFloat 출력 결과===')
console.log(parseFloat(number4), typeof parseFloat(number4)) // 3.14
console.log(parseFloat(number5), typeof parseFloat(number5)) // 3.14
console.log(parseFloat(3.8), typeof parseFloat(3.8)) // 3.8