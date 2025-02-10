import re

class SimpleTokenizer:
  def __init__(self):
    self.token_list = {}
    print("Constructing SimpleTokenizer")
  
  def build_tokens_from_file(self, file_path):
    with open(file_path, "r", encoding="utf-8") as f:
      raw_text = f.read()
    parsed_tokens = re.split(r'([,.:;?_!"()\']|--|\s)',raw_text)
    tmp = []
    for token in parsed_tokens:
      if token.strip():
        self.token_list[token.strip()] = 1
        tmp.append(token.strip())
    print("New list of tokens = " + str(len(self.token_list)))

