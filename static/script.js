function rollDice() {
    fetch("https://tai-xiu-backend.onrender.com/roll")
        .then(res => res.json())
        .then(data => {
            document.getElementById("dice").innerText = data.dice;
            const result = document.getElementById("result");
            result.innerText = data.result;
            result.style.color = data.color;
        });
}

