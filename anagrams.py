import gzip
import timeit
import unittest
from collections import Counter


class CounterAlgorithm:
    def get_anagrams(self, word, words):
        counted_word = Counter(word)
        anagrams = []
        for w in words:
            if Counter(w) == counted_word:
                anagrams.append(w)
        return anagrams


class SortedAlgorithm:
    def get_anagrams(self, word, words):
        sorted_word = sorted(word)
        anagrams = []
        for w in words:
            if sorted(w) == sorted_word:
                anagrams.append(w)
        return anagrams


class Anagrams:
    def __init__(self, words_file_path, algorithm_class=None):
        with gzip.open(f'{words_file_path}.gz', 'r') as f:
            self.words = f.read().decode('utf8').lower().split('\n')

        self.algorithm = algorithm_class() if algorithm_class else CounterAlgorithm()

    def get_anagrams(self, word):
        return self.algorithm.get_anagrams(word, self.words)


class TestAnagrams(unittest.TestCase):
    def test_anagrams(self):
        anagrams = Anagrams('words.txt')
        self.assertEqual(
            anagrams.get_anagrams('dictionary'),
            ['dictionary', 'indicatory']
        )


class TestAlgorithms(unittest.TestCase):
    def setUp(self) -> None:
        self.anagrams = Anagrams('words.txt')
        self.algorithms = [CounterAlgorithm, SortedAlgorithm]

    def test_anagrams(self):
        for algorithm in self.algorithms:
            self.anagrams.algorithm = algorithm()
            self.assertEqual(
                self.anagrams.get_anagrams('dictionary'),
                ['dictionary', 'indicatory']
            )

    def test_anagrams_none(self):
        for algorithm in self.algorithms:
            self.anagrams.algorithm = algorithm()
            self.assertEqual(
                self.anagrams.get_anagrams('rhythm'),
                ['rhythm']
            )


if __name__ == '__main__':
    timing_setup = {
        'algorithms': [CounterAlgorithm, SortedAlgorithm],
        'number': 100
    }

    anagrams = Anagrams('words.txt')
    for algorithm in timing_setup['algorithms']:
        print(f'Testing time for {algorithm.__name__}')
        anagrams.algorithm = algorithm()
        result = timeit.timeit(lambda: anagrams.get_anagrams('dictionary'), number=timing_setup['number'])
        print(
            f"Result: {result} for {timing_setup['number']} iterations, "
            f"{result / timing_setup['number']} for 1 iteration"
        )
