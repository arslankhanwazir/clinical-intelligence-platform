# Clinical and regulatory desk-research notes for M2

**Research date:** 28 November 2026.
**Status:** Candidate sources and regulatory flags only. None of these sources is approved for product rules, model training, ingestion, transformation or commercial software use by this document.

## Pakistan regulatory boundary

- DRAP's published "Is It a Medical Device?" page says the medical-device definition includes software when the manufacturer's intended purpose is one of the specified medical purposes, including diagnosis, prevention, monitoring or treatment of disease.
- DRAP's published risk-classification page describes four risk classes (A-D), with classification based on potential harm, intended use and technologies.
- This product's class, SaMD status, registration/licensing obligations and pathway are **not determined** here. The intended purpose in `docs/product/intended-use-draft.md` must be reviewed by qualified regulatory counsel and the appropriate DRAP route in M2.

## Hypertension guideline candidates for clinician review

1. **4th National Hypertension Guidelines (2023)** - the PHL-hosted PDF identifies the publication as *JPMA* 2023;73(Suppl 7):S1-78 and labels the issue Vol. 73 No. 8 (Suppl. 7), August 2023. The JPMA archive landing page is titled Vol. 73 No. 7 (2023), so the issue-number metadata is inconsistent between the landing page and the PDF. Treat the PDF as a candidate only; confirm the authoritative citation/version, corrections, current status and commercial-use permissions directly with PHL/JPMA before any reuse.
2. **WHO Guideline for the pharmacological treatment of hypertension in adults (2021)** - the WHO page says it targets adults who are non-pregnant, appropriately diagnosed with hypertension and counselled about lifestyle modifications; it includes pharmacological treatment initiation, follow-up intervals and targets. It is not automatically a complete primary-care follow-up rule source.
3. **2024 ESC Guidelines for elevated blood pressure and hypertension** - useful as an international comparator, but ESC states commercial use is not allowed and reuse in software, algorithms or AI/ML requires a formal licence agreement. Do not copy or transform content into product logic without written permission.
4. **2025 AHA/ACC adult high-blood-pressure guideline** - current U.S. guideline candidate for international comparison only; not the default Pakistan policy source without a clinician's jurisdictional decision.

## Source governance questions for M2

- Which guideline is authoritative for the specific pilot site and clinician population?
- Does the source apply to follow-up of previously diagnosed adults, not only diagnosis or medication initiation?
- Are there special populations or exclusions (pregnancy/postpartum, paediatric, frailty, comorbidity, secondary causes, emergencies) requiring abstention or separate handling?
- What exact permissions permit commercial software use, reproduction, extraction, indexing, transformation and algorithm development?
- What version/effective date, update-check interval and withdrawal process apply?
- Who signs off each source and each derived rule pack?

## Sources checked

- DRAP, Is It a Medical Device? (last updated 1 July 2025): https://www.dra.gov.pk/therapeutic-goods/medical-devices/is-it-a-medical-device/
- DRAP, Risk Classification (last updated 22 February 2022): https://www.dra.gov.pk/therapeutic-goods/medical-devices/risk-classification/
- Pakistan Hypertension League, Guidelines: https://phlpk.org/guidelines/
- PHL-hosted PDF of 4th National Hypertension Guidelines: https://phlpk.org/wp-content/uploads/2024/05/phlpk2134231324444444444444_compressed.pdf (PDF cover/citation states JPMA 2023;73(Suppl 7):S1-78 and Vol. 73 No. 8 (Suppl. 7)).
- JPMA archive landing page titled Vol. 73 No. 7 (2023): 4th National Hypertension Guidelines: https://jpma.org.pk/index.php/public_html/issue/view/57 (metadata discrepancy to be resolved with publisher).
- WHO, Guideline for the pharmacological treatment of hypertension in adults (24 August 2021): https://www.who.int/publications/i/item/9789240033986/
- ESC, 2024 Guidelines for elevated blood pressure and hypertension (includes explicit reuse/licensing terms): https://www.escardio.org/guidelines/clinical-practice-guidelines/all-esc-practice-guidelines/elevated-blood-pressure-and-hypertension/
- AHA/ACC et al., 2025 adult high-blood-pressure guideline: https://www.ahajournals.org/doi/10.1161/CIR.0000000000001356
