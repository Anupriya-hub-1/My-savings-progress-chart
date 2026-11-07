import matplotlib.pyplot as plt

weeks = [1, 2, 3, 4, 5, 6]
savings = [400, 600, 800, 900, 995, 100]

plt.plot(weeks, savings)
plt.show()

plt.plot(weeks, savings)
plt.title("My Savings Progress")
plt.xlabel("No. of Weeks")
plt.ylabel("Savings")
plt.grid(True)
plt.ylim(0, 1000)
plt.show()

plt.plot(weeks, savings, color="green", marker="*", linestyle="dashed", linewidth="3")
plt.title("My Savings Progress")
plt.xlabel("No. of Weeks")
plt.ylabel("Savings")
plt.grid(True)
plt.ylim(0, 1000)
plt.show()

plt.bar(weeks, savings, color="orange")
plt.title("My Savings Progress")
plt.xlabel("No. of Weeks")
plt.ylabel("Savings")
plt.ylim(0, 1000)
bars = plt.bar(weeks, savings, color="orange")
plt.bar_label(bars)
plt.show()
