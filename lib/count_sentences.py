#!/usr/bin/env python3

class MyString:
  def __init__(self, value =''):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, new_value):
    if isinstance(new_value, str):
      self._value = new_value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return list(self.value)[-1] == "."


  def is_question(self):
    return list(self.value)[-1] == "?"

  def is_exclamation(self):
    return list(self.value)[-1] == "!"

  def count_sentences(self):
    sans_exclam = self.value.replace("!", ".")
    clean_punc = sans_exclam.replace("?", ".")
    sentences = clean_punc.split(".")
    while "" in sentences:
      sentences.remove("")
    return len(sentences)
