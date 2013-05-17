angular.module('opencolleaServices', ['ngResource'])
    .factory('Auth', function ($resource) {
        return $resource('/api/v1/auth/currentUser', {}, {
            'getCurrentUser': {method: 'GET'}
        });
    })
    .factory('Course', function ($resource) {
        return $resource('/api/v1/course', {}, {
            query: {method: 'GET', isArray: false}
        });
    })
    .factory('Question', function ($resource) {
        return $resource('/api/v1/question', {}, {
            query: {method: 'GET'}
        })
    });
