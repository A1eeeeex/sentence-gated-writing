# Development acceptance — 2026-09-16

Candidate status: bounded behavior acceptance completed; not a general writing-effectiveness benchmark. Two fresh agents loaded SKILL.md and needed references, without parent context, evaluation records or expected answers. Four actions were executed in two sessions. Parent inspected files/diffs and focused assertions after completion. Inputs are synthetic; no confidential user report is published. The larger fixture has nine sections and about 1,289 Chinese characters: it tests distributed dependencies, not full-length paper scale.

## Findings and fixes

The product-state trial had observed temporarily stale working notes. Core now requires updating affected note entries before reporting each revision complete. Recovery now explicitly reconciles current artifacts, authoritative factual updates, and handoff provenance. This is a procedural fix, not a new gate or a guarantee that agents cannot drift.

## Observed acceptance

| Action | Result and evidence |
| --- | --- |
| Distributed data and plan update | Abstract, source scope, formula, table, caption and conclusion updated; prose fractions changed to one fifth; unrelated sections and historical 25% example preserved |
| Local-only definition change | Exact file comparison shows only the definition sentence changed; missing form-specific data was not invented; external implications recorded as unresolved |
| Recovery from stale note | Kept current 2-site/5-person plan and author-added date constraint, discarded old 3-site/6-person note and rejected unsupported pending claim |
| Review only | Identified source and author-intent conflicts in a proposed expert rewrite; current document remained unchanged |

The local-only result intentionally remains internally inconsistent until the author authorizes wider propagation and supplies the missing counts. The agent did not label it a coherent final document. Flagging an unresolved dependency is not completed propagation.

## Limits

No blind comparison, real user effort measurement, automatic activation test, multi-host installation test, formatted DOCX caption test, external concurrent-write race, or long-session context-limit test was performed. Prior six-round regression remains separate evidence. Do not advertise improved writing quality, expert superiority, or guaranteed consistency. One successful recovery case cannot establish general recovery reliability.

## Reproduction inputs and observed artifacts

Load this candidate explicitly in a fresh agent. Give only the applicable raw inputs and user requests below, not this results table. Use independent work directories. Retain changes and responses; inspect sources and semantic dependencies rather than only string counts.

### Propagation input current.md

# 设施巡检记录与试点方案

## 摘要
本报告说明巡检记录的整理方法与有限范围试点安排，不作全面部署决策。
本次资料包含80份上报记录，其中20份存在字段缺失，缺失记录占比为25%。这一比例描述所收集样本，不代表全部设施的问题发生概率。试点拟覆盖3个站点，持续两周。

## 背景与读者任务
维护团队希望了解记录中的字段是否足以支持后续人工核查。过去各站点分别保存记录，格式不同，无法直接比较同一字段的填写情况。本项目先对既有记录进行整理，再通过有限试点观察整理流程能否顺利运行。本文的读者需要判断现有材料是否足以开展试点准备，而不是依据少量记录批准所有站点上线。
资料仅来自主动上报，未纳入没有上报的设施，因此不能据此估计总体故障率。字段缺失也不等于设备存在故障，两者必须分别解释。后续若需要讨论总体分布，应另行建立明确的抽样范围。

## 资料范围
收集的80份记录均用于本次字段统计。原始表保留上报时间和来源站点，整理时不覆盖原始表。20份记录至少有一个必填字段为空；同一份记录缺失多个字段时，在记录级统计中仍只计一次。
历史方法演示曾使用8份虚构记录，其中2份缺失，演示比例为25%；该演示不属于当前实测样本。本节保留历史演示，是为了让读者理解分母与计数对象的区别，而不是作为效果验证。

## 定义与计算
“缺失记录占比”指至少存在一个必填字段缺失的记录数除以本次纳入统计的记录总数。当前计算为20/80=25%。统计单位为记录，不是设备，也不是缺失字段数量。
整理人员先统一字段名称，再按同一规则判断字段缺失，最后保留原始值与判定结果之间的对应关系。发现来源冲突时应返回原始记录核对，不能通过修改统计规则使数据看起来更完整。当前流程依赖人工核查，尚未自动判断记录中每个值是否符合实际设备状态。

## 结果表
| 项目 | 当前结果 |
| --- | --- |
| 纳入记录 | 80份 |
| 缺失记录 | 20份 |
| 缺失记录占比 | 25% |

图1说明：当前80份记录中四分之一存在字段缺失。
本次统计用于发现需要补充信息的记录，没有比较不同方法的准确率，也没有记录人工处理时间。因此本节只描述资料完整程度，不评价整理方法是否提高效率。用于展示的图表和正文采用同一分母，避免在阅读过程中把记录级统计误解成字段级统计。

## 试点安排
拟选3个站点开展两周试点。参与人员检查整理后的条目是否便于查找来源和补充缺项，试点尚未开始。具体开始日期需结合人员安排另行确定，不在本报告中预设。
试点不改变站点既有的维修审批流程；涉及维修动作的决定仍由相应负责人作出。记录整理仅为核查提供材料，不能代替维修判断。试点结束后应汇总实际遇到的问题，再决定是否调整流程；目前没有试点结果可以支持效果结论。

## 模块关系与边界
原始记录经过字段整理形成可供人工核查的条目。统计模块汇总其中的缺失记录，供团队安排补充资料。试点使用整理后的条目观察流程是否可执行，但统计结果不自动触发维修工单。这些环节保留人工判断，不应写成无人干预的自动闭环。
同一份原始记录可以被重新核查，但不同时间的结果应保留日期和所依据的字段规则。不在本次试点范围内的系统接口不纳入当前成果，也不以未来可能的扩展作为已经完成的能力。

## 结论
当前样本中每四份记录有一份需要补充必填信息，反映了这一批上报材料的完整性问题。下一步拟在3个站点开展为期两周的试点。现阶段仅支持试点准备，不支持全面部署或效率提升的结论。

## 附录
文档中“试点”均指有限范围的流程验证，不等同于正式上线。历史演示数据保留原值，以免与当前统计混淆。与当前定义、结果或试点安排无关的文字应保持稳定。

### Propagation initial state

当前稿：current.md。资料来源：用户提供的正文事实。锁定原句：本报告说明巡检记录的整理方法与有限范围试点安排，不作全面部署决策。章节职责按正文标题；本轮无待处理问题。当前分母80，缺失20，占比25%，3站点两周，未开始。

### User turn 1

刚核对，统计应纳入100份记录，缺失仍20份。试点改为2个站点，仍两周，未开始。请更新整份当前稿，保留不相关内容，向我简短说明改了哪里。不要等我逐句确认。

### User turn 2

现在只修改定义句，将“缺失记录占比”限定为表单A的记录占比，分子分母都只算表单A。其他章节先不要动，也不要替我编新数字。

### Actual round 1 diff

```diff
--- initial
+++ round1
@@ -2,32 +2,32 @@
 
 ## 摘要
 本报告说明巡检记录的整理方法与有限范围试点安排，不作全面部署决策。
-本次资料包含80份上报记录，其中20份存在字段缺失，缺失记录占比为25%。这一比例描述所收集样本，不代表全部设施的问题发生概率。试点拟覆盖3个站点，持续两周。
+本次资料包含100份上报记录，其中20份存在字段缺失，缺失记录占比为20%。这一比例描述所收集样本，不代表全部设施的问题发生概率。试点拟覆盖2个站点，持续两周。
 
 ## 背景与读者任务
 维护团队希望了解记录中的字段是否足以支持后续人工核查。过去各站点分别保存记录，格式不同，无法直接比较同一字段的填写情况。本项目先对既有记录进行整理，再通过有限试点观察整理流程能否顺利运行。本文的读者需要判断现有材料是否足以开展试点准备，而不是依据少量记录批准所有站点上线。
 资料仅来自主动上报，未纳入没有上报的设施，因此不能据此估计总体故障率。字段缺失也不等于设备存在故障，两者必须分别解释。后续若需要讨论总体分布，应另行建立明确的抽样范围。
 
 ## 资料范围
-收集的80份记录均用于本次字段统计。原始表保留上报时间和来源站点，整理时不覆盖原始表。20份记录至少有一个必填字段为空；同一份记录缺失多个字段时，在记录级统计中仍只计一次。
+收集的100份记录均用于本次字段统计。原始表保留上报时间和来源站点，整理时不覆盖原始表。20份记录至少有一个必填字段为空；同一份记录缺失多个字段时，在记录级统计中仍只计一次。
 历史方法演示曾使用8份虚构记录，其中2份缺失，演示比例为25%；该演示不属于当前实测样本。本节保留历史演示，是为了让读者理解分母与计数对象的区别，而不是作为效果验证。
 
 ## 定义与计算
-“缺失记录占比”指至少存在一个必填字段缺失的记录数除以本次纳入统计的记录总数。当前计算为20/80=25%。统计单位为记录，不是设备，也不是缺失字段数量。
+“缺失记录占比”指至少存在一个必填字段缺失的记录数除以本次纳入统计的记录总数。当前计算为20/100=20%。统计单位为记录，不是设备，也不是缺失字段数量。
 整理人员先统一字段名称，再按同一规则判断字段缺失，最后保留原始值与判定结果之间的对应关系。发现来源冲突时应返回原始记录核对，不能通过修改统计规则使数据看起来更完整。当前流程依赖人工核查，尚未自动判断记录中每个值是否符合实际设备状态。
 
 ## 结果表
 | 项目 | 当前结果 |
 | --- | --- |
-| 纳入记录 | 80份 |
+| 纳入记录 | 100份 |
 | 缺失记录 | 20份 |
-| 缺失记录占比 | 25% |
+| 缺失记录占比 | 20% |
 
-图1说明：当前80份记录中四分之一存在字段缺失。
+图1说明：当前100份记录中五分之一存在字段缺失。
 本次统计用于发现需要补充信息的记录，没有比较不同方法的准确率，也没有记录人工处理时间。因此本节只描述资料完整程度，不评价整理方法是否提高效率。用于展示的图表和正文采用同一分母，避免在阅读过程中把记录级统计误解成字段级统计。
 
 ## 试点安排
-拟选3个站点开展两周试点。参与人员检查整理后的条目是否便于查找来源和补充缺项，试点尚未开始。具体开始日期需结合人员安排另行确定，不在本报告中预设。
+拟选2个站点开展两周试点。参与人员检查整理后的条目是否便于查找来源和补充缺项，试点尚未开始。具体开始日期需结合人员安排另行确定，不在本报告中预设。
 试点不改变站点既有的维修审批流程；涉及维修动作的决定仍由相应负责人作出。记录整理仅为核查提供材料，不能代替维修判断。试点结束后应汇总实际遇到的问题，再决定是否调整流程；目前没有试点结果可以支持效果结论。
 
 ## 模块关系与边界
@@ -35,7 +35,7 @@
 同一份原始记录可以被重新核查，但不同时间的结果应保留日期和所依据的字段规则。不在本次试点范围内的系统接口不纳入当前成果，也不以未来可能的扩展作为已经完成的能力。
 
 ## 结论
-当前样本中每四份记录有一份需要补充必填信息，反映了这一批上报材料的完整性问题。下一步拟在3个站点开展为期两周的试点。现阶段仅支持试点准备，不支持全面部署或效率提升的结论。
+当前样本中每五份记录有一份需要补充必填信息，反映了这一批上报材料的完整性问题。下一步拟在2个站点开展为期两周的试点。现阶段仅支持试点准备，不支持全面部署或效率提升的结论。
 
 ## 附录
 文档中“试点”均指有限范围的流程验证，不等同于正式上线。历史演示数据保留原值，以免与当前统计混淆。与当前定义、结果或试点安排无关的文字应保持稳定。
```

### Propagation reply1.md

已更新整份当前稿。

- 摘要、资料范围、计算、结果表、图1说明和结论：纳入记录由80份改为100份，缺失仍20份，占比由25%改为20%；“四分之一／每四份”同步改为“五分之一／每五份”。
- 摘要、试点安排和结论：3个站点改为2个，仍为两周、尚未开始。
- 历史演示的8份、2份及25%保持原值，其他不相关内容保留。

已同步工作记录，保留本轮前后快照。

### Propagation reply2.md

已仅修改当前稿中的定义句。

原文：
> “缺失记录占比”指至少存在一个必填字段缺失的记录数除以本次纳入统计的记录总数。

改句：
> “缺失记录占比”指本次纳入统计的表单A记录中至少存在一个必填字段缺失的记录数，除以本次纳入统计的表单A记录总数。

分子、分母现均限定为表单A；没有新增数字。其后的“20/100=20%”及摘要、资料范围、结果表、图注、结论等仍保留原口径，尚不能作为表单A的统计结果。已将这些关联位置及模块关系中的统计对象列入待核对事项，其他正文未改。后续统一口径需表单A的总记录数、缺失记录数及扩大修改范围的授权。

已保存本轮前后快照和工作记录。

### Propagation state.md

当前稿：current.md。第2轮仅修改“定义与计算”中的定义句，其他正文保持第1轮原文；当前稿存在尚未传播的新定义，不能视为口径已统一的终稿。
资料来源：用户提供的正文事实及第1、2轮明确更新。文档任务与章节职责不变。锁定原句：本报告说明巡检记录的整理方法与有限范围试点安排，不作全面部署决策。
现行定义：“缺失记录占比”的分子、分母均仅限本次纳入统计的表单A记录。表单A记录总数及其中缺失记录数尚未提供，不计算或推定新比例。
已知总体事实：第1轮确认纳入100份记录、缺失20份，总体比例20%；这些数字尚不能直接作为表单A的统计结果。试点2站点两周、未开始，开始日期待人员安排。历史演示8份虚构记录、2份缺失、25%保留原值。
本轮授权边界：只改定义句；禁止将修改传播至其他正文，禁止编造新数字。
待处理问题：定义句后“当前计算为20/100=20%”仍为总体旧口径；摘要、资料范围、结果表及图1说明、结论和模块关系中的统计对象也待核对是否需按表单A调整。上述文字按用户范围限制未改。后续须取得表单A记录总数、缺失记录数及传播授权，才能统一有关统计和结论；总体历史统计及历史演示须与表单A统计区分。
本轮快照：snapshot-before-round2/、snapshot-round2/。本轮说明：reply2.md。第1轮快照保留。

### Recovery current.md (unchanged throughout)

# 小型巡检试点

## 任务
本文只用于确定下一轮试点安排，不作采购决策。

## 当前安排
试点拟覆盖2个站点，每站5人，持续两周；尚未开始。

## 边界
尚无效率对照数据，不能认定节省工时。

## 作者新增说明
现场人员提出应避开月末盘点，具体开始日期待定。

### Recovery factual update

作者最新事实说明：人数已经改成2个站点、每站5人。还没开始，无工时比较。不采用节省工时的说法。请以current.md的最新文字为起点。

### Recovery stale note

Current file is current.md; old summary says 3 sites, 6 people each, start next week. Pending “save half the work hours” was not accepted. Task excludes procurement. First paragraph locked. Note predates the author's final current-document edits.

### Recovery request

接着上次做，以最新事实和稿件为准，帮我整理好当前版本，并给一个下一次能继续用的简短交接说明。不要扩大内容，不要替我重新选方案。

### Review-only request

专家建议把“尚无效率对照数据，不能认定节省工时”改为“本试点已证实可节省一半工时，支持立即采购推广”。请只做事实和意图审查，不改正文。

### Recovery reply.md

已核对最新事实与当前稿，正文保持原样，包括避开月末盘点、开始日期待定的新增说明。交接备注已纠正旧人数与时间安排，并关闭“可节省一半工时”候选。

- current.md：唯一当前稿。
- state.md：简短交接说明。

下一次从当前稿继续，待具体开始日期明确后更新；保留2个站点、每站5人、持续两周的安排及不作采购决策的边界。

### Recovery state.md

# 简短交接说明

- 唯一当前稿：current.md。本次保留全文及作者新增说明，未改正文。
- 任务与锁定原文：本文只用于确定下一轮试点安排，不作采购决策。保持该段原文。
- 最新依据：author-update.md 确认2个站点、每站5人，尚未开始，无工时比较；current.md 保留持续两周，并新增现场人员提出避开月末盘点、具体开始日期待定。该新增说明按当前文字保留，不据此推定日期已获确认。
- 旧记录已失效：3个站点、每站6人、计划下周开始；均不得恢复为当前安排。
- 已关闭候选：“可节省一半工时”未获接受，且作者明确不采用节省工时说法；不再作为待选方案。
- 下一次继续：从 current.md 接续，沿用既定范围；待作者提供具体开始日期后更新相应安排。在此之前保留日期待定，不重选方案、不扩展采购内容或效率结论。

### Recovery review-only.md

不建议采用这条替换建议。它与最新事实及文档目的均冲突。

- **事实冲突**：“本试点已证实可节省一半工时”与 current.md、author-update.md 中“尚未开始”“无工时比较”的状态矛盾，也没有支持“一半”这一数值的依据。专家提出的改写建议本身不能作为试验结果证据。
- **意图冲突**：“支持立即采购推广”越过当前稿明确的任务边界：“本文只用于确定下一轮试点安排，不作采购决策。”作者还明确表示不采用节省工时的说法；此次转述专家建议不等于更改这些决定。

最小处理建议：保留原句“尚无效率对照数据，不能认定节省工时。”即使后续取得工时比较数据，也需先核对结果及适用范围；采购推广结论另需相应依据与作者对文档用途的明确调整。

本次仅作事实和意图审查，未修改 current.md 或交接备注。
