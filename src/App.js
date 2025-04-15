import { useState, useEffect } from 'react';
    function App() {
        const [counter, setCounter] = useState(0);
        const [clickCounter, setClickCounter] = useState(0)
        useEffect(() => {
        const interval = setInterval(() => {
            setCounter((prevCounter) => prevCounter + 1);
        }, 1000);
        
        return () => clearInterval(interval);
        }, []);

        const btnClick = () => {
            setCounter(0);
            setClickCounter(clickCounter + 1);
        }
        
        return (
            <div className="App">
                <h1>FrothServer</h1>
                <h2>Time Online {counter}</h2>
                <h2>Number of clicks {clickCounter}</h2>
                <button onClick={btnClick} >reset timer</button>
            </div>
        )
    }

export default App;