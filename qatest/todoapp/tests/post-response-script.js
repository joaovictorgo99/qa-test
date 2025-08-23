// Automate requests for testing

// Get Task request
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// Get Tasks request
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// Create Task request
pm.test("Status code is 201", function () {
    pm.response.to.have.status(201);
});

let resJson = pm.response.json()

if (pm.response.code == 201) {
    pm.environment.set("taskId", resJson.id);
}

// Update Task request
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// Delete Task request
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Task deleted successfully", function () {
    let resJson = pm.response.json()

    pm.expect(resJson.message).to.eql("Task removed successfully")
})
