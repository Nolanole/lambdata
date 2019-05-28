def date_split(X, date_cols):
  '''
  Function to split a date feature in pandas dataframe and create 3 new features,
  day, month, and year
  '''
  X = X.copy() 
  for col in date_cols:
    X[col] = pd.to_datetime(X[col], infer_datetime_format=True)
    X[col + '_year'] = X[col].dt.year
    X[col + '_month'] = X[col].dt.month
    X[col + '_day'] = X[col].dt.day
  return X

def check_nulls(X):
  '''
  Checks a pandas dataframe for nulls, prints a report stating how many null
  observations per feature (only of features that contain nulls)
  '''
  nulls = False
  for col in X.columns:
    col_nulls = X[col].isna().sum()
    if col_nulls != 0:
      nulls = True
      print('The ' + str(col) + ' feature has ' + str(col_nulls) + ' null observations')
    else: 
      continue
  if not nulls:
    print('The dataframe does not contain any null observations')
