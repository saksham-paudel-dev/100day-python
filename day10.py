
import json
import re
from pathlib import Path
from datetime import datetime, timezone


# Folder for input documents and processed output
INPUT_DIR = Path("documents")
OUTPUT_FILE = Path("processed_documents.json")


def clean_text(text):
    """Normalize whitespace and remove unwanted control characters."""
    text = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_document(data, source, index=1):
    """Convert document data into a standard metadata dictionary."""
    if isinstance(data, str):
        text = data
        metadata = {}
    elif isinstance(data, dict):
        text = data.get("text", data.get("content", ""))
        metadata = {
            key: value
            for key, value in data.items()
            if key not in ("text", "content")
        }
    else:
        raise ValueError("Document must be text or a JSON object.")

    if not isinstance(text, str):
        raise ValueError("Document text/content must be a string.")

    return {
        "document_id": f"{source.stem}_{index}",
        "source": source.name,
        "text": clean_text(text),
        "metadata": metadata,
        "loaded_at": datetime.now(timezone.utc).isoformat(),
    }


def load_document(file_path):
    """Load TXT, JSON, or JSONL documents safely."""
    documents = []
    suffix = file_path.suffix.lower()

    with file_path.open("r", encoding="utf-8") as file:
        if suffix == ".txt":
            documents.append(
                normalize_document(file.read(), file_path)
            )

        elif suffix == ".json":
            data = json.load(file)

            if isinstance(data, list):
                for index, item in enumerate(data, start=1):
                    documents.append(
                        normalize_document(item, file_path, index)
                    )
            else:
                documents.append(
                    normalize_document(data, file_path)
                )

        elif suffix == ".jsonl":
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue

                try:
                    data = json.loads(line)
                    documents.append(
                        normalize_document(
                            data, file_path, line_number
                        )
                    )
                except (json.JSONDecodeError, ValueError) as error:
                    print(
                        f"Skipping {file_path.name}, "
                        f"line {line_number}: {error}"
                    )

        else:
            raise ValueError(f"Unsupported format: {suffix}")

    return documents


def main():
    INPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Create sample input files for the first run
    sample_txt = INPUT_DIR / "notes.txt"
    sample_json = INPUT_DIR / "article.json"
    sample_jsonl = INPUT_DIR / "articles.jsonl"

    if not sample_txt.exists():
        with sample_txt.open("w", encoding="utf-8") as file:
            file.write("  Python   is useful for AI engineering. \n")

    if not sample_json.exists():
        with sample_json.open("w", encoding="utf-8") as file:
            json.dump({
                "title": "Learning Python",
                "content": "  JSON documents store structured data. ",
                "category": "programming"
            }, file, indent=4)

    if not sample_jsonl.exists():
        with sample_jsonl.open("w", encoding="utf-8") as file:
            file.write(json.dumps({
                "content": "JSONL stores one JSON object per line.",
                "category": "data"
            }) + "\n")
            file.write(json.dumps({
                "text": "Clean documents are easier to process.",
                "category": "AI"
            }) + "\n")

    all_documents = []

    for file_path in sorted(INPUT_DIR.iterdir()):
        if file_path.suffix.lower() not in {
            ".txt", ".json", ".jsonl"
        }:
            continue

        try:
            loaded = load_document(file_path)
            all_documents.extend(loaded)
            print(f"Loaded {len(loaded)} document(s) from {file_path.name}")

        except (OSError, json.JSONDecodeError, ValueError) as error:
            print(f"Could not load {file_path.name}: {error}")

    # Save normalized documents
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(all_documents, file, indent=4, ensure_ascii=False)

    print(f"\nTotal documents processed: {len(all_documents)}")
    print(f"Output saved to: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    main()
