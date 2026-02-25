import './App2.css';

function App() {
    const title = "Hello World";


    return (
        <div className="container">
            <div className="title">{title}</div>

            <div className="fonm-row">
                <label>아이디 :</label>
                <input type="text" />
            </div>
            <div className="form-row">
                <label>비밀번호 :</label>
                <input type="password" />
            </div>
        </div>
    );
}

export default App;