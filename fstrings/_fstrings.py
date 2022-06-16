string = 42

# :x -> hex
print(f"{string:x}") # -> '2a'

# :X -> hex (uppercase)
print(f"{string:X}") # -> '2A'

# :c -> ascii
print(f"{string:c}") # -> '*'

# :o -> octal
print(f"{string:o}") # -> '52'

# :b -> binary
print(f"{string:b}") # -> '101010'

# :010b -> combined with padding
print(f"{string:010b}") # -> '0000101010'