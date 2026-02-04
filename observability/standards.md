# Observability Standards

## Logging
### Format
- Structured JSON logs.

### Required Fields
- timestamp
- level
- service
- component
- request_id
- trace_id
- span_id
- tenant_id (if available)
- actor_id (if available)
- action (if available)
- decision (if available)
- latency_ms (if available)

### Redaction
- Do not log secrets, credentials, or raw PII.
- Apply hashing or tokenization where needed.

## Tracing
### Propagation
- W3C Trace Context headers: traceparent, tracestate.

### Span Naming
- api.<route>
- governance.authorize
- governance.proxy
- kernel.run
- workflow.step.<name>
- memory.query
- vault.ledger.append

## Metrics
### Naming
- Prefix: illuu.<module>.<metric>

### Standard Metrics
- requests_total
- errors_total
- latency_ms
- governance_denied_total
- cost_usd
- tokens_in
- tokens_out

### Labels
- tenant_id
- env
- route
- decision

## Error Taxonomy
- E_AUTH
- E_POLICY
- E_AUDIT
- E_STORAGE
- E_CONTEXT
- E_TRACE
