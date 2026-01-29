// 1. 문자열
let str = '      Hellow JavaScript World      ';

console.log('원본 str', str);

// .length
console.log('길이: ', str.length); // 함수 X, 하나의 속성

// .trim : 공백 제거
console.log('공백 제거: ', str.trim()); // "Hellow JavaScript World" 앞 뒤 공백 사라짐
console.log('원본 str', str); // 원본 변경 X 

// 대소문자 변환
console.log('대문자 변환: ', str.toUpperCase()); // "        HELLOW JAVASCRIPT WORLD      "
console.log('원본 str', str); // 원본 변경 X 

console.log('소문자 변환: ', str.toLowerCase()) // "        hellow javascript world      "
console.log('원본 str', str); // 원본 변경 X 

// 탐색
console.log('인덱스 찾기: ', str.indexOf('J')); // 13
console.log('인덱스 찾기', str.indexOf('Java')); // 13 -> 매개변수로 받은 문자열의 첫 번째 글자 인덱스 변환
console.log('인덱스 찾기', str.indexOf('Jva')); // -1 -> 매개변수로 받은 문자열이 없다면 -1 반환

console.log('문자열의 포함 여부 확인', str.includes('Java')); // true -> 불리언으로 반환
// indexOf()로도 문자열에 포함 여부 알 수 있음 -> -1 반환하면 없다는 것
console.log('문자열의 포함 여부 확인', str.includes('Jva')); // false -> 불리언으로 반환

// 슬라이싱
console.log('슬라이싱', str.slice(6, 16)); // Hellow Jav -> 6번 인덱스 부터 15번 인덱스 문자열까지 출력
console.log('원본 str', str); // 원본 변경 X 

// 치환
console.log('한 글자 치환: ', str.replace('a', 'e')); //         Hellow JevaScript World      -> 문자열 중에서 가장 처음 나오는 a라는 문자를 e로 치환
console.log('한 단어 치환: ', str.replace('World', 'Universe')); // 단어도 치환 가능
console.log('전부 치환: ', str.replaceAll('l', 'v'));
console.log('원본 str', str); // 원본 변경 X 

// 분할
// ''(공백)을 매개변수로 전달 시 문자열의 모든 글자들이 하나씩 짤려서 배열로 반환
console.log('분할: ', str.split('')); // ' ', ' ', ' ', ' ', ' ', ' ', 'H', 'e', 'l', 'l', 'o', 'w', ' ', 'J', 'a', 'v', 'a', 'S', 'c', 'r', 'i', 'p', 't', ' ', 'W', 'o', 'r', 'l', 'd', ' ', ' ', ' ', ' ', ' ', ' ']

// ' '(공백 한 칸)을 기준으로 문자열을 나눠서 배열로 반환
console.log('분할: ', str.split(' ')); // '', '', '', '', '', '', 'Hellow', 'JavaScript', 'World', '', '', '', '', '', '']

// 분할하는 기준인 매개변수 문자는 사라지고 배열로 만들어져서 반환
console.log('l 기준 분할: ', str.split('l')); // ['      He', '', 'ow JavaScript Wor', 'd      ']
console.log('원본 str', str); // 원본 변경 X 

// 합치기
let str2 = 'with JavaScript';
console.log('문자열 합치기', str.concat(str2)); //        Hellow JavaScript World      with JavaScript

console.log(`문자열합치기 2: ${'Hello'.concat(str2)}`); // Hellowith JavaScript
console.log(`문자열합치기 2: ${'Hello'.concat(str2, str)}`);
console.log(
    `문자열합치기 2: ${'Hello'.concat("I'm jjwan", 'nice to meet you')}`
);


