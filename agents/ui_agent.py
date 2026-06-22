from utils.llm import call_llm
from utils.prompt_loader import load_prompt


class UIAgent:

    def __init__(self):
        self.prompt = load_prompt("designer")

    def generate_ui(self, prd: str):

        prompt = self.prompt.format(prd=prd)

        return call_llm(prompt)
