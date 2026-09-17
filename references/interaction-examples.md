# Interaction boundaries

These are synthetic illustrations, not evaluation results. Follow the user's language and task context.

## Strict start

User: “根据这些事实逐句写，确认一句再继续：原型已完成，只在两个案例上测试。”
Assistant: “这一段说明当前进度及验证范围。\n原型已完成，目前仅在两个案例上进行了测试。”
Then wait; do not provide the next sentence.

English trigger: “Write this sentence by sentence and wait for my approval.” Use the same workflow in English.

## Correction and continuation

Pending: “系统已在12家门店部署。”
User: “是两家，改一下再继续。”
Assistant: “系统已在两家门店部署。”
The correction replaces the candidate; wait for acceptance before advancing in Deliberate Drafting or explicitly strict mode.

## Full draft request

User: “不用一句一句确认，按材料直接写完整段落。”
Switch to batch, apply the checks internally, and produce the requested paragraph. Preserve previously accepted wording unless the user authorizes rewriting it.

## Evidence conflict after acceptance

Accepted: “系统已部署至12家门店。”
New authoritative record: “截至本周，仅2家完成部署；其余10家计划下月完成。”
Flag the accepted sentence and propose “截至本周，系统已在2家门店完成部署，其余10家计划于下月完成。” Do not call the old sentence verified because it was accepted.

## Review scope and latest draft

Old comment: “Do not claim all sites are deployed.”
Latest draft: “Two pilot sites are deployed; ten remain planned.”
Review the latest wording. Do not repeat the resolved deployment comment merely because it exists in the history.

## Non-triggers

“修正这句话的错别字。” / “Translate this greeting.” / “Make this casual caption less stiff.”
Handle as ordinary editing unless the user also requests this skill or its specific evidence/acceptance controls. Do not introduce a one-sentence approval loop.

## Understanding a human correction

Pending: “该平台打造了高效协同的数字化管理闭环。”
User: “我想讲的是以前各部门分别核对，现在先统一发现缺项，不是说它能处理所有问题。”
Assistant: “这句要说明核查方式的变化，不能扩大到问题处理。平台先统一检查材料缺项，供各部门后续核对。”
Only use the stated capability if supported by the task's facts. Apply the correction to later sentences; do not reintroduce automatic problem resolution in a summary.

## Explaining a choice without demanding acceptance

User: “为什么不直接写提高准确率？”
Assistant: “目前只知道几个案例通过测试，没有准确率对照。这里可以写测试范围；要写提高准确率，还需要对应的比较结果。”
Do not treat the question as acceptance or advance the next sentence.

## Direct invocation without specifying mode

User: “用 sentence-gated-writing 和我写报告的局限部分。仅六份访谈，都来自一个团队；没有对照。”
In default Deliberate Drafting, establish the limitations paragraph task and offer its first body sentence, then wait. If the user requests the complete limitations passage, use Accelerated Drafting instead. Do not force input/method/output onto limitations. Discuss a proposed effectiveness conclusion only if it exceeds these facts or its intended meaning remains unresolved.

## Existing-document substantive revision

User confirms that two runtimes use one shared configuration. Explain the original “same conditions and parameters” can mean duplicate manual inputs; propose “one shared structured configuration” with a concise before/after. This factual answer does not accept an unapproved candidate or establish identical runtime results. Integrate only under applicable edit authorization and inspect dependent architecture/summary passages.

## Local edit with outside effects

User: “这里只把‘发生概率’改成‘样本占比’，其它不改。”
Make that local change. If the conclusion still says “真实高发”, report its location and the unresolved mismatch; do not alter it without scope authorization or label the entire draft internally consistent.

## Review only

User: “对比原稿和专家修改稿，看看有没有把结论写大，先别改。”
Review the actual two versions against available evidence, distinguish error from missing support, and propose minimal repairs. Keep the canonical draft unchanged. If one version is absent, identify the comparison limit instead of inventing it.

## Reorganizing accepted text

If a locked background sentence describes an API, explain that the implementation detail belongs in detailed design and propose moving that exact sentence. In strict mode, wait for approval of the move; do not silently relocate it. A later “直接调整全文结构” authorizes structural editing within that scope.

## Resume with a stale note

Read the current artifact and latest source update before treating an old handoff as authoritative. If the author changed a pilot from three sites to two, preserve the new scope and any unrelated author additions. Close rejected pending wording, synchronize the compact note, and identify the current file in the handoff. Do not infer approval or factual truth solely from a file modification time.

## Complete-paragraph request from scattered material (A)

Facts: ratings record experience; recordings contain speed and acceleration; a paired dataset is planned; no model has been trained. User: “帮我写一段技术路线，没有现成结构。”
The explicit request for a complete paragraph authorizes Accelerated Drafting: write a passage that assigns each source a role, motivates pairing, and names the intended output. A planned dataset cannot become a trained predictor or a validated fusion system. Use a proposed interpretation only as such. Do not stop at an outline when useful prose is possible.

## Guided Revision: “这段感觉不对” (B)

Current text: “项目有人工评分、运动记录和配对数据三个模块。” Sources establish that records and ratings will be paired by trial ID to explore associations.
Assistant: “这里列了三项内容，但没有交代配对数据从哪里来、用于什么。我建议把关系写出来：项目拟按试验编号关联人工评分与车辆运动记录，形成配对数据，用于探索运动特征与体验评价之间的关系。”
This is a usable proposal with a reason, not a demand for all gate fields. Retain the planned status.

## Guided acceptance and skip (C–D)

There is one pending revision. User: “认可，继续。”
Integrate the accepted revision under the current scope, carry its meaning forward, then present the next substantive issue if one exists. Do not ask whether “认可” really means acceptance. In Review, “继续” authorizes continuing findings, not editing the draft.

User: “这个没必要，跳过。”
Retain the editorial scope decision and move on. If the skipped item is optional detail, do not bring it back as a differently worded suggestion. If it is a material factual conflict, leave its evidence status unresolved; neither repeatedly argue nor call it verified. After substantive issues are resolved, say further edits would be optional and stop.

## Correcting the purpose without the latest file (E)

Old agent interpretation: accuracy validation. User: “不是验证算法准确率，是验证技术可行性。我在 Word 里又改了一点，先不用传。”
Assistant: “明白，当前要说明流程是否可实施，而不是算法有多准。后面的方案、结果和总结都按这个目标组织。可以先写：本阶段以技术可行性为验证目标，围绕实施过程及其现有证据说明进展与限制。”
Ask for concrete source details only before stating particular steps were executed or passed. Keep the superseded interpretation out of later drafting. Do not claim Word was updated or refuse all useful work until it is uploaded.

## Detailed reliability procedures

Load for artifact integration, recovery, version conflicts or cross-document edits. These support the writing cycle; do not display them as a checklist.


Maintain the following only to the extent needed; do not create nine files or a sentence database:

| State | Retain |
| --- | --- |
| Document Intent | Current central task |
| Audience & Purpose | Reader, use, formality |
| Argument Spine | Main argument and support relationships |
| Section Contracts | What each section answers, excludes, and connects to |
| Fact Ledger | Consequential facts, source/version, scope, implementation/test status, uncertainty |
| Terminology Ledger | Current terms and definitions; superseded aliases when useful |
| Shared Understanding | Latest clarified meaning and goal, superseded interpretations, editorial skips and their scope; distinct from wording approval |
| Locked Decisions | Accepted decisions and scope; separately identify exact wording locks |
| Open Issues | Unresolved choice/conflict, affected locations, required evidence; close resolved issues |
| Canonical Draft | Current artifact/location, revision and scope, incomplete/unresolved status |

State records author decisions and sources, not hidden reasoning. Update affected state entries alongside each draft edit before reporting completion, including section-role summaries and open issues; do not defer reconciliation to final delivery. Do not reread every file or run full reviews on every turn. In a local edit, use only relevant state without creating new bookkeeping. If the author changes their goal explicitly, update intent rather than treating the original as immutable.

Integrate accepted changes and authorized routine edits into the current working draft. Keep pending high-impact alternatives separate. A current draft may contain incomplete sections or disputed passages, visibly identified as unresolved; it is not necessarily a final or fully approved draft. Preserve the complete available document, not merely the latest revised paragraph. At a milestone or handoff identify the current artifact, incorporated changes, remaining decisions, and next useful work. Recover exact accepted wording from the latest artifact if conversation state is unavailable; do not reconstruct it and call it accepted.

On recovery, read the identified current draft and its compact note; reconcile a stale note against the latest artifact and authoritative factual updates before editing. A newer draft is current wording, not automatic proof of a new fact or approval. If competing current files cannot be resolved from provenance, ask which is authoritative. Preserve recoverable work and clearly mark unresolved state instead of guessing.

Before writing, check that the current artifact has not changed since the relevant read. Preserve concurrent author edits and reconcile affected differences; do not overwrite them with a stale full copy. When persistence is unavailable or saving fails, say so and supply recoverable current text without claiming it was saved.

### Consequential change propagation


1. Identify what changed semantically and what scope the user authorized.
2. Search direct wording, old numbers/terms, aliases, and semantic dependents in the latest draft. Inspect relevant abstract, section claims, tables, captions, cross-references, discussion, and conclusion; literal search alone is insufficient.
3. Judge each affected passage. Update only necessary statements and derived conclusions, preserving unrelated wording. Retain valid historical mentions or distinct uses; do not blindly replace every match.
4. If the change conflicts with a locked decision or source, explain the conflict and resolve within authority. A “this sentence only” request does not authorize external edits: report affected locations and keep them as open issues. Do not silently imply consistency while dependencies remain unresolved.
5. Update the draft and applicable state, verify impacted relationships, and summarize substantive propagation results with locations. Distinguish changes made from proposals and checks that required no change.

### Latest-version review

Classify actionable findings as hard errors, credibility risks, or clarity/structure issues. Separate optional rigor from necessary corrections. For each consequential issue, identify the current passage, the reason, and the smallest useful remedy. Verify that the issue remains in the latest available draft; do not repeat resolved comments. If sources or the latest version are unavailable, state the review's limit instead of asserting an error.

Preserve the document's purpose. Do not demand academic completeness that would not change the engineering or practical conclusion. Fix substantive omissions even when they require restructuring.

## Structure-first drafting rhythms (current)

1. **Default:** User: “我们写这一段技术路线。” Given sufficient sources, briefly identify its task if useful, form an internal skeleton, and offer one body sentence. Wait for feedback; do not output the whole paragraph or only an outline. Ordinary sentences can reveal a difference in meaning without being high-risk claims.
2. **Direction correction:** Candidate: “该研究用于验证模型预测准确率。” User: “不是，是先验证方法可行性。” Update the paragraph task and shared purpose, offer a corrected candidate and wait. Future methods, result wording and conclusion must reflect feasibility, without claiming it was demonstrated if no test exists. This factual/intent clarification alone does not approve the corrected sentence.
3. **Accelerated:** User: “假设每句我都认可，直接生成完整章节。” Continue through skeleton, checked sentences, paragraph reviews and integration without pauses. Deliver a draft, not fictitious human acceptance records. Missing evidence still bounds the text.
4. **Paragraph review:** Five sentences were accepted, but 2 and 4 perform the same role. Explain “这两句在段内重复，我建议合并” and present the consolidated paragraph as a proposal in deliberate mode. Authorize any change to accepted technical meaning separately; preserve exact locks. Do not add a sixth sentence merely to keep the loop running.
5. **Guided Revision:** “认可，继续 / 下一个 / 这个没必要，跳过” retains the issue-based rhythm above. Do not switch it to sentence drafting. A local edit or review-only request likewise retains its scope.

The earlier examples and acceptance records reflect the modes stated in each task. Explicit requests for whole passages authorize Accelerated Drafting; an open-ended invitation to co-write an important paragraph defaults to Deliberate Drafting.
