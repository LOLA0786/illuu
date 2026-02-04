# ADR-0006: Workflow Engine Is the Only Orchestration Surface

## Context
Orchestration logic is spread across multiple subsystems, making workflows difficult to audit and test.

## Decision
All orchestration logic belongs in workflows/, defined through explicit step contracts and YAML workflow definitions.

## Consequences
- Orchestration logic elsewhere is migrated to workflows/.
- Kernel delegates multi-step execution to workflow engine.
- Workflow definitions are validated and versioned.

## Migration Notes
- memory/orchestrator and similar constructs will be relocated.
- Legacy runtime flows will be archived once migrated.

## Alternatives Considered
- Allowing orchestration in memory or vault: rejected due to duplication.
