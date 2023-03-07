def username_generator(first_name, last_name):
  user_name = ""
  if len(first_name) <= 3 or len(last_name) <= 3:
    if len(first_name) and len(last_name) <= 3: 
      user_name = first_name + last_name
    elif len(first_name) <= 3:
      user_name = first_name + last_name[0:4]
    else:
      user_name = first_name[0:3] + last_name
  else:
    user_name = first_name[0:3] + last_name[0:4]
  return user_name

#Alternate/Solution Code
# def username_generator(first_name, last_name):
#     if len(first_name) < 3:
#         user_name = first_name
#     else:
#         user_name = first_name[0:3]
#     if len(last_name) < 4:
#         user_name += last_name
#     else:
#         user_name += last_name[0:4]
#     return user_name

print(username_generator("Abe", "Simpson"))
print(username_generator("Mimiko", "Watanabe"))
