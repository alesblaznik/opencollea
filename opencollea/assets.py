from django_assets import Bundle, register

# CSS
css = Bundle('css/bootstrap.min.css',
             'css/bootstrap-responsive.min.css',
             'css/opencollea.css',
             filters='cssmin', output='css/opencollea.css')
register('css_all', css)

# JavaScript
js = Bundle('js/jquery-2.0.0.js',
            'js/bootstrap.js',
            'js/angular.js',
            'js/services.js',
            'js/controllers.js',
            'js/app.js',
            'js/raphael.js',
            'js/pie.js',
            output='js/opencollea.js')
register('js_all', js)