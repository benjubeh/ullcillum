def time_spent(df):
  """Computes the time spent on each task.

  Args:
    df: A pandas DataFrame with columns 'task_id', 'start_time', and 'end_time'.

  Returns:
    A pandas DataFrame with columns 'task_id' and 'time_spent'.
  """

  # Convert the start and end times to timestamps.
  df['start_time'] = pd.to_datetime(df['start_time'])
  df['end_time'] = pd.to_datetime(df['end_time'])

  # Compute the time spent on each task.
  df['time_spent'] = df['end_time'] - df['start_time']

  # Return the DataFrame with the time spent on each task.
  return df[['task_id', 'time_spent']]
