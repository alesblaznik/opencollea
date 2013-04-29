# coding=utf-8
import urllib2
import json
from find_courses.mooc import providers


class Mooc(object):
    MOOC_URL = ''
    COURSES_LIST_URL = ''

    def __init__(self, title, description='', courses=[]):
        self.title = title
        self.description = description
        self.courses = courses

    def fetch_all(self):
        raise NotImplementedError

    def get_html(self, url):
        return urllib2.urlopen(url).read()

    def get_json(self, url):
        return json.load(urllib2.urlopen(url))


class Course(object):
    def __init__(self, title='', url='', university='',
                 professor='', begin_date=None, length=None):
        self.title = title
        self.url = url
        self.university = university
        self.professor = professor
        self.begin_date = begin_date
        self.length = length
        self.categories = set()


class Fetcher(object):
    def get_all_providers(self):
        # todo Providerji naj se naložijo samodejno iz mape providers/*
        from providers.coursera import Coursera
        from providers.edx import Edx
        from providers.udacity import Udacity
        providers_instances = [
            Coursera(), Edx(), Udacity()
        ]
        return providers_instances
