function Input({ setData }) {
    return (
        <>
        내용
        <input
        type="text"
        placeholder="내용을 입력하세요"
        onChange={(e) =>
            setData((prev) => ({...prev, content: e.target.value}))
        }
        />
        </>
    );
}

export default Input;