
app

.factory('Gender', ['$resource', function($resource) {
    return $resource('/api/v1/gender',
        {},
        { query: {method: 'GET', isArray: false} });
}])

.factory('Language', ['$resource', function($resource) {
    return $resource('/api/v1/language',
        {},
        { query: {method: 'GET', isArray: false} });
}])

.factory('AgeRange', ['$resource', function($resource) {
    return $resource('/api/v1/age_range',
        {},
        { query: {method: 'GET', isArray: false} });
}])

.factory('Occupation', ['$resource', function($resource) {
    return $resource('/api/v1/occupation',
        {},
        { query: {method: 'GET', isArray: false} });
}])

.factory('AreaOfStudy', ['$resource', function($resource) {
    return $resource('/api/v1/area_of_study',
        {},
        { query: {method: 'GET', isArray: false} });
}])

;
