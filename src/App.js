import "./assets/css/App.css";

import { useState, useEffect } from 'react';
    function App() {
        const [timeUp, setTimeUp] = useState(0);
        const [counter, setCounter] = useState(0);
        const [totalTime, setTotalTime] = useState(0);
        const [clickCounter, setClickCounter] = useState(0)
        const startTime = Date.now();
        useEffect(() => {
        const interval = setInterval(() => {
            setCounter((prevCounter) => prevCounter + 1);
            setTotalTime(Math.round((Date.now() - startTime)/1000))
        }, 1000);
        
        return () => clearInterval(interval);
        }, []);

        const btnClick = () => {
            setCounter(0);
            setClickCounter(clickCounter + 1);
            
        }
         const btnSpaceGame = (e) => {
            // window.location.href = "/pages/starfield";
            window.location.href = "/pages/starfield.html";
        }
          const btnTwoPlayerGame = (e) => {
            // window.location.href = "/pages/pvp";
            window.location.href = "/pages/pvp.html";
        }
        return (
            <div className="App">
                <h1>FrothServer </h1>
                <h1>Server webpage time since restart {totalTime}</h1>
                <h2>Session Time Since last reset {counter}</h2>
                <h2>Number of clicks of reset {clickCounter}</h2>
                <button onClick={btnClick} >reset timer</button>
                <button type="button" onClick={btnSpaceGame}> Go to My AI generated HTML Space Game  </button>
                <button type="button" onClick={btnTwoPlayerGame}> Go to My AI generated HTML Two Player Game  </button>
            </div>
        )
    }

export default App;