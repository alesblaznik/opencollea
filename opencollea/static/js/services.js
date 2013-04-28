angular.module('openColleaServices', ['ngResource'])
    .factory('User', function ($resource) {
        return $resource('/api/v1/user/:userId', {}, {
           'get': {method: 'GET'}
        });
    })
    .factory('Course', function ($resource) {
        return $resource('/api/v1/course', {}, {
            query: {method: 'GET', isArray: false}
        });
    });


