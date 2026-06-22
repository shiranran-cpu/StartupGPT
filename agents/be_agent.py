from utils.llm import call_llm
from utils.prompt_loader import load_prompt


class BackendAgent:

    def __init__(self):
        self.prompt = load_prompt("backend")

    def generate_backend(self, prd: str, schema: str):

        prompt = self.prompt.format(
            prd=prd,
            schema=schema
        )

        return call_llm(prompt)
