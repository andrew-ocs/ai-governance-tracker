aspects = [
    {
        "name": "AI Strategy & Policy",
        "description": "Strategic direction, principles, policy and AI risk appetite.",
        "elements": [
            {
                "name": "AI Strategy & Objectives",
                "maturity_criteria": {
                    1: "AI opportunities and ambitions are recognised in parts of the organisation, with objectives emerging through individual initiatives or teams. There is no consistent enterprise view of how AI should contribute to organisational outcomes.",
                    2: "A documented AI strategy or set of strategic objectives has been approved, linking AI adoption to organisational priorities, desired outcomes and material constraints. Relevant stakeholders and ownership are identified.",
                    3: "AI strategy and objectives are consistently incorporated into business planning, investment decisions and AI portfolio management. AI initiatives are assessed against strategic objectives, with progress and outcomes monitored through defined measures.",
                    4: "AI strategy is continuously refined using portfolio performance, realised benefits, emerging AI capabilities, market/regulatory developments and organisational learning. Investment and strategic priorities are proactively adjusted based on evidence.",
                },
                "framework_mappings": {
                    "ISO 42001": 3,
                    "NIST AI RMF": 3,
                    "UK AI Playbook": 3,
                    "ETSI": 3,
                }
            },
            {
                "name": "AI Principles & Policy",
                "maturity_criteria": {
                    1: "The organisation recognises the need for responsible AI principles or policies, but expectations are informal, fragmented or applied inconsistently between teams.",
                    2: "Enterprise AI principles and policies are documented, approved and communicated, defining expected behaviours, mandatory requirements and relevant governance responsibilities.",
                    3: "AI principles and policies are consistently incorporated into AI lifecycle processes, procurement, design, deployment and operational activities. Compliance is monitored and exceptions are formally managed.",
                    4: "Policies and principles are continuously improved using assurance findings, incidents, stakeholder feedback, regulatory change and emerging AI risks. Controls and guidance are proactively adapted as the AI landscape evolves.",
                },
                "framework_mappings": {
                    "ISO 42001": 3,
                    "NIST AI RMF": 3,
                    "UK AI Playbook": 3,
                    "ETSI": 3,
                }
            },
            {"name": "AI Risk Appetite"},
            {"name": "AI Technology & Use-Case Boundaries"},
            {"name": "AI Investment & Adoption Management"},
        ]
    },
    {
        "name": "Governance, Accountability & Oversight",
        "description": "Organisational governance, accountability and decision-making.",
        "elements": [
            {"name": "AI Governance Structure"},
            {"name": "Roles & Responsibilities"},
            {"name": "Decision Rights & Approval Authorities"},
            {"name": "Governance Processes & Controls"},
            {"name": "Escalation & Exception Management"},
            {"name": "Governance Performance & Reporting"},
        ]
    },
    {
        "name": "AI Portfolio & Lifecycle Management",
        "description": "Management of AI systems throughout their lifecycle.",
        "elements": [
            {"name": "AI Inventory & Registration"},
            {"name": "AI Use-Case Intake & Classification"},
            {"name": "AI Lifecycle Governance"},
            {"name": "Change & Model Evolution Management"},
            {"name": "AI Retirement & Disposal"},
        ]
    },
    {
        "name": "Risk & Impact Management",
        "description": "Identification, assessment, treatment and monitoring of AI risks and impacts.",
        "elements": [
            {"name": "AI Risk Identification"},
            {"name": "Impact Assessment"},
            {"name": "Risk Assessment & Classification"},
            {"name": "Risk Treatment & Mitigation"},
            {"name": "Residual Risk & Acceptance"},
            {"name": "AI Risk Monitoring"},
        ]
    },
    {
        "name": "Legal, Regulatory & Ethical Compliance",
        "description": "Legal, regulatory, privacy, ethical and responsible AI requirements.",
        "elements": [
            {"name": "Legal Compliance"},
            {"name": "Regulatory Compliance"},
            {"name": "Privacy Compliance"},
            {"name": "Ethical Compliance"},
            {"name": "Responsible AI Implementation"},
        ]
    },
    {
        "name": "Data & Information Governance",
        "description": "Governance of data used by AI systems.",
        "elements": [
            {"name": "Data Quality Management"},
            {"name": "Data Privacy & Protection"},
            {"name": "Data Lineage & Traceability"},
            {"name": "Information Governance"},
        ]
    },
    {
        "name": "AI Security & Resilience",
        "description": "Security, resilience and cybersecurity of AI systems.",
        "elements": [
            {"name": "AI Security Strategy"},
            {"name": "AI System Security Controls"},
            {"name": "AI System Resilience & Continuity"},
            {"name": "Cybersecurity & Threat Intelligence"},
        ]
    },
    {
        "name": "AI Assurance, Transparency & Explainability",
        "description": "Testing, assurance, transparency, explainability and traceability.",
        "elements": [
            {"name": "AI Testing & Validation"},
            {"name": "AI Assurance & Audit"},
            {"name": "Transparency & Explainability"},
            {"name": "Traceability & Documentation"},
        ]
    },
    {
        "name": "Human Oversight, Skills & Adoption",
        "description": "Human control, AI literacy, skills and responsible adoption.",
        "elements": [
            {"name": "Human Oversight & Control"},
            {"name": "AI Literacy & Skills Development"},
            {"name": "Responsible AI Adoption & Change Management"},
        ]
    },
    {
        "name": "Operational Monitoring & Continuous Improvement",
        "description": "Operational monitoring, incidents, metrics and continuous improvement.",
        "elements": [
            {"name": "Operational Monitoring & Metrics"},
            {"name": "Incident Management & Reporting"},
            {"name": "Continuous Improvement & Lessons Learned"},
        ]
    },
]

applicability_levels = {
    0: {
        "name": "N/A",
        "description": "The governance element has no meaningful relevance to the AI system or use case based on its characteristics, context, data, users and intended purpose. No assessment or control is required."
    },
    1: {
        "name": "Low",
        "description": "The element has limited relevance or presents relatively low potential consequences if inadequately addressed. Basic consideration and proportionate controls are appropriate."
    },
    2: {
        "name": "Medium",
        "description": "Materially relevant to the AI system and failure to address it could result in meaningful consequences. Defined controls and evidence are expected."
    },
    3: {
        "name": "High",
        "description": "Highly relevant and failure could result in significant impact or loss of trust. Strong controls, formal assurance and active oversight are expected."
    },
    4: {
        "name": "Critical",
        "description": "Fundamental to the safe, lawful or acceptable operation of the AI system. Failure could result in severe consequences, or undermine the organisation's ability to retain control of the system. Rigorous controls, senior accountability and potentially independent assurance are expected."
    },
}

maturity_levels = {
    0: {
        "name": "Absent",
        "description": "The governance capability has not been established or adopted. There is no defined ownership, process, control or consistent activity relating to the element."
    },
    1: {
        "name": "Initial",
        "description": "The capability is recognised and some governance activity occurs, but adoption is limited, inconsistent or dependent on individual people or teams. Activity is primarily reactive rather than systematic."
    },
    2: {
        "name": "Established",
        "description": "A defined governance approach has been adopted, with documented policies, processes, roles and/or controls. The capability is being applied to relevant AI activities, although adoption or consistency may still be incomplete."
    },
    3: {
        "name": "Embedded",
        "description": "The governance capability is consistently embedded into relevant organisational processes and AI lifecycle activities. Roles and controls are understood and routinely applied, with compliance and effectiveness monitored."
    },
    4: {
        "name": "Optimised",
        "description": "The capability is fully embedded and continuously improved using evidence, performance data, assurance findings, incidents, emerging risks and organisational learning. The organisation proactively adapts the capability as its AI landscape evolves."
    },
}