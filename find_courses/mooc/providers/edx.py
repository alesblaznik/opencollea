from find_courses.mooc.models import Mooc, Course
from bs4 import BeautifulSoup


class Edx(Mooc):
    TITLE = 'edX'
    MOOC_URL = 'https://www.edx.org'
    COURSES_LIST_URL = 'https://www.edx.org/courses'

    def __init__(self):
        super(Edx, self).__init__(self.TITLE)

    def fetch_all(self):
        self.fetch_courses()

    def fetch_courses(self):
        soup = BeautifulSoup(self.get_html(self.COURSES_LIST_URL))
        courses = soup.find_all('article', class_='course')
        for course in courses:
            c = Course()
            c.title = ' '.join(course.find('header').find('h2')
                               .text.split(' ')[1:])
            c.url = self.MOOC_URL + course.find('a').attrs['href']
            c.university = course.section.find('div', class_='bottom')\
                .find('a', class_='university').string
            c.begin_date = course.section.find('div', class_='bottom')\
                .find('span', class_='start-date').string
            self.courses.append(c)
