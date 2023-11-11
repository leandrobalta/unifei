let list = [];

function listItems(list) {
    if(list.length == 0){
        return '---------------------------------\nLista vazia\n---------------------------------';
    }
    let listString = '---------------------------------';
    for(let i = 0; i < list.length; i++){
        listString  += `\n[${i}] - ${list[i]}`;
    }
    listString += '\n---------------------------------';
    
    return listString;
}

let run = true;

while(run){
    let option = window.prompt('O que deseja fazer?\nDigite “novo” para adicionar um item\nDigite “deletar” para remover um item\nDigite “listar”\nDigite “q” para sair');
    
    switch(option){
        case 'novo':
            let itemToAdd = window.prompt('Digite o item que deseja adicionar');
            list.push(itemToAdd);
            break;
        case 'deletar':
            if(list.length == 0){
                alert('Não há itens para remover');
                break;
            }
            listItemsString = listItems(list);
            let indexToDelete = window.prompt('Digite o índice do item que deseja remover\n' + listItemsString);
            list.splice(indexToDelete, 1);
            break;
        case 'listar':
            alert(listItems(list))
            break;
        case 'q':
            console.log('Você saiu do programa. Bye bye!');
            run = false;
            break;
        default:
            alert('Opção inválida');
            break;
    }
}