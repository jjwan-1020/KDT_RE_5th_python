import LifeCycle from './LifeCycle';
import { useState } from 'react'

function UseEffect() {
    const [number, setNumber] = useState(0);
    const [visible, setVisible] = useState(true);
    
    
    const changeNumber = () => {
        setNumber(number + 1);
    };

    const changeVisible = () => {
        setVisible(!visible)
    }
    return (
        <div>
            <button onClick={changeNumber}>Plus</button>
            <button onClick={changeVisible}>ON/OFF</button>

            {visible &&<LifeCycle number= {number} />}
        </div>
    )
}
export default UseEffect;