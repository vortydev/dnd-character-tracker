function loadClassesFromAPI(root) {
    fetch(root+"/api/classes/get")
        .then(response => {
            if (!response.ok) throw new Error("Network response was not ok");
            return response.json();
        })
        .then(data => {
            let classList = data.class_list;
            let classLevels = data.level_list;
            console.log("Classes",classList);
            console.log("Class levels",classLevels);
            
        })
        .catch(error => {
            console.error("Error loading classes:", error);
            alert("Failed to load classes.");
        });
}