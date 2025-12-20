class Evaluator:
    def evaluate(self, exec_results, session):
        return {"reply_text": exec_results.get("reply_text", "")}

