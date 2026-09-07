from django.core.management.base import BaseCommand

from governance.models import (
    AISystem,
    ElementAssessment,
    ReferenceFramework,
    Aspect,
    Element,
    MaturityCriterion,
    ApplicabilityLevel,
    ReferenceFrameworkMapping,
    MaturityLevel,
    Organisation,
)

from governance.data.framework import aspects, applicability_levels, maturity_levels
from governance.data.reference import frameworks
from governance.data.defaults import organisations
from governance.data.example import element_assessments


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Reference Frameworks
        for framework in frameworks:
            ReferenceFramework.objects.get_or_create(
                short_name=framework.get("short name"),
                defaults={
                    "name": framework.get("name"),
                    "version": framework.get("version"),
                    "description": framework.get("description"),
                }
            )
        self.stdout.write("Reference Frameworks created.")

        # Our framework aspects, elements, maturity criteria and framework mappings
        for order, aspect in enumerate(aspects, start=1):
            _aspect = Aspect.objects.get_or_create(
                name=aspect.get("name"),
                defaults={
                    "description": aspect.get("description"),
                    "order": order,
                }
            )

            # Elements
            for element in aspect.get("elements", []):
                _element = Element.objects.get_or_create(
                    aspect=_aspect[0],
                    name=element.get("name"),
                    defaults={
                        "description": element.get("description", ""),
                        "order": order,
                        "active": True,
                    }
                )

                # Maturity Criteria
                for level, criterion in element.get("maturity_criteria", {}).items():
                    MaturityCriterion.objects.update_or_create(
                        element=_element[0],
                        level=level,
                        defaults={
                            "criterion": criterion
                        }
                    )

                # Framework Mappings
                for framework_name, coverage in element.get("framework_mappings", {}).items():
                
                    _framework = ReferenceFramework.objects.get(
                        short_name=framework_name
                    )
    
                    ReferenceFrameworkMapping.objects.update_or_create(
                        element=_element[0],
                        framework=_framework,
                        defaults={
                            "coverage": coverage
                        }
                    )

        # Our framework's Applicability Levels
        for level, applicability_level in applicability_levels.items():
            ApplicabilityLevel.objects.get_or_create(
                value=level,
                defaults={
                    "name": applicability_level.get("name"),
                    "description": applicability_level.get("description"),
                }
            )

        # Our framework's Maturity Levels
        for level, maturity_level in maturity_levels.items():
            MaturityLevel.objects.get_or_create(
                value=level,
                defaults={
                    "name": maturity_level.get("name"),
                    "description": maturity_level.get("description"),
                }
            )

        self.stdout.write("Aspects, elements, maturity criteria, applicability and maturity levels, and framework mappings created.")           

        # Seed Data !!!!!!!!!!!!!!!!!!!!!!!!!!

        # Organisations
        for org in organisations:
            _org = Organisation.objects.get_or_create(
                name=org.get("name")
            )

            # AI Systems
            for ai_system in org.get("ai_systems", []):
                AISystem.objects.get_or_create(
                    organisation=_org[0],
                    name=ai_system.get("name"),
                    defaults={
                        "description": ai_system.get("description")
                    }
            )
        self.stdout.write("Opencast Org and AI systems created.")

        # Example Element Assessments
        for assessment in element_assessments:
            _element = Element.objects.get(
                name=assessment.get("element_name")
            )
            _applicability = ApplicabilityLevel.objects.get(
                value=assessment.get("applicability_level")
            )
            _maturity = MaturityLevel.objects.get(
                value=assessment.get("maturity_level")
            )

            ElementAssessment.objects.create(
                element=_element,
                applicability=_applicability,
                maturity=_maturity,
                rationale=assessment.get("rationale"),
                assessor=assessment.get("assessor", "Andrew"),
            )
        self.stdout.write("Example element assessments created.")