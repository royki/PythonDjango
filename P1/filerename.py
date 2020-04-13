import os
path = 'C:/Users/croy/Downloads/SA/1.Intro'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.mp4'))
    i = i+1