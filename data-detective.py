import csv
import sys
import os

def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
            
    return raw_tweets

def clean_data(tweets):
    """
    QUEST 1: Handle missing fields.
    Check for missing text, and replace empty likes/retweets with 0.
    Return a clean list of tweets.
    """
    clean_tweets = []
    removed = 0
    fixed = 0

    for tweet in tweets:
        if not tweet.get("Text", "").strip():
            removed += 1
            continue

        if tweet.get("Likes", "").strip() == "":
            tweet["Likes"] = "0"
            fixed += 1

        if tweet.get("Retweets", "").strip() == "":
            tweet["Retweets"] = "0"
            fixed += 1

        clean_tweets.append(tweet)

    print(f"Quest 1 - Data Auditor:")
    print(f"  Rows removed (missing Text): {removed}")
    print(f"  Fields fixed (missing Likes/Retweets): {fixed}")
    print(f"  Clean dataset size: {len(clean_tweets)}\n")

    return clean_tweets

def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest 'Likes'.
    """
    if len(tweets) == 0:
        print("Quest 2 - Viral Post: No tweets to search.\n")
        return None

    viral = tweets[0]
    for tweet in tweets:
        if int(tweet["Likes"]) > int(viral["Likes"]):
            viral = tweet

    print(f"Quest 2 - Viral Post:")
    print(f"  Username : {viral['Username']}")
    print(f"  Likes    : {viral['Likes']}")
    print(f"  Text     : {viral['Text'][:100]}...\n")

    return viral

def custom_sort_by_likes(tweets, top_n=10):
    """
    QUEST 3: Partial Selection Sort — finds the top_n tweets by Likes
    without sorting the entire list. Makes exactly top_n passes, each
    time extracting the tweet with the highest Likes from the remaining pool.
    """
    remaining = []
    for tweet in tweets:
        remaining.append(tweet)

    top_tweets = []
    for _ in range(top_n):
        if len(remaining) == 0:
            break
        highest_idx = 0
        for i in range(len(remaining)):
            if int(remaining[i]["Likes"]) > int(remaining[highest_idx]["Likes"]):
                highest_idx = i
        top_tweets.append(remaining[highest_idx])
        remaining.pop(highest_idx)

    print(f"Quest 3 - Top {top_n} Most Liked Tweets:")
    for rank, tweet in enumerate(top_tweets, start=1):
        print(f"  {rank}. [{tweet['Likes']} likes] @{tweet['Username']}: {tweet['Text'][:70]}...")
    print()

    return top_tweets

def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """
    matches = []
    for tweet in tweets:
        if keyword.lower() in tweet["Text"].lower():
            matches.append(tweet)

    print(f"Quest 4 - Content Filter:")
    print(f"  Keyword: '{keyword}'")
    print(f"  Matches found: {len(matches)}\n")
    for tweet in matches:
        print(f"  @{tweet['Username']}: {tweet['Text'][:100]}...")
    print()

    return matches

if __name__ == "__main__":
    # Load the messy data
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")
    
    # Quest 1
    clean_dataset = clean_data(dataset)

    # Quest 2
    find_viral_tweet(clean_dataset)

    # Quest 3
    custom_sort_by_likes(clean_dataset)

    # Quest 4
    keyword = input("Quest 4 - Enter a keyword to search: ")
    search_tweets(clean_dataset, keyword)