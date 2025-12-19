stats = {
    "total": 0,
    "positive": 0,
    "negative": 0,
    "neutral": 0
}

def update_stats(sentiment: str):
    stats["total"] += 1
    if sentiment in stats:
        stats[sentiment] += 1

def get_stats():
    return stats
