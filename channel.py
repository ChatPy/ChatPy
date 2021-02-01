def decode(message):
  data_array = message.split("|")
  return [data_array[0], data_array[1]]
