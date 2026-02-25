function Fruit({ setData }) {
    return (
        <>
        과일
        <select
        onChange={(e) =>
            setData((prev) => ({...prev, fruit: e.target.value}))
        }
        >
            <option value="apple">사과</option>
            <option value="peach">복숭아</option>
            <option value="grape">포도</option>
        </select>
        배경색
        <select
        onChange={(e) => 
            setData((prev) => ({...prev, background: e.target.value}))
        }
        >
            <option value="skyblue">하늘색</option>
            <option value="black">검은색</option>
            <option value="red">빨간색</option>
        </select>   
        글자색
        <select
        onChange={(e) =>
            setData((prev) => ({...prev, color: e.target.value }))
        }
        >
            <option value="black">검정</option>
            <option value="red">빨강색</option>
            <option value="blue">파란색</option>
        </select>
        </>
    )
}
export default Fruit;