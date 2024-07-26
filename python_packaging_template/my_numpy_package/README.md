# My NumPy Package

This is a sample Python package that provides a couple of NumPy functions.


## Installation

You can install the package via pip:

```bash
pip install -e .
```

## Usage

```python
import numpy as np

import my_numpy_package


array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

result = my_numpy_package.add_arrays(array1, array2)

print(result)
```

## Testing

You can run the tests using the following command:

```bash
pytest
```
