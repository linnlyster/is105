#variable makes strings
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#print out strings
print x
print y

#print out strings in strings
print "I said: %r" % x
print "I also said: '%s'-" % y

#new variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#priny variables
print joke_evaluation % hilarious

#new strings
w = "This is the left side of..."
e = "a string with a right side."

print w + e
