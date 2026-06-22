# workflows/startup.py

from agents.pm_agent import PMAgent
from agents.ui_agent import UIAgent
from agents.frontend_agent import FrontendAgent
from agents.backend_agent import BackendAgent
from agents.database_agent import DatabaseAgent
from agents.qa_agent import QAAgent


class StartupWorkflow:

    def __init__(self):

        self.pm = PMAgent()
        self.ui = UIAgent()
        self.frontend = FrontendAgent()
        self.backend = BackendAgent()
        self.database = DatabaseAgent()
        self.qa = QAAgent()

    def run(self, idea):

        print("Generating PRD...")
        prd = self.pm.generate_prd(idea)

        print("Generating UI...")
        ui_design = self.ui.generate_ui(prd)

        print("Generating Database...")
        schema = self.database.generate_schema(prd)

        print("Generating Backend...")
        backend = self.backend.generate_backend(prd, schema)

        print("Generating Frontend...")
        frontend = self.frontend.generate_frontend(
            prd,
            ui_design
        )

        print("Generating Tests...")
        tests = self.qa.generate_tests(prd)

        return {
            "prd": prd,
            "ui": ui_design,
            "schema": schema,
            "backend": backend,
            "frontend": frontend,
            "tests": tests
        }
