import dspy


class PlannerSignature(dspy.Signature):
    """Plan which tool to use based on user query."""
    
    tools: str = dspy.InputField(desc="Available tools and their descriptions")
    history: str = dspy.InputField(desc="Conversation history")
    long_term_memory: str = dspy.InputField(desc="Relevant long-term facts")
    query: str = dspy.InputField(desc="Current user query")
    
    tool: str = dspy.OutputField(desc="Tool name to use")
    input: str = dspy.OutputField(desc="Input to pass to the tool")