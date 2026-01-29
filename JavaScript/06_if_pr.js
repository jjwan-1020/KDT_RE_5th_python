let age = Number(prompt('나이를 입력하세요'));
if (age >= 20) {
    console.log('성인입니다');
} else if (age >= 17) {
    console.log('고등학생입니다');
} else if (age >= 14) {
    console.log('중학생입니다');
} else if (age >= 8) {
    console.log('초등학생입니다');
} else if (age >= 0) {
    console.log('유아입니다');
} else {
    console.log('올바른 나이를 입력하세요');
}