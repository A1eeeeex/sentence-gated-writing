# Claim and review checks

Use for difficult passages; do not display a checklist for every sentence.

## Evidence is separate from approval

“Looks good” accepts wording. “The deployment log confirms 12 sites as of 5 September” supplies a factual statement with scope. Neither a polished sentence nor its repetition creates new evidence. Where sources disagree, retain the conflict until the authoritative source or user clarification resolves it.

## Three independent claim dimensions

| Dimension | Ask | Avoid |
| --- | --- | --- |
| Implementation | Is this planned, designed, implemented, or deployed, and where? | Turning “拟上线” into “已上线” |
| Validation | What was measured, on which cases, with which limits? | Treating deployment or a demonstration as validation |
| Conclusion | Is there evidence for comparison, causality, significance, or generalization? | Turning “tested” into “significantly better” |

Do not order these dimensions as a single ladder. A prototype may be tested before deployment. A deployed system may have no comparative evaluation.

Examples:

- Source: “Deployed at two sites; effectiveness has not been measured.” Write: “The system has been deployed at two sites; its effectiveness has not yet been measured.” Do not claim improved efficiency.
- Source: “Mean completion time was 20 minutes before and 15 after in a pilot; other conditions were not controlled.” Describe the observed reduction within the pilot. Do not attribute it wholly to the system or claim statistical significance.
- Source: “计划明年扩展至全部门店。” Keep the future status; do not write that all stores already use it.

## Fact detail

Check units, denominators, time windows, sample boundaries, variable definitions, formula indices, and table labels when relevant. Distinguish partial from all, example from proof, association from causation, and a source-specific statistic from population prevalence. Name missing evidence precisely rather than adding vague disclaimers.

## Logic and expression

Ask what each sentence adds and why it appears here. Remove premises and conclusions repeated with no new role; preserve a recurring document thread when each occurrence serves a different purpose. Introduce a metric before interpreting its value. Keep the method understandable before adding implementation details. Prefer observable actions and exact objects over impressive abstractions; preserve domain terms that carry real meaning.

## Review triage

First check that the issue still exists in the active draft. Distinguish a demonstrable error from absent evidence, ambiguity, and optional rigor. Change only what improves the document's intended explanation or trustworthiness.

## Precise claims and placement

Narrow claims before weakening language: state the observed object and conditions rather than adding “一定程度上”. Keep real uncertainty and planned status. “Designed to replay recorded positions” does not mean validated dynamics, and observed frequencies in selected problem samples are not road occurrence probabilities. A method design is not an implemented resource allocator.

A connector must reflect evidence: sequence alone does not establish causation. Enumerations must fit their parent statement and use comparable levels. Keep function names and interpolation rates in detailed design when they distract from the background question. Technical paragraph and section checks are in [technical-structure.md](technical-structure.md); they never override factual constraints or accepted-text permissions.

## Intent conflict and propagation

Treat the user's intended meaning as a writing requirement, not evidence that the conclusion is true. Explain a source/intent conflict and offer a supported scoped claim. Acceptance of a candidate and factual clarification are distinct acts. A definition change requires inspection of dependent summaries and conclusions, not only replacing its name. Core SKILL.md defines propagation permissions and current-draft handling; technical profile checks do not override them.
