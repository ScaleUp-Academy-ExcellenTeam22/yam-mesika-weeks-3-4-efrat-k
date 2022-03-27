"""
    :param Gets a number of lists and a character
    :return Merges the lists into one with the character between them
"""

def join(*item, sep='-'):
  if len(item) == 0:
     return None
  new_list=[]
  [l.append(sep) for l in item]
  for l in item:
     new_list+=l
  return new_list[:-1]



if __name__ == "__main__":
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1]))

