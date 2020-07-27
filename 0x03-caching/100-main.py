#!/usr/bin/python3
""" 100-main """
LFUCache = __import__('100-lfu_cache').LFUCache

# {'A': { used: 1, fecha: 1 }}

my_cache = LFUCache()
my_cache.put("A", "Hello") # {'A': { used: 1, date: 1 }}
my_cache.put("B", "World") # {'A': { used: 1, date: 1 }, 'B': { used: 1, date: 2 }}
my_cache.put("C", "Holberton") # {'A': { used: 1, date: 1 }, 'B': { used: 1, date: 2 }, 'C': { used: 1, date: 3 }}
my_cache.put("D", "School") # {'A': { used: 1, date: 1 }, 'B': { used: 1, date: 2 }, 'C': { used: 1, date: 3 }, 'D': { used: 1, date: 4 }}
my_cache.print_cache()
# Current cache:
# A: Hello
# B: World
# C: Holberton
# D: School
print(my_cache.get("B")) # {'A': { used: 1, date: 1 }, 'B': { used: 2, date: 2 }, 'C': { used: 1, date: 3 }, 'D': { used: 1, date: 4 }}
# World
my_cache.put("E", "Battery") # {'B': { used: 2, date: 2 }, 'C': { used: 1, date: 3 }, 'D': { used: 1, date: 4 }, 'E': { used: 1, date: 5 } }
# DISCARD: A
my_cache.print_cache()
# Current cache:
# B: World
# C: Holberton
# D: School
# E: Battery
my_cache.put("C", "Street") # {'B': { used: 2, date: 2 }, 'C': { used: 2, date: 3 }, 'D': { used: 1, date: 4 }, 'E': { used: 1, date: 5 } } # Cambia C ?
my_cache.print_cache()
# Current cache:
# B: World
# C: Street
# D: School
# E: Battery
print(my_cache.get("A")) # {'B': { used: 2, date: 2 }, 'C': { used: 2, date: 3 }, 'D': { used: 1, date: 4 }, 'E': { used: 1, date: 5 } }
# None
print(my_cache.get("B")) # {'B': { used: 3, date: 2 }, 'C': { used: 2, date: 3 }, 'D': { used: 1, date: 4 }, 'E': { used: 1, date: 5 } }
# World
print(my_cache.get("C")) # {'B': { used: 3, date: 2 }, 'C': { used: 3, date: 3 }, 'D': { used: 1, date: 4 }, 'E': { used: 1, date: 5 } }
# Street
my_cache.put("F", "Mission") # {'B': { used: 3, date: 2 }, 'C': { used: 3, date: 3 }, 'E': { used: 1, date: 5 }, 'F': { used: 1, date: 6 } }
# DISCARD: D
my_cache.print_cache()
# Current cache:
# B: World
# C: Street
# E: Battery
# F: Mission
my_cache.put("G", "San Francisco") # {'B': { used: 3, date: 2 }, 'C': { used: 3, date: 3 }, 'F': { used: 1, date: 6 }, 'G': { used: 1, date: 7 } }
# DISCARD: E
my_cache.print_cache()
# Current cache:
# B: World
# C: Street
# F: Mission
# G: San Francisco
my_cache.put("H", "H") # {'B': { used: 3, date: 2 }, 'C': { used: 3, date: 3 }, 'G': { used: 1, date: 7 }, 'H': { used: 1, date: 8 } }
# DISCARD: F
my_cache.print_cache()
# Current cache:
# B: World
# C: Street
# G: San Francisco
# H: H
my_cache.put("I", "I") # {'B': { used: 3, date: 2 }, 'C': { used: 3, date: 3 }, 'H': { used: 1, date: 8 }, 'I': { used: 1, date: 9 } }
# DISCARD: G
my_cache.print_cache()
# Current cache:
# B: World
# C: Street
# H: H
# I: I
print(my_cache.get("I")) # {'B': { used: 3, date: 2 }, 'C': { used: 3, date: 3 }, 'H': { used: 1, date: 8 }, 'I': { used: 2, date: 9 } }
# I
print(my_cache.get("H")) # {'B': { used: 3, date: 2 }, 'C': { used: 3, date: 3 }, 'H': { used: 2, date: 8 }, 'I': { used: 2, date: 9 } }
# H
print(my_cache.get("I")) # {'B': { used: 3, date: 2 }, 'C': { used: 3, date: 3 }, 'H': { used: 2, date: 8 }, 'I': { used: 3, date: 9 } }
# I
print(my_cache.get("H")) # {'B': { used: 3, date: 2 }, 'C': { used: 3, date: 3 }, 'H': { used: 3, date: 8 }, 'I': { used: 3, date: 9 } }
# H
print(my_cache.get("I")) # {'B': { used: 3, date: 2 }, 'C': { used: 3, date: 3 }, 'H': { used: 3, date: 8 }, 'I': { used: 4, date: 9 } }
# I
print(my_cache.get("H")) # {'B': { used: 3, date: 2 }, 'C': { used: 3, date: 3 }, 'H': { used: 4, date: 8 }, 'I': { used: 4, date: 9 } }
# H
my_cache.put("J", "J") # {'C': { used: 3, date: 3 }, 'H': { used: 4, date: 8 }, 'I': { used: 4, date: 9 }, 'J': { used: 1, date: 10 }}
# DISCARD: B
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()