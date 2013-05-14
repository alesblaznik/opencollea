from django.shortcuts import _get_queryset
from code_register.models import Gender, Language, AgeRange, Occupation, \
    AreaOfStudy

from tastypie.resources import ModelResource


class GenderResource(ModelResource):
    class Meta:
        queryset = Gender.objects.all()
        resource_name = 'gender'


class LanguageResource(ModelResource):
    class Meta:
        queryset = Language.objects.all()
        resource_name = 'language'


class AgeRangeResource(ModelResource):
    class Meta:
        queryset = AgeRange.objects.all()
        resource_name = 'age_range'


class OccupationResource(ModelResource):
    class Meta:
        queryset = Occupation.objects.all()
        resource_name = 'occupation'


class AreaOfStudyResource(ModelResource):
    class Meta:
        queryset = AreaOfStudy.objects.all()
        resource_name = 'area_of_study'
