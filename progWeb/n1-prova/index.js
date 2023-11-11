const addButton = document.querySelector(".calculator")
const subButton = document.querySelector('#subBtn')
const multButton = document.getElementById("multBtn")
const divButton = document.getElementById("divBtn")
const equalButton = document.getElementById("equalBtn")
const dotButton = document.getElementById("dotBtn")

const operations = document.getElementsByClassName('operation')
const numbers = document.getElementsByClassName('numberBtn')

let input = []

for(let op of operations){
    op.addEventListener('onClick', () => {
        if(input.length <= 0){
            console.log("nothing to do")
            return
        }

        let someOperationAlreadyExists = false
        for(let operation of operations){
            if(input.includes(operation)){
                someOperationAlreadyExists = true
            }
        }   

        if(someOperationAlreadyExists){
            return
        }

        input.push(op.innerHTML)
    })
}

for(let number of numbers){
    number.addEventListener('onClick', () => {
        input.push(number.innerHTML)
    }) 
}

equalButton.addEventListener('onClick', () => {
    alert("sorry, functon not implemented :(")
})


