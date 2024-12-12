#задание 1

import pandas as pd
import numpy as np

a = pd.Series([4.313, 4.338, 4.358, 4.378, 4.4, 4.425, 4.447, 4.468])
print(a)
b = pd.Series(np.arange(0, 20, 2))
print(b)
c = pd.Series({'в': 1, 'траве': 3, 'сидел': 5, 'кузнечик': 7})
print(c)
