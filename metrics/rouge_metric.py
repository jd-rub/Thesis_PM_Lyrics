from rouge import Rouge
from metric import Metric

class Rouge_Metric(Metric):
    def get_score(self):
        # TODO: ROUGE can't deal with empty hypotheses or references
        references = self.input_data.split('\n')
        hypotheses = self.output_data.split('\n')

        rouge = Rouge()
        scores = rouge.get_scores(hypotheses, references)
        return scores
