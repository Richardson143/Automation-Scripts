from richard.agent.autogpt import AutoGPTAgent
from richard.agent.chromegpt_agent import ChromeGPTAgent
from richard.agent.zeroshot import BabyAGIAgent, ZeroShotAgent


def run_chromegpt(
    task: str,
    model: str = "gemini-1.5-pro",
    agent: str = "zero-shot",
    headless: bool = False,
    verbose: bool = False,
    continuous: bool = True,
) -> str:
    """Run ChromeGPT."""
    # setup agent
    if agent == "auto-gpt":
        agent_obj: ChromeGPTAgent = AutoGPTAgent(
            model=model, verbose=verbose, continuous=continuous
        )
    elif agent == "baby-agi":
        agent_obj = BabyAGIAgent(model=model, verbose=verbose)
    elif agent == "zero-shot":
        agent_obj = ZeroShotAgent(model=model, verbose=verbose)
    else:
        raise ValueError(f"Agent {agent} not found.")
    # run agent
    return agent_obj.run([task])
