from django.db import models

# Create your models here.

class Framework(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    version = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class GovernanceAspect(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

class GovernanceElement(models.Model):
    aspect = models.ForeignKey(
        GovernanceAspect,
        on_delete=models.PROTECT,
        related_name="elements"
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["aspect__order", "order"]

    def __str__(self):
        return self.name

class MaturityCriterion(models.Model):
    element = models.ForeignKey(
        GovernanceElement,
        on_delete=models.CASCADE,
        related_name="maturity_criteria"
    )
    level = models.PositiveSmallIntegerField()
    criterion = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["element", "level"],
                name="unique_element_maturity_level"
            )
        ]
        ordering = ["level"]

    def __str__(self):
        return f"{self.element.name} - Level {self.level}"


class FrameworkMapping(models.Model):
    element = models.ForeignKey(
        GovernanceElement,
        on_delete=models.CASCADE,
        related_name="framework_mappings"
    )
    framework = models.ForeignKey(
        Framework,
        on_delete=models.CASCADE,
        related_name="element_mappings"
    )
    coverage = models.PositiveSmallIntegerField(
        choices=[
            (0, "No / minimal coverage"),
            (1, "Limited coverage"),
            (2, "Significant coverage"),
            (3, "Core coverage"),
        ]
    )
    reference = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["element", "framework"],
                name="unique_element_framework"
            )
        ]

class ApplicabilityLevel(models.Model):
    name = models.CharField(max_length=50)
    value = models.PositiveSmallIntegerField()
    description = models.TextField()

    class Meta:
        ordering = ["value"]

    def __str__(self):
        return self.name

class Organisation(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AISystem(models.Model):
    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        related_name="ai_systems"
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Assessment(models.Model):
    ai_system = models.ForeignKey(
        AISystem,
        on_delete=models.CASCADE,
        related_name="assessments"
    )
    assessment_date = models.DateTimeField(auto_now_add=True)
    assessor = models.CharField(max_length=100, default="paul")
    status = models.CharField(max_length=200)

class ElementAssessment(models.Model):
    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.CASCADE,
        related_name="element_assessments"
    )
    element = models.ForeignKey(
        GovernanceElement,
        on_delete=models.PROTECT
    )

    applicability = models.ForeignKey(
        ApplicabilityLevel,
        on_delete=models.PROTECT
    )

    maturity = models.PositiveSmallIntegerField(
        choices=[
            (1, "Initial"),
            (2, "Established"),
            (3, "Embedded"),
            (4, "Optimised"),
        ]
    )

    rationale = models.TextField()
    evidence = models.TextField(blank=True)