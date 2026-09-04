# 判断者—建议者系统：建议采纳的实验逻辑、证据基础与测量边界

个体如何把外部建议并入既有判断，是社会信息利用、元认知校准与人机协作研究的共同问题。仅比较建议前后的正确率，无法区分判断者是否接触了有用信息、是否真正改变判断，以及改变幅度是否与建议差异相称。判断者—建议者系统（Judge–Advisor System, JAS）通过依次测量初始判断、建议和最终判断，将社会影响表示为可观察的判断修正过程；连续数值任务还可估计建议在最终判断中的相对权重。该范式由此把“是否听取建议”转化为可操控的来源、质量、距离和置信度问题，也保留了准确性收益这一规范性结果。不过，建议采纳同时受初始知识、任务难度、建议来源与策略选择影响，不能直接等同于一般信任、服从倾向或稳定人格特质。

## 1. 范式提出与理论背景

Sniezek 和 Buckley（1995）以 JAS 名称明确区分承担最终决定责任的判断者与提供信息的建议者，并考察提示、认知冲突和责任结构如何改变决策。其方法学贡献在于保留判断者的最终控制权，使建议影响不同于群体共识或共同决策。随后，Harvey 和 Fischer（1997）将初始估计—建议—修订的连续数值结构用于建议采纳研究，表明建议既可能提高判断，也可能分担主观责任。Yaniv 和 Kleinberger（2000）进一步提出自我中心折扣（egocentric discounting）：判断者通常赋予自身估计过高权重，并会依据建议者历史表现形成声誉。

Yaniv（2004）的历史年份估计研究构成当前数值 JAS 的直接协议基础。判断者先独立回答一般知识题，再得到同尺度的他人估计或机械生成建议，最后提交修订值。研究发现，自身知识较高时建议权重较低，建议距初始估计越远越容易被折扣；采纳建议总体改善准确性，但改善幅度低于更充分整合独立估计时的水平。信息不对称解释认为，判断者能检索支持自身判断的理由，却通常看不到建议者的推理依据，因此自身判断具有可得性优势（Yaniv, 2004）。这一解释与保持一致性、来源可信度和任务难度等因素并不互斥。Bonaccio 和 Dalal（2006）的综合综述将判断者特征、建议者特征、任务与互动方式纳入输入—过程—输出模型，确立了 JAS 作为组织判断与建议研究的主要实验结构。

## 2. 任务逻辑、流程与核心指标

经典连续数值 JAS 包含三个必要观测量：初始估计 (I)、建议 (A) 和最终估计 (F)。判断者先在不知建议的条件下形成 (I)，随后评价与自身判断可能一致或冲突的 (A)，再决定保留、折中、完全采纳或越过建议。常用建议权重（weight of advice, WOA）为

\[
WOA=\frac{F-I}{A-I}.
\]

当最终估计不变时，WOA 为 0；最终估计等于建议时为 1；二者等权平均时为 0.5。负值表示向建议反方向修正，大于 1 表示修订越过建议。当 (A=I) 时分母为零，WOA 无定义。部分研究将负值截为 0 或将范围限制在 0—1，这会混同拒绝建议与反向移动，并改变均值含义（Bailey et al., 2023）。因此，原始估计、建议、最终估计及截尾规则均应保留并报告。

范式没有统一的固定呈现时长或自适应算法。常见操控包括建议是否主动请求、来源是人或算法、建议者的专业性与既往正确率、建议置信度、建议—初始判断距离、是否反馈真值，以及是否按准确性付酬。初始阶段反映项目知识、知觉证据和初始置信度的联合结果；建议呈现阶段引入来源评价、差异检测和认知冲突；最终修订阶段反映是否使用建议及使用幅度。由此，`建议条件－无建议条件` 可估计建议暴露的总体影响，`高质量－低质量建议` 更接近质量辨别，WOA 则描述相对于意见距离的行为修正。准确性增益通常定义为初始绝对误差减最终绝对误差，回答建议是否改善结果，不能由 WOA 单独推出。

建议距离既是理论变量，也是比率指标的组成部分。较远建议可能被视为不可信而降低比例权重，也可能使判断者怀疑自身估计而增加修正。不同材料和个体策略得到的距离效应并不一致（Love et al., 2024）。建议由真值方向生成时，还应区分名义方向与实际结果：朝向真值的固定偏移可能越过真值，远离真值的建议则可能放大误差。因而，距离、方向、建议准确性和初始误差应分别建模。

## 3. 主要行为与神经科学发现

### 3.1 自我中心折扣与策略异质性

跨研究最稳定的群体结果是最终估计通常向建议移动，但平均移动不足一半。Bailey 等（2023）综合 53 篇论文、129 个独立数据集中的 346 个效应量，得到平均 WOA 约 0.39；建议者信息所暗示的质量是多变量分析中最稳定的独特预测因素，低、中、高感知质量对应的平均修正约为 0.32、0.37 和 0.48。该结果支持自我中心折扣的总体趋势，也说明建议权重并非只由建议的客观质量决定。判断者对自身知识和置信度的估计、来源声誉以及意见差异均参与加权（Yaniv & Kleinberger, 2000; Yaniv, 2004）。

平均 WOA 容易掩盖离散策略。Soll 和 Larrick（2009）发现修订分布常在 0、0.5 和 1 附近聚集，分别对应坚持自身、平均与完全采纳。Himmelstein（2022）的双门槛模型据此将建议利用分为先拒绝、采纳或折中，再在折中试次中执行连续加权的过程。研究者若只比较被试均值，可能把“多数试次坚持、少数试次全盘采纳”误解为稳定的小幅整合。试次级分布、零值比例、完全采纳率、越界修订与连续 WOA 应共同报告。

建议采纳的规范性价值取决于两份估计的误差结构。两者独立且能力相近时，平均通常降低误差；若共享系统偏差，或建议质量显著较差，0.5 并非普遍最优权重。高风险电视竞赛的自然情境数据中，平均 WOA 达 0.58，且完全采纳更常见，表明实验室中的低风险、匿名和强制建议情境不能代表所有实际决策（Løhre & Halkjelsvik, 2024）。另一方面，将同一数值信息明确表述为“建议”而非“意见”，可通过帮助意图与可信度判断增加其影响（Milyavsky & Gvili, 2024）。这些证据说明 WOA 对互动含义和情境后果敏感。

算法建议扩大了 JAS 的应用范围。Logg 等（2019）在多项估计任务中观察到算法欣赏，即参与者在部分情境下比对人类建议给予算法更高权重；这与算法厌恶并存，差异取决于错误经验、任务类型和控制感。采用大量同质知觉试次的近期研究发现，人机建议下的个体策略包括简单平均、自我怀疑和对建议者的怀疑，聚合结果可能遮蔽这些模式（Love et al., 2024）。因此，计算机来源本身不能保证更高或更低的采纳率，透明披露来源也不等同于操控算法可信度。

### 3.2 fMRI 与 EEG 所揭示的加工阶段

任务特异性功能磁共振成像（functional magnetic resonance imaging, fMRI）证据提示，建议评价与建议整合涉及可区分但重叠的过程。Schilbach 等（2013）在 JAS 中操控建议者能力，发现能力评价改变与他人心理状态推断相关网络的活动，并以试次 WOA 建模实际整合；杏仁核活动随被感知的建议者能力而变化。Goodyear 等（2016）在 X 射线行李筛查中比较人类与机器建议，低可靠建议降低表现和采纳，对错误建议的来源差异涉及楔前叶、后扣带、颞顶联合区和岛叶等网络。后者采用接受/拒绝式判断且包含反馈学习，不能直接解释连续历史年份 JAS 的 WOA。现有 fMRI 结果支持来源评价、冲突与整合的网络参与，尚不足以把单一脑区视为建议采纳的特异性或因果指标。

事件相关电位（event-related potential, ERP）研究为建议呈现后的时间进程提供补充。Wang 等（2025）在点数估计任务中操控建议者地位与建议置信度，发现高置信建议更易被采纳，且社会地位与置信度分别或交互调节反馈相关负波、P3 以及 theta、beta 频段活动。这些结果表明来源线索可在早期差异检测与较晚资源分配阶段发挥不同作用。由于该研究同时呈现社会地位和置信度，并使用知觉判断材料，ERP 成分不能直接归因于 WOA，也不能无条件外推到明确声明为计算机生成、没有人类身份线索的实现。

## 4. 范式发展与主要应用

JAS 已从单次匿名人际建议扩展到多建议者、可选择建议、动态声誉学习、算法辅助和专业判断。Scheunemann 等（2021）以连续多条年龄建议检验精神病性体验者对当前证据的加权，发现高精神病性体验组对当前建议、尤其离群建议赋予更高权重。该适配测量的是动态证据更新，不能据此把经典 WOA 解释为临床诊断指标。2025 年的研究进一步表明，高质量建议还可能改善随后不同题目的初始判断，提示建议的作用可包含跨项目学习，而不仅是同一项目的即时修订（Schultze et al., 2025）。

这些发展改变了范式的研究问题。固定、无反馈的单一建议适合估计一次性社会影响；重复来源和反馈适合研究信誉学习；人机来源比较适合考察算法依赖；临床适配则需要分离一般认知能力、初始置信度与症状相关的更新偏差。版本间的建议真实性、来源披露、反馈、激励、材料难度和建议距离分布若不一致，WOA 数值不宜直接横向比较。

## 5. 测量效度、信度与解释边界

JAS 具有清晰的操作效度：在同一量尺上观测建议前后判断，能够量化建议导致的方向与幅度变化；准确真值又允许独立检验行为修订是否有益。其构念效度受多重过程限制。WOA 同时包含初始误差、意见距离、数值取整和策略选择；接近零的分母会放大微小输入误差，跨项目平均还会受材料知识异质性影响。建议质量、被感知质量与来源标签必须区分。尤其在没有人类建议者互动的任务中，WOA 是计算机建议利用指标，不足以测量人际信任。

群体水平效应不保证个体排序可靠。Karvelis 等（2024）在包含动态帮助/欺骗建议及层级高斯滤波模型的相关任务中发现，多数行为和计算指标的两周重测信度低于 0.50；该任务并非经典连续数值 JAS，结果不能作为后者的信度估计，却表明临床或个体差异推断必须单独验证重测信度、参数可恢复性和聚合试次数。对仅含少量异质知识题的实现，更适合预注册群体内条件效应和试次级模型，不宜未经验证地把平均 WOA 用作稳定特质、临床筛查或跨文化常模。

## 6. TaskBeacon 中的任务实现

### 6.1 任务资源与访问入口

| 资源 | ID | 用途 | 地址 |
| --- | --- | --- | --- |
| 完整实验源码 | T000139 | PsychoPy/PsyFlow 中文行为实验实现 | https://github.com/TaskBeacon/T000139-judge-advisor-task |
| 浏览器伴随源码 | H000139 | 保留同一两遍流程的网页预览实现 | https://github.com/TaskBeacon/H000139-judge-advisor-task |
| 在线体验 | H000139 | 在共享网页运行器中体验行为流程 | https://taskbeacon.github.io/psyflow-web/?task=H000139-judge-advisor-task |

H000139 当前配置与 T000139 均为 12 个配对项目和行为采集，但网页运行环境仍应视为伴随预览；键盘输入、呈现时序与本地 PsychoPy 环境的测量属性需要分别验证，网页版本不替代完整实验源码。

### 6.2 实现流程与关键参数

TaskBeacon 当前版本采用一块、两遍的历史年份估计。第一遍按被试编号与种子打乱 12 道题，逐题在 45 s 内输入整数并按回车提交；全部初始估计结束后，第二遍以相同项目顺序呈现。有效初始估计先与明确标注的“电脑生成建议”共同显示 3 s，随后二者保持可见，参与者在空白输入框中于 45 s 内提交最终估计。任务不呈现真值、对错、奖励或准确性奖金，也没有难度自适应控制器。

![TaskBeacon 判断者—建议者任务流程](../task_flow.png)

**图 1. TaskBeacon T000139 的实现流程。** 第一遍完成全部 12 个独立年份估计，每题最长 45 s、回车提交，提交后显示 0.3 s 中性记录提示；第二遍以同序项目先显示原估计与透明披露的电脑建议 3 s，再开放最长 45 s 的空白最终输入框，提交后同样显示 0.3 s 提示。12 个项目均衡分配近距、中距、远距与朝向、背离真值六类条件；偏移量分别从 15/18/20、40/43/45、70/72/75 年中抽取，并按预定方向加到初始估计上，朝向偏移允许越过真值。若初始估计无效或建议超出允许数值域，则仅显示 1 s 不可用提示，不呈现建议也不收集最终估计。任务无正确性反馈、积分和自适应难度调整。

主要结果为保留负值与大于 1 值的有符号 WOA；同时记录绝对修订比例、自我权重、初始与最终绝对误差及准确性增益。六个距离×方向条件各出现两次，但每道题只进入一个条件，题目知识与条件因此仍可能混杂。12 道中文历史题虽核验了事实真值，尚未建立心理测量学常模或重测信度。该实现适合检验透明机械建议的群体内修订模式，不构成人类建议者互动、临床效度或稳定信任特质的测量。

## 参考文献

Bailey, P. E., Leon, T., Ebner, N. C., Moustafa, A. A., & Weidemann, G. (2023). A meta-analysis of the weight of advice in decision-making. *Current Psychology, 42*(28), 24516–24541. https://doi.org/10.1007/s12144-022-03573-2

Bonaccio, S., & Dalal, R. S. (2006). Advice taking and decision-making: An integrative literature review, and implications for the organizational sciences. *Organizational Behavior and Human Decision Processes, 101*(2), 127–151. https://doi.org/10.1016/j.obhdp.2006.07.001

Goodyear, K., Parasuraman, R., Chernyak, S., Madhavan, P., Deshpande, G., & Krueger, F. (2016). Advice taking from humans and machines: An fMRI and effective connectivity study. *Frontiers in Human Neuroscience, 10*, 542. https://doi.org/10.3389/fnhum.2016.00542

Harvey, N., & Fischer, I. (1997). Taking advice: Accepting help, improving judgment, and sharing responsibility. *Organizational Behavior and Human Decision Processes, 70*(2), 117–133. https://doi.org/10.1006/obhd.1997.2697

Himmelstein, M. (2022). Decline, adopt or compromise? A dual hurdle model for advice utilization. *Journal of Mathematical Psychology, 110*, 102695. https://doi.org/10.1016/j.jmp.2022.102695

Karvelis, P., Hauke, D. J., Wobmann, M., Andreou, C., Mackintosh, A., de Bock, R., Borgwardt, S., & Diaconescu, A. O. (2024). Test-retest reliability of behavioral and computational measures of advice taking under volatility. *PLOS ONE, 19*(11), e0312255. https://doi.org/10.1371/journal.pone.0312255

Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: People prefer algorithmic to human judgment. *Organizational Behavior and Human Decision Processes, 151*, 90–103. https://doi.org/10.1016/j.obhdp.2018.12.005

Love, J., Gronau, Q. F., Palmer, G., Eidels, A., & Brown, S. D. (2024). In human–machine trust, humans rely on a simple averaging strategy. *Cognitive Research: Principles and Implications, 9*, 58. https://doi.org/10.1186/s41235-024-00583-5

Løhre, E., & Halkjelsvik, T. (2024). Advice taking when the stakes are high: Evidence from a game show. *Judgment and Decision Making, 19*, e25. https://doi.org/10.1017/jdm.2024.4

Milyavsky, M., & Gvili, Y. (2024). Advice taking vs. combining opinions: Framing social information as advice increases source’s perceived helping intentions, trust, and influence. *Organizational Behavior and Human Decision Processes, 183*, 104328. https://doi.org/10.1016/j.obhdp.2024.104328

Scheunemann, J., Fischer, R., & Moritz, S. (2021). Probing the hypersalience hypothesis—An adapted Judge-Advisor System tested in individuals with psychotic-like experiences. *Frontiers in Psychiatry, 12*, 612810. https://doi.org/10.3389/fpsyt.2021.612810

Schilbach, L., Eickhoff, S. B., Schultze, T., Mojzisch, A., & Vogeley, K. (2013). To you I am listening: Perceived competence of advisors influences judgment and decision-making via recruitment of the amygdala. *Social Neuroscience, 8*(3), 189–202. https://doi.org/10.1080/17470919.2013.775967

Schultze, T., Stern, A., & Schulz-Hardt, S. (2025). Learning processes in the Judge–Advisor System: A neglected advantage of advice taking. *Journal of Behavioral Decision Making, 38*(3), e70029. https://doi.org/10.1002/bdm.70029

Sniezek, J. A., & Buckley, T. (1995). Cueing and cognitive conflict in Judge-Advisor decision making. *Organizational Behavior and Human Decision Processes, 62*(2), 159–174. https://doi.org/10.1006/obhd.1995.1040

Soll, J. B., & Larrick, R. P. (2009). Strategies for revising judgment: How (and how well) people use others’ opinions. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 35*(3), 780–805. https://doi.org/10.1037/a0015145

Wang, X., Huang, X., & Zhang, E. (2025). How individuals evaluate the confidence of advice from advisors with high- and low-status: A behavioural and ERP study. *Biological Psychology, 194*, 108978. https://doi.org/10.1016/j.biopsycho.2024.108978

Yaniv, I. (2004). Receiving other people’s advice: Influence and benefit. *Organizational Behavior and Human Decision Processes, 93*(1), 1–13. https://doi.org/10.1016/j.obhdp.2003.08.002

Yaniv, I., & Kleinberger, E. (2000). Advice taking in decision making: Egocentric discounting and reputation formation. *Organizational Behavior and Human Decision Processes, 83*(2), 260–281. https://doi.org/10.1006/obhd.2000.2909
