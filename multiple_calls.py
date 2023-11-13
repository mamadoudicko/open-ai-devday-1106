from lib.openai_client import openai_client


# declaring my functions
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# Declaring my functions schemas since GPT doesn't call functions directly but emit intention to call them
# We then call them and recall GPT with the result
# More details https://platform.openai.com/docs/guides/function-calling/function-calling

# Functions are now deprecated, use tools instead
# https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "add",
            "description": "add two numbers",
            "parameters": {
                "type": "object",
                "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
            },
            "required": ["a", "b"],
        },
    },
    {
        "type": "function",
        "function": {
            "name": "sub",
            "description": "subtract two numbers",
            "parameters": {
                "type": "object",
                "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
            },
            "required": ["a", "b"],
        },
    },
]


completion = openai_client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {
            "role": "system",
            "content": "You are a math assistant. But don't do maths yourself. You have access to functions which can do maths for you.",
        },
        {"role": "user", "content": "What is the result of 4+5 and of 9-5"},
    ],
    tools=tools,
    tool_choice="auto",
)

tool_calls = completion.choices[0].message.tool_calls

if tool_calls:
    for tool_call in tool_calls:
        print("name", tool_call.function.name, "argument", tool_call.function.arguments)

# name add argument {"a": 4, "b": 5}
# name sub argument {"a": 9, "b": 5}

# Now we can call our functions and recall GPT with the result
# More details on https://platform.openai.com/docs/guides/function-calling/parallel-function-calling
