let user = {
    name: 'jjwan',
    age: 27,
    city: 'pohang'
};
console.log('user 객체 원본:', user);

// for in
for (let key in user) {
    console.log('key:', key, '| value:', user[key]);
}

// 객체
// 문자열, 숫자, 배열은 내장 메서드가 존재 (ex: concat, filter, sort, ...)
// 하지만 객체는 내장 메서드가 없다
// 객체는 키/값을 쌍으로 가지고 있다는 구조만 명확하고, 해당 값들의 타입이나 의미, 용도가 전부 제각각이다
// 그래서 객체는 아예 object라는 전역 내장 객체를 제공

// key 추출 (배열로 반환)
console.log('key 추출:', Object.keys(user));
// JS에서 기본적으로 제공하는 Object객체의 keys라는 메서드를 사용해서 매개변수로 잔달한 user 객체의 key들을 배열로 변환

// 값 추출
console.log('값 추출:', Object.values(user));

// [키, 값] 추출 (배열로 반환)
console.log('키, 값 추출:', Object.entries(user));

let entries = [
    ['name', 'jjwan'],
    ['age', 27],
    ['city', 'pohang']
];

// 배열을 객체로 변환
console.log('배열을 객체로 변환:', Object.fromEntries(entries));