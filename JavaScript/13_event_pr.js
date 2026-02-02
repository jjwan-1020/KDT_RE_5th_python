const button = document.querySelector("button");
const h2 = document.querySelector("h2");
button.addEventListener("click", () => {
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    const randomColor = `rgb(${r}, ${g}, ${b})`;
    document.body.style.backgroundColor = randomColor;
    h2.style.color = randomColor;
})

/*
const button = document.querySelector('button');
const h2 = document.querySelector('h2');

button.addEventListener
let r = Math.floor(Math.random() * 256);
let g = Math.floor(Math,random() * 256);
let b = Math.floor(Math.random() * 256);

const newColor = `rgb(${r}, ${g}, ${b})`;

*/