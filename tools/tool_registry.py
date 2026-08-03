from tools.calculator import CalculatorTool
from tools.filesystem import FileSystemTool
from typing import Dict, Any, Optional, Protocol
import logging


logger = logging.getLogger(__name__)

class BaseTool(Protocol):
    name: str
    description : str

    def run(self,query:str)->str:
        pass



class ToolRegistry:
    """
    A centralized registry to manage and execute all agent tools dynamically.
    """
    def __init__(self):
        self.tools : Dict[str,BaseTool] = {}

    def register_tool(self,tool:BaseTool):
        if not tool.name and tool.run:
            raise ValueError("Tool {tool} must have a 'name' attribute and a 'run' method.")
        elif tool.name in self.tools:
            logger.warning(f"Overwriting existing tool: {tool.name}")
        else:
            self.tools[tool.name] = tool
            logger.info(f"Successfully registered tool: {tool.name}")


    def get_tool(self,tool_name:str)->Optional[BaseTool]:
        tool = self.tools.get(tool_name)
        if not tool:
            logger.error(f"Tool not found: {tool_name}")
            return None
        return tool

    def execute_tool(self,tool_name:str,query:str):
        tool = self.get_tool(tool_name)
        if not tool:
            logger.error(f"Tool not found: {tool_name}")
            return ValueError(f"Error: Tool '{tool_name}' does not exist.")
        try:
            logger.info(f"Executing tool: {tool_name} for query: {query}")
            return tool.run(query=query)
        except Exception as e:
            logger.error(f"Error executing tool {tool_name}: {str(e)}")
            return f"Error executing {tool_name}: {str(e)}"



        
rregistry = ToolRegistry()

calc = CalculatorTool()
rregistry.register_tool(calc)
        


    






