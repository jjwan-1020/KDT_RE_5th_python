import { useState } from 'react';
import Fruit from './Fruit';
import Input from './Input';
import Result from './Result';

function ExAll() {
    const [data, setData] = useState({
        fruit: "apple",
        background: "white",
        content: "",
    });
    return (
        <>
        <div style={{ display: "flex", justifyContent: "center", marginTop: "10px" }}>
            <Fruit setData={setData}/>
        </div>
        <div style={{ display: "flex", justifyContent: "center", marginTop: "10px" }}>
            <Input setData={setData}/>
        </div>
        <div style={{ display: "flex", justifyContent: "center", marginTop: "10px" }}>
            <Result data={data} />
        </div>
        </>
    );
}

export default ExAll;