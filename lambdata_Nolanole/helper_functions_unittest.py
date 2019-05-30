from helper_functions import date_split
import pandas as pd 
import unittest


class Date_split_test(unittest.TestCase):
  
    def test_date_split(self):
        df = pd.DataFrame([[1,'9/23/1998'], [2,'8/30/1999'], [3,'1/1/2010']], 
                  columns=['event', 'date'])
        df = date_split(df, date_cols=['date'])
        self.assertEqual(len(df.columns), 5) 
    def test_keep_date_cols(self):
        df = pd.DataFrame([[1,'9/23/1998'], [2,'8/30/1999'], [3,'1/1/2010']], 
                  columns=['event', 'date'])
        df = date_split(df, date_cols=['date'], keep_date_cols=False)
        self.assertEqual(len(df.columns), 4)


if __name__ == '__main__':
    unittest.main()
