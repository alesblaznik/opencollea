
var app = angular.module('opencollea', ['openColleaServices','http-auth-interceptor']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {controller: CourseListCtrl})
            .when('/course-list', {templateUrl: '/static/partials/course/course-list.html', controller: CourseListCtrl})
            .when('/profile/:username', {templateUrl: '/static/partials/profile/user-profile-class.html' })
            .when('/profile/:username/edit', {templateUrl: '/static/partials/profile/user-profile-form.html'})
            .when('/auth/:username/edit', {templateUrl: '/static/partials/profile/user-registration-edit-form.html'})
            .when('/new-course', {templateUrl: '/static/partials/course/new-course.html', controller: CourseCtrl})
            .otherwise({redirectTo: '/'});
    }]);

/**
 * Inicializacija
 */
app.run(function($rootScope, Auth) {
    $rootScope.user = Auth.getCurrentUser();
});
