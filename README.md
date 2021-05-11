# Job-interview-corpus
Create a text corpus with the python library of job interview dialogues containing general questions and answers and provide some examples of statistical analysis from the corpus.

To use the corpus first download or clone the file in you device.
```bash
https://github.com/1dipesh/Job-interview-corpus.git
```


You have to install pandas and NLTK python library to use this corpus.
```bash
pip install pandas
```
```bash
pip install nltk
```
You can open the CodeExample.ipynb where 10 functions are provided which are explained below:
1. raw_text : It returns a raw corpus text of the data we have in the corpus
2. raw_question_answer : It returns a dataframe of raw corpus text where each row represents a question and its answer.
3. raw : It returns the unprocessed corpus contents of the corpus.
4. words : It returns every word in the corpus in the form of a list.
5. sents : It returns the sentence in the corpus in the form of a list.
6. tagged_words : It returns the word of the corpus along with it’s POS tag in the form of a tuple. i.e. (word, POS tag)
7. tagged_sents : It returns the word of the corpus of a single sentence with it’s POS tag in the form of tuple.
8. parsed_sents : It returns the parsed sentence of the corpus.
9. dependency_parsed_sents : It returns the dependency parsed sentences of the corpus.
10. visualize_parsed_tree : It returns the parsed tree of the parsed sentences.

