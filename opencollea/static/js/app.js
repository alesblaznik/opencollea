
var app = angular.module('opencollea', ['opencolleaServices','http-auth-interceptor']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {controller: OpenColleaCtrl})
            .when('/courses', {templateUrl: '/templates/courses.html', controller: OpenColleaCtrl})
            .when('/profile/:username', {templateUrl: '/static/partials/profile/user-profile-class.html' })
            .when('/profile/:username/edit', {templateUrl: '/static/partials/profile/user-profile-form.html', controller: 'UserProfileEditCtrl'})
            .when('/auth/:username/edit', {templateUrl: '/static/partials/profile/user-registration-edit-form.html'})
            .otherwise({redirectTo: '/'});
    }]);

/**
 * Inicializacija
 */
app.run(function($rootScope, Auth) {
    $rootScope.currentUser = Auth.getCurrentUser();
});
