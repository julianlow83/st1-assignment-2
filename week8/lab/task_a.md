# A: Architectural Responsibility Analysis

The current codebase contains several mixed responsibilities across architectural layers. 

| Layer | Primary Duty | Current Violation / Leakage |
| :--- | :--- | :--- |
| **Domain** | Business rules, invariants, state transitions | Invariant guards bypassed if initialized directly without a controller guardrail. |
| **Workflow (Service)** | Use case orchestration, entity existence validation | Leaked into procedural test scripts (`manual_tester.py`). |
| **Data-Access** | SQL execution, data mapping | High risk of direct `sqlite3` coupling without a Repository interface. |
| **Presentation** | User I/O (`input()`, `print()`), screen formatting | Mixed directly with application execution logic in client scripts. |