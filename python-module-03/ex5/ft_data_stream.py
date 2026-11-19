from typing import Generator
from random import choice


def gen_event() -> Generator[tuple[str, str]]:

    actions = ["wake up", "sleep", "cry", "run", "walk", "kiss", "hug", "code"]
    names = ["Aleks", "Ilyas", "Ayse", "Ahmet", "Esra", "Zeliha"]

    while True:
        action = choice(actions)
        name = choice(names)

        new_tuple = (name, action)
        yield new_tuple


def consume_event(
    event_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:

    for _ in range(len(event_list)):
        event = choice(event_list)
        event_list.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    generator_gen_events = gen_event()  # implemented the generator#

    for i in range(1000):
        events = next(generator_gen_events)
        print(f"Event {i}: Player {events[0]} did action {events[1]}")

    list_for_events = []
    i = 0
    while i < 10:
        events = next(generator_gen_events)
        list_for_events.append(events)
        i = i + 1

    print(f"Built list of 10 events : {list_for_events} ")

    for events in consume_event(list_for_events):
        print("Got event from list :", events)
        print("Remains in list :", list_for_events)


if __name__ == "__main__":
    main()
