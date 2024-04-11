from google.cloud import texttospeech
from pdfquery import PDFQuery

import os


# You need to use your credentials in CREDENTIALS.json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "CREDENTIALS.json"


def synthesize_speech(text: str, output_filename: str) -> None:

    # Create a Text-to-Speech client
    client = texttospeech.TextToSpeechClient()

    # Set the text input
    input_text = texttospeech.SynthesisInput(text=text)

    # Configure the voice settings
    voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # Set the audio configuration
    audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(
    input=input_text, voice=voice, audio_config=audio_config
    )

    # Save the audio to a file
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print(f"Audio content written to '{output_filename}'")


def main() -> None:
    pdf = PDFQuery('sample.pdf')
    pdf.load()
    # Use CSS-like selectors to locate the elements
    text_elements = pdf.pq('LTTextLineHorizontal').text()

    # Extract the text from the elements
    text_to_convert: str = "".join(text_elements)

    # Test the text-to-speech function
    synthesize_speech(text_to_convert, "output.mp3")


if __name__ == '__main__':
    main()
