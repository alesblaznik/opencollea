angular.module('openColleaServices', ['ngResource'])
    .factory('Course', function ($resource) {
        return $resource('/api/v1/course', {}, {
            query: {method: 'GET', isArray: false}
        });
    });