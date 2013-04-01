# coding=utf-8
from django_cron import CronJobBase, Schedule
from find_courses import models
from find_courses.mooc.models import Fetcher

class ImportMoocCoursesCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440 # Every day
    #RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'find_courses.import_mooc_courses_cron_job'

    def do(self):
        # todo Needs some work!!!
        # todo Napačno vstavi source - vedno nakoncu dobijo Udacity, čeprav
        #      pripadajo drugam
        fetcher = Fetcher()
        for provider in fetcher.get_all_providers():
            provider.fetch_courses()
            for course in provider.courses:
                try:
                    c = models.Course(
                        title=course.title,
                        source=unicode(provider.TITLE),
                        url=course.url)
                    c.save() # ouch!!!
                except:
                    pass

