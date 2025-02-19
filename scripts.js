async function loadScripts() {
    try {
        let response = await fetch("scripts.json");  // Load the generated script list
        let scripts = await response.json();

        let sidebar = document.querySelector(".sidebar");

        Object.keys(scripts).forEach(category => {
            // Create group title
            let groupTitle = document.createElement("div");
            groupTitle.className = "group-title";
            groupTitle.textContent = category.toUpperCase();
            groupTitle.onclick = () => toggleGroup(category);
            sidebar.appendChild(groupTitle);

            // Create list container
            let ul = document.createElement("ul");
            ul.id = category;
            ul.className = "script-list";
            ul.style.display = "none";  // Default hidden

            scripts[category].forEach(script => {
                let li = document.createElement("li");
                li.className = "script-option";
                li.dataset.script = script;
                li.textContent = script.split("/").pop();  // Show only filename
                li.onclick = () => selectScript(li);
                ul.appendChild(li);
            });

            sidebar.appendChild(ul);
        });
    } catch (error) {
        console.error("Error loading scripts:", error);
    }
}

function selectScript(element) {
    document.querySelectorAll(".script-option").forEach(el => el.classList.remove("active"));
    element.classList.add("active");
    selectedScript = element.dataset.script;
}

function toggleGroup(groupId) {
    let group = document.getElementById(groupId);
    if (group.style.display === "none" || group.style.display === "") {
        group.style.display = "block";  // Show scripts in this group
    } else {
        group.style.display = "none";  // Hide them
    }
}

// Call function on page load
loadScripts();
