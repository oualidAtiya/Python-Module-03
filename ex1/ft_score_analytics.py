import sys


def score_analytics():
    score_list = []
    print("=== Player Score Analytics ===")
    if (len(sys.argv) == 1):
        print("No scores provided. Usage: python3", end="")
        print("ft_score_analytics.py <score1> <score2> .")
        return
    try:
        count = 0
        for score in sys.argv:
            if (count):
                score_list.append(int(score))
            count += 1
        print(f"Scores processed: {score_list}")
        print(f"Total players: {len(score_list)}")
        print(f"Total score: {sum(score_list)}")
        print(f"Average score: {sum(score_list) / len(score_list)}")
        print(f"High score: {max(score_list)}")
        print(f"Low score: {min(score_list)}")
        print("Score range: ??")
    except Exception as e:
        print(e)


score_analytics()
