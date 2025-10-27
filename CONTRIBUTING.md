# Contributing to CalC

We love your input! We want to make contributing to CalC as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features

## 📋 Requirements

Before you start contributing, ensure you have the following installed:

### Required

- **Python** (v3.8+)

  - Required for backend development
  - Download from [python.org](https://www.python.org/downloads/)

- **Git**
  - Required for version control
  - Download from [git-scm.com](https://git-scm.com/)

### Recommended MUST

- **VS Code** - Recommended IDE with extensions for Python

## 🚀 Quick Start for Contributors

**Fork and clone the repository:**

```bash
git clone https://github.com/yourusername/CalC.git
cd CalC
```

## 🔄 GitHub Flow

We follow the GitHub Flow for contributions. Here's the proper workflow:

### 1. Fork the Repository

- **Go to the main repository** on GitHub
- **Click the "Fork" button** in the top-right corner
- **This creates your own copy** of the repository under your GitHub account

### 2. Clone Your Fork

- **Clone your forked repository** to your local machine
  ```bash
  git clone https://github.com/yourusername/CalC.git
  cd CalC
  ```
- **Add the original repository as upstream**
  ```bash
  git remote add upstream https://github.com/gn0029/CalC.git
  ```

### 3. Create a Feature Branch

- **Create a new branch** from `main` for your feature or fix
  ```bash
  git checkout -b feature/your-feature-name
  ```
- Use descriptive branch names: `feature/add-emoji-support` or `fix/login-bug`

### 4. Make Your Changes

- **Edit files** and implement your feature or fix
- Keep commits small and focused
- Write clear, descriptive commit messages

### 5. Pull Latest Changes from Upstream

- **Before committing, sync with the original repository**
  ```bash
  git fetch upstream
  git pull upstream main
  ```
- **Resolve any merge conflicts** if they occur
- This ensures your changes are based on the latest code

### 6. Add and Commit Your Changes

- **Stage your changes**
  ```bash
  git add .
  ```
- **Commit with a descriptive message**
  ```bash
  git commit -m "feat: add emoji support to chat messages"
  ```

### 7. Push to Your Fork

- **Push your branch** to your forked repository
  ```bash
  git push origin feature/your-feature-name
  ```

### 8. Open a Pull Request

- **Go to your fork** on GitHub
- **Click "Compare & pull request"** button
- **Fill in the PR details:**
  - Provide a clear description of your changes
  - Reference any related issues (e.g., "Fixes #123")
  - Add screenshots or videos for UI changes

### 9. Respond to Feedback

- **Review comments** from maintainers
- **Make requested changes** in your local branch
- **Commit and push updates** to the same branch
  ```bash
  git add .
  git commit -m "fix: address review feedback"
  git push origin feature/your-feature-name
  ```
- The PR will update automatically

### 10. After Merge

- **Pull the latest changes** to your local main branch
  ```bash
  git checkout main
  git pull upstream main
  ```
- **Delete your feature branch** (optional cleanup)
  ```bash
  git branch -d feature/your-feature-name
  git push origin --delete feature/your-feature-name
  ```

### Branch Naming Conventions

- `feature/` - New features (e.g., `feature/chat-history`)
- `fix/` - Bug fixes (e.g., `fix/message-encoding`)
- `docs/` - Documentation updates (e.g., `docs/api-reference`)
- `refactor/` - Code refactoring (e.g., `refactor/database-queries`)
- `test/` - Test additions or fixes (e.g., `test/api-endpoints`)




## 🐛 Bug Reports

### Good Bug Reports Include:

1. **Clear title** and description
2. **Steps to reproduce** the issue
3. **Expected vs actual behavior**
4. **Environment details** (OS, browser, version)
5. **Screenshots or videos** if applicable

## 💡 Feature Requests

### Good Feature Requests Include:

1. **Clear problem statement**
2. **Proposed solution**
3. **Alternative solutions considered**
4. **Use cases and examples**

## 🤝 Community Guidelines

### Code of Conduct

- **Be respectful** and inclusive
- **Be constructive** in feedback
- **Help others** learn and contribute
- **Stay on topic** in discussions

## ✅ Do's and ❌ Don'ts

### ✅ Do's

- **Do** search existing issues before creating a new one
- **Do** provide detailed information in bug reports and feature requests
- **Do** test your changes thoroughly before submitting a PR
- **Do** follow the code style and conventions used in the project
- **Do** write clear commit messages that explain what and why
- **Do** update documentation when you change functionality
- **Do** be patient and respectful when waiting for reviews
- **Do** ask questions if you're unsure about something
- **Do** link related issues in your PRs
- **Do** keep PRs focused on a single feature or fix

### ❌ Don'ts

- **Don't** create duplicate issues without checking existing ones first
- **Don't** submit spam, low-effort, or placeholder issues/PRs
- **Don't** create issues like "Please assign me" or "+1" comments
- **Don't** make PRs with only whitespace or formatting changes without prior discussion
- **Don't** submit incomplete or untested code
- **Don't** create multiple issues for the same problem
- **Don't** hijack existing issues with unrelated topics
- **Don't** demand immediate responses or reviews
- **Don't** use offensive or inappropriate language
- **Don't** copy code without proper attribution
- **Don't** submit AI-generated PRs without understanding and testing the code

### Getting Help

- 🐛 **Issues**: [GitHub Issues](https://github.com/CalC/CalC/issues)

## 📜 License

By contributing to CalC, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

Thank you for contributing to CalC! 🎉
