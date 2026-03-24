import re
from collections import Counter

def summarize(text, num_sentences=2):
    # Clean and split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    # Count word frequencies
    words = re.findall(r'\w+', text.lower())
    word_freq = Counter(words)

    # Remove common words
    stop_words = ["the", "is", "in", "it", "of", "and", "a", "to", "was", "that", "this"]
    for word in stop_words:
        del word_freq[word]

    # Score each sentence based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in re.findall(r'\w+', sentence.lower()):
            if word in word_freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]

    # Pick top sentences
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

    # Return in original order
    summary = [s for s in sentences if s in top_sentences]
    return " ".join(summary)

print("=== AI Text Summarizer ===")
print("Paste your paragraph below and press Enter twice:\n")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = " ".join(lines)
print("\n--- Summary ---")
print(summarize(text))