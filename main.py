from agent.agent import Agent
import tools.calculator
import tools.chat
import tools.filesystem

agent = Agent()


while True:
    user_input = input("User: ")
    if user_input.lower().strip() == "exit":
        break
    answer = agent.run(query=user_input)
    print(f"Agent: {answer}")