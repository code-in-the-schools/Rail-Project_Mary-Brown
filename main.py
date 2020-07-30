def create_rails(rail_list, n):
  for i in range(n):
    rail_list.append(list())

def fill_rails(rail_list, text):
  current_rail = 0
  change = 1

  for char in text:
    pass
    rail_list[current_rail].append(char)
    current_rail += change
    if current_rail == len(rail_list) - 1: # if we're at the bottom rail
      change = -1   # go up
    elif current_rail == 0: # if we're at the top rail
      change = 1    # go down
    else:
      pass          # do nothing

def get_cipher_text(rail_list):
    text = ''
    for rail in rail_list:
      text += ''.join(rail)

    return text

plain_text = str(input('Enter text: '))
num_rails = int(input('Enter a number: '))
rails = list()

create_rails(rails, num_rails)  # Where we create rails according to num_rails
fill_rails(rails, plain_text)   # where we encrypt, but usign the rail fence algorithm
print(rails)
cipher_text = get_cipher_text(rails)

print(cipher_text)



#I did only this much on my own
#plain_text = str(input('Enter text: '))
#num_rails = int(input('Enter a number: '))

#rails = []
#def func(rail_list, n): #rail list but idk how to name it
#  print(num_rails)