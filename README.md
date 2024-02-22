# mswp, a decorator that clears temporary local variables upon function execution, preventing clutter and mitigating memory leaks
[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg)](https://badge.fury.io/py/tensorflow) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) ![Maintainer](https://img.shields.io/badge/maintainer-@louisbrulenaudet-blue)

mswp is a Python decorator designed to enhance code cleanliness and mitigate potential memory leaks by automatically clearing temporary local variables after function execution.

## Overview

Python functions often create temporary variables for intermediate computations, which can clutter the local namespace and potentially lead to memory leaks if not properly managed. mswp addresses this issue by providing a simple yet powerful decorator that automatically cleans up temporary local variables, ensuring an efficient execution environment.

## Installation
You can install mswp via pip:

```bash
pip3 install mswp
```
## Usage
  
To use mswp, simply decorate your functions with @mswp. This ensures that any temporary local variables used within the function are cleared upon completion, promoting code cleanliness and efficient memory usage.

```python
from mswp import clear

@clear
def my_function():
	temp_var = 10
	# Your code here
	return result
```
In this example, my_function is decorated with @clear, ensuring that any temporary local variables used within it are cleared upon completion.

### Parameters
`func`: The function to be decorated.

### Returns
`function`: The decorated function.

## Features
- Automatic Cleanup: mswp automatically clears temporary local variables after function execution, preventing clutter and potential memory leaks.

- Simplified Syntax: With a simple decorator, mswp streamlines code maintenance and promotes readability.

- Error Handling: mswp provides robust error handling to ensure reliable execution even in the presence of exceptions.

## Citing this project
If you use this code in your research, please use the following BibTeX entry.

```BibTeX
@misc{louisbrulenaudet2023,
	author = {Louis Brulé Naudet},
	title = {mswp, a decorator that automatically clears temporary local variables upon function execution, effectively preventing clutter and mitigating memory leaks},
	howpublished = {\url{https://github.com/louisbrulenaudet/mswp}},
	year = {2024}
}
```
## Feedback
If you have any feedback, please reach out at [louisbrulenaudet@icloud.com](mailto:louisbrulenaudet@icloud.com).
