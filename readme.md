# AI Governance Compass

AI Governance Compass is an enterprise AI governance maturity assessment platform.

The tool helps organisations assess how effectively they govern individual AI systems against a structured set of governance capabilities, drawing on established AI governance and risk frameworks.

The platform is designed to answer three key questions:

> **Where are we now? Where do we need to be? What do we need to do to get there?**

---

## Overview

AI Governance Compass provides a structured way to assess the governance maturity of AI systems across areas including:

* AI strategy and policy
* Governance, accountability and oversight
* AI portfolio and lifecycle management
* Risk and impact management
* Legal, regulatory and ethical compliance
* Data and information governance
* AI security and resilience
* AI assurance, transparency and explainability
* Human oversight, skills and adoption
* Operational monitoring and continuous improvement

Each governance capability can be assessed for:

* **Applicability** — how important the capability is for the AI system
* **Current maturity** — how well the capability is currently implemented
* **Target maturity** — the desired future state
* **Rationale** — why the assessment has been made
* **Evidence** — supporting evidence for the assessment
* **Improvement actions** — activities required to close identified gaps

---

## Reference Frameworks

The governance model is informed by established AI governance and risk frameworks, including:

* **ISO/IEC 42001:2023** — Artificial Intelligence Management System
* **NIST AI Risk Management Framework (AI RMF)**
* **UK Government AI Playbook**
* **ETSI EN 304 223** — AI cybersecurity

The platform does not simply reproduce one of these frameworks. Instead, it provides a common governance model and maps individual governance capabilities to relevant framework requirements and guidance.

This allows organisations to assess their AI governance once while understanding how the assessment relates to multiple external frameworks.

---

## Maturity Model

The current maturity model consists of five levels:

| Level | Name        | Description                                                                                                      |
| ----: | ----------- | ---------------------------------------------------------------------------------------------------------------- |
|     0 | Absent      | The governance capability has not been established or adopted.                                                   |
|     1 | Initial     | Activity exists but is limited, inconsistent or reactive.                                                        |
|     2 | Established | A defined governance approach, process or control has been adopted.                                              |
|     3 | Embedded    | The capability is consistently embedded into relevant organisational and AI lifecycle processes.                 |
|     4 | Optimised   | The capability is continuously improved using evidence, performance data, assurance findings and emerging risks. |

Maturity is assessed independently for each governance element.

---

## Applicability

Not every governance capability has the same importance for every AI system.

Each element can therefore be assigned an applicability level:

| Level | Name     | Meaning                                             |
| ----: | -------- | --------------------------------------------------- |
|     0 | N/A      | No meaningful relevance to the AI system            |
|     1 | Low      | Limited relevance or low potential consequences     |
|     2 | Medium   | Material relevance with meaningful consequences     |
|     3 | High     | Significant relevance or potential impact           |
|     4 | Critical | Fundamental to safe, lawful or acceptable operation |

This allows assessments to be risk- and context-based rather than treating every control as equally important.

---

## Conceptual Model

The application separates **reference data** from **assessment data**.

### Reference data

Reference data defines the governance model:

```text
Frameworks
    ↓
Governance Aspects
    ↓
Governance Elements
    ↓
Maturity Criteria
    ↓
Framework Mappings
```

### Assessment data

Assessment data records how an organisation applies the model:

```text
Organisation
    ↓
AI System
    ↓
Assessment
    ↓
Element Assessments
    ↓
Evidence / Improvement Actions / Assessment History
```

This separation allows the underlying governance model to evolve independently from individual organisational assessments.

---

## Current Data Model

The current Django models include:

### Reference models

* `Framework`
* `GovernanceAspect`
* `GovernanceElement`
* `MaturityCriterion`
* `FrameworkMapping`
* `ApplicabilityLevel`

### Assessment models

* `Organisation`
* `AISystem`
* `Assessment`
* `ElementAssessment`

Additional models for evidence, improvement actions and assessment history can be added as the platform develops.

---

## Technology

The current prototype is built using:

* **Python**
* **Django**
* **Django Admin**
* **Django REST Framework** (planned / available)
* **PostgreSQL** (planned)
* **SQLite** for simple local development
* **React / Next.js** (planned frontend)

The Django Admin interface is currently being used as the initial application interface while the underlying data model is developed.

---

# Getting Started

## Prerequisites

You will need:

* Python 3.x
* pip
* Git

PostgreSQL is not currently required if using the default SQLite configuration.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd ai-governance
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install django djangorestframework psycopg[binary] pytest pytest-django
```

---

## Database Setup

Create the database migrations:

```bash
python manage.py makemigrations
```

Apply the migrations:

```bash
python manage.py migrate
```

---

## Load Reference Data

The project includes a Django management command for loading reference data.

Run:

```bash
python manage.py seed_reference_data
```

This populates the database with the reference frameworks and associated governance data defined by the project.

The seed process is intended to be repeatable, allowing the reference data to be recreated during development.

---

## Create an Admin User

Create a Django superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your local administrator account.

---

## Run the Application

Start the Django development server:

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

The Django Admin interface is available at:

```text
http://127.0.0.1:8000/admin/
```

---

# Typical Assessment Workflow

The intended workflow for an assessment is:

### 1. Create an organisation

Example:

```text
Organisation
    DEFRA
```

### 2. Create an AI system

Example:

```text
AI System
    Reservoir Compliance System
```

### 3. Create an assessment

An assessment represents the governance state of the AI system at a particular point in time.

Example:

```text
Assessment
    AI System: Reservoir Compliance System
    Assessor: Paul
    Date: September 2026
    Status: Draft
```

### 4. Assess governance elements

Each relevant governance element is assessed for:

```text
Applicability
Current maturity
Target maturity
Rationale
```

For example:

```text
AI Security Architecture

Applicability:  Critical
Current maturity: 2
Target maturity: 4
```

### 5. Identify governance gaps

The difference between current and target maturity identifies areas for improvement.

```text
Current maturity: 2
Target maturity: 4

Maturity gap: 2
```

### 6. Track improvement

Future functionality will allow improvement actions, evidence and subsequent assessments to be linked to the identified gaps.

---

# Development Approach

The application is being developed incrementally.

### Phase 1 — Reference Framework

* [x] Framework model
* [x] Governance aspect model
* [x] Governance element model
* [x] Maturity criteria
* [x] Framework mappings
* [x] Applicability levels
* [x] Reference data seed process
* [x] Django Admin interface

### Phase 2 — Assessments

* [x] Organisation model
* [x] AI System model
* [x] Assessment model
* [ ] Element assessment workflow
* [ ] Current maturity assessment
* [ ] Target maturity
* [ ] Assessment rationale
* [ ] Assessment status

### Phase 3 — Evidence & Improvement

* [ ] Evidence model
* [ ] Evidence linked to assessments
* [ ] Improvement actions
* [ ] Action ownership
* [ ] Action status
* [ ] Due dates
* [ ] Assessment change history

### Phase 4 — Reporting

* [ ] Organisation maturity dashboard
* [ ] AI system maturity dashboard
* [ ] Governance gap analysis
* [ ] Framework coverage reporting
* [ ] Maturity trends
* [ ] Risk/applicability analysis
* [ ] Exportable assessment reports

### Phase 5 — Advanced Capabilities

Potential future capabilities include:

* AI governance portfolio management
* Cross-system governance analysis
* Framework change tracking
* Automated evidence analysis
* AI-assisted assessment
* Recommended improvement actions
* Regulatory change monitoring
* Benchmarking
* Executive reporting

---

# Design Principles

## Framework agnostic

The application should not become a simple implementation of one particular AI governance framework.

External frameworks should be mapped onto a common governance model.

## Risk and context based

Not every control is equally relevant to every AI system.

Applicability should reflect the context, risk and potential impact of each system.

## Evidence based

Maturity ratings should ultimately be supported by evidence rather than subjective scoring alone.

## Lifecycle focused

Governance should apply across the AI lifecycle:

```text
Idea
 ↓
Use Case
 ↓
Design
 ↓
Development
 ↓
Deployment
 ↓
Operation
 ↓
Monitoring
 ↓
Change
 ↓
Retirement
```

## Continuous improvement

The objective is not simply to achieve a maturity score.

The platform should help organisations understand weaknesses, prioritise improvements and demonstrate progress over time.

---

# Project Structure

The project currently follows a standard Django structure:

```text
ai-governance/
│
├── manage.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── governance/
│   ├── migrations/
│   ├── management/
│   │   └── commands/
│   │       └── seed_reference_data.py
│   ├── admin.py
│   ├── models.py
│   └── ...
│
├── db.sqlite3
│
└── README.md
```

The application can be split into additional Django apps as the assessment, reporting and evidence capabilities grow.

---

# Status

**Early prototype / active development**

The current priority is establishing the reference governance model and core assessment data model before building a dedicated frontend.

The Django Admin interface is currently the primary UI for validating the data model and assessment workflow.

---

# Future Architecture

The intended architecture is:

```text
                    ┌─────────────────────┐
                    │     Next.js UI      │
                    └──────────┬──────────┘
                               │
                              API
                               │
                    ┌──────────▼──────────┐
                    │       Django        │
                    │     REST API        │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │     PostgreSQL      │
                    └─────────────────────┘
```

Django Admin will remain useful as an administrative interface for maintaining reference frameworks and managing system configuration.

---

# Contributing

The project is currently a prototype.

When adding or changing functionality:

1. Keep reference data separate from assessment data.
2. Avoid hard-coding framework-specific logic into assessment models.
3. Preserve assessment history rather than overwriting previous states.
4. Prefer explicit relationships between governance elements and external frameworks.
5. Keep maturity criteria versionable as the underlying governance model evolves.
6. Add tests as core assessment functionality is introduced.

---

# Licence

Licence to be determined.
