
var app = angular.module('opencollea', ['openColleaServices','http-auth-interceptor']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {controller: OpenColleaCtrl})
            .when('/courses', {templateUrl: '/templates/courses.html', controller: OpenColleaCtrl})
            .when('/profile/:username', {templateUrl: '/static/partials/profile/user-profile-class.html' })
            .when('/profile/:username/edit', {templateUrl: '/static/partials/profile/user-profile-form.html'})
            .when('/auth/:username/edit', {templateUrl: '/static/partials/profile/user-registration-edit-form.html'})
            .otherwise({redirectTo: '/'});
    }]);

/**
 * Inicializacija
 */
app.run(function($rootScope, Auth) {
    $rootScope.user = Auth.getCurrentUser();
});
