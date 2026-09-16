# Sentence-Gated Writing

在多轮协作中，让每次修改进入同一份当前稿，并保持全文事实、意图和论述一致。

Collaborate on formal long documents while maintaining the argument, evidence, terminology, accepted decisions, and one current draft across revisions.

**Sentence Gate is a verification boundary for high-impact statements, not the default unit of writing.** 默认根据问题选择全文、章节、段落、句子或局部修改。关键含义尚未确定时才展开讨论；有明确依据和授权时继续推进，不让用户逐句点头。

## Who and when

For authors, researchers, and project owners developing papers, technical reports, or substantial proposals through multiple revisions. Useful when a changed definition, result, or conclusion affects other parts of the document. It is not a universal proofreader, humanizer, automatic paper generator, research service, or independent review system.

“帮我修改这份报告，保留成立的结构；解释有实质影响的修改，更新当前稿，并同步受影响的摘要和结论。”

“把这个定义改成问题样本频率，并检查正文、表格和总结有没有仍按真实道路概率来解释。”

For a simple local correction, do just that. Explicit sentence-by-sentence, complete-draft, and review-only requests remain supported. Red-team review is opt-in. Do not treat a factual clarification as approval of a candidate rewrite.

## What the workflow maintains

A current document intent, argument and section roles, consequential facts and terms, accepted decisions, unresolved issues, and the canonical draft. Use one working document and an optional compact note, not a large administrative system. Explain substantive changes with relevant before/after text and a reason. Propagate authorized semantic changes to dependent passages while preserving unaffected wording.

The current draft may have visible unresolved items; it is not automatically a final or human-approved document. Respect local-only instructions and mark dependencies that remain inconsistent. Actual persistence depends on host tools; the Skill is a writing protocol, not a database or autonomous document monitor.

## Core and profile

Core governs coherence, facts, author intent, adaptive scope, sentence verification, propagation, and current-draft integrity. The optional [Technical / Analytical Writing Profile](references/technical-structure.md) contains existing technical-structure and engineering-expression guidance. Apply input/method/output only where it helps. Other specialized profiles are not implemented.

Read [Product Definition v1](PRODUCT_DEFINITION.md) for scope, decisions, and five task walkthroughs. Professional quality means clear purpose, responsibilities, evidence boundaries, and relationships; adding jargon is not a goal.

## Evidence

Ordinary chat can also perform these actions. The intended benefit is consistent execution across turns, not exclusive model capability. Prior short or scripted-feedback comparisons did not establish a clear quality or effort advantage. Historical [technicalization checks](evaluation/TECHNICALIZATION.md) used the previous default and are not the current product specification. See [evaluation plan](evaluation/PLAN.md) and [current behavior evidence](evaluation/PRODUCT_STATE.md). Human benefit and long-document comparative reliability remain unproven.

Development base 0.5.0; Product Definition v1 update 2026-09-16. Number unchanged. MIT; see [LICENSE](LICENSE). No runtime dependencies. Explicit-loading behavior tests do not prove automatic discovery or all-host compatibility.

## Try the candidate

Download the candidate branch as a ZIP, or clone this repository and select that branch. The skill entry point is the root `SKILL.md`; retain `references/` beside it. In a host that loads local skills, add this folder using that host's skill installation mechanism and explicitly invoke `sentence-gated-writing` for the first trial. Host-specific installation and automatic triggering have not been validated here.

Start with an existing document and say what may change. For example: “更新这份报告中的定义，并同步受影响的正文和结论；保留其它内容，交付完整当前稿。” Supply source material when a claim needs checking. You do not need to prepare the internal state fields yourself.

Supported guidance: adaptive editing, scoped change propagation, selective fact/intent discussion, and recoverable current-draft handoffs. Not provided: an independent database, continuous background monitoring, guaranteed fact verification, or an automatic research/format-conversion service. Document rendering and storage depend on the host.

Latest candidate checks and reproducible synthetic inputs: [development acceptance](evaluation/ACCEPTANCE.md). This is a review candidate, not evidence of better writing or lower human effort. No GitHub Release tag is implied by the development version.

Maintainers can check packaging with `python3 tools/check_package.py`. The script checks structure and links only.
