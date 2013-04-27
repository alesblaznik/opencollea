
angular.module('opencollea', ['openColleaServices','http-auth-interceptor']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {templateUrl: '/templates/base.html',   controller: OpenColleaCtrl})
            .when('/courses', {templateUrl: '/templates/courses.html',   controller: OpenColleaCtrl})
            .otherwise({redirectTo: '/'});
    }]);
