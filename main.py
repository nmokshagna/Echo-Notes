import argparse
from flow import create_podcast_flow
from utils import DOCS


def main():
    """
    NotebookLM-style Podcast Generator

    Pipeline:
        Documents
            ↓
        AnalyzeDocs
            ↓
        WriteScript (Groq)
            ↓
        TextToSpeech (Edge TTS)
            ↓
        podcast.mp3
    """

    parser = argparse.ArgumentParser(
        description="Generate a NotebookLM-style podcast from documents."
    )

    parser.add_argument(
        "-o",
        "--output",
        default="podcast.mp3",
        help="Output MP3 filename"
    )

    args = parser.parse_args()

    shared = {
        "docs": DOCS,
        "output_file": args.output,
    }

    print("\n" + "=" * 60)
    print("🎙️ NotebookLM-Style AI Podcast Generator")
    print("=" * 60)

    print(f"📄 Documents Loaded : {len(DOCS)}")
    print(f"💾 Output File      : {args.output}")
    print()

    print("🚀 Pipeline")
    print("────────────────────────────────────────")
    print("1️⃣ Analyze uploaded documents")
    print("2️⃣ Generate podcast script using Groq Llama")
    print("3️⃣ Convert script to speech using Microsoft Edge TTS")
    print("4️⃣ Save final podcast as MP3")
    print("────────────────────────────────────────\n")

    try:
        flow = create_podcast_flow()
        flow.run(shared)

        print("\n" + "=" * 60)
        print("✅ Podcast generated successfully!")
        print(f"🎧 Audio File : {shared.get('audio_file', args.output)}")

        if "script" in shared:
            print(f"📝 Script Length : {len(shared['script'])} characters")

        print("=" * 60)

    except Exception as e:
        print("\n❌ Pipeline Failed")
        print("-" * 60)
        print(e)
        print("-" * 60)


if __name__ == "__main__":
    main()