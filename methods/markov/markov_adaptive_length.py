import markov_char_based as markov
from tqdm import tqdm

model_dir = "methods/markov/models/"

class Markov_Adaptive():
    def __init__(self, max_length):
        self.max_length = max_length
        self.models = dict()

    def load_models(self):
        model_lengths = list(filter(lambda x: x <= self.max_length, [1, 2, 4, 8, 16, 32, 64]))
        for i in tqdm(model_lengths, desc="Loading Markov Models"):
            if i <= self.max_length:
                self.models[i] = markov.load_from_file(model_dir + str(i))
            else: 
                return
    
    def generate_text(self, start_string, num_generate=2):
        assert len(self.models) != 0, "Can't generate text: No models loaded"
        assert len(start_string) > 0, "Can't generate text: start_string mustn't be empty"
        
        # find starting model
        # start_length = len(start_string)
        # model_length = 1
        # for i in self.models:
        #     if i > model_length and i <= start_length:
        #         model_length = i
        model_length = self.find_largest_possible_model(start_string)
        current_model = self.models[model_length]
        current_seed = start_string[-model_length:]
        generated_text = start_string

        # Generate text
        for _ in range(num_generate):
            try :
                current_seed = generated_text[-model_length:]
                generated_text += current_model.predict(current_seed)

                if model_length < self.max_length:
                    new_model_length = self.find_largest_possible_model(generated_text)
                    if new_model_length < model_length:
                        print("It happened")
                    elif new_model_length > model_length:
                        print("Model length increased")
                    model_length = new_model_length
                    current_model = self.models[model_length]
            except Exception as e: 
                print(e)
                # String not found in model, Go to next smaller model
                assert model_length != 1, "Can't generate text: unknown character: \'" + current_seed[-1] + "\'"
                # If model length > 1, reduce size
                model_length /= 2
                current_model = self.models[model_length]
        print("Final model length: ", model_length)
        return generated_text

    def find_largest_possible_model(self, search_str):
        search_length = len(search_str)
        model_length = 1
        for i in self.models:
            if i > model_length and i <= search_length:
                current_model = self.models[i]
                if search_str[-i:] in current_model.k_chars_idx_dict.keys():
                    model_length = i
        return model_length