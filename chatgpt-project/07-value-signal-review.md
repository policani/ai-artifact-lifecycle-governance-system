# Value Signal Review

Value evidence should be proportional to class. Do not require heavy ROI for personal tools or team betas. Require stronger proof when promotion creates support obligations.

## Value signal levels

| Level | Description |
|---|---|
| Unknown | No usable evidence yet |
| Weak | Convenience or preference only |
| Anecdotal | User stories but no pattern |
| Directional | Repeated use, plausible savings, quality signal, or workflow pull |
| Strong | Measured impact, adoption, risk reduction, revenue/cost/retention/quality evidence |

## Questions

- What problem does the artifact solve?
- Who uses it without being forced?
- What manual work does it replace or improve?
- Is the workflow close to money, trust, retention, delivery, compliance, or executive decision quality?
- Is the artifact solving a local convenience issue or exposing a missing platform capability?
- What proof would justify promotion?
- If the artifact is promoted or formalized, what measurement contract should travel with it: expected outcome, benefit type, metric, baseline, target, actual if available, measurement period, source, measure owner, review cadence, validation need, confidence, realization risk, finance-sensitive flag, and downstream route?

## Support burden versus value screen

Before promote or formalize, compare value signal to operating obligation:

| Dimension | Question |
|---|---|
| User pull | Who uses it repeatedly without being forced? |
| Value signal | Is value measured, directional, anecdotal, weak, or unknown? |
| Reliance | What business process or decision now depends on it? |
| Data / systems touched | What data, systems, permissions, or records does it touch? |
| Owner readiness | Who owns support, changes, access, exceptions, and retirement? |
| Maintenance effort | What prompt, model, data, connector, documentation, or control upkeep is required? |
| Training / support | Who needs guidance, support path, or onboarding? |
| Failure cost | What happens if output is wrong, stale, unavailable, or misused? |
| Control requirements | What assurance, logging, privacy, security, or approval controls are needed? |
| Formalization route | Stay personal, team beta, promote, formalize, demote, retire, or route to another module? |

## Value Signal Calibration

Published deployments help calibrate where an artifact sits on the signal scale. Use these to pressure-test a rating — not to claim a specific outcome for your artifact.

**Anecdotal → Directional:**
A customer service AI copilot showed anecdotal value (agents reported finding answers faster) within days of deployment. It moved to directional when repeated use patterns and quantitative agent ratings were collected consistently over several weeks of staged rollout. (McKinsey, European telecom, 2024)

**Directional → Strong:**
A developer code-completion tool moved from directional (developers reported saving time on boilerplate) to strong after a controlled study tracked task completion time (2h41min → 1h11min, 55.8% faster) and a field study across 1,974 developers confirmed 12–22% more pull requests per week. Both required defined baselines, controlled conditions, and tracked actuals before the signal was classified as strong. (GitHub Copilot, Microsoft/Harvard, 2023; Communications of the ACM)

**Strong with finance validation:**
JPMorgan's COiN contract review model reached a strong value signal only after multi-year operation with a tracked baseline (~360,000 lawyer-hours/year), measured actuals (same document volume processed in seconds), and documented error rate reduction (~80%). Finance-sensitive savings were validated against the prior staffing model before investment language was used publicly. (JPMorgan, publicly documented, launched 2017)

**Published range anchors by benefit type (for calibration only):**

| Benefit type | Illustrative published range | Context |
|---|---|---|
| Document review cycle time | 45–90% reduction | JPMorgan COiN; Sirion enterprise redlining data (2024) |
| Decision memo production | 30% faster; 2× productivity | McKinsey (2024), North American bank multiagent credit memo system |
| Knowledge retrieval handle time | 30–65% reduction | McKinsey (2024), European telecom service agent copilot |
| Knowledge worker task speed | 12–56% faster | GitHub Copilot controlled study (55.8%) vs. field study (12–22% more output/week) |
| Meeting and documentation overhead | 1–4+ hours/person/week | Otter.ai survey (2024, n=600); varies by meeting load |
| Project on-time delivery | 15–30% improvement | PMO forecasting tools, published 2024–2025 |

**What prevents a signal from reaching Strong:**
- Benefit claimed without a measured baseline
- Adoption reported without connecting to a workflow outcome
- Time savings estimated but not tracked or owned
- Finance-sensitive claim without finance validation
- AI output credited for value created by process cleanup or staffing changes (AI washing)

If a Directional or Strong rating is asserted but the measurement contract fields are empty, downgrade the signal until they are filled.

## Output

State whether the artifact has enough value evidence for its recommended class.
For team beta, promote, or formalize routes, include a provisional measurement
contract and support-burden summary when a value claim exists. Do not require
heavy ROI for lightweight use, and do not certify finance-sensitive value
without explicit human finance validation.
