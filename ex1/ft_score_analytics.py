import sys


def ft_score_analytics():
    argv = sys.argv
    args_len = len(argv)
    args_ints = []
    if args_len == 1:
        print("No scores provided. Usage: python3 ", end="")
        print("ft_score_analytics.py <score1> <score2> ...")
        return
    try:
        for i in argv[1:]:
            args_ints.append(int(i))
        print("=== Player Score Analytics ===")
        print(f"Scores processed: {args_ints}")
        print(f"Total players: {args_len - 1}")
        print(f"Total score: {sum(args_ints)}")
        print(f"Average score: {(sum(args_ints) / (args_len - 1)):.1f}")
        print(f"High score: {max(args_ints)}")
        print(f"Low score: {min(args_ints)}")
        print(f"Score range: {max(args_ints) - min(args_ints)}")
    except Exception:
        return


ft_score_analytics()
