# Grounding block - source: 7faa89be-2ac4-4990-9348-0366849e58fd

## Research idea

Agent in a Bottle: Can LLM Agents Turn Their Capabilities Into Cheap, Scalable Artifacts? — arXiv 2610.08775v1. Auto-candidate from daily research scan (lane ai-agents-epistemics); triage for QNFO research fit.

## Existing paper under revision (remediation only)

(none - new paper)

## Source material (fetched from arXiv)

TITLE: arXiv Query: search_query=&amp;id_list=2610.08775&amp;start=0&amp;max_results=1

ABSTRACT: Large language models (LLMs) can solve many narrow tasks, but querying them separately for millions of related instances can be prohibitively expensive. Can LLM agents autonomously create cheaper solutions for such workloads? We call this ability "bottling": the ability to turn general capabilities into task-specific solutions that balance answer quality and amortised cost. We introduce BOTTLED, a benchmark in which agents receive an entire unlabelled workload and must complete it under fixed time, compute and LLM API budgets. Agents choose their own approach, such as training a small model or writing a reusable program. Across ten models and three tasks, we find that strong zero-shot task performance does not reliably translate into strong bottling capabilities. Models with similar zero-shot scores can differ substantially after bottling, and 48 of 60 bottling runs score below the lower bound of the 95% confidence interval of their model's zero-shot performance. Moreover, 31 of 60 runs underperform the stronger of two small-model distillation baselines with the same token budget. Nevertheless, bottling can yield substantial savings: on query-product relevance classification, Opus 5 retains about 82% of its zero-shot macro-F1 at roughly 657 times lower reported cost. Bottling is also competitive with Jev, a "system one" model built especially for cheap, repetitive inference: Opus 5 on the same task recovers about 94% of Jev's macro-F1 at a quarter of Jev's projected full-workload cost. BOTTLED provides a basis for evaluating and improving agents' ability to invest limited resources in reusable solutions for large, repetitive workloads.

## Related literature (arXiv, real identifiers)

arXiv:2610.08775v1 | Agent in a Bottle: Can LLM Agents Turn Their Capabilities Into Cheap, Scalable Artifacts?
  Large language models (LLMs) can solve many narrow tasks, but querying them separately for millions of related instances can be prohibitively expensive. Can LLM agents autonomously create cheaper solutions for such workloads? We call this ability "bottling": the ability to turn general capabilities into task-specific solutions that balance answer quality and amortised cost. We introduce BOTTLED, a
arXiv:2203.08975v2 | A Survey of Multi-Agent Deep Reinforcement Learning with Communication
  Communication is an effective mechanism for coordinating the behaviors of multiple agents, broadening their views of the environment, and to support their collaborations. In the field of multi-agent deep reinforcement learning (MADRL), agents can improve the overall learning performance and achieve their objectives by communication. Agents can communicate various types of messages, either to all a
arXiv:2601.10758v3 | Agents at Risk: How Users Unwittingly Undermine LLM Safety
  Large language model (LLM)-based agents are increasingly deployed in applications, such as trip-planning agents and web-use agents, to perform complex planning and execution tasks. Prior work has shown that LLM-based agents are vulnerable to context confusion, where external adversarial content incorporated into the agent's reasoning context may be treated as task-relevant constraints. However, ex
arXiv:2409.01907v1 | Focus Agent: LLM-Powered Virtual Focus Group
  In the domain of Human-Computer Interaction, focus groups represent a widely utilised yet resource-intensive methodology, often demanding the expertise of skilled moderators and meticulous preparatory efforts. This study introduces the ``Focus Agent,'' a Large Language Model (LLM) powered framework that simulates both the focus group (for data collection) and acts as a moderator in a focus group s
arXiv:2401.16216v1 | A mechanism for discovering semantic relationships among agent communication protocols
  One relevant aspect in the development of the Semantic Web framework is the achievement of a real inter-agents communication capability at the semantic level. Agents should be able to communicate with each other freely using different communication protocols, constituted by communication acts. For that scenario, we introduce in this paper an efficient mechanism presenting the following main featur
arXiv:2412.06333v3 | Augmenting the action space with conventions to improve multi-agent cooperation in Hanabi
  The card game Hanabi is considered a strong medium for the testing and development of multi-agent reinforcement learning (MARL) algorithms, due to its cooperative nature, partial observability, limited communication and remarkable complexity. Previous research efforts have explored the capabilities of MARL algorithms within Hanabi, focusing largely on advanced architecture design and algorithmic m
arXiv:2602.04518v1 | Learning the Value Systems of Agents with Preference-based and Inverse Reinforcement Learning
  Agreement Technologies refer to open computer systems in which autonomous software agents interact with one another, typically on behalf of humans, in order to come to mutually acceptable agreements. With the advance of AI systems in recent years, it has become apparent that such agreements, in order to be acceptable to the involved parties, must remain aligned with ethical principles and moral va
arXiv:2512.21309v2 | A Plan Reuse Mechanism for LLM-Driven Agent
  Integrating large language models (LLMs) into personal assistants, like Xiao Ai and Blue Heart V, effectively enhances their ability to interact with humans, solve complex tasks, and manage IoT devices. Such assistants are also termed LLM-driven agents. Upon receiving user requests, the LLM-driven agent generates plans using an LLM, executes these plans through various tools, and then returns the 

## QNFO corpus context (Vectorize)

QNFO: Prioritizing Large Language Models for Scientific Research and Agentic AI: A LiveBench-Grounded Audit (August 2026)
  An audit of the frontier large-language-model landscape (August 2026) for mathematics-heavy scientific research and agentic AI, grounded in the LiveBench 2026-06-25 contamination-free benchmark. Findings: no Llama model ranks in the top 42; DeepSeek V4 Pro 0813 is the mathematics price-performance o
QNFO: Epistemic Legibility in AI-Assisted Science: Ignorance Auditing as a Governance Instrument for the Peer-Review and Evaluation Bottleneck
  As AI systems take on hypothesis generation, experiment planning, analysis, and writing, the scientific ecosystem faces a new bottleneck: not production, but evaluation, verification, and governance. This position paper contributes a documented case and an instrument to that problem. The case: a fla
QNFO: Flag Structures and the Flagging Act: A Cross-Domain Survey with Explicit Counting Derivations and a Posed Re-Entry Problem
  The word "flag" names a family of mathematically precise objects — chains of nested subspaces (flag varieties), nested set systems with exchange axioms (flag matroids), asymptotic-inequality certificates (flag algebras), and directional curvature invariants of Finsler spaces — and, in ordinary resea
QNFO: Agentic Collapse
  

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.08775&amp;start=0&amp;max_results=1

ABSTRACT: Large language models (LLMs) can solve many narrow tasks, but querying them separately for millions of related instances can be prohibitively expensive. Can LLM agents autonomously create cheaper solutions for such workloads? We call this ability "bottling": the ability to turn general capabilities into task-specific solutions that balance answer quality and amortised cost. We introduce BOTTLED, a benchmark in which agents receive an entire unlabelled workload and must complete it under fixed time, compute and LLM API budgets. Agents choose their own approach, such as training a small model or writing a reusable program. Across ten models and three tasks, we find that strong zero-shot task performance does not reliably translate into strong bottling capabilities. Models with similar zero-shot scores can differ substantially after bottling, and 48 of 60 bottling runs score below the lower bound of the 95% confidence interval of their model's zero-shot performance. Moreover, 31 of 60 runs underperform the stronger of two small-model distillation baselines with the same token budget. Neve
[2] arXiv:2610.08775v1 | Agent in a Bottle: Can LLM Agents Turn Their Capabilities Into Cheap, Scalable Artifacts?
  Large language models (LLMs) can solve many narrow tasks, but querying them separately for millions of related instances can be prohibitively expensive. Can LLM agents autonomously create cheaper solutions for such workloads? We call this ability "bottling": the ability to turn general capabilities into task-specific solutions that balance answer quality and amortised cost. We introduce BOTTLED, a
[3] arXiv:2203.08975v2 | A Survey of Multi-Agent Deep Reinforcement Learning with Communication
  Communication is an effective mechanism for coordinating the behaviors of multiple agents, broadening their views of the environment, and to support their collaborations. In the field of multi-agent deep reinforcement learning (MADRL), agents can improve the overall learning performance and achieve their objectives by communication. Agents can communicate various types of messages, either to all a
[4] arXiv:2601.10758v3 | Agents at Risk: How Users Unwittingly Undermine LLM Safety
  Large language model (LLM)-based agents are increasingly deployed in applications, such as trip-planning agents and web-use agents, to perform complex planning and execution tasks. Prior work has shown that LLM-based agents are vulnerable to context confusion, where external adversarial content incorporated into the agent's reasoning context may be treated as task-relevant constraints. However, ex
[5] arXiv:2409.01907v1 | Focus Agent: LLM-Powered Virtual Focus Group
  In the domain of Human-Computer Interaction, focus groups represent a widely utilised yet resource-intensive methodology, often demanding the expertise of skilled moderators and meticulous preparatory efforts. This study introduces the ``Focus Agent,'' a Large Language Model (LLM) powered framework that simulates both the focus group (for data collection) and acts as a moderator in a focus group s
[6] arXiv:2401.16216v1 | A mechanism for discovering semantic relationships among agent communication protocols
  One relevant aspect in the development of the Semantic Web framework is the achievement of a real inter-agents communication capability at the semantic level. Agents should be able to communicate with each other freely using different communication protocols, constituted by communication acts. For that scenario, we introduce in this paper an efficient mechanism presenting the following main featur
[7] arXiv:2412.06333v3 | Augmenting the action space with conventions to improve multi-agent cooperation in Hanabi
  The card game Hanabi is considered a strong medium for the testing and development of multi-agent reinforcement learning (MARL) algorithms, due to its cooperative nature, partial observability, limited communication and remarkable complexity. Previous research efforts have explored the capabilities of MARL algorithms within Hanabi, focusing largely on advanced architecture design and algorithmic m
[8] arXiv:2602.04518v1 | Learning the Value Systems of Agents with Preference-based and Inverse Reinforcement Learning
  Agreement Technologies refer to open computer systems in which autonomous software agents interact with one another, typically on behalf of humans, in order to come to mutually acceptable agreements. With the advance of AI systems in recent years, it has become apparent that such agreements, in order to be acceptable to the involved parties, must remain aligned with ethical principles and moral va
[9] arXiv:2512.21309v2 | A Plan Reuse Mechanism for LLM-Driven Agent
  Integrating large language models (LLMs) into personal assistants, like Xiao Ai and Blue Heart V, effectively enhances their ability to interact with humans, solve complex tasks, and manage IoT devices. Such assistants are also termed LLM-driven agents. Upon receiving user requests, the LLM-driven agent generates plans using an LLM, executes these plans through various tools, and then returns the 
[10] QNFO: Prioritizing Large Language Models for Scientific Research and Agentic AI: A LiveBench-Grounded Audit (August 2026)
  An audit of the frontier large-language-model landscape (August 2026) for mathematics-heavy scientific research and agentic AI, grounded in the LiveBench 2026-06-25 contamination-free benchmark. Findings: no Llama model ranks in the top 42; DeepSeek V4 Pro 0813 is the mathematics price-performance o
[11] QNFO: Epistemic Legibility in AI-Assisted Science: Ignorance Auditing as a Governance Instrument for the Peer-Review and Evaluation Bottleneck
  As AI systems take on hypothesis generation, experiment planning, analysis, and writing, the scientific ecosystem faces a new bottleneck: not production, but evaluation, verification, and governance. This position paper contributes a documented case and an instrument to that problem. The case: a fla
[12] QNFO: Flag Structures and the Flagging Act: A Cross-Domain Survey with Explicit Counting Derivations and a Posed Re-Entry Problem
  The word "flag" names a family of mathematically precise objects — chains of nested subspaces (flag varieties), nested set systems with exchange axioms (flag matroids), asymptotic-inequality certificates (flag algebras), and directional curvature invariants of Finsler spaces — and, in ordinary resea
[13] QNFO: Agentic Collapse
  