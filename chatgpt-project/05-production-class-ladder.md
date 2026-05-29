# Production Class Ladder

## Class 1 — Personal Tool

One person uses it for personal productivity.

Minimum standard:
- owner known;
- no unsupported sensitive data handling;
- no shared business dependency;
- no customer-facing promise;
- user understands it is personal and unsupported.

## Class 2 — Team Beta

A small group uses it to test usefulness.

Minimum standard:
- owner and backup owner;
- short description;
- users known;
- systems touched known;
- data sensitivity known;
- basic failure plan;
- clear statement that it is beta/not production.

## Class 3 — Supported Internal Product

The business relies on it internally.

Minimum standard:
- named product/business owner;
- platform or technical partner where needed;
- access management;
- documentation;
- monitoring or usage review;
- support path;
- change process;
- auditability appropriate to risk;
- funding/capacity model if support is non-trivial.

## Class 4 — Customer-Facing Promise

The artifact affects external users, customers, contractual commitments, revenue, brand trust, or customer data.

Minimum standard:
- full product ownership;
- security/privacy/legal/architecture review as applicable;
- AI evals where AI behavior affects outcomes;
- release controls;
- support model;
- rollback/kill switch;
- customer communication model where applicable;
- executive acceptance of material risk.

## Classification rule

Class by actual reliance and exposure, not by how informal the artifact looks.
