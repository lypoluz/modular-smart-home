function sendControlData(group, target, data) {
    const request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            console.log(this.responseText)
        }

    };
    console.log(data);
    request.open("GET","CommandHandler.php?group="+group+"&target="+target+"&data="+data,true);
    request.send();
}

function loadStatus() {
    alert("yes")
}

// loadStatus();