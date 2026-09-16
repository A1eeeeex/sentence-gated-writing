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
The correction replaces the candidate; wait for acceptance before advancing in strict mode.

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
Draft the relevant limitations passage without asking for approval of its first routine sentence. Do not force input/method/output onto limitations. Discuss a proposed effectiveness conclusion only if it exceeds these facts or its intended meaning remains unresolved.

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
