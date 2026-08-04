import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import dspy
from utils.dspy_config import *         
from RL.planner_signature import PlannerSignature
from RL.training_data import examples
from RL.metric import planner_metric
from tools.tool_registry import rregistry
import tools.calculator
import tools.chat
import tools.filesystem
import tools.memory_tools


class DSPyPlannerModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.predict = dspy.Predict(PlannerSignature)

    def forward(self, query):
        tools_desc = rregistry.get_tool_descriptions_for_llm()
        result = self.predict(
            tools=tools_desc,
            history="No previous conversation.",
            long_term_memory="No long-term facts stored.",
            query=query,
        )
        return result


if __name__ == "__main__":
    program = DSPyPlannerModule()

    optimizer = dspy.MIPROv2(
        metric=planner_metric,
        num_threads=1,
        verbose=True,
        auto="light"
    )

    print("🚀 Starting DSPy optimization... this may take a few minutes.")

    optimized_program = optimizer.compile(
        program,
        trainset=examples,
    )

    optimized_instructions = optimized_program.predict.signature.instructions
    
    print("\n" + "="*60)
    print("✅ OPTIMIZED INSTRUCTIONS (copy this into your PLANNER_PROMPT)")
    print("="*60)
    print(optimized_instructions)
    print("="*60)

    with open("RL/optimized_instructions.txt", "w") as f:
        f.write(optimized_instructions)
    
    print("\n Also saved to RL/optimized_instructions.txt")
