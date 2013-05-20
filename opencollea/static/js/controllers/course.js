
app

    .controller('CourseCtrl', ['$scope', '$routeParams', 'Course', function ($scope, $routeParams, Course) {
        $scope.subpage = $routeParams.subpage === undefined ? 'MAIN' : $routeParams.subpage;
        $scope.param = $routeParams.subpageParam === undefined ? '' : $routeParams.subpageParam;

        Course.get({machine_readable_title: $routeParams.courseTitle}, function (course) {
            // Success
            $scope.course = course.objects[0];
        }, function () {
            // Fail
        });
    }])

    .controller('CreateNewNoteCtrl', ['$scope', '$rootScope', '$window', 'EtherpadNote', function($scope, $rootScope, $window, EtherpadNote) {
        $scope.isModalOpen = false;
        $scope.modalOpts = {
            backdropFade: true,
            dialogFade: true
        };

        $scope.openModal = function () {
            $scope.isModalOpen = true;
        };

        $scope.closeModal = function () {
            $scope.isModalOpen = false;
        };

        $scope.createNewNote = function () {
            // Save note and redirect to created note!
            var Note = new EtherpadNote({
                course: $scope.course.resource_uri,
                title: $scope.title
            });
            Note.$save(function () {
                $rootScope.notifications = [{
                    class: 'alert-success',
                    content: 'Note added. You can start writing right away!'
                }];
                $scope.isModalOpen = false;
                $scope.isError = false;

                // Redirect user to this new note
                EtherpadNote.get({course: $scope.course.id, limit: 1, order_by: '-id'}, function (latestNote) {
                    latestNote = latestNote.objects[0];
                    $window.location.href = '#/course/' + $scope.course.machine_readable_title + '/notes/' + latestNote.machine_readable_title;
                });
            }, function () {
                $scope.isError = true;
            });
        };
    }])


    .controller('NotesListCtrl', ['$scope', 'EtherpadNote', function ($scope, EtherpadNote) {
        $scope.$watch('course', function (newValue, oldValue) {
            if (newValue !== undefined) {
                EtherpadNote.get({course: $scope.course.id}, function (notes) {
                    $scope.notes = notes.objects;
                });
            }
        });
    }])


    .controller('NoteCtrl', ['$scope', '$rootScope', '$window', 'EtherpadNote', function ($scope, $rootScope, $window, EtherpadNote) {

        $scope.$watch('course', function (newValue, oldValue) {
            if (newValue !== undefined) {
                EtherpadNote.get({course:$scope.course.id, machine_readable_title: $scope.param}, function (note) {
                    $scope.note = note.objects[0];
                    $('#etherpad').pad({padId: $scope.note.pad_id, height: 450,
                        showControls: true, showChat: true, userName: $scope.currentUser.username});
                }, function () {
                    // Fails
                });
            }
        });

        $scope.confirmNoteDeletion = function () {
            $('#deleteNoteAlert').show();
        }

        $scope.deleteThisNote = function () {
            EtherpadNote.delete({id: $scope.note.id}, function () {
                $rootScope.notifications = [{
                    class: 'alert-success',
                    content: 'Sucky note successfully deleted.'
                }];
                $window.location.href = '#/course/' + $scope.course.machine_readable_title + '/notes'
            });
        }
    }])
/*
    .controller('AddNewAnswerCtrl', ['$scope', '$rootScope', '$window', 'Answer', function($scope, $rootScope, $window, Answer) {

        $scope.addNewAnswer = function () {
            // Save note and redirect to created note!
            var Answer = new Answer({
                course: $scope.course.resource_uri,
                title: $scope.title
            });
            Answer.$save(function () {
                $rootScope.notifications = [{
                    class: 'alert-success',
                    content: 'Answer added.'
                }];
                $scope.isError = false;

                // Redirect user to this new note
                /* EtherpadNote.get({course: $scope.course.id, limit: 1, order_by: '-id'}, function (latestNote) {
                 latestNote = latestNote.objects[0];
                 $window.location.href = '#/course/' + $scope.course.machine_readable_title + '/notes/' + latestNote.machine_readable_title;
                 });
            }, function () {
                $scope.isError = true;
            });
        };
    }])*/

    .controller('CourseDetailCtrl', ['$scope', '$routeParams', 'Question', 'Answer', 'UserProfile', 'Course', function($scope, $routeParams, Question, Answer, UserProfile, Course) {

        Course.get({machine_readable_title: $routeParams.courseTitle}, function (course) {
            $scope.course = course.objects[0];
        });
        $scope.courseTitle = $routeParams.courseTitle;
        $scope.questions = Question.query();
        $scope.user_profile = UserProfile.query();
        $scope.answers = Answer.query();

        $scope.addNewAnswer = function() {
            $scope.answers.push({ question: $scope.question.id, user: 2, content: $scope.newAnswer.content})
        }
    }])



;

