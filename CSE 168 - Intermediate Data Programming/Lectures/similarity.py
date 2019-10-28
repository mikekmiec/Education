# Hunter Schafer (hschafer)
# This program computes the most similar wikipedia page to page for
# a particualr name


import pandas as pd


def count_words(text):
    """
    Takes the text of a document and converets it to
    a dictionary of word counts.
    """
    result = {}
    for word in text.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


def bag_of_words(data):
    """
    Takes a dataframe with name and text columns and converts each
    text into a word-count dictionary. Returns a dictionary with
    names as keys and values are word-count dictionary for that
    person's text.
    """
    result = {}
    for i in data.index:
        row = data.loc[i]
        result[row['name']] = count_words(row['text'])
    return result


def euclidian_distance(d1, d2):
    """
    Takes two bag-of-word dictionaries and computes the Euclidian distance
    between them. The dictionaries are sparse, so any missing words
    have count 0.
    """
    # We need to loop over words in both vectors
    words = d1.keys() | d2.keys()

    total = 0
    for word in words:
        # If the word is missing in either vector, make the count 0
        c1 = d1[word] if word in d1 else 0
        c2 = d2[word] if word in d2 else 0
        total += (c1 - c2) ** 2
    return total ** 0.5


def magnitude(d):
    """
    Returns the magnitude of the given bag-of-words vector.
    The magnitude is defined as the square root of the sum
    the components squared.
    """
    total = 0
    for count in d.values():
        total += count ** 2
    return total ** 0.5


def cosine_distance(d1, d2):
    """
    Computes the cosine distance between the two bag-of-word vectors
    which is related to the angle between them. Vectors that have
    a small angle between them, will have a small distance, while
    vectors with a large angle will have a large difference.
    """
    words = d1.keys() & d2.keys()
    total = 0
    for word in words:
        total += d1[word] * d2[word]
    return 1 - total / (magnitude(d1) * magnitude(d2))


def nearest_neighbor(name, bow):
    """
    Takes a name and a bag of words
    (keys are name, values are word-count dictionaries) and returns
    the nearest neighbor of the given name in the dataset. The name
    itself is not considered in the nearest neighbor computation.
    """
    closest_person = None
    closest_distance = None
    for person in bow.keys():
        # find distance using euclidean or cosine!
        distance = cosine_distance(bow[name], bow[person])
        if person != name and \
                (closest_person is None or distance < closest_distance):
            closest_person = person
            closest_distance = distance
    return closest_person, closest_distance


def main():
    df = pd.read_csv('people_wiki.csv')
    bow = bag_of_words(df)
    print(nearest_neighbor('Barack Obama', bow))
    print(nearest_neighbor('Joe Biden', bow))


if __name__ == "__main__":
    main()
