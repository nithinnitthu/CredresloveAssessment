class Executor:
    async def execute(self, plan, user_id, session):
        return {
            "reply_text": "Hello from Executor",
            "updates": {},
            "tool_outputs": {}
        }

