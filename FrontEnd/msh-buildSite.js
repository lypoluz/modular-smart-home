function createSwitch(parentElement, name, state, group, target) {
    let switchContainer = document.createElement("div");
    switchContainer.class = "switchContainer";

    let nameElement = document.createElement("h3");
    nameElement.innerText = name;

    let labelElement = document.createElement("label");
    labelElement.class = "toggle";

    let inputElement = document.createElement("input");
    inputElement.class = "checkbox";
    inputElement.name = "checkbox";
    inputElement.type = "checkbox";
    inputElement.setAttribute("onchange", "writeTargetData(\""+ group + "\", \"" + target + "\", this.checked)");
    inputElement.checked = state;

    let sliderElement = document.createElement("span");
    sliderElement.class = "slider round";

    switchContainer.append(nameElement);
    labelElement.append(inputElement);
    labelElement.append(sliderElement);
    switchContainer.append(labelElement);
    parentElement.append(switchContainer);
}

function buildSite(site_json) {
    let parent_element = document.body;
    for (let group in site_json) {
        let newGroup = document.createElement("div");
        newGroup.class = "groupContainer";
        newGroup.id = group;
        for (let controllable of site_json[group]) {
            let newControllable = document.createElement("div");
            newControllable.classname = "controllableContainer";
            newControllable.id = controllable.type;
            if(controllable.type == "switch") {
                createSwitch(newControllable, controllable.name, controllable.state, group, controllable.id);
            }
            newGroup.append(newControllable);
        }
        parent_element.append(newGroup);
    }
}

function buildSiteFromServerResponse() {
    readAllDataFromGroup().then(response => {
        buildSite(JSON.parse(response));
    });
}
buildSiteFromServerResponse();

