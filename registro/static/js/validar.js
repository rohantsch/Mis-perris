window.onload=iniciar;
function iniciar(){
    document.getElementById("enviar").addEventListener('click',validar,false);

}

function validarNombre(){
    var elemento = document.getElementById("nombre");
    if(!elemento.checkValidity()){
        error(elemento);
        return false;
    }
    return true;
}
function validarTelefono(){
    var elemento = document.getElementById("telefono");
    if(!elemento.checkValidity()){
        error(elemento);
        return false;
    }
    return true;

}

function validar(e){
    if(validarNombre() && validarTelefono())
    return true;
}

function error(elemento){
    document.getElementById("mensajeError").innerHTML = elemento.validationMessage;

}

