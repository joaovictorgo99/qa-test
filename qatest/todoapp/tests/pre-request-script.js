// Automate login
// Every request will perform the login first

const loginRequest = {
    url: pm.environment.get("baseUrl") + "/login",
    method: "POST",
    body: {
        mode: "raw",
        options: {
            raw: {
                language: "json"
            }
        },
        raw: JSON.stringify({
            username: "admin",
            password: "123"
        })
    }
}

pm.sendRequest(loginRequest, function(err, res) {
    let responseJson = res.json()
    let auth = responseJson["token"]

    pm.globals.set("token", auth)
})
