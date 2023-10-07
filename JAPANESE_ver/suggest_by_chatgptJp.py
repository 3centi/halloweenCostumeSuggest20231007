import openai

class Suggest_by_chatgpt():

    def __init__(self, api_key, gender, last_year_cos, budget):

        self.api_key = api_key
        self.gender = str(gender)
        self.last_year_cos = str(last_year_cos)
        self.budget = str(budget)


    def make_content(self):

        if not self.gender and not self.last_year_cos and not self.budget:
            return 'ハロウィンの仮装を提案してください'
        else:
            content = 'ハロウィンの仮装を次の条件を踏まえて提案してください。'
            if self.gender:
                content += f'性別:{self.gender}、'
            if self.last_year_cos:
                content += f'前回の仮装:{self.last_year_cos}、'
            if self.budget:
                content += f'予算:{self.budget}'
            return content

    def request_chatgpt(self):

        content = self.make_content()
        openai.api_key = self.api_key

        response_json = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": content},],)
        response = response_json["choices"][0]["message"]["content"]

        return response