with open('Movies.txt', 'r') as movie_file:
    readM = movie_file.readlines()

# فقط 60 خط آخر رو نگه می‌داریم
last_60_lines = readM[-60:]

# چاپ با حفظ تب و اینتر
for line in last_60_lines:
    print(line, end='')
