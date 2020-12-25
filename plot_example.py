import matplotlib.pyplot as plt
import seaborn as sns


# ages = [25, 65, 26, 26, 46, 37, 36, 36, 28, 28, 57, 37, 48, 48, 37, 28, 60,
#        25, 65, 46, 26, 46, 37, 36, 37, 29, 58, 47, 47, 48, 48, 47, 48, 60]

# fig, ax = plt.subplots()
# ax.hist(ages)
# plt.show()

fig, ax = plt.subplots()
ax.axis("equal")
ax.pie([24, 18],
        labels = ["Femmes", "Hommes"],
        autopct="%1.1f pourcents")
plt.title("Un diagramme circulaire")
plt.show()