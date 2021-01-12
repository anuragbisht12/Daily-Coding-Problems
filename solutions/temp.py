def find_pallindrome(string_list):
  return_indices=[]
  for i in range(len(string_list)):
    for j in range(len(string_list)):
      print(string_list[i],string_list[j],is_pallindrome(string_list[i]+string_list[j]))
      if is_pallindrome(string_list[i]+string_list[j]):
        return_indices.append((i,j))

  return return_indices


def is_pallindrome(s1):
  return s1==s1[::-1]


print(find_pallindrome(["code", "edoc", "da", "d"]))




