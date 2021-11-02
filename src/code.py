import pandas as pd

def prep_dataframe(dataf: pd.DataFrame) -> pd.DataFrame:
    """
    Two-dimensional, size-mutable, potentially heterogeneous tabular data.
    Data structure also contains labeled axes (rows and columns).
    Arithmetic operations align on both row and column labels. Can be
    thought of as a dict-like container for Series objects. The primary
    pandas data structure.


    Parameters
    ----------
    **data** : *ndarray (structured or homogeneous)*, Iterable, dict, or DataFrame
        Dict can contain Series, arrays, constants, dataclass or list-like objects. If
        data is a dict, column order follows insertion-order. If a dict contains Series
        which have an index defined, it is aligned by its index.
        .. versionchanged:: 0.25.0
           If data is a list of dicts, column order follows insertion-order.


    **index** : *Index or array-like*
        Index to use for resulting frame. Will default to RangeIndex if
        no indexing information part of input data and no index provided.


    **columns** : *Index or array-like*
        Column labels to use for resulting frame when data does not have them,
        defaulting to RangeIndex(0, 1, 2, ..., n). If data contains column labels,
        will perform column selection instead.


    **dtype** : *dtype, default None*
        Data type to force. Only a single dtype is allowed. If None, infer.


    **copy** : bool or None, default None
        Copy data from inputs.
        For dict data, the default of None behaves like ``copy=True``.  For DataFrame
        or 2d ndarray input, the default of None behaves like ``copy=False``.
        .. versionchanged:: 1.3.0
   
    Examples
    --------

    ```python
    Constructing DataFrame from a dictionary.
    >>> d = {'col1': [1, 2], 'col2': [3, 4]}

    >>> df = pd.DataFrame(data=d)

    >>> df
       col1  col2
    0     1     3
    1     2     4

    Notice that the inferred dtype is int64.
    ```
    """
    return dataf.assign(A = lambda d: d["i"] - 10)

def say_hello(name: str, age: int) -> str:
      """
      This function says hello
      """
      A = f"Hello {name} who is {age} yeasr old."
      return A




