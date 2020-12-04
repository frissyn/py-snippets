def typewriter(value: str, stutter: int):
    import time
    
    for char in value:
        print(char, end="", flush=True)
        time.sleep(stutter/1000.0)
    
    print(flush=True)


typewriter("Prints each letter and pauses for a given value of milliseconds.", 100)
