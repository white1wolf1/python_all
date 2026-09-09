from typing import Generator
from random import choice

def gen_event() -> Generator:

    actions = ["wake up", "sleep", "cry", "run", "walk", "kiss", "hug", "code"]
    names = ["Aleks", "Ilyas", "Ayse", "Ahmet", "Esra", "Zeliha"]

    while True:
        action = choice(actions)
        name = choice(names)

        new_tuple = (name, action) 
        yield new_tuple

def consume_event(event_list: list) -> Generator:

    while True:
        yield choice(event_list)

def main() -> None:
    print("=== Game Data Stream Processor ===")
    generator_gen_events = gen_event() #implemented the generator#
    generator_get_event = consume_event()

    for i in range(1000):
        events = next(generator_gen_events)
        print(f"Event {i}: Player {events[0]} did action {events[1]}")

    list_for_events = []
    i = 0
    while i < 10 :
        events = next(generator_gen_events)
        list_for_events.append(events)
        i = i + 1

    print(f"Built list of 10 events : {list_for_events} ")

    while i > 0 :
        events = next(generator_get_event)
        print("Got event from list :",events)
        list_for_events.remove(events)
        print("Remains in list :",list_for_events)
        i = i - 1
    
    
if __name__ == "__main__":
    main() 