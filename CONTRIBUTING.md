# Contributing to Automatic Speech Recognition

Thank you for your interest in contributing to this project! Please read these guidelines carefully before contributing.

---

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Team Workflow](#team-workflow)
- [Branching Strategy](#branching-strategy)
- [Commit Message Convention](#commit-message-convention)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Definition of Done](#definition-of-done)

---

## Code of Conduct

All contributors are expected to:
- Be respectful and inclusive in all communications
- Provide constructive feedback during reviews
- Acknowledge and credit others' contributions
- Escalate conflicts to the project lead

---

## Team Workflow

This project follows an **Agile/Scrum** workflow:

| Ceremony | Frequency | Duration | Owner |
|----------|-----------|----------|-------|
| Sprint Planning | Bi-weekly | 1 hour | Project Lead |
| Daily Standup | Daily | 15 min | All |
| Sprint Review | Bi-weekly | 30 min | All |
| Retrospective | Bi-weekly | 30 min | All |

**Sprint Duration:** 2 weeks  
**Sprint Board:** [Link to Jira / GitHub Projects / Trello]

---

## Branching Strategy

We follow **Git Flow**:

```
main          ← production-ready, protected
develop       ← integration branch for features
feature/*     ← new features (branch from develop)
bugfix/*      ← bug fixes (branch from develop)
hotfix/*      ← urgent fixes (branch from main)
release/*     ← release preparation
```

**Naming conventions:**
```
feature/your-name/short-description
bugfix/issue-number-short-description
hotfix/issue-number-short-description
```

**Example:**
```bash
git checkout develop
git checkout -b feature/john/data-preprocessing
```

---

## Commit Message Convention

Follow the **Conventional Commits** specification:

```
<type>(<scope>): <short summary>

[optional body]

[optional footer]
```

**Types:**

| Type | When to Use |
|------|-------------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation changes only |
| `style` | Formatting, no logic change |
| `refactor` | Code restructuring, no feature change |
| `test` | Adding or updating tests |
| `chore` | Build process, tooling, dependencies |
| `data` | Dataset changes |
| `model` | Model architecture changes |
| `experiment` | Experiment tracking |

**Examples:**
```
feat(model): add transformer encoder layer
fix(dataset): handle missing audio files gracefully
docs(readme): update project timeline
data(preprocessing): normalize audio to 16kHz
```

---

## Pull Request Process

1. **Create a branch** from `develop` following the naming convention above
2. **Make your changes** with clear, focused commits
3. **Update documentation** if your change affects README, docs, or interfaces
4. **Update CHANGELOG.md** under `[Unreleased]`
5. **Open a Pull Request** against `develop` using the PR template
6. **Request review** from at least one team member
7. **Address feedback** — all review comments must be resolved before merge
8. **Squash and merge** once approved

### PR Title Format
```
[TYPE] Short description (Issue #XX)
```

### PR Checklist
Before submitting a PR, confirm:
- [ ] Code follows project conventions
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] No hardcoded credentials or sensitive data
- [ ] Branch is up-to-date with `develop`

---

## Issue Reporting

When filing an issue, use the appropriate template:

- **Bug Report:** Describe the bug, steps to reproduce, expected vs actual behavior
- **Feature Request:** Describe the feature, motivation, and proposed approach
- **Data Issue:** Describe the dataset problem and affected samples

Label issues appropriately: `bug`, `feature`, `data`, `documentation`, `question`

---

## Definition of Done

A task is considered **Done** when:
- [ ] Implementation is complete and reviewed
- [ ] Documentation is updated
- [ ] Tests pass (when applicable)
- [ ] CHANGELOG entry added
- [ ] PR merged to `develop`
- [ ] Reviewer has approved
