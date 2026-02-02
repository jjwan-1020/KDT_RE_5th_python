function cal() {
    const value1 = Number(document.querySelector("#value1").value);
    const value2 = Number(document.querySelector("#value2").value);
    const operator = document.querySelector("#operator").value;
    const resultInput = document.querySelector("#result");

    let result;
    if (operator === "+") {
        result = value1 + value2;
    } else if (operator === "-") {
        result = value1 - value2;
    } else if (operator === "*") {
        result = value1 * value2;
    } else if (operator === "/") {
        result = value1 / value2;
    } else {
        result = "연산자 오류 다시 입력해주세요";
    }
    resultInput.value = result;
}
function resetInput() {
    document.querySelector("#value1").value = "";
    document.querySelector("#value2").value = "";
    document.querySelector("#operator").value = "";
    document.querySelector("#result").value = "";
}