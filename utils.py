import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def call_llm(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=1024,
    )

    return response.choices[0].message.content


DOCS = [
    "PocketFlow is a 100-line minimalist LLM framework. Zero dependencies, zero vendor lock-in. "
    "The core abstraction is a nested directed graph that lets you compose complex AI workflows from simple building blocks.",

    "Nodes have three phases: prep reads from shared store, exec does the work, post writes results back. "
    "This clean separation makes each node easy to test, debug, and reuse across different flows.",

    "A Flow connects nodes with >> for chaining and action strings for branching. "
    "You can nest flows inside flows, giving you infinite composability without complexity.",

    "The key design patterns include Workflow for linear pipelines, Agent for autonomous loops, "
    "RAG for retrieval-augmented generation, Map-Reduce for parallel processing, "
    "and Reflection for self-improving outputs.",
]


if __name__ == "__main__":

    prompt = "What is PocketFlow?"

    print(call_llm(prompt))