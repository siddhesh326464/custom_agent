class CalculatorTool:
    def __init__(self):
        self.name = "calculator"
        self.description = "Evaluates math expressions. Input should be a mathematical string like '2 + 2'."
    
    def run(self,query:str):
        try:
            return str(eval(query))
        except Exception as e:
            return f"Error: {str(e)}"