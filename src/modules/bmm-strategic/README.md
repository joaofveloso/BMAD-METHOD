# BMM-Strategic Module

Strategic leadership agents for SaaS product development. This module provides AI-powered strategic guidance through specialized agents covering vision, market strategy, compliance, UX, and growth.

## Overview

The BMM-Strategic module sits at the **strategic layer** of the BMAD framework, providing high-level guidance that flows down to tactical (PM, Architect) and execution (Dev, QA) layers.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           STRATEGIC LAYER                                    │
│                          (bmm-strategic)                                     │
│                                                                             │
│  🚀 Founder          ☁️ SaaS Specialist    📈 Market Strategist             │
│  🛡️ Compliance       🎯 UX Strategist      🔬 Growth Engineer                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                          Events + Priorities
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           TACTICAL LAYER (bmm)                               │
│  📋 Product Manager   🏗️ Architect          👨‍💼 Scrum Master                  │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          EXECUTION LAYER                                     │
│  ☕ Backend Dev       ⚛️ Frontend Dev       🧪 QA Engineer                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Agents

### 🚀 Founder Agent
**Role:** Visionary Product Leader

The Founder agent drives product vision, strategic priorities, and major decisions.

**Key Capabilities:**
- Define and refine product vision
- Set quarterly strategic priorities
- Make go/no-go decisions on initiatives
- Evaluate pivot opportunities
- Generate investor updates

**Commands:**
- `*vision` - Define product vision
- `*priorities` - Set strategic priorities
- `*decide` - Go/no-go decision framework
- `*pivot` - Evaluate pivot opportunities
- `*quarterly` - Quarterly planning

---

### ☁️ SaaS Specialist Agent
**Role:** SaaS Domain Expert + Platform Architect

Deep expertise in SaaS business models, multi-tenancy, pricing, and subscription economics.

**Key Capabilities:**
- Design multi-tenant architecture
- Define pricing strategy and tiers
- Design user onboarding flows
- Set up SaaS-specific KPIs
- Plan integration strategy

**Commands:**
- `*tenancy` - Design multi-tenant architecture
- `*pricing` - Define pricing strategy
- `*onboarding` - Design onboarding flow
- `*saas-kpis` - Define SaaS metrics
- `*integrations` - Plan integration strategy

---

### 📈 Market Strategist Agent
**Role:** Competitive Intelligence + Growth Strategist

Focused on market dynamics, competitive positioning, and growth opportunities.

**Key Capabilities:**
- Analyze competitors
- Define market positioning
- Create ideal customer profile (ICP)
- Identify market opportunities
- Go-to-market strategy

**Commands:**
- `*competitors` - Competitor analysis
- `*positioning` - Market positioning
- `*icp` - Ideal customer profile
- `*trends` - Market trends analysis
- `*gtm` - Go-to-market strategy

---

### 🛡️ Compliance Officer Agent
**Role:** Security + Privacy + Regulatory Guardian

Ensures compliance with GDPR, SOC2, and other regulatory frameworks.

**Key Capabilities:**
- GDPR compliance assessment
- SOC2 audit preparation
- Data flow mapping
- Security risk assessment
- Policy management

**Commands:**
- `*gdpr` - GDPR assessment
- `*soc2` - SOC2 preparation
- `*data-map` - Data flow mapping
- `*risk` - Security risk assessment
- `*policies` - Policy review

---

### 🎯 UX Strategist Agent
**Role:** User Experience + Retention Specialist

Focused on user experience, retention, and product stickiness.

**Key Capabilities:**
- User journey mapping
- Friction analysis
- Retention analysis
- Usability testing
- Persona development

**Commands:**
- `*journey` - User journey mapping
- `*friction` - Friction analysis
- `*retention` - Retention analysis
- `*usability` - Usability testing
- `*personas` - Persona development

---

### 🔬 Growth Engineer Agent
**Role:** Growth Hacker + Analytics Expert

Data-driven growth through experimentation and funnel optimization.

**Key Capabilities:**
- Funnel analysis
- Experiment design
- Analytics setup
- Activation optimization
- Growth modeling

**Commands:**
- `*funnel` - Funnel analysis
- `*experiment` - Design experiments
- `*analytics` - Analytics tracking plan
- `*activation` - Activation optimization
- `*north-star` - Define north star metric

---

## Event Integration

The strategic module integrates with other BMAD modules through events:

### Events Published

| Event | Agent | Description |
|-------|-------|-------------|
| `vision.defined` | Founder | Vision has been defined |
| `priority.set` | Founder | Priorities have been set |
| `decision.go` | Founder | Go decision on initiative |
| `saas.pricing.defined` | SaaS Specialist | Pricing strategy defined |
| `market.positioning.defined` | Market Strategist | Positioning defined |
| `compliance.flag.raised` | Compliance | Compliance issue identified |
| `ux.friction.identified` | UX Strategist | Friction point found |
| `growth.experiment.completed` | Growth Engineer | Experiment finished |

### Events Subscribed

| Event | Source | Handlers |
|-------|--------|----------|
| `metrics.kpi.updated` | bmm-metrics | Founder, Growth Engineer |
| `feedback.insight.generated` | bmm-feedback | Founder, UX Strategist |
| `roadmap.at.risk` | bmm-roadmap | Founder, Market Strategist |
| `release.deployed` | bmm-release | Growth Engineer, Compliance |

---

## Installation

The module is installed via the BMAD installer:

```bash
npm run bmad:install
# Select bmm-strategic when prompted
```

### Dependencies

- **Required:** `core` (>=1.0.0)
- **Optional:** `bmm`, `bmm-metrics`, `bmm-feedback`, `bmm-roadmap`

---

## Configuration

After installation, configure the module in `.bmad/bmm-strategic/config.yaml`:

```yaml
company:
  name: "Your Company"
  stage: "mvp"  # idea, mvp, growth, scale, mature

vision:
  statement: "Your vision statement"
  mission: "Your mission"

market:
  segment: "smb"  # smb, mid-market, enterprise, consumer
  competitors:
    - "Competitor A"
    - "Competitor B"

compliance:
  frameworks:
    - "gdpr"
    - "soc2"

growth:
  north_star:
    metric: "Weekly Active Users"
    target: "10000"
```

---

## Quick Start

1. **Install the module**
   ```bash
   npm run bmad:install
   ```

2. **Activate the Founder agent**
   ```
   /bmad:bmm-strategic:agents:founder
   ```

3. **Define your vision**
   ```
   *vision
   ```

4. **Set priorities**
   ```
   *priorities
   ```

5. **Make decisions**
   ```
   *decide
   ```

---

## Workflow Examples

### Strategic Planning Flow

```
Founder: *vision
    → Define product vision
    → Events: vision.defined

Founder: *priorities
    → Set Q1 priorities
    → Events: priority.set
        → Market Strategist: Update competitive focus
        → Growth Engineer: Align experiments
        → UX Strategist: Prioritize research

SaaS Specialist: *pricing
    → Define pricing tiers
    → Events: saas.pricing.defined
        → Market Strategist: Update positioning
        → Growth Engineer: Update revenue model
```

### Compliance Review Flow

```
Compliance: *gdpr
    → Run GDPR assessment
    → Events: compliance.assessment.completed

If gaps found:
    → Events: compliance.flag.raised
        → Founder: Review strategic impact
        → Blocks release if critical
```

### Growth Experimentation Flow

```
Growth Engineer: *funnel
    → Analyze conversion funnel
    → Identify bottleneck
    → Events: growth.funnel.analyzed

Growth Engineer: *experiment
    → Design A/B test for bottleneck
    → Events: growth.experiment.proposed

After experiment runs:
    → Events: growth.experiment.completed
        → Founder: Review learnings
        → UX Strategist: Incorporate findings
```

---

## Best Practices

### 1. Start with Vision
Always begin with the Founder agent to establish vision and priorities before diving into details.

### 2. Regular Compliance Checks
Run compliance assessments before major releases and quarterly regardless.

### 3. Data-Driven Decisions
Use Growth Engineer to quantify impact before making major product decisions.

### 4. User-Centric Design
Engage UX Strategist early in feature planning, not just for polish.

### 5. Market Awareness
Regularly update competitive intelligence via Market Strategist.

---

## Integration with Distributed Teams

For teams using SMTP/Git communication with remote contractors:

1. Strategic decisions flow down as prioritized work items
2. Compliance requirements become story acceptance criteria
3. UX requirements inform design specs
4. Growth metrics define success criteria

```
Strategic Layer (you)
    │
    ├── Vision & Priorities
    ├── Compliance Requirements
    ├── UX Guidelines
    └── Success Metrics
    │
    ▼ (via SMTP/Git)

Execution Layer (contractors)
    │
    ├── Receive: Story specs with strategic context
    ├── Deliver: Code via Git PRs
    └── Report: Status via SMTP
```

---

## File Structure

```
bmm-strategic/
├── manifest.yaml              # Module definition
├── config.yaml                # User configuration
├── README.md                  # This file
├── agents/
│   ├── founder.agent.yaml
│   ├── saas-specialist.agent.yaml
│   ├── market-strategist.agent.yaml
│   ├── compliance-officer.agent.yaml
│   ├── ux-strategist.agent.yaml
│   └── growth-engineer.agent.yaml
├── events/
│   ├── publications.yaml      # Events this module publishes
│   └── subscriptions.yaml     # Events this module listens to
├── workflows/
│   ├── define-vision/
│   ├── set-priorities/
│   ├── pricing-strategy/
│   └── ... (other workflows)
├── state/
│   └── module-state.yaml      # Runtime state
└── docs/
    └── ... (additional documentation)
```

---

## Version History

- **1.0.0** - Initial release with 6 strategic agents

---

## Contributing

When extending this module:

1. Follow the agent YAML schema
2. Define events in publications.yaml
3. Register handlers in subscriptions.yaml
4. Update this README
5. Add workflow documentation
6. **Follow the [Verification Protocol](../../core/docs/verification-protocol.md)**

---

## Verification Protocol

All bmm-strategic agents and workflows must follow the **[Verification Protocol](../../core/docs/verification-protocol.md)**.

- Never claim success without actual verification
- Distinguish between "configured" and "confirmed working"
- Test end-to-end flows, not just individual components
- Report clearly what was verified vs. what remains untested
