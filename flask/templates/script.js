function validateForm(){
    var TN = document.getElementById('tn').value;
    if (TN.trim()===""){
        alert('Please enter a team name!');
        return false;
    }
    return true;
}