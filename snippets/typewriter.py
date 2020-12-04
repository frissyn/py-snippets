def typewriter(value: str, stutter: int):
    import time
    
    for char in value:
        print(char, end="", flush=True)
        time.sleep(sutter/1000.0)


typewriter("Prints each letter and pauses for a given value of milliseconds.", 100)
