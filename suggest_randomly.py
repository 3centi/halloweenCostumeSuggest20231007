import random

class Suggest_randomly():

    def __init__(self, cos_list):
        self.cos_list = cos_list

    def suggest_randomly(self):
        random_ints = random.sample(
            range(0, len(self.cos_list["cos_idea"])-1),
            k = (10 if len(self.cos_list["cos_idea"]) >= 10 else len(self.cos_list["cos_idea"]))
        )

        suggested_cos = []

        for i in random_ints:
            suggested_cos.append(self.cos_list["cos_idea"][i])

        return suggested_cos