fname = "majid "
lname = "gorkani"
name = fname + lname
print(name)

#replace() method replace in evry where and multiple
name = name.replace("majid","milad")
print(name)
str = "majid gourkani is a god majid and is a new majid"
#replace() have 3 input, [old word, new word, count]
print(str.replace("majid","milad",2))

#.count() methos find how much a word exist
print(str.count("majid"))
