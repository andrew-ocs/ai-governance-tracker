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

mappings = {

    "AI Strategy & Objectives": {
        "ISO 42001": 3,
        "NIST AI RMF": 3,
        "UK AI Playbook": 3,
        "ETSI": 3,
    },

    "AI Principles & Policy": {
        "ISO 42001": 3,
        "NIST AI RMF": 3,
        "UK AI Playbook": 3,
        "ETSI": 3,
    },

}