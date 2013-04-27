angular.module('opencollea', ['openColleaServices']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {templateUrl: '/templates/base.html',   controller: OpenColleaCtrl})
            .when('/courses', {templateUrl: '/templates/courses.html',   controller: OpenColleaCtrl})
            .otherwise({redirectTo: '/'});
    }]);
