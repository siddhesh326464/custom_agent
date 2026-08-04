import dspy

examples = [
    # --- remember fact examples ---
    dspy.Example(
        query="my name is Siddhesh",
        tool="remember fact",
        input="user_name | Siddhesh"
    ).with_inputs("query"),

    dspy.Example(
        query="I am 21 years old",
        tool="remember fact",
        input="user_age | 21"
    ).with_inputs("query"),

    dspy.Example(
        query="I prefer dark mode",
        tool="remember fact",
        input="user_preference_theme | dark mode"
    ).with_inputs("query"),

    dspy.Example(
        query="I live in Pune",
        tool="remember fact",
        input="user_location | Pune"
    ).with_inputs("query"),

    dspy.Example(
        query="I am a Python developer",
        tool="remember fact",
        input="user_profession | Python developer"
    ).with_inputs("query"),

    # --- calculator examples ---
    dspy.Example(
        query="what is 10 + 5",
        tool="calculator",
        input="10 + 5"
    ).with_inputs("query"),

    dspy.Example(
        query="calculate 200 divided by 4",
        tool="calculator",
        input="200 / 4"
    ).with_inputs("query"),

    dspy.Example(
        query="what is 7 to the power of 3",
        tool="calculator",
        input="7 ** 3"
    ).with_inputs("query"),

    # --- llm / chat examples ---
    dspy.Example(
        query="hello how are you",
        tool="llm",
        input="I am doing great! How can I help you today?"
    ).with_inputs("query"),

    dspy.Example(
        query="tell me a joke",
        tool="llm",
        input="Why don't scientists trust atoms? Because they make up everything!"
    ).with_inputs("query"),

    dspy.Example(
        query="what is machine learning",
        tool="llm",
        input="Machine learning is a type of AI that allows systems to learn from data."
    ).with_inputs("query"),

    dspy.Example(
        query="list all files in downloads",
        tool="list_directory",
        input="C:/Users/siddhesh/Downloads"
    ).with_inputs("query"),

    dspy.Example(
        query="read the file notes.txt from desktop",
        tool="read_file",
        input="C:/Users/siddhesh/Desktop/notes.txt"
    ).with_inputs("query"),
]
