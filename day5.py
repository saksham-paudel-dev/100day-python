
import asyncio

# Sample texts to summarize
texts = [
    "Python is a popular programming language used in web development, automation, and AI.",
    "Artificial intelligence enables computers to perform tasks that normally require human intelligence.",
    "Async programming allows multiple tasks to make progress without waiting for each task to finish.",
    "GitHub is a platform where developers store code and collaborate on software projects.",
    "Machine learning is a branch of AI that allows systems to learn patterns from data."
]


async def summarize_text(text, task_number):
    print(f"Starting summary {task_number}...")

    # Simulate waiting for an external summarization service
    await asyncio.sleep(2)

    # Simple demo summary: return the first sentence
    summary = text.split(".")[0]

    print(f"Completed summary {task_number}")
    return summary


async def main():
    tasks = [
        summarize_text(text, i + 1)
        for i, text in enumerate(texts)
    ]

    summaries = await asyncio.gather(*tasks)

    print("\n--- BATCH SUMMARIES ---")

    for i, summary in enumerate(summaries, start=1):
        print(f"{i}. {summary}")


if __name__ == "__main__":
    asyncio.run(main())
