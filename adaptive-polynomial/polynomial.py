d = input("What is the degree of the polynomial?\n> ")

print
print "Using polynomial of form: "
print "p(x) = " + " + ".join(["a{0}N^{0}".format(n) for n in range(d)])
print

print "Enter coefficients:"
print

coefficients = []
for i in range(d):
  coefficients.append(input("a{0} = ".format(i)))

print
print "Using polynomial:"
print "p(x) = " + " + ".join(["{0}N^{1}".format(coefficients[n], n) for n in range(d)])
print

p1 = sum(coefficients)
print "p(1) = {0}".format(p1)

N = p1+1
pN = sum([coefficients[i] * (N**i) for i in range(d)])

print "p({0} + 1) = p({1}) = {2}".format(p1, N, pN)
