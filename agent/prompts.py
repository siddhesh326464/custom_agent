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

IMPORTANT MEMORY RULE: If the user shares ANY personal information (name, age, location, preferences, habits, job, etc.), you MUST use the "remember fact" tool to store it. Format: "key | value" e.g. "user_name | Siddhesh". Always store first, answer after in follow-up turns.

Long-Term Memory (relevant facts about the user):
{long_term_memory}

Conversation History:
{history}

User Query: {query}
"""

SUMMERIZER_PROMPT = "Please read the following file and provide a 3-sentence summary of what it contains:\n\n{content}"