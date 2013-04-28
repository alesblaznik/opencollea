
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

function OpenColleaCtrl($scope, Course) {
    $scope.courses = Course.query();
}

function CourseCtrl($scope, $http) {
    $scope.newCourse = function() {
        data = {
          'title': $scope.title,
          'machine_readable_title': $scope.machine_readable_title,
          'description': $scope.description,
          'website': $scope.website
        }
        var formEl = $('#newCourseForm');
        var msgDiv = $(formEl).find('.msgDiv:eq(0)');

        // reset:
        $(formEl).find('input[type="text"]').each(function(i,e){
            $(e).removeClass('requiredFieldError');
        });
        $(msgDiv).hide().removeClass('alert alert-error alert-success').text('');

        $http.post('/api/v1/course/new', data).success(function(response) {
            if (true == response.success) {
                $(msgDiv).addClass('alert-success').text('Course inserted');
                $(formEl).find('input[type="text"]').each(function(i,e){
                    $(e).val('');
                });
            } else if (response.required) {
                for (var i = 0; i < response.required.length; i++){
                    $('input[ng-model="' + response.required[i] + '"]').addClass('requiredFieldError');
                }
                $(msgDiv).addClass('alert').text('Please, fill in required fields');
            } else {
                $(msgDiv).addClass('alert-error').text('Error creating new course');
                console.warn(response);
            }
            $(msgDiv).show();
        });
    }
}