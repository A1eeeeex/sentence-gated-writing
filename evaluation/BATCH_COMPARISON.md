# Preliminary batch comparison — 2026-09-14

## Design and limits

Two fresh subagents received the same three task texts. One used an ordinary prompt without Skill/file access; the other read the writing Skill and was told to return complete prose without approval pauses. Both inherited the parent model; no model override was used. Exact backend revision, sampling seed, and token cost were not exposed. Each arm ran once, with three tasks in one thread. Source facts, language, length targets, and requested result were matched; incidental runtime context is not guaranteed identical.

The author reviewed results with arm identities visible. This is an unblinded, exploratory batch diagnostic, not a controlled estimate of general quality or of strict-mode human benefit. No human edits were made to the outputs below. No numerical quality score or significance claim is warranted.

## Inputs

T1: 中文，写一段80–120字项目汇报。材料：档案工具完成原型；在3个合成案例上通过字段提取测试；无真实门店上线；拟下月邀请2家门店试用；尚未测量节省工时。要求专业自然，清楚说明进度和下一步，只基于材料。

T2: English, write 60–90 words reporting pilot results. Source: eight volunteers used a prototype; mean task time was 20 minutes before and 15 minutes after; they did the same task twice; no control group; error rates not measured; no production release. Report findings and limitations, use only these facts.

T3: 中文，给同事一条不超过60字的消息：今天15点的会议改到明天10点，地点不变，请对方告知能否参加。语气日常，不添加理由。

## Raw ordinary-prompt outputs

T1: 档案工具已完成原型，并在3个合成案例上通过字段提取测试。目前尚未在真实门店上线，也未测量节省工时的情况。下一步拟于下月邀请2家门店试用，进一步了解原型在实际门店中的使用情况。

T2: Eight volunteers used the prototype, with mean task time falling from 20 minutes before use to 15 minutes after use. This represents a five-minute reduction in the observed average. However, participants completed the same task twice, and there was no control group, so the results do not establish that the prototype caused the improvement. Error rates were not measured, and the prototype has not been released to production.

T3: 今天15点的会议改到明天10点，地点不变。你看看能否参加，麻烦告诉我一声。

## Raw Skill outputs

T1: 档案工具已完成原型，并在3个合成案例上通过字段提取测试，目前尚未在真实门店上线，也未测量节省工时的情况。下一步拟于下月邀请2家门店试用，以了解工具在实际使用场景中的表现。

T2: Eight volunteers used the prototype, with mean task time falling from 20 minutes before use to 15 minutes after use. However, participants completed the same task twice, and there was no control group, so the observed difference cannot be attributed confidently to the prototype alone. Error rates were not measured, leaving the effect on accuracy unknown. These findings come from a prototype pilot; there has been no production release.

T3: 今天15点的会议改到明天10点，地点不变。你看能参加吗？麻烦回复一下。

## Observations

| Task | Both arms | Difference that matters |
| --- | --- | --- |
| T1 | Preserved prototype status, synthetic tests, no live rollout, planned invitation, and missing time measurements | No clear factual advantage; both add a reasonable but not explicitly sourced purpose for the pilot |
| T2 | Preserved sample, times, repetition, missing control, missing accuracy data, and absent production release | Ordinary prompt explicitly calculates the five-minute change; both avoid a causal conclusion |
| T3 | Kept the requested time change, unchanged location, and availability question | Stylistic difference only; no evident need for Skill overhead |

No material factual-fidelity advantage was observed in these three tasks. This is useful negative evidence: careful baseline instructions already handled these simple boundaries. Do not claim the Skill improved accuracy from this comparison. Its intended distinctive value—preserving accepted text and managing revisions across turns—still needs live multi-turn evaluation. No further rules were added in response to these known examples.
