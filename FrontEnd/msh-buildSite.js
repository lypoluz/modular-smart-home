

function firstLetterCapitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function makeGroupReadable(group) {
    group = group.replace("_", " ")
    group = firstLetterCapitalize(group)
    return group;
}

function buildSite(site_json) {
    let parent_element = document.body;
    for (let group in site_json) {
        let newGroup = document.createElement("div");
        newGroup.classList.add("groupContainer");
        newGroup.id = group;

        let groupHeader = document.createElement("h4");
        groupHeader.classList.add("groupHeader");
        groupHeader.innerText = makeGroupReadable(group);
        newGroup.append(groupHeader)

        let controllables = document.createElement("div");
        for (let controllable of site_json[group]) {
            controllables.append(window["create"+firstLetterCapitalize(controllable.type)](
                controllables,
                controllable.name,
                controllable.state,
                group,
                controllable.id));
        }
        newGroup.append(controllables);
        parent_element.append(newGroup);
    }
}

function buildSiteFromServerResponse() {
    readAllDataFromGroup().then(response => {
        buildSite(JSON.parse(response));
    });
}
buildSiteFromServerResponse();

