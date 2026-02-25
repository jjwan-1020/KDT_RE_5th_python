function changeColor(color, delay) {
    return new Promise((resolve) => {
        setTimeout(() => {
            document.body.style.backgroundColor = color;
            resolve();
        }, delay);
    });
}
changeColor("red", 1000)
    .then(() => changeColor("orange", 1000))
    .then(() => changeColor("yellow", 1000))
    .then(() => changeColor("green", 1000))
    .then(() => changeColor("blue", 1000));
