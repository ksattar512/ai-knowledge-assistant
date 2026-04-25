# 🔐 Security Notes

## Recommended Enterprise Security Controls

- API key or OAuth2 authentication
- Microsoft Entra ID / Azure AD integration
- Role-based document access
- Tenant-aware vector indexes
- Encryption at rest and in transit
- Prompt injection protection
- PII redaction
- Query audit logs
- Source-level authorization checks

## Data Handling Principle

Sensitive documents should remain in approved enterprise storage. The vector index should store only the minimum required searchable representation and metadata.
