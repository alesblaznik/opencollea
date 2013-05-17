app

.factory('UserProfile', ['$resource', function($resource) {
    return $resource('/api/v1/user_profile/:userId',
        {}, {
            'update': {method:'PUT'},
            'getByUsername': {method:'GET', params:{username:':username'}}
        });
}])

.factory('RegistrationDetails', ['$resource', function($resource) {
    return $resource('/api/v1/registration_details/:userId',
        {}, {
           'update': {method:'PUT'}
        });
}])

;
