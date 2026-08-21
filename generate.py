import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from google import genai
from google.genai import types


# ============================================================
# CONFIGURATION
# ============================================================

ROOT = Path(__file__).resolve().parent

MODEL = "gemini-3.5-flash-lite"

MAX_ATTEMPTS = 3

API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("ERROR: GEMINI_API_KEY is not set.")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)


# ============================================================
# PROJECT DISCOVERY
# ============================================================

def get_existing_projects():
    """
    Find existing project folders such as:

    two-sum
    array-rotation
    string-reversal
    """

    projects = []

    excluded = {
        ".git",
        ".github",
        "__pycache__",
    }

    for item in ROOT.iterdir():

        if not item.is_dir():
            continue

        if item.name in excluded:
            continue

        projects.append({
            "day": len(projects) + 1,
            "slug": item.name,
            "folder": item.name
        })

    return sorted(
        projects,
        key=lambda project: project["folder"]
    )


def get_next_day(projects):

    return len(projects) + 1


# ============================================================
# LEARNING CURRICULUM
# ============================================================

def get_topic(day):

    if day <= 20:
        return "Arrays"

    if day <= 40:
        return "Strings"

    if day <= 60:
        return "Hash Maps and Sets"

    if day <= 80:
        return "Two Pointers"

    if day <= 100:
        return "Sliding Window"

    if day <= 120:
        return "Stacks and Queues"

    if day <= 150:
        return "Linked Lists"

    if day <= 180:
        return "Binary Search"

    if day <= 220:
        return "Trees"

    if day <= 250:
        return "Heaps and Priority Queues"

    if day <= 290:
        return "Graphs"

    if day <= 320:
        return "Backtracking"

    if day <= 365:
        return "Dynamic Programming"

    return "Mixed Interview Algorithms"


def get_difficulty(day):

    if day <= 30:
        return "Easy"

    if day <= 100:
        return "Easy to Medium"

    if day <= 180:
        return "Medium"

    if day <= 280:
        return "Medium to Hard"

    return "Hard"


# ============================================================
# SLUG CREATION
# ============================================================

def make_slug(title):

    slug = title.lower()

    slug = re.sub(
        r"[^a-z0-9]+",
        "-",
        slug
    )

    slug = slug.strip("-")

    return slug[:70]


# ============================================================
# GEMINI GENERATION
# ============================================================

def generate_problem(
    day,
    topic,
    difficulty,
    previous_projects
):

    previous_titles = "\n".join(
        f"- {project['slug']}"
        for project in previous_projects
    )

    if not previous_titles:
        previous_titles = "None"

    prompt = f"""
You are an expert coding interview problem designer.

Generate ONE ORIGINAL Python coding interview problem.

CURRENT DAY:
{day}

REQUIRED TOPIC:
{topic}

REQUIRED DIFFICULTY:
{difficulty}

PREVIOUSLY GENERATED PROJECTS:
{previous_titles}

IMPORTANT RULES:

1. Create an ORIGINAL problem.
2. Do not copy or reproduce a LeetCode problem statement.
3. Do not use the exact title of a well-known LeetCode problem.
4. Do not create a duplicate of any previous project.
5. The algorithmic concept must be meaningfully different from previous projects.
6. The problem must be appropriate for the requested topic and difficulty.
7. The solution must be Python 3.
8. The solution must NOT use input().
9. The solution must NOT depend on interactive user input.
10. The solution must expose a function named solve().
11. tests.py must import solve from solution.py.
12. tests.py must be executable directly with:
       python tests.py
13. Tests must use unittest or plain assertions.
14. Include edge cases.
15. Do not use Markdown code fences inside JSON.
16. Return ONLY valid JSON.

Required JSON:

{{
    "title": "Original problem title",
    "difficulty": "Easy",
    "category": "Algorithm category",

    "summary": "Original concise description of the problem.",

    "examples": [
        {{
            "input": "Human-readable input",
            "output": "Expected output",
            "explanation": "Short explanation"
        }}
    ],

    "constraints": [
        "Constraint 1",
        "Constraint 2"
    ],

    "solution": "Complete Python 3 code containing solve().",

    "explanation": "Detailed explanation of the algorithm.",

    "time_complexity": "O(...)",

    "space_complexity": "O(...)",

    "tests": "Complete executable Python test code."
}}

The tests must actually import the solution like:

from solution import solve

and then test solve().
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        )
    )

    text = response.text.strip()

    # Remove accidental Markdown fences.
    if text.startswith("```"):

        text = re.sub(
            r"^```(?:json)?\s*",
            "",
            text
        )

        text = re.sub(
            r"\s*```$",
            "",
            text
        )

    return json.loads(text)


# ============================================================
# BASIC DATA VALIDATION
# ============================================================

def validate_generated_data(data):

    required_fields = [
        "title",
        "difficulty",
        "category",
        "summary",
        "examples",
        "constraints",
        "solution",
        "explanation",
        "time_complexity",
        "space_complexity",
        "tests"
    ]

    for field in required_fields:

        if field not in data:
            raise ValueError(
                f"Missing field: {field}"
            )

    if not isinstance(data["examples"], list):
        raise ValueError(
            "examples must be a list"
        )

    if not isinstance(data["constraints"], list):
        raise ValueError(
            "constraints must be a list"
        )

    if "def solve(" not in data["solution"]:
        raise ValueError(
            "solution.py must contain solve()"
        )

    if "from solution import solve" not in data["tests"]:
        raise ValueError(
            "tests.py must import solve"
        )


# ============================================================
# CREATE PROJECT
# ============================================================

def create_project(day, data):

    title = data["title"]

    slug = make_slug(title)

    folder = ROOT / slug

    if folder.exists():

        raise FileExistsError(
            f"Folder already exists: {folder}"
        )

    folder.mkdir(
        parents=True
    )

    # --------------------------------------------------------
    # README
    # --------------------------------------------------------

    readme = f"""# {title}

**Day:** {day}

**Difficulty:** {data["difficulty"]}

**Category:** {data["category"]}

## Problem

{data["summary"]}

## Examples

"""

    for example in data["examples"]:

        readme += f"""### Input

{example["input"]}

### Output

{example["output"]}

### Explanation

{example["explanation"]}

"""

    readme += """## Constraints

"""

    for constraint in data["constraints"]:

        readme += f"- {constraint}\n"

    readme += f"""

## Complexity

**Time Complexity:** {data["time_complexity"]}

**Space Complexity:** {data["space_complexity"]}
"""

    # --------------------------------------------------------
    # Explanation
    # --------------------------------------------------------

    explanation = f"""# Explanation

{data["explanation"]}

## Time Complexity

{data["time_complexity"]}

## Space Complexity

{data["space_complexity"]}
"""

    # --------------------------------------------------------
    # Write files
    # --------------------------------------------------------

    (folder / "README.md").write_text(
        readme,
        encoding="utf-8"
    )

    (folder / "solution.py").write_text(
        data["solution"].strip() + "\n",
        encoding="utf-8"
    )

    (folder / "explanation.md").write_text(
        explanation,
        encoding="utf-8"
    )

    (folder / "tests.py").write_text(
        data["tests"].strip() + "\n",
        encoding="utf-8"
    )

    return folder


# ============================================================
# VALIDATE PYTHON SYNTAX
# ============================================================

def validate_syntax(folder):

    print("Testing solution syntax...")

    solution = folder / "solution.py"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "py_compile",
            str(solution)
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:

        print("Syntax test FAILED.")

        if result.stderr:
            print(result.stderr)

        return False

    print("Syntax test PASSED.")

    return True


# ============================================================
# RUN TESTS
# ============================================================

def run_tests(folder):

    print("Running automated tests...")

    tests = folder / "tests.py"

    try:

        result = subprocess.run(
            [
                sys.executable,
                str(tests)
            ],
            cwd=folder,
            capture_output=True,
            text=True,
            timeout=30
        )

    except subprocess.TimeoutExpired:

        print("Tests timed out.")

        return False

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:

        print("Tests FAILED.")

        return False

    print("Tests PASSED.")

    return True


# ============================================================
# REMOVE FAILED PROJECT
# ============================================================

def remove_project(folder):

    if folder and folder.exists():

        print(
            f"Removing failed project: {folder.name}"
        )

        shutil.rmtree(folder)


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 60)
    print("DAILY LEETCODE GENERATOR")
    print("=" * 60)

    print(f"Model: {MODEL}")

    # --------------------------------------------------------
    # Find previous projects
    # --------------------------------------------------------

    projects = get_existing_projects()

    day = get_next_day(projects)

    topic = get_topic(day)

    difficulty = get_difficulty(day)

    print()
    print(f"Day: {day}")
    print(f"Topic: {topic}")
    print(f"Difficulty: {difficulty}")

    folder = None
    data = None

    # --------------------------------------------------------
    # Generate up to 3 times
    # --------------------------------------------------------

    for attempt in range(
        1,
        MAX_ATTEMPTS + 1
    ):

        print()
        print(
            f"Generation attempt "
            f"{attempt}/{MAX_ATTEMPTS}"
        )

        folder = None

        try:

            data = generate_problem(
                day,
                topic,
                difficulty,
                projects
            )

            validate_generated_data(data)

            print(
                f"Project: {data['title']}"
            )

            folder = create_project(
                day,
                data
            )

            print(
                f"Created: {folder}"
            )

            # Syntax validation.
            if not validate_syntax(folder):

                remove_project(folder)

                continue

            # Functional testing.
            if not run_tests(folder):

                remove_project(folder)

                continue

            # Everything passed.
            print()
            print("=" * 60)
            print("PROJECT VALIDATION PASSED")
            print("=" * 60)

            break

        except Exception as error:

            print()
            print(
                f"Generation failed: {error}"
            )

            remove_project(folder)

            if attempt == MAX_ATTEMPTS:

                raise

    else:

        raise RuntimeError(
            "Could not create a valid project."
        )

    # --------------------------------------------------------
    # Success
    # --------------------------------------------------------

    print()
    print("=" * 60)
    print("SUCCESS")
    print("=" * 60)

    print(
        f"Day {day}: {data['title']}"
    )

    print(
        f"Folder: {folder.name}"
    )

    print("Ready for GitHub Actions to commit.")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()