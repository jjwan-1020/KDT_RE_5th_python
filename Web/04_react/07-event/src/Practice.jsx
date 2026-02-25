import { useState } from "react";

function Practice() {
    const [color, setColor] = useState("black");
    const [text, setText] = useState("검정색 글씨");

    const changeRed = () => {
        setColor("red");
        setText("빨간색 글씨");
    };

    const changeBlue = () => {
        setColor("blue");
        setText("파란색 글씨");
    };

    const changeBlack = () => {
        setColor("black");
        setText("검은색 글씨")
    };

    return (
        <div style={{ padding: "20px"}}>
            <h1 style={{ color }}>{text}</h1>

            <button onClick={changeRed}>빨간색</button>
            <button onClick={changeBlue} style={{marginLeft: "10px"}}>
                파란색
            </button>
            <button onClick={changeBlack} style={{marginRight: "10px"}}>
                검은색
            </button>
        </div>
    );
}

export default Practice;