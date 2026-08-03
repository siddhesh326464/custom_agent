import os
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

                with open(path,"w") as f:
                    f.write(content)
                return f"File '{path}' created successfully with {len(content)} characters."
            else:
                path = query.strip()
                os.makedirs(path,exist_ok=True)
                return f"Folder '{path}' created successfully."
        except Exception as e:
            return f"Error creating file or folder: {str(e)}"