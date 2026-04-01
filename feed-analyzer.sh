#!/bin/bash

# Feed Analyzer - Top 5 Most Active Users
# Usage: ./feed-analyzer.sh twitter_dataset.csv

FILE=${1:-twitter_dataset.csv}

if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found."
    exit 1
fi

echo "Top 5 Most Active Users in $FILE:"
echo "-----------------------------------"
printf "%-20s %s\n" "Username" "Tweet Count"
echo "-----------------------------------"

# grep filters to lines starting with a Tweet_ID (digit,) to skip multi-line text continuations
# awk reorders uniq -c output (count username) to (username count)
grep -E '^[0-9]+,' "$FILE" | cut -d',' -f2 | sort | uniq -c | sort -rn | head -5 | awk '{printf "%-20s %s\n", $2, $1}'
