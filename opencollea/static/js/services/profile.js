app.factory('UserProfile', ['$resource', function($resource) {
    return $resource('/api/v1/user_profile/:userId?username=:username',
        {},
        {'update':   {method:'PUT'}});
}]);
