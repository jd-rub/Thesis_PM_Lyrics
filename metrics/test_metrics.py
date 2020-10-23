corpus_file = open("corpus_clean.txt", encoding='utf-8')
corpus = corpus_file.read()

test_data = (
    "Playing games has always been thought to be important to "
    "the development of well-balanced and creative children; "
    "however, what part, if any, they should play in the lives "
    "of adults has never been researched that deeply. I believe "
    "that playing games is every bit as important for adults "
    "as for children. Not only is taking time out to play games "
    "with our children and other adults valuable to building "
    "interpersonal relationships but is also a wonderful way "
    "to release built up tension. He likes archaeology. Really? She likes archeology, too."
)
test = ["Playing games has always been thought to be important to the development of well-balanced and creative children; "]
from metric_suite import Metric_Suite
test_suite = Metric_Suite([""], [""])
corpus_suite = Metric_Suite(corpus, corpus)
# print("SMOG Score: ", test_suite.get_smog_score())
# print("SMOG Delta: ", test_suite.get_smog_delta())
# print("Fleisch-Kincaid Score: ", test_suite.get_fleisch_kincaid_score())
# print("Fleisch-Kincaid Delta: ", test_suite.get_fleisch_kincaid_delta())
print("Hunspell Score: ", corpus_suite.get_hunspell_score())
# print("BLEU Score: ", test_suite.get_bleu_score())
# print("Corpus BLEU Score: ", corpus_suite.get_bleu_score())
# print("ROUGE Score: ", corpus_suite.get_rouge_score())#
# print("Language Test Score: ", test_suite.get_language_tool_score())
# print("BLEURT Score: ", test_suite.get_bleurt_score())