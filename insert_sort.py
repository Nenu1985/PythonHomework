def insertion(data):
	for i in range(1, len(data)):
		j = i - 1
		item_to_insert = data[i]
		while data[j] > item_to_insert and j >= 0:
			data[j + 1] = data[j]
			j -= 1
		data[j + 1] = item_to_insert
	return data

if __name__ == '__main__':
    print(insertion([9, 1, 15, 28, 6]))