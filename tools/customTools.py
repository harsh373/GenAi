from langchain_core.tools import tool

#using @tool decorator



# Step 1 - create a function

def multiply(a, b):
    """Multiply two numbers"""  #highly recommended to add this line as llm will be able to configure what does this tool do
    return a*b


# Step 2 - add type hints

def multiply(a: int, b:int) -> int:
    """Multiply two numbers"""
    return a*b


# Step 3 - add tool decorator

@tool
def multiply(a: int, b:int) -> int:
    """Multiply two numbers"""
    return a*b


result = multiply.invoke({"a":3, "b":5})

print(result)
print(multiply.name)
print(multiply.args)
print(multiply.description)






