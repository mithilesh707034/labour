/* Function to Generat Captcha */
function GenerateCaptcha() {
    var chr1 = Math.ceil(Math.random() * 10) + '';
    var chr2 = Math.ceil(Math.random() * 10) + '';
    var chr3 = Math.ceil(Math.random() * 10) + '';

    var str = new Array(4).join().replace(/(.|$)/g, function () { return ((Math.random() * 36) | 0).toString(36)[Math.random() < .5 ? "toString" : "toUpperCase"](); });
    var captchaCode = str + chr1 + ' ' + chr2 + ' ' + chr3;
    document.getElementById("newcaptcha1").value = captchaCode
}

/* Validating Captcha Function */
function ValidCaptcha() {
    var str1 = removeSpaces(document.getElementById('newcaptcha1').value);
    var str2 = removeSpaces(document.getElementById('captcha').value);

    if (str1 == str2)
        document.write("Successfully Login");
    else
        document.write("Failed Login");
}

/* Remove spaces from Captcha Code */
function removeSpaces(string) {
    return string.split(' ').join('');
}

// Registration Password Compare
function pswdcompare() {
    var ps1 = document.getElementById('pswd1').value;
    var ps2 = document.getElementById('pswd2').value;
    if (ps1 == ps2)
        document.write("You are registered successfully:")
    else
        document.write("Both Password are not match please Try Again")
}