app

    .controller('HomeCtrl', ['$scope', '$routeParams', 'Question', 'Answer', 'UserProfile', 'Course', function($scope, $routeParams, Question, Answer, UserProfile, Course) {

        $scope.user_profile = UserProfile.get({userId: $scope.currentUser.id});

        Course.get({machine_readable_title: $routeParams.courseTitle}, function (course) {
            $scope.course = course.objects[0];
        });

        $scope.questions = Question.query();
        $scope.answers = Answer.query();
        $scope.courses = Course.query();
        /*
         Course.get({limit: 1, order_by: 'id'}, function (course) {
         // Success
         $scope.course = course.objects[0];
         }, function () {
         // Fail
         });*/

         $scope.lastquestions = Question.get({limit:3, order_by: '-published'});

    }])