import random
import typing


def gen_event() -> typing.Generator:  # kesinlikle tam anlamadım
    players = ["Alex", "Ilyas", "ayse", "mehmet", "ikra"]
    actions = [
        "eat",
        "sleep",
        "cry",
        "walk",
        "kiss",
        "hug",
        "kick",
        "run",
        "be depressed",
        "breath"
    ]

    while True:
        player = random.choice(players)
        action = random.choice(actions)

        yield (player, action)  # bu da


def consume_event(events: list) -> typing.Generator:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield event


def main() -> None:
    event_generator = gen_event()

    for i in range(1000):
        event = next(event_generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    events = []

    for i in range(10):
        events.append(next(event_generator))

    for event in consume_event(events):
        print(event)


if __name__ == "__main__":
    main()
