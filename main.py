import os
import whisper
from docx import Document
from performance_monitor import monitor_resources


def transcribe_and_save_documents(audio_folder):
    # Load the Whisper model
    model = whisper.load_model("medium.en")

    # Loop through each file in the  directory
    for filename in os.listdir(audio_folder):
        if filename.endswith('.mp3'):
            # Full path to the MP3 file
            file_path = os.path.join(audio_folder, filename)

            # Transcribe the audio file
            result = model.transcribe(file_path, fp16=False)

            # Create a new Word document
            doc = Document()
            doc.add_paragraph(result['text'])  # Add the transcript to the document

            # Save the document with the same base name as the audio file
            doc_name = filename.replace('.mp3', '.docx')
            doc.save(os.path.join(audio_folder, doc_name))

            print(f"Document saved: {doc_name}")


# transcribe_and_save_documents('mis')

monitor_resources(transcribe_and_save_documents, 'mis')


