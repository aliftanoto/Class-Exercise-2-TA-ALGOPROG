import matplotlib.pyplot as plt
X = [2004,2005,2006,2007,2008,2009,2010]
Y = [100,120,130,140,150,160,170]

plt.plot(X,Y)


plt.xlabel('Crash Number')
plt.ylabel('Years')
plt.title('Crash Cases In Jakarta')

plt.grid(True)

plt.savefig('crash.png')

plt.show()