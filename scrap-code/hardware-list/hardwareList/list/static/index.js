function show(param){
    if(param==0){
        document.getElementById('text').style.display = 'block'
        document.getElementById('text2').style.display = 'none'
    }
    else if(param==1){
        document.getElementById('text2').style.display = 'block'
        document.getElementById('text').style.display = 'none'
    }
}