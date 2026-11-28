# ADR-0005: Bounded model gateway; local/private inference direction

**Status:** Accepted by product owner as a design decision; implementation and independent verification pending.
**Date:** 28 November 2026.

## Context

The model must not become the system of record, authorization engine, clinical policy engine or audit authority. Data protection and patient privacy constrain inference location and providers.

## Accepted design decision

- Create a provider-agnostic model gateway; avoid coupling product modules to one model vendor.
- Local/private inference is the preferred direction for any later sensitive-data workflow.
- During current development, synthetic data only. No external model receives patient information.
- No model is enabled for clinical outputs until M2 sources/intended use and M8 verification gates are met.
- Model tools are disabled by default; no unrestricted SQL, shell, network, database write or EHR write-back.
- Require schema-constrained output, source-linked evidence, verifier checks and abstention; output remains a draft for clinician review.
- Record provider/model version, prompt version, settings and evaluation result for each draft, without logging unnecessary clinical content.

## Current workstation observation

The owner previously ran `ollama list` and the command returned an empty model list. Therefore the documents must not assume that an Ollama model is currently downloaded or available. Model availability and resource suitability must be checked at the M8 stage.
