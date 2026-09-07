from django.contrib import admin
from .models import ReferenceFramework, Aspect, Element, MaturityCriterion, ApplicabilityLevel, ReferenceFrameworkMapping, Organisation, AISystem, ElementAssessment, MaturityLevel

# Register your models here.

admin.site.register(ReferenceFramework, list_display=["name", "version", "description"])
admin.site.register(Aspect, list_display=["name", "description"])
admin.site.register(Element, list_display=["name", "aspect"])
admin.site.register(MaturityCriterion, list_display=["element", "level", "criterion"])
admin.site.register(ApplicabilityLevel, list_display=["name", "value", "description"])
admin.site.register(ReferenceFrameworkMapping, list_display=["element", "framework", "coverage"])
admin.site.register(Organisation, list_display=["name"])
admin.site.register(AISystem, list_display=["name", "organisation"])
admin.site.register(MaturityLevel, list_display=["name", "value", "description"])


#admin.site.register(ElementAssessment, list_display=["element", "applicability", "maturity"])
@admin.register(ElementAssessment)
class ElementAssessmentAdmin(admin.ModelAdmin):
    list_display = ["element", "aspect", "applicability", "maturity", "assessment_date"]
    ordering = ["-assessment_date"]

    @admin.display(description="Aspect")
    def aspect(self, obj):
        return obj.element.aspect