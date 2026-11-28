# M3 - Security control reference map

**Status:** Framework mapping for design and later verification. It is not a certification or an audit result.

| Reference | Current edition checked 28 Nov 2026 | NORTHSTAR use |
|---|---|---|
| OWASP ASVS | Stable 5.0.0 | Select relevant application-security requirements, map controls to tests, record evidence and exceptions |
| OWASP API Security Top 10 | 2023 | Prioritize object-, function- and property-level authorization; authentication; resource limits; SSRF; configuration and upstream API risks |
| OWASP GenAI Security Project - LLM Top 10 | 2026 (published 4 Aug 2026) | Map prompt injection, sensitive information disclosure, improper output handling, excessive agency and other LLM risks to design/tests |
| NIST Cybersecurity Framework | CSF 2.0 | Organize governance, identify, protect, detect, respond and recover outcomes; do not treat the framework as a technical control checklist by itself |

## Implementation rule

- Select the assurance target and relevant ASVS requirements before M4 security tests are written.
- Map every applicable requirement to an implementation, test, owner and evidence record.
- Use the API Top 10 to drive negative authorization and API abuse tests.
- Use the GenAI 2026 guidance in later model threat and evaluation design; no clinical model functionality is enabled by this control map.
- Use NIST CSF 2.0 to organize the security programme, not to claim certification.

## Official references

- OWASP ASVS: https://asvs.owasp.org/ (stable 5.0.0; do not use the bleeding-edge branch as the fixed baseline)
- OWASP API Security Top 10 2023: https://api-security.owasp.org/editions/2023/en/0x00-header/
- OWASP GenAI Security Project / LLM Top 10 2026: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
- NIST CSF 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20


## Verification notes - 28 November 2026

- OWASP ASVS 5.0.0 remains the latest stable release. The OWASP repository's bleeding-edge branch is not the stable production baseline.
- OWASP GenAI LLM Top 10 2026 is published; its current risk categories include prompt injection, sensitive-information disclosure, excessive agency, supply chain, data/model poisoning, unbounded consumption, misinformation, hidden-context exposure, vector/embedding weaknesses and improper output handling.
- NIST CSF 2.0 is a risk-management outcomes framework, not a technical control checklist and not a certification.

References: https://owasp.org/projects/ASVS ; https://asvs.owasp.org/ ; https://genai.owasp.org/top-10-for-llm-applications-2026/ ; https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
