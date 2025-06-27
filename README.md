🧠 Junior Software Engineer Agent

A fully autonomous CLI agent that performs GitHub issue triage, generates PRs in Go/TypeScript, updates docs, and reviews code — built to accelerate engineering velocity without human overhead.

---
```
🔧 Features

✅ 1. Issue Triage Agent
- Auto-labels issues (e.g., `bug`, `enhancement`)
- Adds reproducible steps or context using Gemini
- Prioritizes based on keywords and severity

 ✅ 2. PR Generator Agent
- Generates Go/TypeScript code fixes using Gemini 1.5 Flash
- Opens PRs with changelog entries and doc updates
- Follows coding best practices (dry-run supported)

✅ 3. Doc Updater Agent
- Automatically updates changelogs and documentation from PR diffs

✅ 4. PR Reviewer Agent
- Reviews pull requests using Gemini
- Comments structured feedback directly on PRs

---

🧪 Tech Stack

- Python 3.11+
- Gemini 1.5 Flash (Google GenAI)
- GitHub API (PyGitHub)
- dotenv for secrets/config
```


### 🚀 How to Run (CLI Mode)

### 🧱 Setup


git clone https://github.com/your-username/junior-software-agent.git
cd junior-software-agent

# Create virtualenv
python3 -m venv junior
source junior/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your environment variables
cp .env.example .env  # Then fill values


# Run triage
python run.py --triage

# Generate PRs (auto code + docs)
python run.py --generate-prs

# Review open PRs
python run.py --review-prs

# Run everything (using shell script)
bash run_all.sh


```
junior-software-agent/
├── _1_triage/
│   └── triage_agent.py
├── _2_pr_generation/
│   ├── pr_agent.py
│   ├── code_generator.py
│   └── github_committer.py
├── _3_doc_updater/
│   └── doc_agent.py
├── _4_reviewer/
│   ├── review_runner.py
│   ├── gemini_reviewer.py
│   └── review_classifier.py
├── _5_core/
│   ├── config.py
│   ├── github_api.py
│   └── github_utils.py
├── test_repo/
├── data/
│   ├── logs/
│   └── issues/
├── run.py
├── run_all.sh
└── README.md

```

```
👤 Author
Built by Rahul Chauhan
Contact: rahul_c@me.iitr.ac.in.com
For internship or collaboration, feel free to connect!
```
