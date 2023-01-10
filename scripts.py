values = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
value_list = values.split()


def encode(input):
  output_list = []
  for c in input:
    if c == ' ':
      output_list.append(0)
    else:
      output_list.append(value_list.index(c) + 1)
  return output_list


def printn(list):
  output = ""
  for i in list:
    output += str(i)
  print(output)

def returnstring(list):
  output = ""
  for i in list:
    output += str(i)
  return output


def decode(list):
  output_list = []
  for i in list:
    if i == 0:
      output_list.append(' ')
    else:
      output_list.append(value_list[i - 1])
  return output_list


##printn(decode([8, 5, 12, 12, 15, 0, 8, 5, 12, 12, 15]))