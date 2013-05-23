from django.db.models.signals import post_save
from django.dispatch import receiver

from opencollea.models import CourseActivity, Question, Answer, EtherpadNote


@receiver(post_save)
def course_activity_stream(sender, instance, created, **kwargs):
    if isinstance(instance, Answer) or isinstance(instance, Question) or \
            isinstance(instance, EtherpadNote):
        if isinstance(instance, Answer):
            course = instance.question.course
        else:
            course = instance.course
        activity = CourseActivity(
            course=course,
            user=instance.user,
            model_name=instance.__class__.__name__,
            model_id=instance.pk,
            action_performed=CourseActivity.ACTION_CREATED
        )
        activity.save()

