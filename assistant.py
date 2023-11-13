import time

from lib.openai_client import openai_client

# uploading the file to OpenAI
print("uploading file", "\n")
file = openai_client.files.create(
    file=open("./assets/presentation.txt", "rb"), purpose="assistants"
)
print("fileId", file.id, "\n")

# now we can create an assistant
assistant = openai_client.beta.assistants.create(
    name="Answer generator",
    description="You are a helpful assistant. Your can answer questions.",
    model="gpt-3.5-turbo-1106",
    tools=[
        {"type": "retrieval"}
    ],  # since we are adding files, we need to specify that we need to activate one tool which need files as `retrieval` or `code_interpreter`
    file_ids=[
        file.id
    ],  # files specified here will be available in to all threads of this assistant
)

# now to use the assistant we'll create a thread
thread = (
    openai_client.beta.threads.create()
)  # you can also add message when creating a thread
print("threadId", thread.id, "\n")

# send a message to the tread
completion = openai_client.beta.threads.messages.create(
    content="What is in the file?", thread_id=thread.id, role="user"
)

# you can list your tread messages
messages = openai_client.beta.threads.messages.list(thread_id=thread.id)
for message in messages.data:
    print("thread message", message.content, "\n")

# now we can run the thread meaning that the assistant will answer to the last messages
run = openai_client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
)
print("runId", run, "\n")

run_final_steps = ["cancelled", "failed", "completed", "expired"]
# you need to wait for the assistant to answer then poll the run for the answer
# thread is locked while run is not completed (no new message, now new run)
while run.status not in run_final_steps:
    print("run status", run.status)
    sleep_time = 3
    print(f"sleeping {sleep_time} seconds")
    time.sleep(sleep_time)
    run = openai_client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

messages = openai_client.beta.threads.messages.list(thread_id=thread.id, order="asc")
print("thread current messages", "\n")
for message in messages.data:
    print(message.content, "\n")


# context following
# send a message to the tread
completion = openai_client.beta.threads.messages.create(
    content="What was my last message?", thread_id=thread.id, role="user"
)

# re run the thread
run = openai_client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
)
print("runId", run, "\n")

while run.status not in run_final_steps:
    print("run status", run.status)
    sleep_time = 3
    print(f"sleeping {sleep_time} seconds")
    time.sleep(sleep_time)
    run = openai_client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

messages = openai_client.beta.threads.messages.list(thread_id=thread.id, order="asc")
print("thread current messages", "\n")
for message in messages.data:
    print(message.content, "\n")
