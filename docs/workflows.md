# Workflows

## Purpose
Provide a deterministic, auditable workflow engine for multi-step agent execution.

## Responsibilities
- Execute Planner → Executor → Verifier → Compliance → Approver
- Validate YAML workflow definitions
- Support human-in-loop approvals
- Emit workflow audit trail

## Interfaces
- WorkflowEngine.execute
- WorkflowDefinition.validate

## Data Flow
1. Workflow definition is loaded and validated.
2. Steps execute with governance checks at each boundary.
3. Results are persisted via state layer and ledgered.

## Extension Points
- New step types
- Custom validators
- Human approval queues

## Failure Modes
- Partial execution without checkpoint
- Invalid workflow schema
- Approver unavailable

## Testing Strategy
- Unit tests for step transitions
- Integration tests with governance and state
