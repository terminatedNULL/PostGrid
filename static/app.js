function togglePassword() {
    const passField = document.getElementsByName("dbPass")[0];
    const checkbox = document.getElementsByName("passReq")[0];

    if(passField.disabled) {
        document.getElementsByName("dbPass")[0].disabled = false;
        document.getElementsByName("dbPass")[0].enabled = true;
        checkbox.value = "1";
        return;
    }

    document.getElementsByName("dbPass")[0].disabled = true;
    document.getElementsByName("dbPass")[0].enabled = false;
    checkbox.value = "0";
}

function hidePassword() {
    const passField = document.getElementsByName("dbPass")[0];
    const passBtn = document.getElementsByName("passVisibility")[0];

    if(passField.type === "password") {
        document.getElementsByName("dbPass")[0].type = "text";
        passBtn.value = "Hide";
        return;
    }

    document.getElementsByName("dbPass")[0].type = "password";
    passBtn.value = "Show";
}