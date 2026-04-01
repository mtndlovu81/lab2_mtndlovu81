# Lab 2: The Social Media Data Detective

A Python data analysis tool and Bash script for exploring a Twitter dataset.

---

## Files

| File | Description |
|------|-------------|
| `data-detective.py` | Main Python script with all four analysis quests |
| `feed-analyzer.sh` | Bash script to find the top 5 most active users |
| `twitter_dataset.csv` | Twitter dataset used for analysis |

---

## Requirements

- Python 3.x
- A Unix/Linux shell (for the Bash script)

---

## Usage

### Python Script

```bash
python3 data-detective.py
```

The script runs all four quests sequentially:

1. **Quest 1 – Data Auditor:** Cleans the dataset by removing tweets with missing `Text` and replacing empty `Likes`/`Retweets` with `0`.
2. **Quest 2 – Viral Post:** Finds and prints the tweet with the highest number of Likes.
3. **Quest 3 – Top 10 Most Liked:** Sorts all tweets by Likes (descending) and prints the top 10.
4. **Quest 4 – Content Filter:** Prompts you for a keyword and prints all tweets containing that word.

### Bash Script

```bash
chmod +x feed-analyzer.sh
./feed-analyzer.sh twitter_dataset.csv
```

Prints the **Top 5 Most Active Users** (by tweet count) from the dataset.

---

## How the Custom Sorting Algorithm Works

Quest 3 uses **Bubble Sort**: it repeatedly steps through the list, comparing each adjacent pair of tweets by their `Likes` count and swapping them if they are in the wrong order (lower before higher). After each full pass through the list, the tweet with the current lowest Likes among the unsorted portion "bubbles" to the end, and the process repeats until the entire list is sorted from highest to lowest Likes.
