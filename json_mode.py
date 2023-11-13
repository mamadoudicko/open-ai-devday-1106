from lib.openai_client import openai_client

# model should be: gpt-4-1106-preview | gpt-3.5-turbo-1106

# For more details: https://platform.openai.com/docs/api-reference/chat/create#chat-create-response_format
# ⚠️ when using JSON mode you must still instruct the model to produce JSON yourself via some conversation message, for example via your system message.
completion = openai_client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. Your name is GPT demo",
        },
        {"role": "user", "content": "Give me your role and your name as JSON"},
    ],
    response_format={"type": "json_object"},
)

print(completion.choices[0].message.content)

# {
#   "name": "GPT demo",
#   "role": "Helpful Assistant"
# }
