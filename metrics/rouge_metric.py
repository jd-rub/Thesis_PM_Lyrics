from rouge import Rouge
from .metric import Metric

class Rouge_Metric(Metric):
    def get_score(self):
        # TODO: ROUGE can't deal with empty hypotheses or references
        reference = self.input_data
        hypothesis = self.output_data

        rouge = Rouge()
        scores = dict()
        try:
            scores_raw = rouge.get_scores([hypothesis], [reference])[0]
        except:
            scores["ROUGE-1"] = 0
            scores["ROUGE-2"] = 0
            scores["ROUGE-L"] = 0
            return scores

        scores["ROUGE-1"] = scores_raw["rouge-1"]["r"]
        scores["ROUGE-2"] = scores_raw["rouge-2"]["r"]
        scores["ROUGE-L"] = scores_raw["rouge-l"]["r"]

        return scores
