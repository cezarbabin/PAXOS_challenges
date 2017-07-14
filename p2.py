import sys

def pretty_print(registry, top_prices):
	#because we need to print only one combination
	price1 = top_prices[0][0]
	price2 = top_prices[0][1]
	first_item = registry[price1].pop(0) + " " + str(price1)
	second_item = registry[price2].pop(0) + " " + str(price2)
	return  first_item + ", " + second_item

def pretty_print3(registry, top_prices):
	#because we need to print only one combination
	price1 = top_prices[0][0]
	price2 = top_prices[0][1]
	price3 = top_prices[0][2]
	first_item = registry[price1].pop(0) + " " + str(price1)
	second_item = registry[price2].pop(0) + " " + str(price2)
	third_item = registry[price3].pop(0) + " " + str(price3)
	return  first_item + ", " + second_item + ", " + third_item

def find_closest(price, prices):
	start = 0
	end = len(prices) - 1
	if end < 0:
		return
	if end == 0:
		return prices[0]
	# perform binary search for the closest value to price
	while start < end:
		middle = start + int((end - start)/2)
		if prices[middle] == price:
			return price
		if prices[middle] > price:
			end = middle
		if prices[middle] < price:
			start = middle + 1
	return prices[end]

def find_items(budget, registry, prices):
	totals = []
	totals_dict = {}
	while len(prices) > 0:
		most_expensive = prices.pop()
		complement = find_closest(budget - most_expensive, prices)
		if complement == None:
			break
		total = most_expensive + complement
		if  total <= budget:
			if total in totals_dict:
				totals_dict[total].append((most_expensive, complement))
			else:
				totals_dict[total] = [(most_expensive, complement)]
				totals.append(total)			
	if len(totals) > 0:
		totals = sorted(totals)
		pmax = totals[len(totals) - 1] 
		return totals_dict[pmax]
	return None

def find_items3(budget, registry, prices):
	totals = []
	totals_dict = {}
	for i in range(len(prices) - 2):
		j = i + 1
		k = len(prices) - 1
		while j < k:
			total = prices[i] + prices[j] + prices[k]
			if total > budget:
				k -= 1
			else:
				totals.append(total)
				if (prices[i], prices[j], prices[k]) in totals_dict:
					totals_dict[total].append((prices[i], prices[j], prices[k]))
				else:
					totals_dict[total] = [(prices[i], prices[j], prices[k])]
				j += 1
	if len(totals) > 0:
		totals = sorted(totals)
		pmax = totals[len(totals) - 1] 
		return totals_dict[pmax]
	return None


def read_file(file_name, budget, registry, prices):
	with open(file_name, "r") as ins:
		array = []
		for line in ins:
			line = line.strip()
			item, price = line.split(',')
			price = int(price)
			# since list is sorted - we are not interested in the rest of the elements
			if price < budget:
				# avoid duplicates in prices array 
				prices.append(price)
				if price in registry:
					registry[price].append(item)					
				else:
					registry[price] = [item]
			else:
				return

file_name = sys.argv[1]
budget = int(sys.argv[3])
number_of_items = int(sys.argv[2])
registry = {}
prices = []
read_file(file_name, budget, registry, prices)

if number_of_items == 2:
	top_prices = find_items(budget, registry, prices)
	if top_prices == None:
		print "Not possible"
	else:
		print pretty_print(registry, top_prices)
else:
	top_prices = find_items3(budget, registry, prices)
	if top_prices == None:
		print "Not possible"
	else:
		print pretty_print3(registry, top_prices)

"""

"""
