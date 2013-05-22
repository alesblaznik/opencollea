

app

.controller('DiscoverCtrl', ['$scope', '$rootScope', '$window', 'CoursesUserNotEnrolled', 'MoocCoursesNooneTook', 'UserProfile', 'Course',
    function ($scope, $rootScope, $window, CoursesUserNotEnrolled, MoocCoursesNooneTook, UserProfile, Course) {
    $scope.courses_list = [];

    $scope.showOptions = [
        {k: 'im-not-enrolled', v: 'I\'m not enrolled'},
        {k: 'no-one-enrolled', v: 'Be first from MOOC'}
        // ,{k: 'show-all', v: 'Show ALL'}
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
                    $scope.courses_list = data.objects;
                });
                break;
            case $scope.showOptions[2]:
                // Show all
                // @todo
                $window.location.href = '#/course-list';
                break;
        }
    }

    /**
     * Enroll current user to class
     *
     * @param course
     */
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


    /**
     * Create new class from MOOC
     *
     * @param moocClass
     */
    $scope.createClassFromMooc = function (mixedCourse) {
        var MoocCourse = new Course({
            title: mixedCourse.title,
            website: mixedCourse.url,
            mooc: '/api/v1/mooc_course/' + mixedCourse.id
        });
        MoocCourse.$save(function () {
            $rootScope.notifications = [{
                class: 'alert-success',
                content: 'Awesome! You\'ve just created and enrolled to <b>' + mixedCourse.title + '</b>.'
            }];

            // Now we can enroll our user in Class
            Course.get({mooc: mixedCourse.id}, function (newCourse) {
                $scope.enroll(newCourse.objects[0]);
                $rootScope.notifications = [{
                    class: 'alert-success',
                    content: 'You\'ve created and entrolled in <b>' +
                        newCourse.title + '</b>.'
                }];
            });
        });
    }

    $scope.$watch('showOption', function (newValue, oldValue) {
        $scope.loadList();
    });

}])


;


