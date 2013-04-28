
angular.module('opencollea', ['openColleaServices','http-auth-interceptor']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {templateUrl: '/templates/base.html',   controller: OpenColleaCtrl})
            .when('/courses', {templateUrl: '/templates/courses.html',   controller: OpenColleaCtrl})
            .when('/profile/:username', {templateUrl: '/static/partials/profile/user-profile-class.html'})
            .when('/new-course', {templateUrl: '/static/partials/course/new-course.html', controller: CourseCtrl})
            .otherwise({redirectTo: '/'});
    }]);
