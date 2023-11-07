
from utils.openai_client import openai_client
import io
from pydub import AudioSegment
from pydub.playback import play

def audio_answer_generator(question: str):
  
    answer = openai_client.chat.completions.create(
        model='gpt-3.5-turbo-1106',
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
    )

    response = openai_client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=answer.choices[0].message.content,
    )

    # Convert the binary response content to a byte stream
    byte_stream = io.BytesIO(response.content)

    # Read the audio data from the byte stream
    audio = AudioSegment.from_file(byte_stream, format="mp3")

    # Play the audio
    play(audio)


if __name__ == "__main__":
    text = input("Enter your text: ")
    audio_answer_generator(text)