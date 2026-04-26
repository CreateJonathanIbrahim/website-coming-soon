# Pillar: Claude Code Architecture & Practical AI Tooling

## Core Concepts in This Territory

- **CLAUDE.md design and the 200-line discipline.** CLAUDE.md is a user-message context file, not a system prompt. That distinction matters because it changes how Claude weights the instructions, how token cost accumulates, and how performance degrades as the file grows. More is not better. Under 200 lines is structural discipline, the only way CLAUDE.md keeps improving performance instead of degrading it.

- **The five components of Claude Code and which job each does.** Skills are atomic tasks. Agents coordinate multiple tasks across time. Hooks enforce deterministically. Rules load conditionally based on file path. Settings configure permissions and behavior. Conflating any two of these produces architectural mistakes that look functional until they fail.

- **Path-scoped rules loading.** Rules in `.claude/rules/` load only when Claude is working on files matching the rule's glob. A carousel rule does not need to be in context when distilling a source. Path-scoped loading is the system's mechanism for keeping context relevant, not optional intelligence layered on top of it.

- **Layer 3 vs. Layer 4 distinction.** Layer 3 files load every session and define stable behavior (voice files, pillar files). Layer 4 files load per-run and carry working material (source files, content drafts, briefs). Treating a Layer 4 file as a Layer 3 reference (for example, internalizing a source's writing style) is a category error that corrupts voice consistency.

- **Hooks vs. CLAUDE.md as enforcement tools.** CLAUDE.md suggests. Hooks enforce deterministically. For things that must never occur (destructive commands, force pushes, raw files used as production input), hooks are the correct tool. For things that should usually occur (loading voice files, following format patterns), CLAUDE.md and rules are correct. Conflating these creates either rigid systems or porous safety.

- **Context window management as the central engineering problem.** Token budget is the constraint that shapes every other architectural decision. CLAUDE.md length, rules scoping, source file size, when to spawn subagents, what goes into a skill vs. an agent. All of these answer the same question: how do I keep the relevant context in the window and the irrelevant context out.

- **The automation vs. scaling distinction.** Automation removes a human from a repetitive task. Scaling raises the capacity ceiling. They are different problems with different solutions. Most "AI workflow" content conflates them, which leads to over-engineering small problems and under-designing capacity problems.

- **API vs. subscription calculus.** The default advice is API-first. At agency volume across multiple workflows, the Claude subscription model frequently outperforms the API on cost-per-output. The right choice depends on usage pattern, model tier, and whether the work benefits from programmatic control. Knowing where the threshold falls is a practical business decision, not a technical preference.

- **Orchestration glue as a separate layer.** Make.com, n8n, Zapier, and MCP servers sit at the connection layer. They trigger Claude calls from external events and route outputs to delivery destinations. The intelligence lives in the prompt. The plumbing lives in the orchestrator. Mixing the two produces systems that are hard to debug and harder to maintain.

- **Why complex frameworks are usually unnecessary.** LangChain, CrewAI, AutoGen, and similar add significant complexity for use cases Claude Code, the Claude API, and an orchestrator like Make.com handle directly. Frameworks are the right answer when there is a specific capability gap they address, not as a default starting point.

- **AI happenings filtered through workflow impact.** Model releases, capability updates, and pricing changes get covered well by the AI commentary genre. What is missing is the practitioner reading: how does this specific change move the cost calculus, which existing workflow does it unlock or break, what is the actual operational implication. That filter is the angle.

---

## Jonathan's Position

Jonathan was Head of PM at WISE Digital Partners (February 2025 through April 2026), a digital marketing agency. He is not an AI infrastructure or product builder. He uses Claude Code as an operator to do delivery work better and documents the architectural decisions along the way. JonathanOS and the WISE Content Engine are both products of that perspective. This is a specific and underrepresented position in the Claude Code conversation.

Most Claude Code content is produced by developers building products or by AI enthusiasts documenting features. Jonathan's content is produced by a practitioner who has run real systems with real clients and real deadlines. The question he answers is not "how does this work" but "how did I actually build it and what did I find out."

---

## Canonical Artifacts

- JonathanOS (2026): personal operating system in Claude Code. Connects an Obsidian knowledge vault, content production pipeline, and modular skill library. Orchestrated by filesystem structure rather than application code. Task layer wired to ClickUp via MCP.
- WISE Content Engine (2026): 10-skill AI workflow producing publish-ready website copy and SEO content end-to-end. Runs inside Claude Code with automated QA gates via Python validation scripts.
- Meeting summary automation pipeline (transcript in, structured summary out, distributed to stakeholders).
- Transcript processing pipelines as a general pattern across audio and text inputs.
- Production stack: Claude Code, Claude API, Make.com, n8n, Zapier, MCP servers (ClickUp MCP, Brave Search MCP, Firecrawl MCP, Playwright MCP).
- The CLAUDE.md / hooks / rules / skills / agents architectural decisions inside JonathanOS itself, documented in the repository.

---

## Common Angles

- Most CLAUDE.md files are written as documentation. They should be written as instructions.
- The five components of Claude Code and which job each does (skills, agents, hooks, rules, settings).
- Hooks vs. CLAUDE.md: when each is the right enforcement tool.
- Why your AI workflow probably should not start with LangChain.
- API vs. subscription: the calculation that goes against the default advice.
- What [latest Claude release] actually changes in my workflow (not features, cost calculus and unlocked patterns).
- The 200-line CLAUDE.md ceiling and why it exists.
- Layer 3 vs. Layer 4 as a context discipline.
- Automation removed a human step. It did not scale anything. Here is the difference.

---

## What the Audience Gets Wrong

**That CLAUDE.md is a system prompt.** It loads as a user message. The distinction affects token counting, weighting, and how Claude follows the instructions. Treating it like a system prompt produces a file that is too long and too prescriptive.

**That more CLAUDE.md is better.** Context bloat degrades performance. The goal is the minimum sufficient context that keeps Claude oriented without crowding out the working material.

**That skills and agents are the same.** A skill does one atomic task. An agent coordinates multiple tasks. Building a pipeline as a skill produces an unextendable monolith. Building a single task as an agent produces unnecessary coordination overhead.

**That API is always cheaper than subscription.** The math reverses at certain volume and pattern thresholds. Defaulting to the API without running the calculation costs money.

**That an AI workflow needs a framework.** Most agency-scale automation runs on the Claude API, an orchestrator (Make.com, n8n, Zapier), and a destination layer (Drive, ClickUp, email). Adding a framework adds complexity without adding capability for these use cases.

---

## Out of Scope

- Model wars, benchmark posts, capability shootouts (Claude vs. GPT vs. Gemini as a genre).
- Prompt engineering tips as a standalone content type.
- Generic AI hype takes (the angle is always practitioner reading, never industry commentary).
- AI ethics / policy as a primary topic.
- Building AI products for sale (Jonathan's position is operator, not builder).

---

## Surface Notes

- LinkedIn carousels: architectural concepts (the five components, layer hierarchy, hook enforcement decision tree).
- LinkedIn posts: sharp observations from production, AI release commentary filtered through workflow impact.
- Personal site Insights: long-form essays on Claude Code platform design and orchestration patterns.
- Personal site case studies: JonathanOS as a Claude Code architecture case, WISE Content Engine as a practical AI tooling case.
