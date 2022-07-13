# Assumptions
- Client code must stay the same.
- Tests must pass and define the interface.
- Single word anagram.
- `get_anagrams` returns a list where the first element is the input string, so for words with no anagrams one element will be returned. 

# Design
Initially the Counter implementation was used as it looks clean and `Counter()` will return a nice count of each letter in the string.

Further work showed a simple comparison using `sorted()` had higher performance.

I then refactored this into seperate algorithm classes that can be injected at runtime (see the Strategy pattern). I also kept the original client and interface code the same and used a default.

To test the performance I use `timeit` where we can see that the `SortedAlgorithm` is much faster.

For unittests I kept the existing client code and added a false test where there is no anagram and also tested both algorithms and code worked correctly.

To prevent any environment issues I have provided a `Dockerfile` that will run the tests and timings.

# Installation and usage

    docker build -t ms .
    docker run ms

# Output

    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 1.972s
    
    OK
    Testing time for CounterAlgorithm
    Result: 52.16491198300355 for 100 iterations, 0.5216491198300355 for 1 iteration
    Testing time for SortedAlgorithm
    Result: 13.22338408900032 for 100 iterations, 0.1322338408900032 for 1 iteration

# Conclusions
`SortedAlgorithm` is provably faster than `CounterAlgorithm`

Further improvements could include:
- Multi word anagrams are much more difficult and require a more advanced algorith as the computation increases exponentially. Also could utilise multiprocessing.  This was beyond the scope of the suggested 2hr research and development time.
- A simple gzip read on class instantion was used as it is quick and easy to read. This could be decoded into text, memory caching could be used.
- For more complicated implementations the data could be preprocessed e.g. multi combinations of anagrams could be calculated and gzipped or cached, which would reduce computation later. Storage is cheap.