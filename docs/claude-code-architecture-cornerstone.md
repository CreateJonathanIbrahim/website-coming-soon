# Claude Code Architecture: A Cornerstone Reference

**Compiled from:** Extended architectural design session, April 2026
**Author:** Jonathan Ibrahim
**Purpose:** Personal reference document capturing everything learned about
Claude Code architecture, best practices, and system design for production
content and automation workflows.

---

## Table of Contents

1. The Central Insight: What Claude Code Architecture Is Really About
2. The Sources That Shaped This Thinking
3. The Complete Folder Architecture
4. CLAUDE.md: The Foundation Layer
5. The Three-Tier Loading System
6. Hooks: Deterministic Enforcement
7. Path-Scoped Rules
8. Skills vs. Agents: The Most Misunderstood Distinction
9. The Layer 3 / Layer 4 Principle
10. The Audit Trail System
11. Context Window Management
12. MCP Configuration
13. The MWP Paper: Academic Grounding for the Architecture
14. Boris Cherny's Principles: What to Add to Your CLAUDE.md
15. Jake Van Clief's Voice Architecture
16. The Everything Claude Code Repository: What to Borrow
17. Principles That Govern All Future Decisions
18. Common Mistakes and Why They Happen
19. The Translation Map: Claude Code to Web Application
20. Decision Framework: When to Use What

---

## 1. The Central Insight: What Claude Code Architecture Is Really About

Everything in Claude Code architecture traces back to one problem: **context window management**. Claude has a finite context window. Everything loaded into it costs tokens and competes for attention. As context accumulates across a long session, performance degrades. Irrelevant earlier content crowds out the current task. The quality of output is directly tied to how focused and appropriately sized the context is at any given moment.

This means the question behind every architectural decision is not "how do I give Claude more information?" It is "what is the minimum necessary information, at exactly the right moment, for this specific task?"

The folder structure is the answer to that question. Not code. Not framework abstractions. The filesystem itself, when designed correctly, controls what enters Claude's context window, when it enters, and in what order. This is why the carousel, the MWP paper, and Jake Van Clief's practical work all arrive at the same conclusion from different directions: **the filesystem is the orchestration layer.**

A well-designed Claude Code project is not the project with the most thorough CLAUDE.md. It is the project where:

- Permanent orientation loads once at session start
- Domain-specific constraints load only when working in that domain
- Execution-specific context loads only for that specific task
- Nothing irrelevant is ever in the context window

Every design decision described in this document serves this principle.

---

## 2. The Sources That Shaped This Thinking

### Source 1: The Claude Code Folder Structure Carousel (Manthan Patel)

An Instagram carousel presenting the "Claude Code Starter Pack: 8 Files Every Project Should Ship With." The carousel laid out a complete folder architecture and explained the rationale behind each component. Its central claim: the filesystem is the orchestration layer. No coordination framework needed.

**Key components from the carousel:**

- CLAUDE.md: always-loaded operating manual, under 200 lines, a user message not a system prompt
- CLAUDE.local.md: personal machine-local overrides, gitignored, never shared
- .claude/rules/: path-scoped instruction fragments with YAML frontmatter glob patterns
- .claude/skills/: repeatable playbooks, each a folder with SKILL.md
- .claude/agents/: subagent definitions with isolated context, tools, and permissions
- .claude/hooks/: deterministic automation on lifecycle events
- settings.json: shared permissions and config, committed
- settings.local.json: personal config overrides, gitignored
- .mcp.json: MCP server roster, at project root (not inside .claude/)

**The carousel's critical distinction:** CLAUDE.md is a user message, not a system prompt. This means Claude reads it as context and acts on it at its discretion. It influences behavior but does not override Claude's core operation. This is why CLAUDE.md cannot be the place for enforcement. Enforcement belongs in hooks.

### Source 2: The MWP Paper (Jake Van Clief and David McDermott)

_"Interpretable Context Methodology: Folder Structure as Agent Architecture"_ — An academic paper presenting Model Workspace Protocol (MWP). The paper's core observation: for sequential workflows where a human reviews output at each step, multi-agent frameworks introduce engineering overhead the problem does not require. A numbered folder structure with plain markdown files can do the same coordination work.

**The paper's five-layer context hierarchy:**

- Layer 0: Global identity (~800 tokens) — "Where am I?"
- Layer 1: Workspace routing (~300 tokens) — "Where do I go?"
- Layer 2: Stage contract (200-500 tokens) — "What do I do?"
- Layer 3: Reference material (500-2k tokens) — "What rules apply?" (THE FACTORY)
- Layer 4: Working artifacts (varies) — "What am I working with?" (THE PRODUCT)

**The "lost in the middle" finding:** The paper cites Liu et al.'s research proving LLMs perform significantly worse when relevant information is buried in long contexts. A monolithic approach loading all stage instructions and prior outputs reaches 30,000 to 50,000 tokens, most of it irrelevant. Each focused MWP stage receives 2,000 to 8,000 tokens. Scoped architecture prevents degradation by construction.

**The multi-pass compiler analogy:** MWP stages map to compiler passes. Each pass reads the previous pass's output, transforms it, and writes an intermediate representation. Incremental recompilation means only re-running stages whose inputs changed. This framing provides a principled way to think about when to re-run which pieces of a pipeline.

**The edit-source principle:** Editing output fixes one run. Editing source fixes every future run. Recurring output edits are diagnostic data pointing to fixable source-level problems in skill files or reference material.

### Source 3: Boris Cherny's CLAUDE.md

A shared screenshot of Boris Cherny's personal CLAUDE.md showing his workflow orchestration principles. Key contributions:

- Self-improvement loop: after any correction, update a lessons file with the pattern
- Plan mode for non-trivial tasks (3+ steps or architectural decisions)
- Subagent strategy: use subagents liberally to keep main context window clean
- Stop-and-replan: if something goes sideways, stop immediately and re-plan
- Verification before done: never mark complete without proving it works
- The "Would a staff engineer approve this?" quality bar

### Source 4: Jake Van Clief's YouTube Video

The MWP paper author demonstrating his personal content production workflow. Key contributions:

- Arrived at the same tension you face: Claude app is simpler but VS Code is more powerful
- Voice document architecture: three files rather than one (tone/style, format patterns, constraints)
- The constraints file loads every time; the others load contextually
- Warning against locking content into concrete templates: direct toward concepts, not structures
- Confirmed the 200-line discipline for markdown files by example

### Source 5: The Everything Claude Code Repository (affaan-m)

159k-star open source repository of agents, skills, hooks, rules, and MCP configurations. The most relevant findings:

- article-writing and content-engine skills are worth reading for content production systems
- brand-voice skill exists and is worth comparing against your own voice files
- strategic-compact skill and token optimization settings are immediately applicable
- AgentShield runs as `npx ecc-agentshield scan` for a one-time security audit
- The coding-specific agents and language rules do not apply to content production systems

---

## 3. The Complete Folder Architecture

This is the canonical folder structure for a Claude Code project. Every component has a specific purpose. Nothing is decorative.

```
your-project/
│
├── CLAUDE.md                    ← Always loaded. Under 200 lines. User message,
│                                   not system prompt. Project operating manual.
├── CLAUDE.local.md              ← Gitignored. Personal machine-local overrides.
│                                   Active clients, personal shortcuts, tool prefs.
│                                   Not needed for solo work. Add when team expands.
│
├── .mcp.json                    ← MUST be at project root (not inside .claude/).
│                                   MCP server roster. Committed so team inherits.
│                                   Secrets via ${ENV_VAR} expansion, never hardcoded.
│
├── .claude/
│   ├── settings.json            ← Shared config. Committed. Permissions, model,
│   │                               hooks, env. Deny always wins.
│   ├── settings.local.json      ← Personal config. Gitignored.
│   │
│   ├── agents/                  ← Coordinators. Run in isolated context.
│   │   └── [agent-name].md         Return only summary to main session.
│   │                               Use when side task would pollute main context.
│   │                               YAML frontmatter with name, description, model,
│   │                               tools, allowed_paths, denied_tools.
│   │
│   ├── rules/                   ← Path-scoped fragments. Load automatically
│   │   └── [domain].md             when Claude touches matching files.
│   │                               YAML frontmatter with paths: glob patterns.
│   │                               No trigger phrase needed. Ambient constraints.
│   │
│   └── skills/                  ← Repeatable playbooks. Invoked by name.
│       └── [skill-name]/           Each skill is a folder with SKILL.md.
│           ├── SKILL.md            One task per skill.
│           └── references/         Reference material loaded when skill runs.
│               └── [ref].md
│
└── [project-specific dirs]
```

**The three tiers of loading:**

1. **Always loaded:** CLAUDE.md and hooks. Fire every session regardless.
2. **Conditionally loaded:** rules/ fragments, based on which files Claude touches.
3. **On-demand loaded:** skills/ and agents/, only when explicitly invoked.

---

## 4. CLAUDE.md: The Foundation Layer

### What It Is

The always-loaded project operating manual. Loads every Claude Code session without any trigger. It is a user message, not a system prompt. Claude reads it as context and acts on it at its discretion.

### What It Must Contain

- What the project is (2-3 sentences maximum)
- Folder structure and what each directory is for
- Trigger phrase vocabulary (the complete list of skill invocations)
- File naming conventions
- Output locations for each content type
- QA standards and hard gates
- When to stop and report (non-negotiable)
- Loading order for content production

### The 200-Line Discipline

This is a hard constraint, not a guideline. Beyond 200 lines, Claude begins to treat CLAUDE.md as background noise. The constraint forces the right behavior: if content cannot fit in 200 lines, it belongs in a more targeted location.

**Where overflow content belongs:**

- Path-scoped guidance → .claude/rules/ file
- Skill-specific reference → skills/[skill]/references/
- Client-specific context → clients/[client]/\_layer-map.md
- Stage-specific instructions → \_stage-context.md in the working folder

### What CLAUDE.md Is Not

- A system prompt (Claude can choose to deprioritize parts of it)
- The place for enforcement (hooks enforce, CLAUDE.md guides)
- A comprehensive manual (it is orientation, not documentation)
- A dumping ground for everything Claude might need

### The Stop-and-Replan Instruction (Must Include)

Derived from Boris Cherny's principle:

> If anything unexpected is encountered during a pipeline run or manual skill execution, STOP immediately and report. Do not improvise, infer, or continue past an unresolved condition. Report: which step failed, what the expected state was, what was actually found, what a human needs to do before proceeding.

---

## 5. The Three-Tier Loading System

Understanding this is the difference between a good Claude Code project and an excellent one.

### Tier 1: Always Loaded (Every Session)

**What:** CLAUDE.md, hooks
**When:** Every session, every task, no exceptions
**Purpose:** Permanent orientation and deterministic enforcement
**Design principle:** Keep it minimal. Every token here costs on every session.

### Tier 2: Conditionally Loaded (Path-Triggered)

**What:** .claude/rules/ files
**When:** Claude touches a file matching the rule's glob pattern
**Purpose:** Domain-specific constraints that load without being invoked
**Design principle:** Write rules for domains that have consistent constraints, not for one-off situations.

**Example:** A rule for `clients/*/blog/articles/**` that loads the four NLP hard gates automatically whenever Claude is working in a blog article folder. The team member running the full-auto pipeline benefits from it just as much as someone doing manual step-by-step work. Neither has to do anything differently.

### Tier 3: On-Demand Loaded (Explicitly Invoked)

**What:** skills/ and agents/
**When:** Explicitly triggered by the user or by an agent
**Purpose:** Repeatable playbooks and coordinated multi-step execution
**Design principle:** Skills do one thing. Agents coordinate multiple things doing one thing each.

---

## 6. Hooks: Deterministic Enforcement

### The Most Critical Architectural Distinction

CLAUDE.md suggests. Hooks enforce. This is the most important sentence in Claude Code architecture.

Everything in CLAUDE.md, everything in rules/ files, everything in skill instructions: Claude reads these and acts on them at its discretion, with varying attention depending on context, session length, and competing priorities. Hooks bypass all of this. They are shell scripts and commands that fire on lifecycle events deterministically. Claude cannot choose not to run a hook.

This means hooks are the only component in the entire architecture where you can guarantee something happens. Everything else is guidance. Hooks are enforcement.

### The Four Lifecycle Events

**PreToolUse:** Fires before any tool use (Bash commands, file writes, etc.)

- Use for: blocking destructive operations, safety checks, secret scanning
- Example: grep for `rm -rf` and `git push --force` before any Bash command. Exit 2 to block. Exit 0 to allow.

**PostToolUse:** Fires after any tool use

- Use for: automatic QA, formatting, validation, scanning output for markers
- Example: After every Write or Edit, route the written file path to the appropriate validation script.

**SessionStart:** Fires when a Claude Code session opens

- Use for: surfacing active context, orienting Claude to current project state
- Example: Scan the clients/ directory, surface the most recently modified client, print an inventory of what pipeline outputs exist.

**Stop:** Fires when the session ends

- Use for: summary reports, flagging unresolved issues, audit aggregation
- Example: Scan for files modified in the last 6 hours, group by client, scan for FAIL markers, surface anything that needs human review.

### The Dispatcher Pattern

Rather than one hook per validation script, use a single dispatcher that reads the filename and routes to the correct script. This is more maintainable and extends naturally as new output types are added.

```python
# dispatch-validator.py receives the file path just written
# Routes to validate_brand_guide.py, nlp_threshold_check.py, etc.
# Also scans for FAIL: and REVIEW: markers
# Also reads _audit.md files and surfaces FAIL/BLOCK entries
```

### Hook Runtime Controls (from ECC)

Environment variables for tuning without editing hook files:

```bash
export ECC_HOOK_PROFILE=minimal|standard|strict
export ECC_DISABLED_HOOKS="hook-id-1,hook-id-2"
```

### What Belongs in Hooks vs. CLAUDE.md

| Situation                                | Where It Belongs     |
| ---------------------------------------- | -------------------- |
| Must happen every time without exception | Hooks                |
| Should happen but Claude can adapt       | CLAUDE.md or rules/  |
| Prevents data loss or security issues    | Hooks (PreToolUse)   |
| Surfaces quality issues after writing    | Hooks (PostToolUse)  |
| Orients Claude to project state          | Hooks (SessionStart) |
| Reports session results                  | Hooks (Stop)         |
| Explains what the project is             | CLAUDE.md            |
| Defines file conventions                 | CLAUDE.md            |
| Provides skill invocation vocabulary     | CLAUDE.md            |
| Domain-specific quality standards        | rules/ files         |

---

## 7. Path-Scoped Rules

### What They Are

Short instruction fragments in .claude/rules/ that load automatically based on glob patterns. They require no trigger phrase. They are ambient constraints that fire when Claude touches files matching their pattern.

### The YAML Frontmatter Format

```yaml
---
paths:
    - 'clients/*/blog/articles/**'
    - 'clients/*/blog/topical-map.csv'
---
```

### The Critical Distinction From Skill References

Skill reference files load when a skill is explicitly invoked.
Rules files load based on where Claude is working, regardless of which skill triggered the work.

A team member running a full-auto pipeline gets the same rules benefits as someone doing manual step-by-step work. Neither has to do anything differently. The rules fire based on filesystem location, not on user intent.

### Design Principles for Rules Files

**Scope by domain, not by task.** A rules file for `clients/*/blog/articles/**` covers everything that happens in blog article folders: pre-write brand checks, post-write alignment verification, NLP gate requirements, humanizer requirements. It does not cover only one of these things.

**Write as direct instructions to Claude.** "Before writing any copy.md, confirm you have read the following three files." Not "The writer should read brand files." Second person, imperative mood.

**Keep under 200 lines.** Same discipline as CLAUDE.md. If a rules file is bloating, the detailed reference material belongs in a skill references/ file instead.

**REVIEW: marker format.** Any REVIEW: markers mentioned in rules files must use the exact format: the word REVIEW followed by a colon, then a specific description, inline in the content file before saving. This allows hook dispatchers to scan for them consistently.

### Example Rules Architecture (Five Files)

For the WISE Content Engine:

1. **blog-content.md** — paths: `clients/*/blog/articles/**` — NLP hard gates, page type logic, humanizer requirement, brief alignment check
2. **website-content.md** — paths: `clients/*/website/pages/**` — brand check requirement, copy-to-brief alignment, sitemap status update rules, allowed status values
3. **brand-assets.md** — paths: `clients/*/brand/**` — nine required brand guide sections, source doc dependency chain, read-only protection for intake/ files
4. **skill-authoring.md** — paths: `skills/**` — no edits during production, branch naming convention, VERSION and CHANGELOG requirements
5. **client-setup.md** — paths: `clients/*/_client.md` — TES placeholder detection with hard stop, required field validation

---

## 8. Skills vs. Agents: The Most Misunderstood Distinction

### The Fundamental Difference

**A skill does one thing.**
A skill is a repeatable, callable playbook for a specific, well-defined task. It has defined inputs, a defined process, and defined outputs. It executes. It does not coordinate.

**An agent coordinates multiple things doing one thing each.**
An agent plans, sequences, delegates, verifies, and reports. It reads the project structure to understand what needs to happen, delegates execution to subagents or skills, and returns a summary to the main session. It does not execute the work itself.

### Why This Distinction Matters

When the WISE Content Engine pipeline orchestrator lived in skills/, it made a false claim about what it was. The orchestrator coordinates 6+ skill steps across a 60-90 minute run. That is an agent by function, not a skill.

The practical cost: the orchestrator ran in the main Claude Code session, accumulating context across all steps. By page 8 of a 12-page site, Claude was carrying the full brand guide read at page 1, every brief and copy file from preceding pages, every sitemap update, every intermediate thought from the entire run. Quality degraded on later pages.

When the orchestrator moved to .claude/agents/, each skill step became a subagent call with its own isolated context window. The brand guide generator ran with just source docs and skill instructions. The copy writer ran with just brief and brand guide. None carried accumulated weight from prior steps. Pages 10, 11, and 12 came out as well as pages 1, 2, and 3.

### The Test for Agent vs. Skill

Ask: does this component do one thing, or does it manage multiple things doing one thing each?

If it does one thing → skill in skills/
If it manages multiple things → agent in .claude/agents/

### Agent Definition Format

```yaml
---
name: pipeline-orchestrator
description: Full website content pipeline. Reads client folder structure,
  sequences all website-track skills, delegates to subagents, writes
  completion report. Invoke: Run full website pipeline for [client]
model: claude-opus-4-5
tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(python scripts/*)
  - Bash(git add*)
  - Bash(git commit*)
  - Bash(git status)
allowed_paths:
  - clients/**
  - scripts/**
denied_tools:
  - Bash(rm -rf*)
  - Bash(git push --force*)
  - Write(skills/**)
  - Write(.claude/**)
---
```

### The Two-Tier Model Pattern

Both the carousel and the MWP paper describe this. The orchestrator runs on a more capable model (Opus 4) for planning, sequencing, and decision-making. Individual skill execution steps run on faster models (Sonnet 4.5) for well-defined transformation tasks. Match model capability to task type. Coordination demands capability. Execution demands speed and cost efficiency.

### Skip Logic for Re-Run Safety

Every agent that runs a multi-step pipeline must check whether each expected output already exists before delegating a step. If brand-guide.md exists and is non-empty, skip Skill 1. If a page has HUMANIZED status in the sitemap, skip it. This allows re-triggering the pipeline midway through a run without duplicating completed work.

---

## 9. The Layer 3 / Layer 4 Principle

### The Core Distinction

This is the MWP paper's most practically useful concept, and the one most absent from typical Claude Code projects.

**Layer 3: The Factory (stable reference, internalize as constraints)**
Files that are configured once and remain stable across every pipeline run. Claude should read these and treat them as rules that govern everything it produces.

Examples: brand-guide.md, \_client.md, visual-style.md, \_sitemap.md, topical-map.csv, voice/tone-and-style.md, voice/constraints.md

**Layer 4: The Product (per-run artifacts, process as input/output)**
Files that are created or consumed during a specific pipeline execution. Claude should read these as raw material to transform or as the output it is writing.

Examples: brief.md, copy.md, article.md, nlp-report.md, page-layout.md, source distillation files

### Why Mixing Them Causes Problems

When Claude has brand-guide.md and brief.md in context simultaneously without structural signals about their roles, it has to sort out the difference on its own. Brand-guide.md is a constraint (write inside these rules). Brief.md is an input (transform this into copy). Without explicit structural differentiation, Claude occasionally treats them as equivalent, producing copy that technically follows the brief but drifts from brand voice.

### The Implementation: Routing Files

**\_layer-map.md at the project or client root**
The first file Claude reads when entering a project or client folder. Contains two explicit tables: Layer 3 files with their purpose and how Claude should treat them (as constraints), and Layer 4 file patterns with their role and how Claude should treat them (as inputs to transform or outputs to write).

Also defines a mandatory loading order:

1. \_layer-map.md (this file)
2. Stable reference files (Layer 3)
3. Then and only then: the specific working files for the current task

**\_stage-context.md inside each working folder**
A stage-level routing file inside each individual page or article folder. Tells Claude exactly what it is doing in this specific folder. Contains:

- The constraint layer with explicit relative paths to stable reference files
- The input layer identifying the brief as the specification to transform
- The output layer identifying what files to write and where
- A completion checklist with specific pass/fail criteria

### Relative Path Discipline

Stage context files use relative paths, not absolute paths. From a website page folder (clients/[client]/website/pages/[slug]/), the brand guide is at:

```
../../../brand/brand-guide.md
```

This makes client folders portable. Any client folder copied from the template inherits correct relative paths automatically.

---

## 10. The Audit Trail System

### The Problem It Solves

Without structured verification, skill handoffs have no active quality check. Skill 3 writes brief.md. Skill 4 reads brief.md and writes copy.md. But Skill 4 does not actively confirm that copy.md delivered what brief.md specified. Quality problems at delivery are difficult to trace. The Humanizer produces an unstructured log. The NLP analyzer produces a report. REVIEW: markers exist in rules files. These are three different formats in three different files with no common schema.

### The Multi-Pass Compiler Analogy Applied

Multi-pass compilers emit structured diagnostics at each pass: what was found, what was transformed, what the next pass should know. Each skill in a production pipeline should do the same.

### The Three Components

**audit-checks.py (verification engine)**
Performs content verification checks before and after skill execution. Check types:

- `brief-input`: verifies brief.md contains required fields before copy production begins
- `copy-output`: verifies copy.md meets brief.md specifications after writing
- `article-output`: same as copy-output for articles
- `brand-guide-output`: verifies nine required sections are present
- `humanizer-output`: verifies humanization completed and scans for remaining AI phrases
- `nlp-gate`: verifies four hard gates against nlp-report.md
- `layout-output`: verifies page-layout files exist and are valid JSON

Exits with code 0 for pass/warn. Exits with code 1 for any FAIL or BLOCK.

**audit-writer.py (record keeper)**
Writes structured audit entries to \_audit.md in the working folder. Append-only — never overwrites. Maintains a history of every skill execution for that piece of content. Entry format:

```
## Skill Name — skill-slug
Date: YYYY-MM-DD HH:MM
Status: PASS | PASS_WITH_WARNINGS | WARN | FAIL | BLOCK
Checks:
  - [PASS] Primary keyword in H1: confirmed
  - [WARN] Word count 1,142 — 14% above brief target of 1,000
  - [FAIL] CTA type from brief not found in copy
```

**\_audit.md (cumulative pipeline record)**
Lives inside each page or article folder. Accumulates entries from each skill execution, creating a full history of every stage's verification results. When a piece of content comes back with a quality issue, open \_audit.md and trace exactly when and where the drift happened.

### The Severity Hierarchy

| Level | Meaning                               | Action                                              |
| ----- | ------------------------------------- | --------------------------------------------------- |
| BLOCK | Critical failure, do not write output | Stop execution before writing file                  |
| FAIL  | Output written but has problems       | Write file, add REVIEW: marker at top, log in audit |
| WARN  | Minor issue, output acceptable        | Write file, log in audit, no marker                 |
| INFO  | Informational only                    | Log in audit, no action                             |

This hierarchy must be consistent across all scripts and all skill audit blocks.

### Integration with Hooks

The PostToolUse dispatcher detects \_audit.md writes and surfaces FAIL/BLOCK entries immediately. The Stop hook session-summary.py aggregates audit results across all \_audit.md files modified in the session, producing a session-level summary of total PASS, WARN, and FAIL counts and listing pages requiring attention.

### Audit Trail Protocol in Skill Files

Each skill file receives an appended "Audit Trail Protocol" section (not modifying existing content). This section defines:

- Whether to run pre-write input verification (skills that consume upstream output)
- The exact commands to run (audit-checks.py then audit-writer.py)
- How to interpret the exit code
- What to do if BLOCK or FAIL is returned

---

## 11. Context Window Management

### The Numbers That Matter

From the MWP paper (confirmed empirically):

- A focused MWP stage: 2,000 to 8,000 tokens
- A monolithic approach loading everything: 30,000 to 50,000 tokens
- Performance degrades significantly above ~8,000 tokens for retrieval tasks
- Each MCP tool definition consumes tokens. Too many active MCPs reduce effective context from 200k to ~70k

### Token Optimization Settings (from ECC)

Add to .claude/settings.json or ~/.claude/settings.json:

```json
{
    "model": "sonnet",
    "env": {
        "MAX_THINKING_TOKENS": "10000",
        "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50",
        "CLAUDE_CODE_SUBAGENT_MODEL": "sonnet"
    }
}
```

Rationale:

- `model: sonnet` — ~60% cost reduction; handles 80%+ of tasks
- `MAX_THINKING_TOKENS: 10000` — reduces hidden thinking cost by ~70%
- `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: 50` — compacts earlier, better quality in long sessions

Switch to Opus only for complex architectural decisions or deep reasoning tasks.

### Strategic Compaction

The strategic-compact skill (from ECC) suggests running `/compact` at logical breakpoints rather than relying on auto-compaction at 95% context.

**When to compact:**

- After research/exploration phase, before implementation
- After completing a major milestone, before starting the next
- After a debugging session, before continuing feature work
- Between major pipeline stages (after brand guide, before per-page loop)

**When NOT to compact:**

- Mid-implementation (you lose variable names, file paths, partial state)
- In the middle of a skill execution
- When the agent needs the previous step's output to continue

### MCP Server Management

Keep under 10 MCPs enabled per project. Keep under 80 tools active. Use `disabledMcpServers` in project settings.json to disable unused ones:

```json
{
    "disabledMcpServers": ["supabase", "railway", "vercel"]
}
```

---

## 12. MCP Configuration

### Critical Rule: .mcp.json Lives at Project Root

The carousel is explicit. .mcp.json must be at the project root, not inside .claude/. Committing it means the entire team gets the tool roster automatically.

```json
{
    "mcpServers": {
        "google-drive": {
            "command": "npx",
            "args": ["-y", "@google/mcp-server-drive"],
            "env": {
                "GOOGLE_OAUTH_TOKEN": "${GOOGLE_OAUTH_TOKEN}"
            }
        }
    }
}
```

**Secrets never go in .mcp.json.** The `${ENV_VAR}` syntax expands from your shell environment at launch. The file is safe to commit. The actual credentials live in environment variables.

### The Distinction Between MCP and MWP

The MWP paper makes this explicit: MCP (Model Context Protocol) standardizes how models access external tools and data sources. MWP addresses how to structure and deliver context to an agent across a multi-stage workflow. The two are complementary. An MWP stage might use MCP connections to access external services, while the stage's folder structure determines what context the agent receives when doing so.

---

## 13. The MWP Paper: Academic Grounding for the Architecture

### Core Design Principles (Verbatim)

**One stage, one job.** Each stage handles a single step of the workflow. A stage that fetches data does not also filter it. A stage that filters does not also format the output.

**Plain text as the interface.** Stages communicate through markdown and JSON files. No binary formats, no database connections, no proprietary serialization. Any tool that can read a text file can participate in the workflow. Any human who can open a text editor can inspect or modify any artifact.

**Layered context loading.** Agents load only the context they need for the current stage. Prevention rather than compression.

**Every output is an edit surface.** The intermediate output of each stage is a file a human can open, read, edit, and save before the next stage runs. The human works with visible, manipulable objects, and the system picks up whatever the human left there.

**Configure the factory, not the product.** A workspace is set up once with preferences, brand, style, and structural decisions. After that, each run of the pipeline produces a new deliverable using the same configuration.

### Where MWP Works and Where It Does Not

**Works for:**

- Sequential multi-step workflows
- Human-reviewed output at each stage
- Repeatable pipelines running regularly with different input
- Content production, training material, academic research, policy analysis

**Does not work for:**

- Real-time multi-agent collaboration with tight message-passing loops
- High-concurrency systems with many simultaneous users
- Workflows requiring complex automated branching based on AI decisions mid-pipeline

### The Observability Insight

The most useful property of the MWP architecture may be one that was not designed as a feature. Because every intermediate output is a plain file, the system is observable by default. There is no logging layer to build, no dashboard to configure, no special tooling to inspect pipeline state. You open a folder and read the files.

---

## 14. Boris Cherny's Principles: What to Add to Your CLAUDE.md

### The Six Workflow Orchestration Principles

**1. Plan Mode Default**
Enter plan mode for any non-trivial task (3+ steps or architectural decisions). Write detailed specs upfront to reduce ambiguity. Use plan mode for verification steps, not just building.

**2. Subagent Strategy**
Use subagents liberally to keep the main context window clean. Offload research, exploration, and parallel analysis to subagents. One task per subagent for focused execution.

**3. Self-Improvement Loop**
After any correction from the user, update a lessons file with the pattern. Write rules for yourself that prevent the same mistake. Review lessons at session start for the relevant project.

This is the practical implementation of the MWP paper's edit-source principle: recurring corrections are diagnostic data, not one-off events.

**4. Verification Before Done**
Never mark a task complete without proving it works. Ask yourself: "Would a staff engineer approve this?" Run tests, check logs, demonstrate correctness.

**5. Demand Elegance (Balanced)**
For non-trivial changes, pause and ask "is there a more elegant way?" If a fix feels hacky: "Knowing everything I know now, implement the elegant solution." Skip this for simple, obvious fixes.

**6. Autonomous Bug Fixing**
When given a bug report, fix it. Do not ask for hand-holding. Point at logs, errors, failing tests, then resolve them.

### The Task Management Pattern

A pattern worth adding to complex projects: maintain a tasks/todo.md with checkable items. The pattern:

1. Write plan to tasks/todo.md with checkable items
2. Check in before starting implementation
3. Mark items complete as you go
4. Add high-level summary at each step
5. Add review section to tasks/todo.md
6. Update tasks/lessons.md after corrections

For the WISE Content Engine, the pipeline orchestrator writes a \_todo.md at pipeline start and marks items complete as steps finish.

### The "Would a Staff Engineer Approve This?" Quality Bar

Reframe for content production: "Would a senior content strategist with full knowledge of the client's brand and the WISE production standards approve this?"

Apply before presenting any skill file edit, new skill file, or audit protocol section as complete.

---

## 15. Jake Van Clief's Voice Architecture

### The Three-File Voice System

The key insight: one large voice document is wrong. Break it into three files with different loading contexts.

**File 1: tone-and-style.md (how you think and communicate)**
Not rules about what words to use. Descriptions of the underlying intellectual moves you make. How you enter a topic. How you handle authority. What you value in communication. What makes your voice distinct. Written as descriptions, not prescriptions.

**File 2: format-patterns.md (structural rules per format)**
How a carousel differs from a post. How a short-form piece differs from long-form. The structural guidance for each format without dictating content. This file prevents the generic "Problem / Solution / Benefit / CTA" pattern that makes content recognizable as AI-assisted.

**File 3: constraints.md (never-do-this list)**
This file loads every time, for every piece of content. The others load contextually. Constraints include specific prohibited phrases, structural patterns to avoid, and formatting rules. Specific enough that Claude reading it for the first time would produce content that reads differently from generic AI content.

### The Pillar Architecture

Pillars describe thematic territories, not content templates. The goal: direct Claude toward concepts, not lock it into structures. A pillar file says what territory to operate in. It does not dictate how to write.

Pillars contain:

- Core concepts in this territory
- Your specific position (what differentiates your perspective)
- What the audience typically gets wrong that you can correct
- Content potential (what angles live in this territory)

### The 100-Line Discipline

Van Clief's observation: files over 100 lines probably need to be broken down further. Could be broken apart more into thought process because the whole goal of these markdown files is to break apart thinking itself. Separation of concerns applied to cognition.

### The Content Warning About AI Voice Files

When AI analyzes your voice without you writing about your voice, it writes about your voice in a way that an AI would write about your voice. Even the best models struggle with this. If you want accurate voice characteristics, write or at least voice-to-text them yourself. The AI can organize and structure, but the raw characterization should come from you.

---

## 16. The Everything Claude Code Repository: What to Borrow

### Immediately Applicable

**Token optimization settings:**

```json
{
    "model": "sonnet",
    "env": {
        "MAX_THINKING_TOKENS": "10000",
        "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50",
        "CLAUDE_CODE_SUBAGENT_MODEL": "haiku"
    }
}
```

**AgentShield security audit (one-time):**

```bash
npx ecc-agentshield scan
```

Scans CLAUDE.md, settings.json, MCP configs, hooks, agent definitions, and skills. Run after the system is built before using it on real client data.

**Strategic-compact skill:** Defines when to run /compact during long sessions. The decision framework maps directly to pipeline stage boundaries.

### Skills Worth Reading Before Building Your Own

- `article-writing` — long-form writing without generic AI tone
- `content-engine` — multi-platform content and repurposing workflows
- `brand-voice` — source-derived writing style profiles

Compare these against your own implementations. Borrow what is better. Keep what is more domain-specific.

### What Does Not Apply to Content Production Systems

- The 48 coding-specific agents (code reviewer, build error resolver, TDD guide, etc.)
- Language-specific rules directories (TypeScript, Python, Go, Swift, PHP)
- The continuous learning v2 instinct extraction system
- The PM2 multi-service orchestration commands
- The E2E testing and CI/CD infrastructure

---

## 17. Principles That Govern All Future Decisions

These are the principles to apply before making any architectural change to a Claude Code project.

### Principle 1: Load the Minimum Necessary Context at the Exact Right Moment

Before adding anything to CLAUDE.md, a rules file, or a stage context file, ask: does this need to be here, or is there a more targeted location? What is the cost in tokens per session of having this here? Is there a more specific location where it would load only when relevant?

### Principle 2: Deterministic Enforcement Belongs in Hooks. Guidance Belongs in Markdown.

If something must happen every time without exception, it belongs in hooks. If it should happen but can be adapted, it belongs in CLAUDE.md or rules/. Never rely on markdown files for things that cannot be optional.

### Principle 3: Edit Source, Not Output

When a piece of output is edited before delivery, ask whether the edit reveals a fixable problem in a skill file, a reference file, or a stage instruction. A one-time edit to copy.md fixes one page. An update to the content-creation-engine's writing-engine.md reference file fixes every page from that skill forward.

The audit trail exists to surface patterns that point to source-level fixes. Three consecutive sessions where you make the same type of edit to the same type of output means you need to update the source, not the output.

### Principle 4: Skills Do One Thing. Agents Coordinate.

Any component that manages multiple things doing one thing each is an agent and belongs in .claude/agents/. Any component that executes one well-defined task is a skill and belongs in skills/.

### Principle 5: The Folder Structure Is the Orchestration Logic

A well-designed folder structure tells the orchestrator what to do. The \_layer-map.md tells Claude what role each file plays. The \_sitemap.md tells the orchestrator what pages need work. The \_stage-context.md tells the orchestrator what to delegate and what context to provide. When the orchestrator reads the folder structure to plan its work, improving the folder structure automatically improves the orchestrator's behavior.

### Principle 6: Every Intermediate Output Is an Edit Surface

Any file Claude writes should be readable and editable by a human before the next stage runs. If a stage's output cannot be opened, read, and understood by a non-technical person, the stage is not producing the right intermediate representation.

### Principle 7: Plain Text Is the Universal Interface

Stages communicate through markdown and JSON. No binary formats, no proprietary serialization, no database connections required to inspect state. Any tool that can read a text file can participate in the workflow.

---

## 18. Common Mistakes and Why They Happen

### Mistake 1: Treating CLAUDE.md as a System Prompt

**What happens:** CLAUDE.md grows to 500+ lines with everything Claude might need to know. Claude treats it as background noise.

**Why it happens:** The intuition that more instructions produce better behavior. In reality, bloat degrades performance.

**The fix:** 200-line discipline. Everything that overflows goes to a more targeted location.

### Mistake 2: Putting the Orchestrator in Skills

**What happens:** The pipeline runs in the main session context, accumulating all prior steps. Quality degrades on later pages.

**Why it happens:** The orchestrator is invoked by a trigger phrase, which looks like a skill invocation. But what it does is agent behavior.

**The fix:** Apply the test. Does this component do one thing, or manage multiple things? If the latter, it is an agent.

### Mistake 3: Relying on CLAUDE.md for Enforcement

**What happens:** CLAUDE.md says "never modify skill files during a production session." A team member asks Claude to fix a skill during a production run. Claude does it.

**Why it happens:** CLAUDE.md is guidance, not enforcement. Claude can deprioritize parts of it under pressure.

**The fix:** Hooks for enforcement. A PreToolUse hook that blocks writes to skills/ during a production session cannot be overridden by user request.

### Mistake 4: One Large Voice Document

**What happens:** The voice document is 300 lines and covers everything. It loads every session at full cost. Claude produces content that sounds vaguely like the voice but misses the nuances because the relevant constraints are buried in the middle.

**Why it happens:** It feels thorough. More is more.

**The fix:** Three files. Constraints load every time. Tone and format load contextually. Specific constraints are specific enough to actually prevent the unwanted patterns.

### Mistake 5: No Layer 3/Layer 4 Distinction

**What happens:** Claude receives brand-guide.md and brief.md in the same context without structural signals. It occasionally treats them as equivalent, producing copy that follows the brief but drifts from brand voice.

**Why it happens:** No explicit routing file distinguishes stable constraints from per-run inputs.

**The fix:** \_layer-map.md at project root. \_stage-context.md in each working folder. Explicit loading order that puts stable reference files first, every time.

### Mistake 6: No Audit Trail

**What happens:** Quality problems at delivery cannot be traced. The same types of errors recur because there is no record of where they originated.

**Why it happens:** Audit infrastructure feels like overhead before you need it.

**The fix:** audit-checks.py + audit-writer.py producing \_audit.md in each working folder. The overhead is low. The diagnostic value when something goes wrong is high.

### Mistake 7: Context Accumulation in Long Pipeline Runs

**What happens:** A 12-page pipeline run produces excellent pages 1-4 and degraded pages 9-12.

**Why it happens:** The main session context accumulates every brand guide, brief, and copy from all preceding pages. By page 9, the context is dominated by irrelevant prior work.

**The fix:** Orchestrator as agent. Each skill step as an isolated subagent with scoped context. The orchestrator delegates rather than executing. Each subagent starts clean.

---

## 19. The Translation Map: Claude Code to Web Application

If and when the system needs a web frontend, nothing built in Claude Code is wasted. Every component translates.

| Claude Code Component      | Web Application Equivalent                    |
| -------------------------- | --------------------------------------------- |
| CLAUDE.md                  | Base system prompt loaded on every API call   |
| skills/[skill]/SKILL.md    | Skill system prompts loaded per execution     |
| skills/[skill]/references/ | Reference context injected into skill prompts |
| .claude/rules/ files       | Context injected based on content type        |
| .claude/agents/            | Server-side orchestration functions           |
| hooks/                     | API middleware and database event triggers    |
| \_client.md                | clients table in database                     |
| brand-guide.md             | client_brand_assets table (text column)       |
| \_sitemap.md               | website_pages table with status column        |
| brief.md / copy.md         | content_outputs table (versioned rows)        |
| \_audit.md                 | audit_entries table in database               |
| Python validation scripts  | JavaScript validation functions (server-side) |

The skill instruction files are the hardest thing to write and they are already written. The engineering work of a web application is substantial but it is well-defined. You are not starting from scratch on the intelligence layer.

**The recommended build sequence for a web application:**

1. Prove the Claude API integration works with one skill (brand guide generator)
2. Get streaming working and producing consistent output
3. Add auth and one protected route
4. Build the minimal UI that consumes the working skill
5. Everything after follows naturally

**The honest assessment of web application scope:**
10-12 weeks of work at 15-20 hours per week. The risk is not the UI work. The risk is the Claude API integration producing inconsistent results. Prove that out first before committing to the full build.

---

## 20. Decision Framework: When to Use What

### Should this go in CLAUDE.md or a rules/ file?

If it needs to load for every task regardless of what files Claude is working with → CLAUDE.md

If it only needs to load when Claude is working in a specific part of the project → rules/ with a glob pattern

### Should this be a skill or an agent?

If it executes one well-defined task with specific inputs and outputs → skill in skills/

If it plans, sequences, delegates, or coordinates multiple steps → agent in .claude/agents/

### Should this go in hooks or in markdown?

If it must happen without exception regardless of Claude's interpretation → hooks

If it should happen but Claude can adapt based on context → markdown (CLAUDE.md or rules/)

### Should this go in a voice file or a constraints file?

If it describes how you think and communicate (positive characterization) → voice/tone-and-style.md

If it describes structural patterns for a specific format → voice/format-patterns.md

If it is something that must never appear in any output → voice/constraints.md (loads every time)

### Should this be Layer 3 or Layer 4?

If it is stable across all runs, used as a constraint governing the output → Layer 3 (stable reference)

If it is unique to this specific execution, used as input to transform → Layer 4 (working artifact)

### Should I build a custom API system or use Claude's subscription tools?

If the goal is value creation through the technology rather than building the technology → subscription

If you have a specific niche capability that requires custom control → API

If clients will use the system themselves, convincing them to get their own subscription is more economically and operationally efficient than managing API billing across many clients.

---

## Appendix: Quick Reference Checklists

### Before Creating a New CLAUDE.md

- [ ] Is it under 200 lines?
- [ ] Does it include the full trigger phrase vocabulary?
- [ ] Does it include the stop-and-replan instruction?
- [ ] Does it define the loading order for content production?
- [ ] Does it avoid duplicating content that belongs in rules/ files?
- [ ] Is it written as instructions to Claude (second person, imperative)?

### Before Creating a New Skill

- [ ] Does it do exactly one thing?
- [ ] Does it have defined inputs, a defined process, and defined outputs?
- [ ] Does it have an Audit Trail Protocol section?
- [ ] Are references/ files specific to this skill's execution?
- [ ] Is there a VERSION file and CHANGELOG.md in the skill directory?

### Before Creating a New Agent

- [ ] Is this definitely an agent (coordinates multiple things) and not a skill (does one thing)?
- [ ] Does the YAML frontmatter include model, tools, allowed_paths, and denied_tools?
- [ ] Does it have skip logic for re-run safety?
- [ ] Does it delegate to subagents rather than executing steps itself?
- [ ] Does it write a completion report?

### Before Creating a New Rules File

- [ ] Are the glob patterns specific enough to not over-fire?
- [ ] Is it under 200 lines?
- [ ] Is it written as direct instructions to Claude (second person)?
- [ ] Does it reference REVIEW: markers in the exact standard format?
- [ ] Is detailed reference material in a skill references/ file rather than here?

### Before Running a Production Pipeline

- [ ] Does brand-guide.md exist and pass validation?
- [ ] Does \_client.md exist with no placeholder values?
- [ ] Do source-docs exist in the appropriate directory?
- [ ] Does \_layer-map.md exist at the client root?
- [ ] Are all voice files present (for personal content systems)?
- [ ] Is the orchestrator agent properly scoped with denied_tools for skill/ and .claude/ writes?

---

## Final Note

The architecture described in this document is not theoretical. Every component was designed to solve a specific, observed problem in production use. The 200-line CLAUDE.md discipline prevents context bloat that causes quality degradation. The rules/ loading system ensures QA standards apply without human remembering to invoke them. The agent vs. skill distinction prevents context accumulation in long pipeline runs. The Layer 3/Layer 4 distinction ensures Claude treats constraints and inputs appropriately. The audit trail makes quality problems traceable rather than mysterious.

The underlying principle behind all of it: the filesystem is the orchestration layer. When the folder structure is designed correctly, it controls what enters Claude's context window, when it enters, and in what order. Folder structure is not an administrative decision. It is the primary engineering decision in a Claude Code project.

Build with that principle at the center and the rest follows.
