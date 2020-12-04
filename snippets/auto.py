def auto(value: str):
    return eval(value, {})

print(f"'1' autotypes to {type(auto('1'))}")
print(f"'True' autotypes to {type(auto('True'))}")
print(f"'[1, 2, 3]' autotypes to {type(auto('[1, 2, 3]'))}")
