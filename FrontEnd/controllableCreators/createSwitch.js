function createSwitch(name, state, group, target) {
    let switchContainer = document.createElement("div");
    switchContainer.classList.add("switchContainer");
    switchContainer.id = target;

    let nameElement = document.createElement("h3");
    nameElement.innerText = name;

    let labelElement = document.createElement("label");
    labelElement.classList.add("toggle");

    let inputElement = document.createElement("input");
    inputElement.classList.add("checkbox");
    inputElement.name = "checkbox";
    inputElement.type = "checkbox";
    inputElement.setAttribute("onchange", "writeTargetData(\""+ group + "\", \"" + target + "\", this.checked)");
    inputElement.checked = state;

    let sliderElement = document.createElement("span");
    sliderElement.classList.add("slider");
    sliderElement.classList.add("round");

    switchContainer.append(nameElement);
    labelElement.append(inputElement);
    labelElement.append(sliderElement);
    switchContainer.append(labelElement);
    return switchContainer;
}