import os

path = os.chdir("C:\Users\engra\PycharmProjects\pic_down\cats\ltl")

i = 0

for file in os.listdir(path):
    new_file_name = "pic{}.png".format(i)
    os.rename(file,new_file_name)
    i = i + 1