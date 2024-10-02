with open("Color names.txt") as f:
    color_names = f.read().split(", ")

result = ",\n".join(['  "{}": {}'.format(name, name) for name in color_names])

print("{\n" + result + "\n}")


#with open("Color names.txt") as f:
#    color_names = f.read().split(", ")
#
#result = ",\n".join(['  {}: "{}"'.format(name, name) for name in color_names])
#
#print("{\n" + result + "\n}")
