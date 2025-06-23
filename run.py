# run.py
from agent.triage_agent import triage_issues, validate_environment

if __name__ == "__main__":
    try:
        validate_environment()
        triage_issues()
    except Exception as e:
        print(f"Run failed: {e}")
