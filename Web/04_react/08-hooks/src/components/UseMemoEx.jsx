// useMemo
import { useMemo, useState } from "react";
// - 메모이제이션으로 수행한 연산의 결과 값을 기억함으로서 불필요한 연산 최소화

function UseMemoEX() {
    const [count, setCount] = useState(0);
    const [input, setInput] = useState('');

    // 임의의 큰 연산을 하는 함수
    // const calc = () => {
    //     console.log('계산중..')
        
        
    //     for (let i = 0; i < 10000000; i++) {}

    //     return count ** 2;
    // }
    //  [after]
    // count의 값이 바뀔 때만 함수를 실행
    // input 상태가 바뀌면 컴포넌트는 리렌더링 되지만, calc연산되지 않도록
    const calcnum = useMemo(() => {
        console.log("계산중...");
    for (let i = 0; i < 100000000; i++) {}
        return count ** 2;
    }, [count]);
    return (
        <div>
            <h1>useMemo Ex</h1>
            <input type="text" value={input} onChange={(e) => setInput(e.target.value)} />
            <button onClick={() => setCount(() => count + 1)}>Plus</button>
            <p>count: {count}</p>
        
            {/*<p>calc: {calc()}</p>*/}
            <p>calc: {calcnum}</p>
        </div>
    );
}

export default UseMemoEX;