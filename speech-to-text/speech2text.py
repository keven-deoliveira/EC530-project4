# from google.cloud import speech_v1 as speech


# def speech_to_text(config, audio):
#     client = speech.SpeechClient()
#     response = client.recognize(config=config, audio=audio)
#     print_sentences(response)


# def print_sentences(response):
#     for result in response.results:
#         best_alternative = result.alternatives[0]
#         transcript = best_alternative.transcript
#         confidence = best_alternative.confidence
#         print("-" * 80)
#         print(f"Transcript: {transcript}")
#         print(f"Confidence: {confidence:.0%}")


# config = dict(language_code="en-US")
# config.update(dict(enable_automatic_punctuation=True))

# audio = dict(uri="gs://cloud-samples-data/speech/brooklyn_bridge.flac")

# speech_to_text(config, audio)

def transcribe_file(speech_file):
    """Transcribe the given audio file asynchronously."""
    from google.cloud import speech

    client = speech.SpeechClient()

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    """
     Note that transcription is limited to a 60 seconds audio file.
     Use a GCS file for audio longer than 1 minute.
    """
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=48000,
        language_code="en-US",
    )


    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))

audio = "audio.flac"
audio2 = "audio2.flac"

transcribe_file(audio)

print()

transcribe_file(audio2)
