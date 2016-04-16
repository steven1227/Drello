angular.module('authentication', [])
    .factory('AuthService', ['$q', '$timeout', '$http', function($q, $timeout, $http) {

        var user = null;

        function register() {

        }


        function isLoggedIn() {
            if (user) {
                return true;
            } else {
                return false;
            }
        }

        function login(email, password) {

            var deferred = $q.defer();

            $http.post('/api/login', { email: email, password: password })
                // handle success
                .success(function(data, status) {
                    if (status === 200 && data.result) {
                        user = true;
                        deferred.resolve();
                    } else {
                        user = false;
                        deferred.reject();
                    }
                })
                // handle error
                .error(function(data) {
                    user = false;
                    deferred.reject();
                });

            // return promise object
            return deferred.promise;

        }


        function logout() {
            var deferred = $q.defer();

            $http.get('/api/logout')
                .success(function(data) {
                    user = false;
                    deferred.resolve();
                })
                .error(function(data) {
                    user = false;
                    deferred.reject();
                })
            return deferred.promise;
        }

        return ({
            isLoggedIn: isLoggedIn,
            login: login,
            logout: logout,
            test: 'register'
        });

    }]);
