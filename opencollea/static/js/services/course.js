
app


.factory('EtherpadNote', ['$resource', function ($resource) {
    return $resource('/api/v1/etherpad_note/:id',
        {}, {
            'update': {method:'PUT'},
            'getByPadId': {method:'GET', params:{pad_id:':padId'}}
        });
}])


.factory('Course', ['$resource', function ($resource) {
        /*         return $resource('/api/v1/course', {}, { */
   return $resource('/api/v1/course/:id',
       {}, {
           query: {method: 'GET', isArray: false},
           'update': {method:'PUT'},
           'getByCourseTitle': {method:'GET', params:{machine_readable_title:':title'}}
       });
}])

;