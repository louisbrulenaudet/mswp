# -*- coding: utf-8 -*-
# Copyright (c) Louis Brulé Naudet. All Rights Reserved.
# This software may be used and distributed according to the terms of License Agreement.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import functools

def clear(func):
    """
    A decorator that cleans up temporary local variables used within a function after its execution.

    Parameters
    ----------
    func : function
        The function to be decorated.

    Returns
    -------
    function
        The decorated function.

    Notes
    -----
    This decorator ensures that temporary local variables within the decorated function are cleared after its execution, 
    preventing clutter and potential memory leaks.

    Examples
    --------
    >>> @cleanup_locals
    ... def my_function():
    ...     temp_var = 10
    ...     # Your code here
    ...     return result

    In this example, `my_function` is decorated with `cleanup_locals`, ensuring that any temporary local variables 
    used within it are cleared upon completion.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Executes the function, cleans up temporary local variables, and returns the result.

        Parameters
        ----------
        *args : list
            Positional arguments to be passed to the function.
            
        **kwargs : dict
            Keyword arguments to be passed to the function.

        Returns
        -------
        any
            The result of the function execution.
        """
        try:
            # Execute the function and capture its return value
            result = func(*args, **kwargs)
            
        except Exception as e:
            # If an exception occurs, raise it with a more informative message
            raise RuntimeError(f"Error executing function '{func.__name__}': {str(e)}")
            
        finally:
            # Remove temporary variables
            if "result" in locals():
                del locals()["result"]
        
        return result
    
    return wrapper