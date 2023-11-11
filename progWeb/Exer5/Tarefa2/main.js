let formCompras = document.querySelector('#form-compras')
let listPedidos = document.querySelector('#lista-pedidos')
let qntd = document.querySelector('#qtd')
let nomeProduto = document.querySelector('#produto')
let defaultMsgListaProdutos = document.querySelector('.lista-pedidos p')

function RemoveItem(event){
    event.target.parentNode.remove()
    const items = document.querySelectorAll('ul li')

    if(items.length === 0){
        defaultMsgListaProdutos.innerText = 'Seu carrinho está vazio!'
    }
}

formCompras.addEventListener('submit', (event) => {
    event.preventDefault();
    
    if(qntd.value === '' || qntd.value <= 0 || nomeProduto.value.trim() === ''){
        alert('invalido!')
        return;
    }

    let li = document.createElement('li')
    li.innerText = `${qntd.value}: ${nomeProduto.value}`
    
    let button = document.createElement('button')
    button.innerText = 'X'
    button.addEventListener('click', RemoveItem)
    
    li.insertAdjacentElement('beforeend', button)

    listPedidos.append(li)

    defaultMsgListaProdutos.innerText = ''
});