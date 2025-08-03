import random

ds = [str(random.randint(1, 100)) for _ in range(20)]
with open('random.txt', 'w') as f:
    f.write('\n'.join(ds))
