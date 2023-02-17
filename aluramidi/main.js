function TocaSom(seletorAudio){
    const elemento =document.querySelector(seletorAudio);

    
    if(elemento && elemento.localName === 'audio'){
        elemento.play();
    }
    else{
        console.log("não encontado");
    }
}

const ListaDeTeclas = document.querySelectorAll('.tecla');


//enquanto
for(let contador = 0; contador < ListaDeTeclas.length; contador++){
    const tecla = ListaDeTeclas[contador];
    const instrumento =tecla.classList[1];
    const idAudio = `#som_${instrumento}`;

    tecla.onclick = function(){
        TocaSom(idAudio);
    }
    tecla.onkeydown= function(evento){
        console.log(evento);
        if(evento.code ==='Space' || evento.code ==='Enter'){
        tecla.classList.add('ativa');
        }
    }
    tecla.onkeyup= function(){
        tecla.classList.remove('ativa');
    }
    
}


