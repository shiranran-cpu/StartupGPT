# workflows/saas.py

from workflows.startup import StartupWorkflow


class SaaSWorkflow(StartupWorkflow):

    def run(self, idea):

        result = super().run(idea)

        result["auth"] = self.generate_auth()

        result["billing"] = self.generate_billing()

        result["subscription"] = self.generate_subscription()

        result["rbac"] = self.generate_rbac()

        return result

    def generate_auth(self):

        return {
            "login": True,
            "register": True,
            "oauth": True,
            "jwt": True
        }

    def generate_billing(self):

        return {
            "stripe": True,
            "paypal": True
        }

    def generate_subscription(self):

        return {
            "free": True,
            "pro": True,
            "enterprise": True
        }

    def generate_rbac(self):

        return {
            "admin": True,
            "member": True,
            "guest": True
        }
