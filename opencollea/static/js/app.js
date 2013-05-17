
var app = angular.module('opencollea', ['opencolleaServices','http-auth-interceptor']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {templateUrl: '/static/partials/home/home.html'})
            .when('/course-list', {templateUrl: '/static/partials/course/course-list.html', controller: CourseListCtrl})
            .when('/course/:courseTitle', {templateUrl: 'static/partials/course/course-detail.html', controller: CourseDetailCtrl})
            .when('/profile/:username', {templateUrl: '/static/partials/profile/user-profile-class.html' })
            .when('/profile/:username/edit', {templateUrl: '/static/partials/profile/user-profile-form.html', controller: 'UserProfileEditCtrl'})
            .when('/auth/edit', {templateUrl: '/static/partials/profile/user-registration-edit-form.html', controller: 'UserRegistrationDetailsEditCtrl'})
            .when('/new-course', {templateUrl: '/static/partials/course/new-course.html', controller: CourseCtrl})
            .otherwise({redirectTo: '/'});
    }]);

/**
 * Inicializacija
 */
app.run(function($rootScope, Auth) {
    $rootScope.currentUser = Auth.getCurrentUser();
});
