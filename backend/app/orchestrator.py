import time
import logging
import os

from app.memory import MemoryStore
from app.planner import Planner
from app.executor import Executor
from app.evaluator import Evaluator
from app.llm_client import LLMClient

logger = logging.getLogger("orchestrator")
logger.setLevel(logging.INFO)

class AgentOrchestrator:
    def __init__(self):
        self.memory = MemoryStore()
        self.planner = Planner()
        self.executor = Executor()
        self.evaluator = Evaluator()
        self.llm = LLMClient()  # optional polish step

    async def handle_turn(self, user_id: str, session_id: str, text: str):
        start = time.time()
        # load session memory
        session = self.memory.get_session(user_id, session_id)

        plan = self.planner.plan(text, session)
        logger.info(f"Planner produced plan: {plan}")

        exec_results = await self.executor.execute(plan, user_id, session)
        logger.info(f"Executor results: {exec_results}")

        evaluation = self.evaluator.evaluate(exec_results, session)
        logger.info(f"Evaluator decision: {evaluation}")

        # update memory
        self.memory.update_session(user_id, session_id, exec_results.get("updates", {}))

        reply_text = evaluation.get("reply_text", "")
        # If an LLM provider is configured, ask it to polish or rewrite the reply in Telugu
        try:
            if os.environ.get("LLM_PROVIDER", "mock") != "mock":
                context = {
                    "recent_actions": evaluation.get("schemes") or exec_results.get("tool_outputs", {})
                }
                polished = self.llm.generate_reply_in_telugu(reply_text, context=str(context))
                if polished:
                    reply_text = polished
        except Exception as e:
            logger.exception("LLM polish step failed: %s", e)

        response = {
            "reply_text": reply_text,
            "tts_text": reply_text,  # TTS will render this text
            "actions_log": {
                "plan": plan,
                "executor": exec_results,
                "evaluation": evaluation,
            },
            "memory_snapshot": self.memory.get_session(user_id, session_id),
            "latency_s": time.time() - start
        }
        return response
