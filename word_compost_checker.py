def main():
    # read file
    word_list = open('wordcompost_rem.txt', 'r')
    
    # empty dictionary to add terms from word list
    compost = {}
    word_count = 1

    for word in word_list:
        # convert each line from text file to string
        term = word.strip()
        # if term is not in dic, add to dic and make key (count) 1
        if term not in compost:
            compost[term] = word_count
        # if term is already in dic, raise count by 1
        else:
            compost[term] += 1

    for word, count in compost.items():
        # if word appears more than once, print out word
        if count > 1:
            print(f"{word} was found in the Word Compost {count} times.")

    word_list.close()

    remove = input('Enter "Yes" if you would like to remove duplicate words: ')
    # ask user if they want to remove duplicated words
    if remove == "Yes":
        word_list = open('wordcompost_rem.txt', 'w')
        # rewrite wordcompost_rem.txt w/ only words whose count is 1
        for key in compost.keys():
            word_list.write(f"{key}\n")
        word_list.close()
        print("Duplicated words have been removed.")
    else:
        print("Exiting program.")

main()

# TO DO
# remove duplicate words with suffixes
