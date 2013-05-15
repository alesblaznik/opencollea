from find_courses.mooc.models import Mooc, Course
from find_courses.mooc.utils import FetchError, ParseError


class Coursera(Mooc):
    TITLE = 'Coursera'
    MOOC_URL = 'https://www.coursera.org'
    COURSES_LIST_URL = 'https://www.coursera.org/courses'

    COURSES_LIST_JSON = \
        'https://www.coursera.org/maestro/api/topic/list?full=1'

    def __init__(self):
        super(Coursera, self).__init__(self.TITLE)

    def fetch_all(self):
        self.fetch_courses()

    def fetch_courses(self):
        try:
            courses = self.get_json(self.COURSES_LIST_JSON)
        except ValueError:
            raise ParseError('Invalid JSON format')
        except:
            raise FetchError('Couldn\'t fetch JSON.')

        for course in courses:
            c = Course(
                course['name'],
                course['social_link'],
                course['university-ids'][0],
                course['instructor']
            )
            self.courses.append(c)
