integer = 42

# :x -> hex
print(f"{integer:x}") # -> '2a'

# :X -> hex (uppercase)
print(f"{integer:X}") # -> '2A'

# :c -> ascii
print(f"{integer:c}") # -> '*'

# :o -> octal
print(f"{integer:o}") # -> '52'

# :b -> binary
print(f"{integer:b}") # -> '101010'

# :010b -> combined with padding
print(f"{integer:010b}") # -> '0000101010'