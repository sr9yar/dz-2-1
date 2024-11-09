word_one = 'test'
word_two = 'testing'

def main(word: str):
  if len(word) % 2:
    return parse_odd(word)
  return parse_even(word)

def parse_odd(word: str):
  if len(word) < 2:
    return word
  start_index = int((len(word) - 1) / 2)
  end_index = start_index + 1 
  return word[start_index:end_index]

def parse_even(word: str):
  start_index = int(((len(word)) / 2) - 1)
  end_index = start_index + 2 
  return word[start_index:end_index]



result_one = main(word_one)
result_two = main(word_two)


print(f"Two middle letters for input '{word_one}' are: {result_one}")
print(f"One middle letter for input '{word_two}' is: {result_two}")
