var container = document.getElementById('container');
window.onload = function(){
    container.textContent = add_new_chars(3);
}

function add_new_chars(x){
    var n = Math.floor(Math.random() * x) + 1;
    var str = '';
    for(let i = 0 ; i < n; i++){
        str += String.fromCharCode(97 + Math.floor(Math.random() * 26));
    }
    return str;
};

window.addEventListener("keyup", function(e){
    var firstone = container.textContent.substring(0, 1);
    if (e.key == firstone){
        container.textContent = container.textContent.substring(1, container.textContent.length);
    }else{
        container.textContent += e.key;
    }
    container.textContent += add_new_chars(3);
});