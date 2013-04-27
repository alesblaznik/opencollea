from django_assets import Bundle, register

# CSS
css = Bundle('css/bootstrap.min.css',
             'css/bootstrap-responsive.min.css',
             'css/opencollea.css',
             filters='cssmin', output='css/opencollea.css')
register('css_all', css)

# JavaScript
js = Bundle('js/jquery-2.0.0.min.js',
            'js/bootstrap.min.js',
            output='js/opencollea.js')
register('js_all', js)
