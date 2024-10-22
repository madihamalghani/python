name="Madiha"
# length
print(len(name))
# endswith
print(name.endswith('iha'))
# starts with
print(name.startswith('mad'))
print(name.startswith('Mad'))
# capitalize
print(name.capitalize())
# upper,lower,title,find etc
# ========================================#
string_with_double_quote='Hi I am a little \"programmer\"'
print(string_with_double_quote)
print(f'{string_with_double_quote} and my name is {name}')
# ========================================#
company='"\Money is honey\"'
letter=f"""
Dear {name} You are selected as the CEO of {company} company.
"""
print(letter)
# To find double space
str="Madiha is a  good  good girl hehe"
print(str.find("  "))
# if no double space
str1='name is madiha'
print('with no double space', str1.find("  "))