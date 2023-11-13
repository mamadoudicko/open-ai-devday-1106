from lib.openai_client import openai_client

# More details https://platform.openai.com/docs/guides/vision/vision
response = openai_client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What are in these images in few words?"},
                {
                    "type": "image_url",
                    "image_url": "https://media.routard.com/image/38/0/pt103731.1312380.w430.jpg",
                },
                {
                    "type": "image_url",
                    "image_url": "https://avatars.githubusercontent.com/u/63923024?v=4",
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0].message.content)
# The first image features a monument and a car in the foreground with the flag of Mali flying beside it. The second image is a portrait of a smiling man.
