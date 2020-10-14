from smog import SMOG
from fleisch_kincaid import Fleisch_Kincaid
from hunspell_metric import Hunspell_Metric
from bleu import Bleu_Metric
from rouge_metric import Rouge_Metric
from grammar import Language_Tool_Metric
from bleurt_metric import Bleurt_Metric

class Metric_Suite():
    def __init__(self, input_data, output_data):
        self.input_data = input_data
        self.output_data = output_data
        self.smog = SMOG(input_data, output_data)
        self.fleisch_kincaid = Fleisch_Kincaid(input_data, output_data)
        self.hunspell_metric = Hunspell_Metric(input_data, output_data)
        self.bleu_metric = Bleu_Metric(input_data, output_data)
        self.rouge_metric = Rouge_Metric(input_data, output_data)
        self.language_tool_metric = Language_Tool_Metric(input_data, output_data)
        self.bleurt_metric = Bleurt_Metric(input_data, output_data)
    
    def get_smog_score(self):
        return self.smog.get_score()

    def get_smog_delta(self):
        return self.smog.get_delta()

    def get_fleisch_kincaid_score(self):
        return self.fleisch_kincaid.get_score()

    def get_fleisch_kincaid_delta(self):
        return self.fleisch_kincaid.get_delta()

    def get_hunspell_score(self):
        return self.hunspell_metric.get_score()

    def get_bleu_score(self):
        return self.bleu_metric.get_score()

    def get_rouge_score(self):
        return self.rouge_metric.get_score()    
    
    def get_language_tool_score(self):
        return self.language_tool_metric.get_score()

    def get_bleurt_score(self):
        return self.bleurt_metric.get_score()