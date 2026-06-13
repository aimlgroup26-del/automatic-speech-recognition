# Risk Register
## Automatic Speech Recognition (ASR)

| Field | Details |
|-------|---------|
| **Version** | 1.0 |
| **Date** | 2026-06-13 |
| **Owner** | Project Lead |
| **Review Frequency** | Bi-weekly |

---

## Risk Matrix

| Likelihood \ Impact | Low (1) | Medium (2) | High (3) |
|---------------------|---------|------------|----------|
| **High (3)** | 3 | 6 | 9 |
| **Medium (2)** | 2 | 4 | 6 |
| **Low (1)** | 1 | 2 | 3 |

**Score:** Likelihood × Impact  
- 🔴 7–9: Critical — immediate action required  
- 🟠 4–6: High — mitigation plan required  
- 🟡 2–3: Medium — monitor closely  
- 🟢 1: Low — accept / monitor

---

## Risk Register

| ID | Risk | Category | Likelihood | Impact | Score | Status | Mitigation | Owner | Review Date |
|----|------|----------|-----------|--------|-------|--------|------------|-------|-------------|
| R01 | Insufficient labeled audio data | Data | Medium (2) | High (3) | 🟠 6 | Open | Use public datasets (LibriSpeech, CommonVoice); apply data augmentation | Data Lead | YYYY-MM-DD |
| R02 | Model underfitting / poor convergence | Model | Medium (2) | High (3) | 🟠 6 | Open | Hyperparameter tuning; try alternative architectures | ML Lead | YYYY-MM-DD |
| R03 | Compute resource unavailability | Infrastructure | Low (1) | High (3) | 🟡 3 | Open | Pre-book cloud instances; use spot/preemptible VMs | MLOps | YYYY-MM-DD |
| R04 | Scope creep | Project | Medium (2) | Medium (2) | 🟡 4 | Open | Strict scope change process; weekly scope review | Project Lead | YYYY-MM-DD |
| R05 | Team member unavailability | People | Low (1) | Medium (2) | 🟢 2 | Open | Cross-train team; maintain up-to-date documentation | Project Lead | YYYY-MM-DD |
| R06 | Audio data quality issues | Data | Medium (2) | Medium (2) | 🟡 4 | Open | Implement data validation and QA pipeline | Data Lead | YYYY-MM-DD |
| R07 | Overfitting on training data | Model | Medium (2) | Medium (2) | 🟡 4 | Open | Regularization (dropout, weight decay); early stopping | ML Lead | YYYY-MM-DD |
| R08 | Dependency/package incompatibilities | Technical | Low (1) | Low (1) | 🟢 1 | Open | Pin dependencies in requirements.txt; use Docker | MLOps | YYYY-MM-DD |
| R09 | Data privacy / licensing issues | Compliance | Low (1) | High (3) | 🟡 3 | Open | Review dataset licenses before use; avoid PII data | Project Lead | YYYY-MM-DD |
| R10 | Missed project deadline | Schedule | Medium (2) | High (3) | 🟠 6 | Open | Weekly progress tracking; buffer time in schedule | Project Lead | YYYY-MM-DD |

---

## Risk Log (Updates)

| Date | Risk ID | Update | Updated By |
|------|---------|--------|------------|
| 2026-06-13 | All | Initial risk identification | Project Lead |

---

_Risks should be reviewed at every sprint review. New risks should be added immediately upon identification._
