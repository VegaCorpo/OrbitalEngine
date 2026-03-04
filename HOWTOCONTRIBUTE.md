# Contributing to Orbital Engine

Thank you for your interest in contributing to Orbital Engine! We welcome contributions from the community and are excited to have you here.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Bug Reports](#bug-reports)
- [Feature Requests](#feature-requests)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone. Please:

- Be respectful and considerate in your communication
- Welcome newcomers and help them get started
- Accept constructive criticism gracefully
- Focus on what's best for the project and community

## Getting Started

1. **Fork the repository** to your own GitHub account
2. **Clone your fork** locally:
   ```bash
   git clone git@github.com:VegaCorpo/OrbitalEngine.git
   cd OrbitalEngine
   ```
3. **Add the upstream repository**:
   ```bash
   git remote add upstream git@github.com:VegaCorpo/OrbitalEngine.git
   ```

## Development Setup

### Prerequisites

- C++20 or later compiler (GCC, Clang, or MSVC)
- CMake 3.15 or later
- Git

### Building the Project

```bash
cmake -S . -B build
cmake --build build -j $(nproc)

#or if just is installed on your pc

just
```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug fixes**: Fix issues reported in the issue tracker
- **Features**: Implement new gameplay features or improvements
- **Documentation**: Improve README, code comments, or add documentation
- **Performance**: Optimize existing code
- **Tests**: Add or improve test coverage
- **Code quality**: Refactoring and code cleanup

### Before You Start

1. **Check existing issues** to see if someone is already working on it
2. **Open an issue** to discuss major changes before starting work
3. **Keep changes focused**: One feature or fix per pull request

## Coding Standards

### C++ Style Guidelines

- **Language Standard**: Use C++20 features appropriately
- **Naming Conventions**:
  - Classes and structs: `PascalCase` (e.g., `Mass`)
  - Functions and methods: `camelCase` (e.g., `updatePosition()`)
  - Variables: `camelCase` (e.g., `gravityVector`)
  - Constants: `UPPER_SNAKE_CASE` (e.g., `GRAVITATIONAL_CONSTANT`, `DEFAULT_SPEED`)
  - Private members: prefix with `_` (e.g., `_position`, `_velocity`)

- **Formatting**:
  - Indentation: 4 spaces (no tabs)
  - Line length: Maximum 120 characters
  - Braces: Opening brace on same line for condition/loop/classes
  and different lines for functions

  ```cpp
  class Example {
      public:
            void doSomething()
            {
                if (condition) {
                    // code here
                }
            }
  };
  ```

- **Best Practices**:
  - Use smart pointers (`std::unique_ptr`, `std::shared_ptr`) instead of raw pointers
  - Prefer `const` correctness
  - Use `auto` when type is obvious or complex
  - Avoid `using namespace std;` in headers
  - Include guards or `#pragma once` in all headers
  - Document public APIs with comments

In case of doubt please follow what the clang-tidy impose.

### CMake Guidelines

- Keep CMakeLists.txt files clean and well-organized
- Use modern CMake practices (target-based)
- Document any new dependencies or build options

## Commit Guidelines

### Commit Message Format

Use clear, descriptive commit messages following this format:

```
<type>(<scope>): <subject>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `build`: Changes to build system or dependencies
- `ci`: CI/CD changes

**Examples**:
```
feat(relativity): add space distorsion for black holes

docs: update README with new build instructions

```

### Commit Best Practices

- Keep commits atomic (one logical change per commit)
- Write meaningful commit messages
- Reference issue numbers when applicable (e.g., "fixes #42")

## Pull Request Process

1. **Update your fork** with the latest changes from upstream:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** following the coding standards

4. **Test your changes** thoroughly:
   - Build the project without warnings
   - Run existing tests
   - Add new tests for your changes
   - Test the game manually

5. **Commit your changes** with clear commit messages

6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**:
   - Provide a clear title and description
   - Reference any related issues
   - Describe what changes you made and why
   - Include screenshots/videos for UI changes

### Pull Request Checklist

- [ ] Code follows the project's style guidelines
- [ ] Code compiles without warnings
- [ ] All tests pass
- [ ] New tests added for new functionality
- [ ] Documentation updated (if applicable)
- [ ] Commit messages are clear and descriptive
- [ ] PR description clearly explains the changes

### Review Process

- Maintainers will review your PR and may request changes
- Address feedback by pushing new commits to your branch
- Once approved, a maintainer will merge your PR
- Please be patient - reviews may take some time

## Bug Reports

When filing a bug report, please include:

- **Clear title**: Concise description of the issue
- **Description**: Detailed explanation of the problem
- **Steps to reproduce**: Numbered steps to trigger the bug
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**:
  - OS (Windows, Linux, macOS)
  - Compiler and version
  - CMake version
  - Any relevant hardware specs
- **Screenshots/logs**: If applicable
- **Additional context**: Any other relevant information

## Feature Requests

We love hearing ideas! When proposing a feature:

- **Describe the feature**: Clear explanation of what you want
- **Use case**: Why is this feature useful?
- **Possible implementation**: Ideas on how it could work (optional)
- **Alternatives**: Other solutions you've considered

## Questions?

If you have questions about contributing, feel free to:

- Open an issue with the `question` label
- Reach out to the maintainers
