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


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Frameworks
        iso42001, _ = Framework.objects.get_or_create(
            short_name="ISO 42001",
            defaults={
                "name": "ISO/IEC 42001:2023",
                "version": "2023",
                "description": "Artificial intelligence management system standard.",
            }
        )

        nist, _ = Framework.objects.get_or_create(
            short_name="NIST AI RMF",
            defaults={
                "name": "NIST AI Risk Management Framework",
                "version": "1.0",
                "description": "Framework for managing risks associated with artificial intelligence.",
            }
        )

        uk_playbook, _ = Framework.objects.get_or_create(
            short_name="UK AI Playbook",
            defaults={
                "name": "UK Government AI Playbook",
                "version": "2025",
                "description": "UK Government guidance for using AI safely, responsibly and effectively.",
            }
        )

        etsi, _ = Framework.objects.get_or_create(
            short_name="ETSI EN 304 223",
            defaults={
                "name": "ETSI EN 304 223",
                "version": "2025",
                "description": "AI cybersecurity standard.",
            }
        )

        self.stdout.write("Frameworks created.")

        aspects = [
            ("AI Strategy & Policy", "Strategic direction, principles, policy and AI risk appetite."),
            ("Governance, Accountability & Oversight", "Organisational governance, accountability and decision-making."),
            ("AI Portfolio & Lifecycle Management", "Management of AI systems throughout their lifecycle."),
            ("Risk & Impact Management", "Identification, assessment, treatment and monitoring of AI risks and impacts."),
            ("Legal, Regulatory & Ethical Compliance", "Legal, regulatory, privacy, ethical and responsible AI requirements."),
            ("Data & Information Governance", "Governance of data used by AI systems."),
            ("AI Security & Resilience", "Security, resilience and cybersecurity of AI systems."),
            ("AI Assurance, Transparency & Explainability", "Testing, assurance, transparency, explainability and traceability."),
            ("Human Oversight, Skills & Adoption", "Human control, AI literacy, skills and responsible adoption."),
            ("Operational Monitoring & Continuous Improvement", "Operational monitoring, incidents, metrics and continuous improvement."),
        ]

        for order, (name, description) in enumerate(aspects, start=1):

            GovernanceAspect.objects.get_or_create(
                name=name,
                defaults={
                    "description": description,
                    "order": order,
                }
            )

        self.stdout.write("Aspects created.")

        elements = {
            "AI Strategy & Policy": [
                "AI Strategy & Objectives",
                "AI Principles & Policy",
                "AI Risk Appetite",
                "AI Technology & Use-Case Boundaries",
                "AI Investment & Adoption Management",
            ],

            "Governance, Accountability & Oversight": [
                "AI Governance Structure",
                "Roles & Responsibilities",
                "Decision Rights & Approval Authorities",
                "Governance Processes & Controls",
                "Escalation & Exception Management",
                "Governance Performance & Reporting",
            ],

            "AI Portfolio & Lifecycle Management": [
                "AI Inventory & Registration",
                "AI Use-Case Intake & Classification",
                "AI Lifecycle Governance",
                "Change & Model Evolution Management",
                "AI Retirement & Disposal",
            ],

            "Risk & Impact Management": [
                "AI Risk Identification",
                "Impact Assessment",
                "Risk Assessment & Classification",
                "Risk Treatment & Mitigation",
                "Residual Risk & Acceptance",
                "AI Risk Monitoring",
            ],

            # ...etc
        }

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

        maturity = {

            "AI Strategy & Objectives": {

                1: "AI opportunities and ambitions are recognised in parts of the organisation, with objectives emerging through individual initiatives or teams. There is no consistent enterprise view of how AI should contribute to organisational outcomes.",

                2: "A documented AI strategy or set of strategic objectives has been approved, linking AI adoption to organisational priorities, desired outcomes and material constraints. Relevant stakeholders and ownership are identified.",

                3: "AI strategy and objectives are consistently incorporated into business planning, investment decisions and AI portfolio management. AI initiatives are assessed against strategic objectives, with progress and outcomes monitored through defined measures.",

                4: "AI strategy is continuously refined using portfolio performance, realised benefits, emerging AI capabilities, market/regulatory developments and organisational learning. Investment and strategic priorities are proactively adjusted based on evidence.",
            },

            "AI Principles & Policy": {

                1: "The organisation recognises the need for responsible AI principles or policies, but expectations are informal, fragmented or applied inconsistently between teams.",

                2: "Enterprise AI principles and policies are documented, approved and communicated, defining expected behaviours, mandatory requirements and relevant governance responsibilities.",

                3: "AI principles and policies are consistently incorporated into AI lifecycle processes, procurement, design, deployment and operational activities. Compliance is monitored and exceptions are formally managed.",

                4: "Policies and principles are continuously improved using assurance findings, incidents, stakeholder feedback, regulatory change and emerging AI risks. Controls and guidance are proactively adapted as the AI landscape evolves.",
            },

        }

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

        mappings = {

            "AI Strategy & Objectives": {
                "ISO 42001": 3,
                "NIST AI RMF": 3,
                "UK AI Playbook": 3,
                "ETSI EN 304 223": 3,
            },

            "AI Principles & Policy": {
                "ISO 42001": 3,
                "NIST AI RMF": 3,
                "UK AI Playbook": 3,
                "ETSI EN 304 223": 3,
            },

        }

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

        applicability_levels = [
            (0, "N/A", "No meaningful relevance to the AI system."),
            (1, "Low", "Limited relevance or low potential consequences."),
            (2, "Medium", "Material relevance with meaningful consequences."),
            (3, "High", "High relevance with significant potential consequences."),
            (4, "Critical", "Fundamental to safe, lawful or acceptable operation."),
        ]

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
        opencast_org = Organisation.objects.get_or_create(
            name="Opencast Software Ltd"
        )

        # AI Systems
        AISystem.objects.get_or_create(
            organisation=opencast_org[0],
            name="Customer Service Chatbot",
            defaults={
                "description": "An AI-powered chatbot designed to assist customers with inquiries, provide support, and enhance the overall customer service experience. It leverages natural language processing and machine learning to understand and respond to user queries effectively."
            }
        )

        self.stdout.write("Org and AI systems created.")