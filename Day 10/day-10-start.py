# First way
def format_name(f_name, l_name):
  f_name = f_name.title()
  l_name = l_name.title()

  print(f"{f_name} {l_name}")

format_name("ANGEla", "yu")

# Second way
def format_name(f_name, l_name):
  f_name = f_name.title()
  l_name = l_name.title()

  return f"{f_name} {l_name}"

output = format_name("ANGEla", "yu")
print(output)
