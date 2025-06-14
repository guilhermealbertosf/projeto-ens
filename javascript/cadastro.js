function cadastro(opcao){
    let txtnome = document.getElementById("inome")
    let txtemail = document.getElementById("iemail")
    let txtsenha = document.getElementById("isenha")

    if (opcao == "voltar"){
        window.location = '../index.html'
    }else if (txtnome.value.length == 0 || txtemail.value.length == 0 || txtsenha.value.length == 0 ){
        alert(`Preencha as informções`)
    }else{
        let nome = String(txtnome.value)
        let email = String(txtemail.value)
        let senha = Number(txtsenha.value)
        
        
        window.location = '../index.html'
    }
            
}
