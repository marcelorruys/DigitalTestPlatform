const screen = document.getElementById('screen');
let saidas = 0

document.addEventListener('mouseleave', () => {
  screen.style.backgroundColor = 'red'; // Altera a cor para vermelho quando o cursor sai da tela
  saidas++
  console.log(saidas)

  if(saidas < 2) {
    alert("VocÊ não pode tirar o cursor da tela da prova")
    screen.style.backgroundColor = 'green';
} else if (saidas < 3) {
    alert("último aviso, não retire o cursor da tela")
    screen.style.backgroundColor = 'green';
} else if (saidas < 4) {
    alert("Sua prova foi bloqueada")
    document.getElementById("prova").innerHTML="Prova Bloqueada"
    window.location.href = ""
}
});

