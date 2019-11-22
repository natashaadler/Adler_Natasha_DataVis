import csv
import matplotlib.pyplot as plt 

#pie chart for mens hockey medal colors (gold, silver, bronze)
#arrays for each color


golds = []
silvers = []
bronzes = []




categories =[]



#asking the csv reader to open it so we can parse it
with open('mensHockey.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0 

	for row in reader:
		if line_count is 0:
			#parse that first row of text data out of the file
			categories.append(row)
			line_count += 1
		else:
			if row[7] == "Gold":
				print("Won, Gold!")
				golds.append(row[7])
			elif row[7] == "Silver":
				print("Won, Silver!")
				silvers.append(row[7])
			elif row[7] == "Bronze":
				print("Won, Bronze!")
				bronzes.append(row[7])

			line_count += 1

print("Gold medals:", len(golds))
print("Silver medals:", len(silvers))
print("Bronze medals:", len(bronzes))

#plot a pie chart

labels = ("Gold", "Silver", "Bronze")
#sizes are how many and how large the slices of the pie chart will be
sizes = [len(golds), len(silvers), len(bronzes)]
colors = ["gold", "silver", "darkgoldenrod"]
explode = (0.1, 0, 0)

plt.pie(sizes, explode=explode, colors=colors, autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis("equal")

plt.legend(labels, loc=1)
plt.title("Gold Medles For Men's Hockey")
plt.xlabel("Medals since 1924")
plt.show()

















