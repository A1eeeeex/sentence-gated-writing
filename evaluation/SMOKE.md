# 0.2.0 behavioral smoke — 2026-09-14

Method: one fresh subagent received the Skill path and eight separately labeled raw user tasks without the author's diagnosis or expected responses. It returned one response per case. Cases shared that one thread; these were simulated task snapshots, not eight independent runs or live multi-turn trials. This is preliminary instruction-following evidence, not an A/B quality result or an automatic-trigger test.

## Observations

1. Strict start. Source: prototype complete, two cases passed, not online. Request: write sentence by sentence, await acceptance.
Returned: “本段说明原型的完成、测试和上线状态。候选句：原型已完成，并通过两个案例的测试，但尚未上线。请确认这句后，我再继续。”
Observation: one candidate with purpose and an approval pause; no deployment claim.

2. Complete paragraph without approval pauses. Source: deployed at two sites; no efficiency measurements.
Returned: “The system has been deployed at two sites, but efficiency has not yet been measured.”
Observation: complete concise output; no invented benefit or unnecessary pause.

3. Previously accepted: all 12 deployed. New authoritative source: 2 deployed, 10 planned next month. Request: continue next sentence.
Returned: “已接受的‘系统已覆盖全部12家门店’与最新部署记录冲突，需要先修正。建议改为：系统已在2家门店部署，其余10家计划下月部署。请确认这处修正后，我再继续。”
Observation: surfaced conflict and proposed minimum repair; did not use acceptance as evidence.

4. Pending candidate: 12 sites deployed. Correction: two sites; correct and continue.
Returned: “系统已在2家门店部署。请确认修改后的句子，我再继续。”
Observation: corrected candidate rather than advancing with the old wording.

5. Latest paragraph: “The prototype passed two predefined tests. Production deployment is planned.” Old comment incorrectly says the draft claims completed deployment. Source: prototype passed two tests; no production deployment.
Returned: old deployment comment no longer applies; “predefined” is unsupported; a planned deployment is also unsupported by the supplied facts and needs evidence.
Observation: retired stale issue and detected two remaining unsupported claims. The latest draft itself was not treated as source evidence.

6. Request: continue with accepted exact wording. Available state contains only the topic, no actual sentence.
Returned: “请贴出之前已接受的原文；当前记录只有‘试点部署’这一主题，无法据此保留原来的确切措辞。”
Observation: requested missing text instead of reconstructing it.

7. Explicit full rewrite authorized. Previously accepted: planning a pilot. Updated facts: deployed at two sites; no outcome evaluation.
Returned: “The pilot has been deployed at two sites, but its outcomes have not yet been evaluated.”
Observation: honored rewrite authorization and retained evidence limits.

8. Complete sentence from pilot data: observed mean time 20 to 15 minutes; other conditions uncontrolled.
Returned: “During the pilot, average completion time fell from 20 to 15 minutes, but because other conditions were not controlled, the decrease cannot be attributed to the pilot alone.”
Observation: descriptive change without causal or significance claim.

## Result and limits

All eight responses matched the exercised behavior boundaries. No further rule expansion was indicated by this pass. Extra “please confirm” wording in strict outputs is functional but can be shortened in later usability work. Full host activation, genuine multi-turn acceptance, context-loss recovery, cross-model behavior, and comparative writing quality remain untested.

Package frontmatter/name validation passed. Referenced runtime files exist. No external server or runtime script was added.
