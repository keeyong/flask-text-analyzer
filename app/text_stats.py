"""
Simple text analysis utilities.
NOTE (review points):
- Tokenization uses English-centric regex; improve for Unicode (Korean, accents, emoji).
- Reading time rounding policy (floor vs ceil) could be discussed.
- Hyphen/apostrophe policy is simplistic.
"""

from __future__ import annotations
import re
from collections import Counter
from typing import Dict, List

WORD_SPLIT = re.compile(r"[^a-zA-Z]+")  # REVIEW: English only; consider Unicode classes \p{L}

def tokenize(text: str) -> List[str]:
    """Lowercase + split on non-letters.
    Returns empty list for empty/whitespace-only input.
    """
    return [t for t in WORD_SPLIT.split(text.lower()) if t]

def count_words(text: str) -> int:
    return len(tokenize(text))

def top_n_words(text: str, n: int = 5) -> List[Dict[str, int]]:
    words = tokenize(text)
    freq = Counter(words)
    # REVIEW: For large vocabularies, consider heapq.nlargest instead of sorting entire items
    items = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return [{"word": w, "count": c} for w, c in items[: max(0, n)]]

def count_sentences(text: str) -> int:
    # REVIEW: naive split; abbreviations like "Mr." will overcount
    parts = [p.strip() for p in re.split(r"[.!?]+", text) if p.strip()]
    return len(parts)

def estimate_reading_time_sec(text: str, words_per_minute: int = 200) -> int:
    wpm = max(words_per_minute, 1)
    minutes = count_words(text) / wpm
    # REVIEW: floor vs ceil vs round?
    return int(minutes * 60)

def is_palindrome(raw: str) -> bool:
    s = re.sub(r"[^a-z0-9]", "", raw.lower())
    if not s:
        return False
    return s == s[::-1]

def find_palindromes(text: str) -> List[str]:
    uniq = set()
    for w in tokenize(text):
        if is_palindrome(w):
            uniq.add(w)
    return sorted(uniq)

def analyze_text(text: str, top: int = 5, words_per_minute: int = 200) -> Dict:
    return {
        "charCount": len(text),
        "wordCount": count_words(text),
        "uniqueWordCount": len(set(tokenize(text))),
        "topWords": top_n_words(text, top),
        "sentenceCount": count_sentences(text),
        "estimatedReadingTimeSec": estimate_reading_time_sec(text, words_per_minute),
        "palindromes": find_palindromes(text),
    }
