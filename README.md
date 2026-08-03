# Custom AI Agent Framework 🤖

A modular, from-scratch AI Agent framework built in Python. This project demonstrates the core mechanics of how modern LLM agents operate under the hood, completely bypassing heavy abstractions like LangChain or LlamaIndex.

By building the orchestration layer manually, this framework showcases a deep understanding of **State Management**, **Tool Execution**, **Session Memory**, and **ReAct (Reasoning and Acting) prompting strategies**.

## 🌟 Key Features

* **Zero-Abstraction Architecture**: Built entirely from scratch to understand and control the exact flow of data between the LLM and the tools.
* **Modular Tool Registry**: A scalable registry pattern that allows developers to dynamically register new tools without modifying the core agent logic.
* **Session Memory**: Implements short-term conversational memory, allowing the agent to retain context across multiple conversational turns.
* **State-Driven Routing**: Passes a unified `AgentState` object through the Planner and Executor nodes for clean, predictable execution (similar to LangGraph).
* **Groq Integration**: Powered by Groq API for lightning-fast inference.

## 🏗️ Architecture

```mermaid
graph TD
    User([User Input]) --> Main[Agent.run]
    
    subgraph Core Agent Loop
        Main -->|1. Gets Context| Mem[(Memory)]
        Main -->|2. Creates| State[{AgentState}]
        Main -->|3. Plans Action| Planner[Planner]
        
        Planner -.->|Reads| Reg[Tool Registry]
        Planner <-->|Prompts| LLM((Groq LLM))
        Planner -->|Writes Plan| State
        
        Main -->|4. Executes| Exec[Executor]
        Exec -.->|Routes to| Reg
        Exec -->|Writes Output| State
        
        Main -->|5. Saves Result| Mem
    end
    
    Reg --> Tools[[Tools: Calculator, FileSystem]]
    Main --> Result([Final Response])
```
The framework is broken down into distinct, decoupled components:

1. **`Planner`**: Takes the user's natural language query and the conversation history, analyzes the available tools, and outputs a structured JSON plan of action.
2. **`Executor`**: Parses the Planner's JSON output, safely executes the requested Python tools, and catches any runtime errors.
3. **`State` (`AgentState`)**: A Dataclass that holds the current query, planned actions, and final response for the current execution loop.
4. **`Memory`**: Manages the conversational context window, formatting recent interactions to inject into the LLM prompt.
5. **`Tool Registry`**: A centralized dictionary mapping tool names to actual Python classes, automatically generating tool descriptions for the LLM.

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* A [Groq API Key](https://console.groq.com/)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/siddhesh326464/custom_agent.git
cd custom_agent
```

2. Set up the virtual environment:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set your environment variables (create a `.env` file or `config.py`):
```python
# config.py
API_KEY = "your_groq_api_key_here"
MODEL_NAME = "llama3-70b-8192" # or whichever model you prefer
```

### Usage
Run the main script to start interacting with your agent in the terminal:
```bash
python main.py
```

### Example Interaction
```text
User: What is 150 * 5?
Agent: 750
User: Now divide that result by 10
Agent: 75.0
```

## 🗺️ Roadmap
Future plans for evolving this framework into a production-grade AI system:
- [ ] **Long-Term Memory (LTM)**: Integrating a Vector Database (e.g., ChromaDB) for semantic recall of past sessions.
- [ ] **Model Context Protocol (MCP)**: Adding an MCP client to dynamically consume external APIs and data sources.
- [ ] **Self-Healing / Reflection**: Implementing a feedback loop where the executor feeds runtime errors back to the planner for self-correction.
