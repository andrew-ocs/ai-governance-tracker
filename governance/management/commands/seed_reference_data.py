from django.core.management.base import BaseCommand

from governance.models import (
    AISystem,
    Framework,
    GovernanceAspect,
    GovernanceElement,
    MaturityCriterion,
    ApplicabilityLevel,
    FrameworkMapping,
    Organisation,
)

from governance.data.framework import aspects, elements, maturity, mappings
from governance.data.reference import frameworks, applicability_levels
from governance.data.defaults import organisations, ai_systems


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Frameworks
        for framework in frameworks:
            Framework.objects.get_or_create(
                short_name=framework.get("short name"),
                defaults={
                    "name": framework.get("name"),
                    "version": framework.get("version"),
                    "description": framework.get("description"),
                }
            )
        self.stdout.write("Frameworks created.")

        # Aspects
        for order, (name, description) in enumerate(aspects, start=1):
            GovernanceAspect.objects.get_or_create(
                name=name,
                defaults={
                    "description": description,
                    "order": order,
                }
            )
        self.stdout.write("Aspects created.")

        # Elements
        for aspect_name, element_names in elements.items():
            aspect = GovernanceAspect.objects.get(
                name=aspect_name
            )

            for order, element_name in enumerate(element_names, start=1):
                GovernanceElement.objects.get_or_create(
                    aspect=aspect,
                    name=element_name,
                    defaults={
                        "description": "",
                        "order": order,
                        "active": True,
                    }
                )
        self.stdout.write("Elements created.")

        # Maturity Criteria
        for element_name, levels in maturity.items():
            element = GovernanceElement.objects.get(
                name=element_name
            )

            for level, criterion in levels.items():

                MaturityCriterion.objects.update_or_create(
                    element=element,
                    level=level,
                    defaults={
                        "criterion": criterion
                    }
                )
        self.stdout.write("Maturity criteria created.")

        # Framework Mappings
        for element_name, framework_mappings in mappings.items():
            element = GovernanceElement.objects.get(
                name=element_name
            )

            for framework_name, coverage in framework_mappings.items():

                framework = Framework.objects.get(
                    short_name=framework_name
                )

                FrameworkMapping.objects.update_or_create(
                    element=element,
                    framework=framework,
                    defaults={
                        "coverage": coverage
                    }
                )
        self.stdout.write("Framework mappings created.")

        # Applicability Levels
        for value, name, description in applicability_levels:
            ApplicabilityLevel.objects.get_or_create(
                value=value,
                defaults={
                    "name": name,
                    "description": description,
                }
            )
        self.stdout.write("Applicability levels created.")

        # Organisations
        for org in organisations:
            Organisation.objects.get_or_create(
                name=org.get("name")
            )

        # AI Systems
        for ai_system in ai_systems:
            AISystem.objects.get_or_create(
                organisation=Organisation.objects.get(name=ai_system.get("organisation")),
                name=ai_system.get("name"),
                defaults={
                    "description": ai_system.get("description")
                }
        )

        self.stdout.write("Org and AI systems created.")