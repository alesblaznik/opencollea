angular.module('opencolleaServices', ['ngResource'])
    .factory('Auth', function ($resource) {
        return $resource('/api/v1/auth/currentUser', {}, {
            'getCurrentUser': {method: 'GET'}
        });
    })
    .factory('Question', function ($resource) {
        return $resource('/api/v1/question', {}, {
            query: {method: 'GET'}
        })
    });
