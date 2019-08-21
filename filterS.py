import csv

#Name of the file that is being filtered
#filename = "400.csv"
filename = input("Input name of the file to be filtered:")

#Name of the file after it's been filtered
#filtername = 'filteredData.csv'
filtername = input("Input new file name:")

counter = 0

#Variables for Tweet and Hashtag index
tweetindex = 3
hashtagindex = 21
locationindex = 11

with open(filename, 'r', encoding='utf-8') as csvfile:
    with open(filtername, 'w', encoding='utf-8',newline='') as ofile:
        reader = csv.reader(csvfile)
        writer = csv.writer(ofile)

        for row in reader:
            if counter == 0:
                writer.writerow(row)
                counter = counter + 1
#CHECK TWEET
            elif "storm" in str(row[tweetindex]) or "Storm" in str(row[tweetindex]):
                writer.writerow(row)
            elif "hurricane michael" in str(row[tweetindex]) or "Hurricane Michael" in str(row[tweetindex]):
                writer.writerow(row)
            elif "hurricane Michael" in str(row[tweetindex]) or "Hurricane michael" in str(row[tweetindex]):
                writer.writerow(row)
            elif "hurricanemichael" in str(row[tweetindex]) or "HurricaneMichael" in str(row[tweetindex]):
                writer.writerow(row)
            elif "Hurricanemichael" in str(row[tweetindex]) or "hurricaneMichael" in str(row[tweetindex]):
                writer.writerow(row)
            elif "hurricane" in str(row[tweetindex]) or "Hurricane" in str(row[tweetindex]):
                writer.writerow(row)
#CHECK HASHTAG
            elif "storm" in str(row[hashtagindex]) or "Storm" in str(row[hashtagindex]):
                writer.writerow(row)
            elif "hurricane michael" in str(row[hashtagindex]) or "Hurricane Michael" in str(row[hashtagindex]):
                writer.writerow(row)
            elif "hurricane Michael" in str(row[hashtagindex]) or "Hurricane michael" in str(row[hashtagindex]):
                writer.writerow(row)
            elif "hurricanemichael" in str(row[hashtagindex]) or "HurricaneMichael" in str(row[hashtagindex]):
                writer.writerow(row)
            elif "Hurricanemichael" in str(row[hashtagindex]) or "hurricaneMichael" in str(row[hashtagindex]):
                writer.writerow(row)
            elif "hurricane" in str(row[hashtagindex]) or "Hurricane" in str(row[hashtagindex]):
                writer.writerow(row)
#LOCATION INDEX
#            elif "Panama City, FL" in str(row[locationindex]):
#                writer.writerow(row)
