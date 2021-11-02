import pandas as pd

def prep_dataframe(dataf: pd.DataFrame) -> pd.DataFrame:
      """[summary]

      Args:
          dataf (pd.DataFrame): [description]

      Returns:
          pd.DataFrame: [description]
      """
      return dataf.assign(A = lambda d: d["i"] - 10)

def say_hello(name: str, age: int) -> str:
      """[summary]

      Args:
          name (str): [description]
          age (int): [description]

      Returns:
          str: [description]
      """
      A = f"Hello {name} who is {age} yeasr old."
      return A




