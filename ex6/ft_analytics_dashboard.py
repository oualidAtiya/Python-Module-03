data = {
    'players': {
        'alice': {
            'level': 41,
            'total_score': 6500,
            'sessions_played': 13,
            'favorite_mode': 'ranked',
            'achievements_count': 5
        },
        'bob': {
            'level': 16,
            'total_score': 2824,
            'sessions_played': 27,
            'favorite_mode': 'ranked',
            'achievements_count': 2
        },
        'diana': {
            'level': 3,
            'total_score': 1488,
            'sessions_played': 21,
            'favorite_mode': 'casual',
            'achievements_count': 4
        },
        'oualid': {
            'level': 6,
            'total_score': 500,
            'sessions_played': 21,
            'favorite_mode': 'casual',
            'achievements_count': 4
        },
    },

    'sessions': [
        {
            'player': 'bob', 'duration_minutes': 94,
            'score': 1839, 'mode': 'competitive', 'completed': False,
            "region": "north"
        },
        {
            'player': 'bob', 'duration_minutes': 32,
            'score': 1478, 'mode': 'casual', 'completed': True,
            "region": "east"
        },
        {
            'player': 'diana', 'duration_minutes': 17, 'score': 1570,
            'mode': 'competitive', 'completed': False, "region": "north"
        },
        {
            'player': 'alice', 'duration_minutes': 98,
            'score': 1981, 'mode': 'ranked', 'completed': True,
            "region": "central"
        },
        {
            'player': 'diana', 'duration_minutes': 15,
            'score': 2361, 'mode': 'competitive', 'completed': False,
            "region": 'east'
        },
    ],
    'game_modes': [
        'casual',
        'competitive',
        'ranked'
    ],
    'achievements': [
        'first_blood',
        'level_master',
        'speed_runner',
        'treasure_seeker',
        'boss_hunter',
        'pixel_perfect',
        'speed_runner',
        'treasure_seeker',
        'boss_hunter',
        'pixel_perfect',
        'combo_king',
        'combo_king',
        'explorer'
    ]
}


def list_comprehension():
    players = [
        k for k, v in data.get('players').items()
        if v.get("total_score") > 2000
    ]
    scores_doubled = [
        v.get("total_score") * 2 for v in data.get('players').values()
    ]
    active_players = [
        k for k in data.get("players").keys()
    ]
    print("High scorers (>2000): ", end="")
    print(players)
    print("Scores doubled: ", end="")
    print(scores_doubled)
    print("Active players: ", end="")
    print(active_players)


def combined_analysis(players, unique_ach, scores):
    print("Total players: ", len(players))
    print("Total unique achievements: ", len(unique_ach))
    scores = [v for v in scores.values()]
    print("Average score: ", sum(scores) / len(scores))
    top_performer = {
        k: v for k, v in data.get("players").items()
        if v.get('total_score') == max(scores)
    }
    name = [k for k in top_performer]
    score = [v.get("total_score") for v in top_performer.values()]
    count_ach = [v.get("achievements_count") for v in top_performer.values()]
    print(f"Top performer: {name[0]} ({score[0]} points", end="")
    print(f", {count_ach[0]} achievements)")


def dict_comprehension():
    player_scores = {
        k: v.get("total_score") for k, v in data.get("players").items()
    }
    achievement_counts = {
        k: v.get("achievements_count") for k, v in data.get("players").items()
    }
    score_categories = {}
    print("Player scores: ", end="")
    print(player_scores)
    print("Achievement counts: ", end="")
    print(achievement_counts)
    print("Score categories: ", end="")
    print(score_categories)


def set_comprehension():
    unique_players = set(v.get("player") for v in data.get("sessions"))
    print(f"Unique players: {unique_players}")
    unique_ach = set(v for v in data.get("achievements"))
    print(f"Unique achievements: {unique_ach}")
    active_regions = set(v.get("region") for v in data.get("sessions"))
    print(f"Active regions: {active_regions}")


def ft_analytics_dashboard():
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    list_comprehension()
    print("=== Dict Comprehension Examples ===")
    dict_comprehension()
    print("=== Set Comprehension Examples ===")
    set_comprehension()
    print("=== Combined Analysis ===")
    unique_players = set(v.get("player") for v in data.get("sessions"))
    unique_ach = set(v for v in data.get("achievements"))
    player_scores = {
        k: v.get("total_score") for k, v in data.get("players").items()
    }
    combined_analysis(unique_players, unique_ach, player_scores)


ft_analytics_dashboard()
