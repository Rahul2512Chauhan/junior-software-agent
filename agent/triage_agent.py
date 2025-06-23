import os
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

import time
import logging
from typing import Optional
from dotenv import load_dotenv
import google.generativeai as genai
from gh_api.github_api import get_open_issues, label_issue

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY")) # type: ignore

# Labels to choose from
LABELS = ["bug", "enhancement", "documentation", "question"]

# Rate limiting
RATE_LIMIT_DELAY = 1  # seconds between API calls

model = genai.GenerativeModel("gemini-1.5-flash") # type: ignore

def classify_issue_with_gemini(title: str, body: str) -> Optional[str]:
    """
    Classify a GitHub issue using Gemini AI.
    
    Args:
        title: Issue title
        body: Issue body content
        
    Returns:
        Classified label or None if classification fails
    """
    # Handle empty body
    body = body or "No description provided"
    
    prompt = f"""
You are a GitHub issue classifier.
Given an issue title and body, return EXACTLY ONE of these labels: {', '.join(LABELS)}

Rules:
- Return only the label name, nothing else
- Choose the most appropriate label based on the content
- If unsure, default to "question"

Title: {title}
Body: {body}

Label:"""
    
    try:
        response = model.generate_content(prompt)
        label = response.text.strip().lower()
        
        # Validate the returned label
        if label in LABELS:
            return label
        else:
            logger.warning(f"Gemini returned invalid label: {label}")
            return None
            
    except Exception as e:
        logger.error(f"Error calling Gemini API: {e}")
        return None

def triage_issues():
    """
    Main function to triage open GitHub issues.
    """
    try:
        issues = get_open_issues()
        issues_list = list(issues)
        logger.info(f"Found {len(issues_list)} open issues")
        
        processed_count = 0
        labeled_count = 0
        for issue in issues_list:
            # Skip issues that already have labels
            if issue.labels:
                logger.debug(f"Issue #{issue.number} already has labels, skipping")
                continue
                continue
            
            logger.info(f"Processing issue #{issue.number}: {issue.title}")
            
            # Classify the issue
            label = classify_issue_with_gemini(issue.title, issue.body)
            
            if label:
                try:
                    # Apply the label
                    label_issue(issue.number, label)
                    logger.info(f"✅ Issue #{issue.number} labeled as: {label}")
                    labeled_count += 1
                    
                except Exception as e:
                    logger.error(f"❌ Failed to label issue #{issue.number}: {e}")
            else:
                logger.warning(f"⚠️  Could not classify issue #{issue.number}")
            
            processed_count += 1
            
            # Rate limiting
            time.sleep(RATE_LIMIT_DELAY)
        
        logger.info(f"Triage complete: {labeled_count}/{processed_count} issues labeled")
        
    except Exception as e:
        logger.error(f"Error during triage process: {e}")
        raise

def validate_environment():
    """Validate required environment variables and API keys."""
    if not os.getenv("GEMINI_API_KEY"):
        raise ValueError("GEMINI_API_KEY environment variable is required")
    
    # You might want to add GitHub token validation here too
    logger.info("Environment validation passed")

if __name__ == "__main__":
    try:
        validate_environment()
        triage_issues()
    except Exception as e:
        logger.error(f"Application failed: {e}")
        exit(1)