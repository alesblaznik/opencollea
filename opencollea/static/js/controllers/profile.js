app

/**
 * UserProfile form
 *
 * Route: /profile/[username]/edit
 */
.controller('UserProfileEditCtrl', ['$scope', '$rootScope', '$window', 'UserProfile', 'Gender', 'Language', 'AgeRange', 'Occupation', 'AreaOfStudy',
    function($scope, $rootScope, $window, UserProfile, Gender, Language, AgeRange, Occupation, AreaOfStudy) {
    $scope.errors = { user_profile: null };

    // Load UserProfile
    $scope.user_profile = UserProfile.get({userId: $scope.currentUser.id});

    // Select options
    $scope.gender_options = Gender.query();
    $scope.language_options = Language.query();
    $scope.age_range_options = AgeRange.query();
    $scope.occupation_options = Occupation.query();
    $scope.area_of_study_options = AreaOfStudy.query();

    $scope.saveProfile = function() {
        $scope.loading = true;
        $scope.user_profile.$update({userId: $scope.currentUser.id},
            // Success
            function() {
                $scope.loading = false;

                $rootScope.notifications = [{
                  class: 'alert-success',
                  content: 'Your profile was successfuly saved.'
                }];
                $window.scrollTo(0,0);

                // Redirect back
                if ($scope.redirectBack) {
                    $window.history.back()
                }
            },
            // Failed
            function(response) {
                $scope.loading = false;
                $scope.errors.user_profile = response.data.user_profile;

                $rootScope.notifications = [{
                  class: 'alert-error',
                  content: "We're sorry, but please check again those pretty red labels."
                }];
                $window.scrollTo(0,0);
            }
        );
    }
}])

.controller('UserClassProfileCtrl', ['$scope', '$http', '$rootScope', '$routeParams', 'UserProfile',
   function($scope, $http, $rootScope, $routeParams, UserProfile) {
       UserProfile.getByUsername({username: $routeParams.username}, function(users) {
           if (users.objects.length != 1) {
               // User doesn't exists!
               $rootScope.notifications = [{
                  'class': 'alert-error',
                  'content': 'User <b>' + $routeParams.username + '</b>' + ' doesn\'t exists!'
               }];

               return;
           }

           // Now we have our user
           $scope.user_profile = users.objects[0];

           // Load language
           $http.get($scope.user_profile.language_code).success(function(data) {
               $scope.user_profile.language_code = data;
           });
       });
}])

;
