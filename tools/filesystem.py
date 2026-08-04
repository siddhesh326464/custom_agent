import os,shutil
from tools.tool_registry import rregistry
from llm.groqllm import GroqLLM
from agent.prompts import SUMMERIZER_PROMPT


@rregistry.register_tool()
class CreateFileFolderTool:
    def __init__(self):
        self.name = "create file or folder"
        self.description = "Creates a file or folder. Input format: 'path' to create a folder, or 'path|content' to create a file with text inside."


    def run(self,query:str):
        try:
            if "|" in query:
                path,content = query.split("|",1)
                path = path.strip()
                content = content.strip()

                directory = os.path.dirname(path)
                if directory:
                    os.makedirs(directory, exist_ok=True)

                with open(path,"w") as f:
                    f.write(content)
                return f"File '{path}' created successfully with {len(content)} characters."
            else:
                path = query.strip()
                os.makedirs(path,exist_ok=True)
                return f"Folder '{path}' created successfully."
        except Exception as e:
            return f"Error creating file or folder: {str(e)}"

@rregistry.register_tool()
class SummarizeTool:
    def __init__(self):
        self.name = "summarize_file"
        self.description = "Reads a file and returns a short summary of its contents. Input must be the absolute file path."
        self.summarizer = GroqLLM()

    def run(self,query:str):
        try:
            path = query.strip()
            if not os.path.exists(path):
                return f"Error: File '{path}' not found."
            
            if not os.path.isfile(path):
                return f"Error: '{path}' is not a file."
            
            with open(path, "r") as f:
                content = f.read()
            
            if len(content.strip()) == 0:
                return f"File '{path}' is empty."

            prompt = SUMMERIZER_PROMPT.format(content = content)
            response = self.summarizer.generate(prompt)
            return response
        except Exception as e:
            return f"Error summarizing file: {str(e)}"


@rregistry.register_tool()
class DeleteFileFolderTool:
    def __init__(self):
        self.name = "delete file or folder"
        self.description = "Deletes a file or folder. Input must be the path to delete."

    def run(self,query:str):
        try:
            path = query.strip()
            if not os.path.exists(path):
                return f"path not found:{path}"

            confirmation  = input(f"Agent: Are you sure you want to allow this deletion? Type 'yes' to confirm {path} : ")
            if confirmation.lower().strip() != "yes":
                return f"Deletion of '{path}' was cancelled by the user."
            if os.path.isfile(path):
                os.remove(path)
                return f"File '{path}' deleted successfully."
            elif os.path.isdir(path):
                shutil.rmtree(path)
                return f"Folder '{path}' and all its contents deleted successfully."
            else:
                return f"Error: '{path}' is neither a standard file nor a folder."

        except Exception as e:
            return f"Error deleting file or folder: {str(e)}"

            
            
