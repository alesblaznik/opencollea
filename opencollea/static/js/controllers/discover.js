

app

.controller('DiscoverCtrl', ['$scope', '$rootScope', '$window', 'CoursesUserNotEnrolled', 'MoocCoursesNooneTook', 'UserProfile',
    function ($scope, $rootScope, $window, CoursesUserNotEnrolled, MoocCoursesNooneTook, UserProfile) {
    $scope.courses_list = [];

    $scope.showOptions = [
        {k: 'im-not-enrolled', v: 'I\'m not enrolled'},
        {k: 'no-one-enrolled', v: 'Be first from MOOC'},
        {k: 'show-all', v: 'Show ALL'}
    ];
    if ($scope.showOption === undefined) {
        $scope.showOption = $scope.showOptions[0];
    }

    $scope.loadList = function () {
        switch ($scope.showOption) {
            case $scope.showOptions[0]:
                // User can Enroll on this
                CoursesUserNotEnrolled.get({userId: $scope.currentUser.id}, function (data) {
                    $scope.courses_list = data.objects;
                });
                break;
            case $scope.showOptions[1]:
                // Be first from MOOC
                MoocCoursesNooneTook.get(function (data) {
                    $scope.courses_list = data.objects;;
                });
                break;
            case $scope.showOptions[2]:
                // Show all
                // @todo
                $window.location.href = '#/course-list';
                break;
        }
    }

    $scope.enroll = function (course) {
        // Enrolling user to new Class
        UserProfile.get({userId: $scope.currentUser.id}, function (user) {
            user.courses_enrolled.push(course.id);
            user.$update({userId: user.id}, function () {
                $scope.loadList();
                $rootScope.notifications = [{
                    class: 'alert-success',
                    content: 'You\'re enrolled to <b>' + course.title + '</b>.'
                }];
            });
        });
    }

    $scope.$watch('showOption', function (newValue, oldValue) {
        $scope.loadList();
    });

}])


;


