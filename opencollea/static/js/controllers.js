
angular.module('opencollea').controller({

  AuthController: function($scope, $http, authService) {
    $scope.login = function() {
      data = {
          'username': $scope.username,
          'password': $scope.password,
          'redirectTo': $scope.redirectTo
      }

      $http.post('/api/v1/auth/login', data).success(function(response) {
        if (true == response.success) {
          authService.loginConfirmed();
          window.location.href = response.redirectTo;
        } else {
          $scope.showLoginMessage = true;
        }
      });
    },

    $scope.logout = function() {
        $http.get('/api/v1/auth/logout').success(function() {
            window.location.href = '/login/'
        });
    }
  }

});
