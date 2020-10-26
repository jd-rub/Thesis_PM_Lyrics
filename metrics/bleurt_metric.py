from bleurt import score
from .metric import Metric
# USAGE EXAMPLE: 
# References and candidates MUST be lists, single strings need to be wrapped in a single-element list
# checkpoint = "metrics/bleurt/bleurt-base-128"
# references = ["Bud Powell was a legendary pianist.", 
# "Bud Powell was a historical piano player.",
# "Bud Powell was a new yorker.",
# "Bud a day keeps the doctor away."]
# candidates = ["Bud Powell was a legendary pianist.",
# "Bud Powell was a legendary pianist.",
# "Bud Powell was a legendary pianist.",
# "Bud Powell was a legendary pianist.",]

# scorer = score.BleurtScorer(checkpoint)
# scores = scorer.score(references, candidates)
# print(scores)

checkpoint = "metrics/bleurt/bleurt-base-128"
scorer = score.BleurtScorer(checkpoint)

class Bleurt_Metric(Metric):
    def get_score(self):
        scores = scorer.score(self.input_data, self.output_data)
        return scores