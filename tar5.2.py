def join(*item, tav='-'):
  if len(item)==0:
     return None
  new_list=[]
  flag = False
  for l in item:
     if flag:
        new_list.append(tav)
     flag = True
     new_list+=l;

  return new_list



print(join([1, 2], [8], [9, 5, 6], tav='@'))
print(join([1, 2], [8], [9, 5, 6], tav='@'))
print(join([1]))

