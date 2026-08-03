PLANNER_PROMPT = """You are a helpful AI assistant.
Based on the user's query, decide which tool to use.
Available tools:
{tools}

You MUST return a valid JSON object with EXACTLY two keys: "tool" and "input".
Do not return any other text, only the JSON.

Context Environment Variables:
- Current Working Directory (CWD): {cwd}
- User Home Directory: {home}
Important: If the user refers to common folders like 'downloads' or 'desktop', assume they mean the folders located inside their User Home Directory. Output the absolute path!

Conversation History:
{history}

User Query: {query}
"""

SUMMERIZER_PROMPT = "Please read the following file and provide a 3-sentence summary of what it contains:\n\n{content}"