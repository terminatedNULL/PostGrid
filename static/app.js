function togglePassword() {
    var passField = document.getElementById("dbPass")
    var checkbox = document.getElementById("passReq")

    if(passField.disabled) {
        document.getElementById("dbPass").disabled = false
        document.getElementById("dbPass").enabled = true
        checkbox.value = "1"
        return
    }

    document.getElementById("dbPass").disabled = true
    document.getElementById("dbPass").enabled = false
    checkbox.value = "0"
}