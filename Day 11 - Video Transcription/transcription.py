import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Open the video file
with sr.AudioFile(r"video.wav") as source:
    # Read the audio data from the file
    audio_data = r.record(source)

    # Transcribe the audio data
    print("Transcribeing audio...")
    text = r.recognize_google(audio_data, language='en-US', show_all=True)

    # Print the transcription
    print(f"Transcription: {text}")
