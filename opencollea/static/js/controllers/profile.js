app.controller('UserProfileEditCtrl', ['$scope', 'UserProfile', 'Gender', 'Language', 'AgeRange', 'Occupation', 'AreaOfStudy',
    function($scope, UserProfile, Gender, Language, AgeRange, Occupation, AreaOfStudy) {
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
            $scope.user_profile.$update({userId: $scope.currentUser.id}, function() {
                $scope.loading = false;
            });
        }
}]);
