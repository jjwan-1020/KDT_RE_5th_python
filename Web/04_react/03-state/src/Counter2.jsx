import { useState } from "react";
function Counter2() {
    const [ num, setNum ] = useState(0);
    const increase = () => {
        setNum(num + 1);
    };
    const decrease = () => {
        setNum(num - 2);
    };

    return (
        <div>
            <h1>{num}</h1>
            <button onClick={increase}>증가</button>
            <button onClick={decrease}>감소</button>
        </div>
    );
}

export default Counter2;
