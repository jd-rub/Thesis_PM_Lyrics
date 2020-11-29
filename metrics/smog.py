from .metric import Metric
from textstat import textstat
"""
test_data = (
    "Playing games has always been thought to be important to "
    "the development of well-balanced and creative children; "
    "however, what part, if any, they should play in the lives "
    "of adults has never been researched that deeply. I believe "
    "that playing games is every bit as important for adults "
    "as for children. Not only is taking time out to play games "
    "with our children and other adults valuable to building "
    "interpersonal relationships but is also a wonderful way "
    "to release built up tension."
)

print(textstat.smog_index(test_data))
"""
class SMOG(Metric):
    def get_score(self):
        self.input_data = self.input_data.replace("\n", ". ")
        return textstat.smog_index(self.input_data)
    def get_delta(self):
        return abs(textstat.smog_index(self.input_data) - textstat.smog_index(self.output_data))