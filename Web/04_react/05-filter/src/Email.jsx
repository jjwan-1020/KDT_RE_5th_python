import { useState } from "react";

function Email() {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");


const [users, setUsers] = useState([])
const addUser = () => {
    if (name === "" || email === "") return;
    setUsers([...users, { name, email }]);
    setName("");
    setEmail("");
};

return (
    <div>
        <input
        placeholder="이름"
        value={name}
        onChange={(e) => setName(e.target.value)}
        />

        <input
        placeholder="이메일"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        />
        <button onClick={addUser}>등록</button>
        <hr />
        {users.map((user, index) => (
            <div key={index}>
                {user.name} : {user.email}
            </div>
        ))}
    </div>
    );
}

export default Email