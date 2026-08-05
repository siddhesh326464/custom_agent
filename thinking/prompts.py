EXPANDER_PROMPT = f"""You are an expert researcher. The user wants to know: "{original_query}".
Generate exactly 3 distinct, highly targeted search queries to gather comprehensive data.
Return ONLY a JSON list of strings."""


SYNTHESIZER_PROMPT=f"""The user asked: "{original_query}"
        Here is the research data gathered from multiple sources:
        {aggregated_results}
        Synthesize this data into a clear, concise, and helpful response for the user.
        Do not include information that is not present in the research data."""