from utils.llm import call_llm
from utils.prompt_loader import load_prompt


class PMAgent:

    def __init__(self):
        self.prompt = load_prompt("pm")

    def generate_prd(self, idea: str):

        prompt = self.prompt.format(idea=idea)

        return call_llm(prompt)
