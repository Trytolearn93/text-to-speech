from google.cloud import texttospeech


def text_to_speech(
    text,
    output_filename,
    language_code="en-US",
    voice_name="en-US-Wavenet-D",
    audio_format=texttospeech.AudioEncoding.MP3,
):
    # Initialize client
    client = texttospeech.TextToSpeechClient()

    # Set up synthesis input
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Configure voice parameters
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )

    # Configure audio output format
    audio_config = texttospeech.AudioConfig(audio_encoding=audio_format)

    # Perform text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Write the audio content to file
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)
    print(f"Audio content written to '{output_filename}'")


if __name__ == "__main__":
    import os

    # Set your Google Cloud credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
        "path/to/your/service-account-key.json"
    )

    # Input text and output file
    text = "Hello, this is a sample text to convert to speech."
    output_file = "output.mp3"

    # Call the function
    text_to_speech(text, output_file)
