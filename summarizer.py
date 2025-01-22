import nltk
import re
from heapq import nlargest

try:
    stopwords = nltk.corpus.stopwords.words('english')
except:
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('english')


# Get raw text from document, Tokenize into sentences
def get_sentences(filepath):
    with open(filepath, "r") as file:
        raw_text = file.read()

    sentences = nltk.sent_tokenize(raw_text)
    return sentences


# Clean the sentences
def get_clean_sentences(sentences):
    clean_sentences = []
    for sentence in sentences:
        clean_sent = re.sub('[^a-zA-Z]', " ", sentence)
        clean_sent = clean_sent.lower()
        clean_sentences.append(clean_sent)

    return clean_sentences


# Scoring each word
def get_word_counts(clean_sentences):
    word_count = {}

    for sentence in clean_sentences:
        for word in sentence.split():
            if word in stopwords:
                continue
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

    max_word_count = max(word_count.values())

    # Normalize Counts: word_count/max_word_count
    for word, cnt in word_count.items():
        word_count[word] = cnt/max_word_count

    return word_count


# Scoring Each sentence
def get_sentence_scores(clean_sentences, word_counts):
    sentence_scores = {sent:0 for sent in clean_sentences}  # Initialize each sentence score as 0

    for sentence in clean_sentences:
        for word in sentence.split():
            if word not in stopwords:
                sentence_scores[sentence] += word_counts[word]

    return sentence_scores


# Get top sentences
def get_top_sentences(sentences, clean_sentences, sentence_scores, percentage):
    clean_sent_idx = {s: i for i, s in enumerate(clean_sentences)}  # clean_sentences: sentence -> idx
    no_of_sentences = int(percentage * len(clean_sentences))


    # Top clean sentences
    top_clean_sentences = nlargest(no_of_sentences, sentence_scores)
    # Sort them according to paragraph order
    top_clean_sentences = sorted(top_clean_sentences, key=lambda sent: clean_sent_idx[sent])  

    # Top Clean sentences to Top sentences
    top_sentences = []
    for clean_sent in top_clean_sentences:
        idx = clean_sent_idx[clean_sent]
        top_sentences.append(sentences[idx])

    return top_sentences


# Summarize sentences using helper functions
def summarize(filepath: str, percentage: float = 0.2) -> str:
    """
        The function that summarizes the text document given as input.
    """
    sentences = get_sentences(filepath)
    clean_sentences = get_clean_sentences(sentences)

    word_counts = get_word_counts(clean_sentences)
    sentence_scores = get_sentence_scores(clean_sentences, word_counts)

    top_sentences = get_top_sentences(sentences, clean_sentences, sentence_scores, percentage)


    return "".join(top_sentences)



# SUMMARIZATION TOOL DEMO
if __name__ == "__main__":
    filepath = "documents/harry_potter_plot.txt"
    summary = summarize(filepath, percentage=0.2)
    print(summary)