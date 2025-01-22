# NLP Document Summarizer

This repository contains Implementation code of an extractive summarization technique to create concise summaries of longer documents. This technique is extractive type, So it uses the NLP processes such as sentence_tokenzation and the **nltk library**.

**Project Outcome:** A tool that generates summaries by selecting and combining the most important sentences from the original text.

## File Structure

The file structure of this Project Repsoitory is shown below:

```none
│───summarize.ipynb     (code for document summarization technique)
│───summarizer.py       (same code in in python functions)
│───README.md
│───requirements.txt    (required python packages)
│   
└───documents           (documents for summarization)
    │   
    │───harry_potter_plot.txt 
    │───sorcerer_stone.txt
```

## Summarization Technique Algorithm

Here is the detailed explination of how this summarization technique:

1. Read the Raw text from the file.
2. Tokenize the text into sentences
3. Clean each sentence
4. Find word count for each word in all sentences and normalize those counts.
5. Calculate the sentence score of each sentence as the sum of normalized counts of all words in the sentence.
6. Finally find/extract the top sentences from the cleaned sentences based on their score.
7. Order these top clean sentences according to their occurance in paragraph.
8. Now find the actual sentence for each cleaned sentence and print it to output as summary.

**Note**: In word counts don't consider stop words for counting.