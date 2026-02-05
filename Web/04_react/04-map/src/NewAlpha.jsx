import { useState } from "react";

function NewAlpha() {
  const [text, setText] = useState("");
  const [list, setList] = useState(["a", "b", "c", "d", "e"]);

  const addAlpha = () => {
    if (text.trim() === "") return;
    setList(prev => [...prev, text]);
    setText("");
  };

  const handleSubmit = (e) => {
    e.preventDefault(); 
    addAlpha();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={text}
        onChange={e => setText(e.target.value)}
        placeholder="알파벳 입력"
      />
      <button type="submit">추가</button>

      <ol>
        {list.map((value, idx) => (
          <li key={idx}>{value}</li>
        ))}
      </ol>
    </form>
  );
}

export default NewAlpha;
