# [OpenAI-devday-demo](https://www.youtube.com/watch?v=U9mJuUkhUzk)

During their first-ever DevDay, OpenAI pushed the game further. Let's dive into what developers can now accomplish.

## [GPT-4 Turbo](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo)

- 2x faster
- 2.75x cheaper
- 128k context input, 4k output
- JSON mode to enforce responses in JSON format ([demo here](/json_mode.py))
- Support for multiple functions calls in a single request ([demo here](/multiple_calls.py))
- Knowledge extended through April 2023
- Ability to pass images as input ([demo here](/image_input.py))

## [Text to Speech (TTS)](https://platform.openai.com/docs/guides/text-to-speech)

- OpenAI API can now generate speech from text ([demo here](/audio_answer_generator.py))
- Offers 6 voices ([documentation](https://platform.openai.com/docs/guides/text-to-speech/voice-options))
- Supports real-time streaming (songs start playing before audio generation completion)([demo here](/audio_answer_generator.py))
- Note ⚠️ : Custom voices are not available at this time

## [GPTs & Actions](https://platform.openai.com/docs/actions)

```
⚠️ Available on ChatGPT GUI only ⚠️
```

- OpenAI now provides the ability to create your custom versions of ChatGPT, called GPTs
- GPTs can be shared with others
- OpenAI introduces the option to create an `action`, enabling APIs for your GPTs (already utilized by Canva and Zapier)
- OpenAI can host your OpenAPI (API!) specifications for these actions
- Actions can be used with APIs that require authentication

## [Assistants API](https://platform.openai.com/docs/assistants/overview)

- OpenAI introduces Assistants ([demo here](/assistant.py))
- You can upload files to OpenAI, which will be accessible to your assistants ([demo here](/assistant.py))
- Each assistant can link up to 20 files, each with a maximum size of 512MB
- Assistant have access to various tools, including functions and code interpreter
- OpenAI introduces Threads, a way to organize conversations ([demo here](/assistant.py))
- Threads inherit the files and other configurations linked to the assistant ([demo here](/assistant.py))
- You can attach up to 10 files to a thread message
