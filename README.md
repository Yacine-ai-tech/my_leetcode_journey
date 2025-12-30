# My LeetCode Journey

This repository contains my solutions to LeetCode problems, implemented in Java, Python, and C++. The goal is to solve every problem on LeetCode across these three languages to improve coding skills and algorithmic thinking.

## Repository Structure

```
my_leetcode_journey/
├── problems/
│   ├── 0001-two-sum/
│   │   ├── java/
│   │   │   └── Solution.java
│   │   ├── python/
│   │   │   └── solution.py
│   │   └── cpp/
│   │       └── solution.cpp
│   └── ...
├── templates/
│   ├── java_template.java
│   ├── python_template.py
│   └── cpp_template.cpp
├── scripts/
│   └── create_problem.py
├── .gitignore
└── README.md
```

- `problems/`: Contains folders for each LeetCode problem, named by problem number and title (e.g., `0001-two-sum`).
- `templates/`: Template files for each language to start new solutions.
- `scripts/`: Utility scripts for managing the repository.

## How to Add a New Problem

1. Use the `create_problem.py` script to create a new problem folder:
   ```
   python scripts/create_problem.py <problem_number> "<problem_title>"
   ```
   For example:
   ```
   python scripts/create_problem.py 0002 "Add Two Numbers"
   ```

2. Copy the problem description from LeetCode and add it as a comment at the top of each solution file.

3. Implement the solution in Java, Python, and C++ using the templates.

4. Test your solutions and commit the changes.

## Languages

- **Java**: Solutions in Java, following standard coding practices.
- **Python**: Pythonic solutions, focusing on readability.
- **C++**: Efficient C++ implementations.

## Contribution Guidelines

- Each problem should have solutions in all three languages.
- Include comments explaining the approach and time/space complexity.
- Follow the naming conventions: `Solution.java`, `solution.py`, `solution.cpp`.
- Keep code clean and well-documented.

## Pushing from LeetCode

To push your solutions from LeetCode:

1. Solve the problem on LeetCode.
2. Copy the code from LeetCode's editor.
3. Paste into the appropriate file in this repository.
4. Add problem description and comments.
5. Commit and push to GitHub.

For bulk uploads, you can manually copy multiple solutions or use scripts if available.

## License

This repository is for personal learning purposes. Solutions are based on LeetCode problems.