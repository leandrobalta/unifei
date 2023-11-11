let pntsPlayer1 = document.getElementById("ptPlayer1");
let pntsPlayer2 = document.getElementById("ptPlayer2");
let ptVitoriaSelect = document.getElementById("ptVitoriaSelect");
let btnPlayer1 = document.getElementById("btnPlayer1");
let btnPlayer2 = document.getElementById("btnPlayer2");
let btnReset = document.getElementById("btnReset");
let winPnts = ptVitoriaSelect.value

let player1 = {
    pontuacao: 0,
    win: false,
    btn: btnPlayer1,
    spanPnts: pntsPlayer1
}

let player2 = {
    pontuacao: 0,
    win: false,
    btn: btnPlayer2,
    spanPnts: pntsPlayer2
}

const SomeoneWins = () => {
    console.log("points to win is: ", winPnts)

    if(player1.win || player2.win){
        console.log("someone wins")
        return true
    }

    console.log("nobody wins yet    ")
    return false    
}

const PlayerButtonsHandler = (player, enemy) => {
    if(SomeoneWins()) return;
    
    player.pontuacao++;
    
    player.spanPnts.innerText = `${player.pontuacao}`;
    
    if(player.pontuacao >= winPnts){
        player.win = true;
        player.spanPnts.style.color = '#008000';
        enemy.spanPnts.style.color = '#ff0000';
    }
}

player1.btn.addEventListener('click', (evt) => PlayerButtonsHandler(player1, player2))
player2.btn.addEventListener('click', (evt) => PlayerButtonsHandler(player2, player1))

ptVitoriaSelect.addEventListener('change', (evt) => {
    winPnts = evt.target.value;
})

