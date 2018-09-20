function usernameLogin(username, password) {
    return function (dispatch) {
        fetch("/rest-auth/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                password
            })
        })
            .then(response => reponse.json())
            .then(json => {
                if (json.token) {
                    dispatch(saveToken(json.token))
                }
            })
            .catch(err => console.log(err));
    };
}
