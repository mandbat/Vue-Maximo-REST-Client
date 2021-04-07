function checkCred() {
    return {
        checkLogin: function(value) {
            return value;
        }
    }
}
let a = checkCred();
console.log(a.checkLogin("AAA"));