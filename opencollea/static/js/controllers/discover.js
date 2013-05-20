

app

.controller('DiscoverCtrl', ['$scope', '$window', 'CoursesUserNotEnrolled', 'MoocCoursesNooneTook',
    function ($scope, $window, CoursesUserNotEnrolled, MoocCoursesNooneTook) {
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

    $scope.$watch('showOption', function (newValue, oldValue) {
        $scope.loadList();
    });

}])


;


