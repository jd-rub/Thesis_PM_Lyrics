from abc import ABC, abstractmethod

class Metric(ABC):
    @abstractmethod
    def get_score(self):
        pass

    def __init__(self, input_data, output_data=None):
        self.input_data = input_data
        self.output_data = output_data
