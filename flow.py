from pocketflow import Flow
from nodes import AnalyzeDocs, WriteScript, TextToSpeech


def create_podcast_flow():
    """
    NotebookLM-style AI Podcast Generator

    Pipeline:
    1. AnalyzeDocs
       - Reads uploaded PDF/TXT/DOCX files
       - Extracts important concepts, facts, and summaries

    2. WriteScript
       - Sends the extracted content to Groq Llama 3/4
       - Generates a natural conversation between two hosts
       - Produces a NotebookLM-style podcast script

    3. TextToSpeech
       - Uses Microsoft Edge TTS
       - Converts the script into speech
       - Saves the final podcast as an MP3 file

    Returns:
        Flow: Complete podcast generation workflow
    """

    # Step 1: Analyze uploaded documents
    analyze_docs = AnalyzeDocs()

    # Step 2: Generate podcast script using Groq
    write_script = WriteScript()

    # Step 3: Convert script into audio using Edge TTS
    generate_audio = TextToSpeech()

    # Connect nodes
    analyze_docs >> write_script >> generate_audio

    # Create flow
    podcast_flow = Flow(start=analyze_docs)

    return podcast_flow