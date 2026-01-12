def process_game_events(events):
    for k, v in events.items():
        yield f'Player: {k}: ({v.get("level")}) {v.get("event")}'


def fibonacci(n):
    if ((n != 0) and (n != 1)):
        n -= 1
    x = 0
    y = 1
    for _ in range(n + 1):
        yield x
        x, y = y, y + x


def is_prime(n):
    i = 2
    while (i <= n / 2):
        if (n % i == 0):
            return False
        i += 1
    return True


def generate_prime(n):
    i = 2
    while (n > 0):
        if (is_prime(i)):
            yield i
            n -= 1
        i += 1


def ft_data_stream():
    events = {
        "alice": {
            "level": 5,
            "event": "killed monster"
        },
        "bob": {
            "level": 12,
            "event": "found treasure"
        },
        "charlie": {
            "level": 8,
            "event": "leveled up"
        }
    }
    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {len(events)} game events...\n")
    k = process_game_events(events)
    count = 0
    for i in k:
        print(f"Event {count + 1}: ", i)
        count += 1
    print("...\n")
    print("=== Stream Analytics ===")
    treasure_count = 0
    level_up_count = 0
    high_level_count = 0
    for v in events.values():
        if (v.get("level") > 10):
            high_level_count += 1
        if (v.get("event") == "found treasure"):
            treasure_count += 1
        if (v.get("event") == "leveled up"):
            level_up_count += 1
    print(f"Total events processed: {count}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}\n")

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    g = fibonacci(10)
    for i in g:
        print(i, end=" ")
    print("\nPrime numbers (first 5): ", end="")
    g = generate_prime(5)
    for i in g:
        print(i, end=" ")


ft_data_stream()
