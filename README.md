
# Local AI Orchestration Toolchain

An air-gapped, terminal-based AI orchestration environment built for Cloud Engineering, DevSecOps, and Financial Analysis workflows. This toolchain integrates local open-weight Large Language Models (LLMs) with a custom Python orchestration script (`weave`) and autonomous execution agents.

## 🚀 Features

* **Privacy-First Architecture:** 100% offline data processing using locally hosted models via Ollama. No telemetry, no API keys, and no data leaks.
* **Role-Based Execution (54 Patterns):** A library of 54 highly specialized prompt patterns injecting deep context for tasks like AWS Well-Architected reviews, OWASP security audits, CI/CD pipeline design, and Smart Money Concepts (SMC) quantitative trading analysis.
* **Seamless Terminal Integration:** Designed for Unix philosophy. Pipe logs, code, or configuration files directly into specialized AI personas via standard input (`stdin`).
* **Autonomous Agent Compatibility:** Integrates with Aider for automated codebase refactoring and Open Interpreter for live, permissioned system diagnostics and bash execution.

## 🛠️ Tech Stack

* **Core Logic:** Python 3.12, Bash
* **Engine:** Ollama (Local LLM Server)
* **Models:** `llama3.1` (General Reasoning/Architecture), `qwen2.5-coder:7b` (Deep Scripting/Refactoring)
* **Agentic Frameworks:** Open Interpreter (System/OS access), Aider (Git-aware pair programming)

## 📦 Installation

**1. Install Dependencies**
```bash
curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
pip install open-interpreter aider-chat --break-system-packages

```

**2. Pull Local Models**

```bash
ollama pull llama3.1
ollama pull qwen2.5-coder:7b

```

**3. Configure Weave CLI**

```bash
# Add weave to your local bin
chmod +x weave.py
ln -sf $(pwd)/weave.py ~/.local/bin/weave

# Ensure patterns directory exists
mkdir -p ~/.weave
cp -r patterns ~/.weave/

```

## 💻 Usage & Workflows

### 1. Rapid Text & Code Analysis (`weave`)

Use the custom CLI to pass files or strings into specific AI personas.

**AWS Infrastructure Review:**

```bash
cat cloudformation_template.yml | weave -p aws_review -m llama3.1

```

**Automated Code Review:**

```bash
cat app.py | weave -p code_review -m qwen2.5-coder:7b

```

### 2. Live System Diagnostics (Open Interpreter)

Inject a specific DevSecOps or SysAdmin pattern into Open Interpreter to grant the LLM permission to read system states and execute diagnostic commands.

```bash
interpreter --model ollama/llama3.1 \
  --no-llm_supports_functions \
  --custom_instructions "$(cat ~/.weave/patterns/security_audit.md)"

```

### 3. Autonomous Codebase Editing (Aider)

Launch an AI pair programmer directly into your git repository to squash bugs or build features autonomously.

```bash
aider --model ollama/qwen2.5-coder:7b

```

## 📂 Project Structure

```text
├── weave.py               # Main Python CLI orchestrator
├── README.md              # Project documentation
└── patterns/              # 54 Markdown-based context profiles
    ├── aws_free_tier_audit.md
    ├── devops_pipeline.md
    ├── frankenstein_setup.md
    ├── security_audit.md
    └── ...

```

## 🤝 Contributing

This toolchain is built for rapid, secure iteration. If you want to add new system patterns, simply create a new `.md` file in the `/patterns` directory detailing the Role, Context, and Output constraints.

```

```
