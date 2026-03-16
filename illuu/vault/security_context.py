"""Compatibility shim. Use governance.internal.security.security_context instead."""
from governance.internal.security import security_context as _sc

_load_context_keys = _sc._load_context_keys
_get_context_key = _sc._get_context_key
compute_request_hash = _sc.compute_request_hash
_verify_signature = _sc._verify_signature
_parse_context = _sc._parse_context
_assert_required_fields = _sc._assert_required_fields
_assert_timestamp_valid = _sc._assert_timestamp_valid
require_signed_context = _sc.require_signed_context

__all__ = [
    "_load_context_keys",
    "_get_context_key",
    "compute_request_hash",
    "_verify_signature",
    "_parse_context",
    "_assert_required_fields",
    "_assert_timestamp_valid",
    "require_signed_context",
]
