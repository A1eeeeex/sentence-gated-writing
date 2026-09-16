# Technical / Analytical Writing Profile

Load selectively for technical or analytical parts of reports, methods, proposals, and system descriptions. Core develops prose through shared understanding, author calibration, and adaptive collaboration, supported by fact control, scoped propagation, and a current draft. This profile supplies genre-specific structure and expression guidance, not another mandatory workflow. These are fallible editing heuristics, not validated expert-writing theory. Keep checks internal unless a finding requires explanation or a human choice. Facts take priority over structural completeness.

## Organize technical reasoning before checking it

Turn correct but scattered material into an argument the reader can follow. Identify the practical problem, what the available approaches each contribute, what remains unresolved, and how the documented methods address it. Write the passage, then use the checks below to refine it. A proposed synthesis must remain distinguishable from a project fact.

Use **capability–boundary–need** when the materials support it: explain what a method can establish, what it leaves unanswered, and why another step is needed. Look for real tensions between requirements or complementary approaches; not every project has a technical contradiction, and not every gap determines a unique method. Do not invent missing modules or convert a plausible rationale into an implemented architecture.

For module descriptions, actively organize the supported relationships: why A needs B, whether A supplies B, whether routes are serial, parallel, or alternatives, and which connections are planned versus working. When the sources establish only separate components, describe that actual partial structure. A structural closing sentence may summarize their distinct responsibilities; omit promotional claims that add no meaning.

### Example: scattered facts → an argument

Assumed materials: manual ratings describe reported experience but vary between raters; speed and acceleration recordings quantify motion but do not alone establish subjective experience; the team plans to explore an association between features and ratings. No predictive model or fusion system has been implemented.

Scattered notes: “有人工评分。采了速度和加速度。想把两者结合。”

Usable prose: “人工评分用于记录驾驶体验，速度和加速度数据用于描述车辆运动。两类信息分别反映体验判断与运动过程，当前尚未建立二者之间的关联。项目拟结合人工评分与运动特征，探索哪些运动变化与体验差异有关；现阶段尚不能据此预测评分或声称评价效果得到改善。”

The writing identifies complementary roles and motivates the next step without inventing a three-route architecture. If the source only says “combine both” and does not establish the intended association, propose that interpretation for calibration rather than assert it. Add prediction, objective evaluation, or fusion routes only if the actual project supports them. These are generative heuristics, not proven theory or mandatory sentence templates.

## Paragraph technicalization

- **Technical Structure:** Identify why this paragraph exists, its input, treatment, and output where relevant. Missing source information is a gap, not permission to invent. Distribute elements across adjacent paragraphs if that reads better; do not generate a fixed four-clause sentence.
- **Hierarchy:** Compare items in an enumeration at the same abstraction level. “Road structure, CARLA, vehicle behavior, test effectiveness” mixes object, platform, behavior, and result. Reorganize by the actual argument, keeping useful platform details at their proper level.
- **Role:** Explain responsibilities and boundaries when naming modules or stages. A name alone does not explain a design. Do not infer behavior from a module label.
- **Outcome:** Identify a concrete artifact or supported result. Preserve whether it is intended, designed, produced, or tested. Some paragraphs legitimately end with a limitation or unresolved question.

## Section architecture

- **Transformation Chain:** Track source-supported changes of state. Label manual handoffs, proposed steps, and missing links. A collection, scoring method, and simulator can coexist without an integrated pipeline.
- **Architecture Relationship:** Establish whether one output is another input, stages run in sequence or parallel, routes are alternatives, or modules remain independent. Input compatibility and reuse across environments require evidence; “modular” does not prove either.
- **Generalization Coverage:** Ensure all expanded items fit the introductory categories. Change the summary or regroup the detail when needed; do not silently discard an outlying method to make the count fit.
- **Structural Repetition:** Preserve the same thread when it explains need in background, connections in the route, and completion status in conclusions. Delete only repetition without added informational or structural function.
- **Terminology:** Keep one stable name per concept and distinguish source, configuration, execution, and result. Do not equate recorded motion with dynamics or source frequency with population probability.

## Expression within the evidence boundary

Use identifiable engineering actions: classify objects, map fields, configure conditions, interpolate recorded positions, or check units only when those operations actually occurred. Do not substitute “数据治理闭环” for unspecified sorting. Use ordinary verbs when they are accurate.

**Claim Precision:** Narrow scope rather than adding vague hedges, but retain genuine uncertainty. “May improve fidelity” cannot become “reproduces motion accurately” without evidence. A supported purpose statement is different from a performance result.

**Embedded Value:** If supported facts explain a benefit, do not append “显著提高效率”. A separate value section may summarize implications, clearly separating inferred utility from measured gains.

**Contrast Pair:** Use distinctions the source supports, such as recorded trajectory playback and rule-based behavior generation. Do not force two exclusive categories if methods overlap or a third route exists. Avoid artificial rhetorical oppositions.

## Source-bounded before / after cases

These are abstracted illustrations inspired by the user's examples, not reproductions of a confidential report or measured improvement evidence. Every added detail below has an explicit assumed source. The actual expert-edited report was not supplied for this update.

### 1. Actions → technical structure

Assumed source: the project aims to represent a surveyed road; map, photographs, and measurements were used to model road geometry, facilities, and surfaces; a road-environment asset was produced. Reuse and fidelity were not evaluated.

Before: 使用地图、照片和测量数据制作虚拟道路。

After: 为表达所测道路的环境特征，项目依据地图、现场照片和实测数据，对道路几何、沿线设施及表面材质进行建模，形成该路段的虚拟道路环境资产。

The change names the goal, input, objects, and output. It does not claim high fidelity or reusable deployment. Without those source details, retain the simpler original or ask for the missing facts.

### 2. Vague benefit → bounded purpose

Assumed source: software replays recorded vehicle positions over time. It has no fidelity comparison and does not model vehicle dynamics.

Before: 该方法能够在一定程度上提高仿真复现效果。

After: 该方法依据实车试验记录的位置与时间，在虚拟环境中回放车辆运动过程。

This replaces an unsupported improvement claim with a supported operation. If only a design exists, write “该方案拟依据……” instead. Do not remove uncertainty from an actual hypothesis.

### 3. Module list → supported transformations

Assumed source: raw descriptions were structured as entries; a scoring method was designed for comparison but not run; two independently selected entries were manually converted into simulation configurations. No score-based selection or automatic export exists.

Before: 项目包括场景库、评价和仿真三个模块。

After: 原始场景描述经结构化整理形成场景条目。评价方法面向条目间的比较，目前尚未产生评价结果。另有两个经独立选取的条目已人工转换为仿真配置，尚未与评价过程衔接。

A partial chain is more accurate than inventing a complete pipeline. Only write “评价结果用于筛选并转化场景” when the project actually implements that relationship.
