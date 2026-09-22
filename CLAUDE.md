# Project Instructions

## 1. Project Overview

This project is a Python tool that implements a local mock server based on a Swagger/OpenAPI specification.

The goal is to generate dynamic API responses from an OpenAPI specification so that APIs can be tested without a real backend.

Keep the implementation simple, maintainable, and focused on the assignment requirements.

Do not implement speculative features that are not required by the assignment.

---

## 2. Mandatory Course Requirements

The following requirements are mandatory and have no exceptions:

- Git must be used for version control.
- A Python virtual environment must always be used.
- Development must follow an Agentic TDD workflow.
- Plan Mode must be used before implementation work.
- The development process must preserve clear, logical Git checkpoints.

Do not bypass or weaken these requirements.

---

## 3. Agentic TDD Workflow

Use a strict test-first Agentic TDD workflow.

The development process must follow this sequence:

1. Plan.
2. Define requirements and acceptance criteria.
3. Define test cases.
4. Write automated tests.
5. Run the tests and verify RED.
6. Implement the minimum production code required.
7. Run the tests and verify GREEN.
8. Refactor only after GREEN.
9. Run the full test suite and quality checks.
10. Review the changes.
11. Save the completed logical step using the Git Skill.

Never implement a feature first and add tests afterward.

---

## 4. Plan Mode

Plan Mode is mandatory before implementation work.

Before implementing a feature:

1. Inspect the repository structure.
2. Read relevant existing files.
3. Analyze the assignment requirements relevant to the feature.
4. Identify the smallest meaningful vertical slice.
5. Define acceptance criteria.
6. Identify the automated tests required to verify the expected behavior.
7. Consider relevant edge cases.
8. Present the proposed plan before implementation.

Do not write production code while planning.

Do not skip Plan Mode for implementation work.

If the requirements are ambiguous, identify the ambiguity and ask for clarification rather than inventing requirements.

---

## 5. Test-First Development

For every feature or requirement:

1. Define the expected behavior.
2. Create automated tests before production code.
3. Run the tests.
4. Confirm that the new tests are RED because the required functionality is not implemented yet.
5. Implement the minimum production code required to satisfy the tests.
6. Run the tests again.
7. Confirm that they are GREEN.
8. Refactor only after the tests are GREEN.
9. Run the relevant tests again after refactoring.

A meaningful RED state means that the test fails because the required functionality is not implemented.

Do not consider setup errors, missing dependencies, syntax errors, or unrelated failures to be a valid RED state.

If the test fails for an unexpected reason, fix the test or environment problem before considering the RED state confirmed.

---

## 6. Test Independence and Quality

Tests must be derived from:

- assignment requirements;
- acceptance criteria;
- expected observable behavior.

Tests must NOT be derived from:

- the current implementation;
- implementation details;
- assumptions about code structure;
- the easiest way to make the implementation pass.

Never:

- weaken an assertion to make a test pass;
- delete a failing test because the implementation fails it;
- change expected behavior to match the implementation;
- hardcode values specifically to satisfy a test;
- mock away the functionality that the test is supposed to verify;
- change requirements simply because they are difficult to implement.

If a test appears to be incorrect, or if a requirement is ambiguous, stop and explain the issue.

---

## 7. Iterative Development

Do not implement the entire application in one step.

Work in small, meaningful vertical slices.

Each iteration should:

1. Have a clearly defined goal.
2. Have explicit acceptance criteria.
3. Have automated tests.
4. Have a verified RED state before implementation.
5. Have a verified GREEN state after implementation.
6. Pass the required quality checks.
7. End with a logical Git checkpoint.

Prefer end-to-end observable behavior over isolated implementation details when defining vertical slices.

After completing an iteration, report:

- what was implemented;
- what tests were added;
- RED result;
- GREEN result;
- full test suite result;
- Ruff result;
- mypy result;
- known limitations or assumptions;
- suggested next iteration.

Do not claim that something works without actually running the relevant verification.

---

## 8. Test Strategy

Tests should verify real user-visible or API-visible behavior.

Include both normal cases and relevant edge cases.

For this project, consider cases such as:

- valid OpenAPI specifications;
- invalid OpenAPI specifications;
- invalid YAML or JSON;
- missing or invalid schemas;
- GET endpoints;
- POST endpoints;
- path parameters;
- query parameters;
- request bodies;
- primitive response properties;
- nested objects;
- arrays;
- enums;
- multiple response status codes;
- empty responses;
- malformed requests;
- unsupported OpenAPI features.

Do not add speculative features or tests that are not required or reasonably implied by the assignment.

---

## 9. Test Plan

Maintain a test plan for the project.

The test plan should describe:

- test case ID;
- requirement or behavior being verified;
- test scenario;
- expected result;
- priority.

Use the test plan to ensure important requirements are covered.

Do not treat the test plan as a substitute for automated tests.

Automated tests must still verify the expected behavior.

---

## 10. Input / Output Directory Protocol

Never modify or delete files in `input` directories.

Input directories contain reference data and test fixtures.

Always save generated files to `output` directories when an input/output directory is relevant to a task.

Never overwrite source or reference files in `input`.

If an input/output directory is not required by the assignment or current task, do not create unnecessary directories merely to satisfy this rule.

---

## 11. Python Environment

This is a Python project.

Always use the project's virtual environment.

Before running Python commands, tests, scripts, linters, type checkers, or other Python tooling, ensure that the project's virtual environment is active.

Never install project dependencies globally.

Do not use the system Python when the project virtual environment is available.

The project currently uses Python 3.14.7.

Prefer dependencies that support Python 3.14.7.

If a dependency has compatibility issues with Python 3.14.7, explain the issue before changing the Python version.

The following directories must not be committed to Git:

- `.venv/`
- `venv/`

---

## 12. Dependencies

Keep dependencies minimal.

Before adding a dependency:

1. Determine whether the functionality can reasonably be implemented using the Python standard library or existing project dependencies.
2. If a new dependency is justified, explain why it is needed.
3. Prefer mature, well-maintained libraries compatible with Python 3.14.7.

Do not add dependencies unnecessarily.

---

## 13. Code Quality

Before considering an iteration complete, run:

- relevant automated tests;
- the full test suite;
- `ruff check`;
- `mypy`.

All required checks must pass before considering the iteration complete.

Do not suppress linting or type-checking errors simply to make the checks pass.

If a linter or type-checker exception is genuinely necessary, document the reason in a code comment.

Do not hide errors merely to obtain a passing result.

---

## 14. Implementation Principles

Prefer:

- simple solutions;
- clear naming;
- small functions;
- standard Python practices;
- minimal dependencies;
- maintainable code;
- behavior that generalizes beyond the current test cases;
- explicit and understandable error handling.

Avoid:

- unnecessary abstractions;
- premature optimization;
- speculative features;
- duplicated logic;
- unnecessary configuration;
- unnecessary dependencies;
- hardcoded test-specific behavior.

Implement the actual requirement rather than optimizing only for the current tests.

---

## 15. Repository Investigation

Before modifying the project:

1. Inspect the repository structure.
2. Read relevant existing files.
3. Check existing tests.
4. Check existing configuration.
5. Understand the current implementation before making changes.

Do not assume that a file, dependency, configuration, or feature exists without checking.

Do not overwrite existing work without understanding it first.

Never claim that a feature works without actually running the relevant verification.

---

## 16. Error Handling and Ambiguity

If a requirement is ambiguous:

1. Identify the ambiguity.
2. Explain the possible interpretations.
3. Do not silently choose an interpretation that materially changes the expected behavior.
4. Ask the user for clarification when necessary.

If an implementation approach conflicts with the assignment requirements, stop and explain the conflict.

Do not hide limitations or unsupported behavior.

---

## 17. Git

Git is mandatory for this project.

Use the Git Skill for Git operations, including:

- reviewing changes;
- checking repository state;
- staging files;
- creating commits;
- undoing or reverting changes.

Do not duplicate the Git workflow from the Git Skill in this file.

Use Git to preserve clear, logical checkpoints after completed development iterations.

Never push to a remote repository unless the user explicitly asks for it.

---

## 18. Communication

Be explicit about the current development state.

When reporting progress, distinguish clearly between:

- planned;
- tests written;
- RED verified;
- implementation completed;
- GREEN verified;
- refactored;
- linted;
- type-checked;
- committed;
- pushed.

Do not claim that a step was completed if it was not actually verified.

When reporting test results, include the relevant command and outcome.

When reporting failures, explain the actual failure rather than hiding or minimizing it.

---

## 19. Scope Control

Stay focused on the assignment.

Do not add features merely because they might be useful.

Do not over-engineer the solution.

If a potential improvement is outside the current scope:

1. Mention it as a possible future improvement if relevant.
2. Do not implement it without justification.

The primary goal is a correct, testable, maintainable solution that satisfies the assignment requirements.