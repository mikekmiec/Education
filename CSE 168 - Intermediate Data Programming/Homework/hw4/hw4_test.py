from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine


# This file is left blank for you to fill in with your tests!

doc = Document('dog.txt')
doc2 = Document('abcd.txt')
se = SearchEngine("test")


def test_term_frequency():
    """
    Test the function term_frequency from the document class
    """
    assert_equals(0.07142857142857142, doc.term_frequency('dog'))
    assert_equals(0.21428571428571427, doc.term_frequency('cutest'))
    assert_equals(0, doc.term_frequency('a'))


def test_get_words():
    """
    Test the function get_words from the document class
    """
    assert_equals(['the', 'cutest', 'dog', 'but', 'cat', 'is', 'than',
                  'big'], doc.get_words())
    assert_equals(True, 'a' in doc2.get_words())


def test_get_filename():
    """
    Test the function get_fname from the document class
    """
    assert_equals('dog.txt', doc.get_filename())
    assert_equals('abcd.txt', doc2.get_filename())


def test_get_word_idf():
    """
    Test the function get_word_idf from the SearchEngine class
    """
    assert_equals(0.4054651081081644, se.get_word_idf('hello'))
    assert_equals(1.0986122886681098, se.get_word_idf('meet'))
    assert_equals(0, se.get_word_idf('swan'))


def test_get_dname():
    """
    Test the function get_dname from the SearchEngine class
    """
    assert_equals('test', se.get_dname())


def test_search():
    """
    Test the function search from the SearchEngine class
    """
#    assert_equals(None, se.search('hi'))
#    assert_equals(['test/hello.txt', 'test/nice.txt', 'test/temp.txt'],
#                  se.search('hello'))
#    assert_equals(['test/temp.txt', 'test/hello.txt', 'test/nice.txt'],
#                  se.search('hi emily'))
#    assert_equals(['test/nice.txt'], se.search('meet you'))
#    assert_equals(None, se.search('hi baby'))
    
    
def main():
    test_term_frequency()
    test_get_words()
    test_get_filename()
#    test_get_word_idf()
#    test_get_dname()
#    test_search()
    
if __name__ == '__main__':
    main()