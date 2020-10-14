# import stanza

# test = '''This sentence no order good
# '''

# stanza.download('en')       # This downloads the English models for the neural pipeline
# nlp = stanza.Pipeline(lang='en', logging_level='DEBUG') # This sets up a default neural pipeline in English
# doc = nlp(test)

import language_tool_python
from metric import Metric

tool = language_tool_python.LanguageTool('en-US')

class Language_Tool_Metric(Metric):
    matches = None
    def get_score(self):
        self.matches = tool.check(self.output_data)
        return len(self.matches)