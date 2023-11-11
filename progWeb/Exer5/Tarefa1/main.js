let h1 = document.querySelector('h1')
let button = document.querySelector('button')
let section = document.querySelector('section')

button.addEventListener('click', (event) => {
    event.preventDefault();
    console.log('Clicou')

    let rgb = [255, 255, 255];

    for (let index = 0; index < rgb.length; index++) {
        rgb[index] = Math.floor(Math.random() * 256);
    }

    console.log("rgb: ", rgb)

    let color = `rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;

    section.style.backgroundColor = color;

    h1.innerHTML = `Cor de Fundo: ${color}`;
})