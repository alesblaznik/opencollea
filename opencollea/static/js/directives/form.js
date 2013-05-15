
app

/**
 * formSaveButtonLoading
 *  - Loading text in disabled text ko se obrazec shranjuje.
 */
.directive('formSaveButtonLoading', [function() {
    return {
        link: function(scope, iElement, iAttrs) {
            // Shrani prvotno besedilo gumba
            iElement.attr('data-html-orig', iElement.html());

            scope.$watch('loading', function(isLoading) {
                if (isLoading) {
                    iElement.html(iAttrs.formSaveButtonLoading);
                    iElement.attr('disabled', true);
                } else {
                    iElement.html(iElement.attr('data-html-orig'));
                    iElement.attr('disabled', false);
                }
            });
        }
    }
}])

;
