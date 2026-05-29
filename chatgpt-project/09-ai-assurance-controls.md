# AI Assurance Controls

Apply when the artifact uses AI behavior in a way that affects decisions, users, workflow actions, or customer-facing outputs.

## Control areas

| Control | Use when |
|---|---|
| Eval set | Output quality or decision quality matters |
| Human review | AI suggests or triggers consequential actions |
| Prompt/version control | Behavior must be repeatable |
| Retrieval/data boundary | AI uses internal sources or knowledge bases |
| Logging | Decisions, prompts, outputs, or actions need traceability |
| Monitoring | Recurring use could fail silently |
| Rollback/kill switch | Bad behavior could affect operations or customers |
| Access control | Tool touches restricted data or systems |
| Cost guardrail | Usage could create material spend |
| Model/vendor review | External model behavior, terms, or retention matter |

## Output

For each AI-enabled artifact, state the minimum assurance controls needed for the recommended class. Avoid turning personal tools into production systems by accident.
