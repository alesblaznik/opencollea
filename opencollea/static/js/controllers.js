function OpenColleaCtrl($scope, Course) {
    $scope.courses = Course.query();
}