# Ryan Lugo: RJL 11/12/21

colors = ["yellow","blue","red","purple"]
colors.extend(["black","white","green"])

print(colors.count("yellow"))

colors.insert(3,"indigo")

colors.clear()

print(colors.count("red")) # Should be none