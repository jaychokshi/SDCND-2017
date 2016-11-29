"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    word_list = s.split(' ')
    word_occur_array = []
    for word in word_list:
        if word in s:
            o_count = word_list.count(word)
            word_occur_array.append((word, o_count))
        else:
            word_occur_array.append((word, 0))
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    word_occur_array = list(set(word_occur_array))
    word_occur_array.sort(key=lambda tup: (-tup[1], tup[0]))
   
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = word_occur_array[:n]
    return top_n

def test_run():
    """Test count_words() with some inputs."""
    print(count_words("cat bat mat cat bat cat", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter", 3))

if __name__ == '__main__':
    test_run()
