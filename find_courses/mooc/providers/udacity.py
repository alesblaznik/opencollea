from find_courses.mooc.models import Mooc, Course
from find_courses.mooc.utils import FetchError, ParseError
from bs4 import BeautifulSoup

class Udacity(Mooc):
    TITLE = 'Udacity'
    MOOC_URL = 'https://www.udacity.com'
    COURSES_LIST_URL = 'https://www.udacity.com/courses'

    def __init__(self):
        super(Udacity, self).__init__(self.TITLE)

    def fetch_all(self):
        self.fetch_courses()

    def fetch_courses(self):
        soup = BeautifulSoup(self.get_html(self.COURSES_LIST_URL))
        courses = soup.find_all('div', class_='crs-li-info')
        for course in courses:
            c = Course()
            c.title = course.find('div', class_='crs-li-title').string
            c.url = self.MOOC_URL + course.parent.attrs['href']
            c.categories.add(
                course.find('div', class_='crs-li-tags-category').string
            )
            self.courses.append(c)

