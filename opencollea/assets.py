from django_assets import Bundle, register

# CSS
css = Bundle('css/bootstrap.css',
             'css/bootstrap-responsive.css',
             'css/opencollea.css',
             filters='cssmin', output='css/opencollea.css')
register('css_all', css)

# JavaScript
js = Bundle('js/jquery-2.0.0.js',
            'js/bootstrap.js',
            'js/angular.js',
            'js/http-auth-interceptor.js',
            'js/app.js',
            'js/controllers.js',
            output='js/opencollea.js')
register('js_all', js)
