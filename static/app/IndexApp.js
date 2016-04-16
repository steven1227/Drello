var app = angular.module('IndexApp', ['ngMaterial', 'authentication']);

app.controller('LoginControl', ['AuthService', function(AuthService) {
    this.username = "rendong_liu@hotmail.com"
    this.password = 123;
    this.login = function() {
        AuthService.login(this.username, this.password)
            .then(function() {
            	console.log("success")
            })
            .catch(function(){
            	console.log("Error")
            })
    }
}]);
