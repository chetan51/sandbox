print "Choose a polynomial with nonnegative integer coefficients, p(x)."
print "I'll ask you two questions, and then guess p(x)."
print

p1 = input("What is p(1)?\n> ")
N = p1+1
pN = input("What is p({0} + 1) = p({1})?\n> ".format(p1, N))

print
print "Your polynomial, p(x), is:"

coefficients = []
yi = pN

while yi > 0:
  ai = yi % N
  coefficients.append(ai)
  yi = (yi - ai) / N

d = len(coefficients)
print "p(x) = " + " + ".join(["{0}N^{1}".format(coefficients[n], n) for n in range(d)])
