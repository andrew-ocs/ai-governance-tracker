from django.contrib import admin
from .models import Framework, GovernanceAspect, GovernanceElement, MaturityCriterion, ApplicabilityLevel, FrameworkMapping, Organisation, AISystem, Assessment, ElementAssessment

# Register your models here.

admin.site.register(Framework)
admin.site.register(GovernanceAspect)
admin.site.register(GovernanceElement)
admin.site.register(MaturityCriterion)
admin.site.register(ApplicabilityLevel)
admin.site.register(FrameworkMapping)
admin.site.register(Organisation)
admin.site.register(AISystem)
admin.site.register(Assessment)
admin.site.register(ElementAssessment)
