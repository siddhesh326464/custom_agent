from agent.agent import Agent

agent = Agent()


while True:
    user_input = input("User: ")
    if user_input.lower().strip() == "exit":
        break
    answer = agent.run(query=user_input)
    print(f"Agent: {answer}")