from .bleu import Bleu_Metric
from .rouge_metric import Rouge_Metric

class Translation_Metrics():
    def __init__(self, hypothesis, reference):
        self.bleu = Bleu_Metric(hypothesis, reference)
        self.rouge = Rouge_Metric(hypothesis, reference)
        self.scores = dict()
    
    def calculate_metrics(self):
        self.scores['bleu'] = self.bleu.get_score()
        self.scores['rouge'] = self.rouge.get_score()
        