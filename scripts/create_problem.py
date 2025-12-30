#!/usr/bin/env python3
"""
Script to create a new LeetCode problem folder with templates for Java, Python, and C++.
Usage: python create_problem.py <problem_number> "<problem_title>"
Example: python create_problem.py 0002 "Add Two Numbers"
"""

import os
import sys
import shutil

def create_problem_folder(problem_number, problem_title):
    # Format the folder name
    folder_name = f"{problem_number}-{problem_title.lower().replace(' ', '-')}"
    folder_path = os.path.join("problems", folder_name)

    # Create main folder
    os.makedirs(folder_path, exist_ok=True)

    # Create language subfolders
    languages = ["java", "python", "cpp"]
    for lang in languages:
        lang_path = os.path.join(folder_path, lang)
        os.makedirs(lang_path, exist_ok=True)

        # Copy template to the solution file
        template_file = f"templates/{lang}_template.{lang if lang != 'cpp' else 'cpp'}"
        if lang == "python":
            solution_file = os.path.join(lang_path, "solution.py")
        elif lang == "java":
            solution_file = os.path.join(lang_path, "Solution.java")
        else:
            solution_file = os.path.join(lang_path, "solution.cpp")

        if os.path.exists(template_file):
            shutil.copy(template_file, solution_file)
            print(f"Created {solution_file}")
        else:
            print(f"Template {template_file} not found")

    print(f"Created problem folder: {folder_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_problem.py <problem_number> \"<problem_title>\"")
        sys.exit(1)

    problem_number = sys.argv[1].zfill(4)  # Pad with zeros to 4 digits
    problem_title = sys.argv[2]

    create_problem_folder(problem_number, problem_title)