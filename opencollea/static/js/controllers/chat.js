

app

.controller('ChatCtrl', ['$scope', '$window', 'UserProfile', 'Course',
    function ($scope, $window, UserProfile, Course) {

        // OK vem, tale array je temp, ampak samo zato, ker ni povezano s socketi in sem rabil vsebino:
        $scope.messages = [
            {email: 'andraz.oberstar@gmail.com', author: 'Obi Wan Kenobi', time: '1 Day(s) ago',
                content: 'May the force be with you!'}
            ,{email: 'ziga.emersic@gmail.com', author: 'Frauen Parkplatz', time: '2 Hour(s) ago',
                content: 'Tale objava je zelo dolga \n in je zgolj testne narave!\n\nIma tudi nekaj new lineov in tega'}
        ];

        $scope.user_profile = UserProfile.get({userId: $scope.currentUser.id});
        $scope.postMessage = function() {
            $scope.messages.push({
                email: $scope.currentUser.email,
                author: $scope.user_profile.first_name + ' ' + $scope.user_profile.last_name,
                time: 'Just now',
                content: this.messageTextArea});
            this.messageTextArea = '';
        }
    }
])

.filter('reverse', function() {
  return function(items) {
    return items.slice().reverse();
  };
});


