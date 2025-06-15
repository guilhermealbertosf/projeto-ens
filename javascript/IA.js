function ENS_IA(local){

    let pergunta = prompt("A ENS+IA está aqui para sanar as suas dúvidas! Fique à vontade para perguntar! :)")

    if (local == 'index'){
        window.location = "paginas/cadastro.html"
    }
    else{
        window.location = "../paginas/cadastro.html"
    }
    
    window.alert("Cadastre-se para usar a IA! ")
}