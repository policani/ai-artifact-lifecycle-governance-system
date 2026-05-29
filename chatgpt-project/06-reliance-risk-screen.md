# Reliance Risk Screen

Use this screen to determine whether the business already depends on an artifact.

## Reliance indicators

| Signal | Interpretation |
|---|---|
| Used by one person only | Usually personal tool |
| Used by multiple people weekly | Team beta or supported candidate |
| Used in recurring operational process | Supported internal product candidate |
| Required for reporting, compliance, billing, customer response, delivery, or decision-making | High reliance |
| Writes to system of record | Elevated control need |
| Customers see output or experience downstream effect | Customer-facing promise candidate |
| No owner but recurring use | Unmanaged dependency |

## Output

For each artifact, state:

- current reliance level;
- likely impact if it fails;
- whether reliance is explicit or hidden;
- owner gap;
- route implication.
