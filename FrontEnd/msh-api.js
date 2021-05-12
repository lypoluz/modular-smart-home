function writeTargetData(group, target, data) {
    doConnection("mode=write&group="+group+"&target="+target+"&data="+data).then();
}

function readDataFromGroup(group) {
    return doConnection("mode=read&group="+group, true);
}

function readAllDataFromGroup() {
    return doConnection("mode=read&group=all", true);
}



function doConnection(GET_string, receive_response=false) {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "CommandHandler.php?" + GET_string, true);
        if (receive_response) {
            xhr.onload = () => {
                console.log(xhr.status);
                if(xhr.status >= 400)
                    reject(xhr.response)
                else
                    resolve(xhr.response);
            }
        }
        xhr.send();
        if(!receive_response)
            resolve(true);
    });
}