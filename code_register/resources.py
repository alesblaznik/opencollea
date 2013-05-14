from code_register.models import Gender, Language, AgeRange, Occupation, \
    AreaOfStudy
from tastypie.resources import ModelResource


class GenderResource(ModelResource):
    class Meta:
        queryset = Gender.objects.all()
        resource_name = 'gender'
        allowed_methods = ['get']


class LanguageResource(ModelResource):
    class Meta:
        queryset = Language.objects.all()
        resource_name = 'language'
        allowed_methods = ['get']


class AgeRangeResource(ModelResource):
    class Meta:
        queryset = AgeRange.objects.all()
        resource_name = 'age_range'
        allowed_methods = ['get']


class OccupationResource(ModelResource):
    class Meta:
        queryset = Occupation.objects.all()
        resource_name = 'occupation'
        allowed_methods = ['get']


class AreaOfStudyResource(ModelResource):
    class Meta:
        queryset = AreaOfStudy.objects.all()
        resource_name = 'area_of_study'
        allowed_methods = ['get']
