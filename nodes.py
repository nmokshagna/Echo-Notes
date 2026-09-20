
from pocketflow import Node
from utils import call_llm, DOCS
import yaml
import asyncio
import edge_tts
import os

VOICES = {
    "Alex": "en-US-GuyNeural",
    "Jamie": "en-US-JennyNeural",
}


class AnalyzeDocs(Node):

    def prep(self, shared):
        return shared.get("docs", DOCS)

    def exec(self, docs):
        documents = "\n\n".join(
            f"Document {i+1}:\n{doc}"
            for i, doc in enumerate(docs)
        )

        prompt = f"""
Read all of the documents below.

Extract 2-3 interesting facts from EACH document.

Documents:

{documents}
"""
        return call_llm(prompt)

    def post(self, shared, prep_res, exec_res):
        shared["nuggets"] = exec_res
        print("✓ Nuggets extracted")


class WriteScript(Node):

    def prep(self, shared):
        return shared["nuggets"]

    def exec(self, nuggets):
        
        
        

        prompt = f"""
You are an expert podcast writer.

Your task is to create a natural, engaging, two-host podcast conversation inspired by Google's NotebookLM.

Hosts:
- Alex: Curious, energetic, asks interesting questions.
- Jamie: Knowledgeable, explains concepts clearly with simple examples.

Requirements:
- Return ONLY valid YAML.
- Do NOT include markdown.
- Do NOT include explanations.
- Every dialogue line MUST be enclosed in double quotes.
- Generate 10-12 exchanges (20-24 dialogue lines total).
- Keep the conversation friendly and conversational.
- Include follow-up questions.
- Explain technical concepts in simple language.
- Occasionally express surprise or curiosity.
- Do not repeat information.
- End with a short conclusion.

The output MUST follow this exact format:

script:
  - name: Alex
    line: "Welcome everyone!"

  - name: Jamie
    line: "Today we're exploring something fascinating."

  - name: Alex
    line: "That sounds interesting!"

  - name: Jamie
    line: "Let me explain."

Use ONLY the information below when writing the podcast.

Facts:

{nuggets}
"""




        response = call_llm(prompt)


        response = response.strip()

        if response.startswith("```yaml"):
            response = response[7:]
        elif response.startswith("```"):
            response = response[3:]

        if response.endswith("```"):
            response = response[:-3]

        response = response.strip()

        try:
            parsed = yaml.safe_load(response)
        except yaml.YAMLError as e:
            print(response)
            raise ValueError(e)

        if not isinstance(parsed, dict) or "script" not in parsed:
            raise ValueError("Model did not return valid YAML.")

        return parsed["script"]

    def post(self, shared, prep_res, exec_res):
        shared["script"] = exec_res
        print("✓ Script generated")
'''
class WriteScript(Node):

    def prep(self, shared):
        return shared["nuggets"]

    def exec(self, nuggets):
        prompt = f"""
You are writing a NotebookLM style podcast.

Hosts:
Alex
Jamie

Return ONLY valid YAML.

Example:

script:
  - name: Alex
    line: Welcome everyone!

  - name: Jamie
    line: Great to be here!

Facts:

{nuggets}
"""
       
        response = call_llm(prompt)

        if "```yaml" in response:
            response = response.split("```yaml")[1].split("```")[0].strip()
        elif "```" in response:
            response = response.split("```")[1].split("```")[0].strip()

        parsed = yaml.safe_load(response)

        if not parsed or "script" not in parsed:
            raise ValueError("Model did not return valid YAML.")

        return parsed["script"]

    def post(self, shared, prep_res, exec_res):
        shared["script"] = exec_res
        print("✓ Script generated")
'''

class TextToSpeech(Node):

    def prep(self, shared):
        return (
            shared["script"],
            shared.get("output_file", "podcast.mp3")
        )

    async def _generate(self, script, output_file):

        with open(output_file, "wb") as outfile:

            for item in script:

                voice = VOICES.get(item["name"], "en-US-GuyNeural")

                communicate = edge_tts.Communicate(
                    text=item["line"],
                    voice=voice
                )

                temp = "_temp.mp3"

                await communicate.save(temp)

                with open(temp, "rb") as f:
                    outfile.write(f.read())

                os.remove(temp)

        return output_file

    def exec(self, prep_res):
        script, output_file = prep_res
        return asyncio.run(self._generate(script, output_file))

    def post(self, shared, prep_res, exec_res):
        shared["audio_file"] = exec_res
        print(f"✓ Podcast saved as {exec_res}")