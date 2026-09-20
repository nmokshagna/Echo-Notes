# Echo-Notes
# 🎙️ NotebookLM-Style AI Podcast Generator

An AI-powered podcast generator inspired by **Google NotebookLM**.
It analyzes documents, extracts interesting facts, generates a natural two-host conversation using **Llama via Groq**, and converts the conversation into an MP3 podcast using **Microsoft Edge TTS**.

## ✨ Features

* 📄 **Document Analysis** — Extracts interesting facts and key information from documents.
* 🧠 **AI-Powered Script Generation** — Uses Llama through the Groq API to create a conversational podcast.
* 🎙️ **Two AI Hosts** — Alex and Jamie have different personalities and voices.
* 🗣️ **Text-to-Speech** — Converts the generated script into natural-sounding speech.
* 🎧 **MP3 Output** — Produces a ready-to-listen podcast file.
* 🔗 **Workflow-Based Architecture** — Uses PocketFlow to organize the AI pipeline into reusable nodes.
* ⚡ **Simple CLI** — Generate a podcast directly from the command line.

---

## 🏗️ How It Works

The project follows a simple AI pipeline:

```text
             📄 Documents
                  │
                  ▼
        ┌──────────────────┐
        │   AnalyzeDocs    │
        │                  │
        │ Extract facts &  │
        │ important ideas  │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │   WriteScript    │
        │                  │
        │ Groq + Llama     │
        │ generates a      │
        │ podcast dialogue │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │   TextToSpeech   │
        │                  │
        │ Microsoft Edge   │
        │      TTS         │
        └────────┬─────────┘
                 │
                 ▼
             🎧 podcast.mp3
```

---

## 🧰 Tech Stack

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| 🐍 Python        | Core programming language       |
| 🧠 Groq          | LLM API                         |
| 🦙 Llama 3.3 70B | Podcast script generation       |
| 🔄 PocketFlow    | AI workflow orchestration       |
| 🗣️ Edge TTS     | Text-to-speech generation       |
| 📦 PyYAML        | Parsing generated YAML scripts  |
| 🔐 python-dotenv | Environment variable management |
| 🤖 OpenAI SDK    | Communicating with the Groq API |

---

## 📁 Project Structure

```text
nnlm/
│
├── main.py             # CLI entry point
├── flow.py             # Podcast workflow definition
├── nodes.py            # AI processing nodes
├── utils.py            # LLM configuration and document data
├── requirements.txt    # Python dependencies
├── .env                # API credentials
│
└── podcast.mp3         # Generated podcast
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace `YOUR_USERNAME/YOUR_REPOSITORY` with your GitHub repository.

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Groq API key

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can get a Groq API key from the Groq developer platform.

> ⚠️ Never commit your `.env` file or expose your API key publicly.

---

## ▶️ Run the Project

Run the default podcast generation:

```bash
python main.py
```

The generated podcast will be saved as:

```text
podcast.mp3
```

### Specify an output filename

```bash
python main.py --output my_podcast.mp3
```

or:

```bash
python main.py -o my_podcast.mp3
```

---

## 🎙️ AI Hosts

The podcast currently uses two AI hosts:

### Alex

**Voice:** `en-US-GuyNeural`

* Curious
* Energetic
* Asks follow-up questions
* Drives the conversation

### Jamie

**Voice:** `en-US-JennyNeural`

* Knowledgeable
* Explains concepts clearly
* Uses simple examples
* Provides detailed answers

The voices can be customized in `nodes.py`:

```python
VOICES = {
    "Alex": "en-US-GuyNeural",
    "Jamie": "en-US-JennyNeural",
}
```

---

## 🧠 AI Pipeline

### 1. Analyze Documents

The `AnalyzeDocs` node sends the provided documents to the Llama model and asks it to extract **2–3 interesting facts from each document**.

```python
AnalyzeDocs()
```

The extracted information is stored as:

```python
shared["nuggets"]
```

### 2. Generate Podcast Script

The `WriteScript` node uses the extracted facts to create a two-host conversation.

The generated script follows a YAML structure:

```yaml
script:
  - name: Alex
    line: "Welcome everyone!"

  - name: Jamie
    line: "Today we're exploring something fascinating."

  - name: Alex
    line: "That sounds interesting!"

  - name: Jamie
    line: "Let me explain."
```

### 3. Convert Script to Audio

The `TextToSpeech` node processes every dialogue line and assigns the appropriate voice.

```python
edge_tts.Communicate(
    text=item["line"],
    voice=voice
)
```

The individual audio segments are combined into the final MP3.

---

## 🔑 Environment Variables

The project requires:

| Variable       | Description                             |
| -------------- | --------------------------------------- |
| `GROQ_API_KEY` | API key used to access the Groq LLM API |

Example:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
```

---

## 📚 Current Input

The project currently contains example documents in `utils.py`.

For example:

```python
DOCS = [
    "PocketFlow is a 100-line minimalist LLM framework...",
    "Nodes have three phases...",
    "A Flow connects nodes with >>...",
]
```

You can replace these with your own content.

---

## 🔮 Future Improvements

Some possible improvements:

* [ ] Support PDF files
* [ ] Support DOCX files
* [ ] Support TXT and Markdown files
* [ ] Upload documents through a web interface
* [ ] Add a Streamlit frontend
* [ ] Add more AI host personalities
* [ ] Allow users to select different voices
* [ ] Add background music
* [ ] Add automatic intro/outro generation
* [ ] Generate podcast cover art
* [ ] Add episode metadata
* [ ] Support multiple languages
* [ ] Add a web-based audio player
* [ ] Improve audio stitching between speakers
* [ ] Add conversation length controls

---

## ⚠️ Notes

This project is a **NotebookLM-inspired educational project** and is not affiliated with or endorsed by Google.

The quality of the generated podcast depends on the quality of the source documents and the LLM output.

You will need an active Groq API key to generate the podcast script.

---

## 🤝 Contributing

Contributions, ideas, and improvements are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/my-feature
```

3. Make your changes
4. Commit your changes

```bash
git add .
git commit -m "Add my feature"
```

5. Push the branch

```bash
git push origin feature/my-feature
```

6. Open a Pull Request

---

## 📜 License

Add your preferred open-source license here, such as **MIT License**, before publishing the repository.

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub!

Built with Python, Groq, Llama, PocketFlow, and Edge TTS. 🎙️🤖
