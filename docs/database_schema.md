# AIMetricMate Database Schema

## Cosmos DB Container Structure

### Users Container
- Partition Key: `/guild_id`
```json
{
    "id": "user_id",
    "guild_id": "discord_guild_id",
    "username": "discord_username",
    "settings": {
        "notifications_enabled": boolean,
        "preferred_currency": string
    },
    "created_at": timestamp,
    "updated_at": timestamp
}
```

### LLM Usage Container
- Partition Key: `/user_id`
```json
{
    "id": "usage_id",
    "user_id": "discord_user_id",
    "llm_type": "string",
    "tokens_used": number,
    "cost": number,
    "timestamp": timestamp,
    "metadata": {
        "model": string,
        "purpose": string
    }
}
```

### Copilot Usage Container
- Partition Key: `/user_id`
```json
{
    "id": "usage_id",
    "user_id": "discord_user_id",
    "suggestions_count": number,
    "accepted_count": number,
    "repository": string,
    "language": string,
    "timestamp": timestamp
}
```

### Prompts Container
- Partition Key: `/user_id`
```json
{
    "id": "prompt_id",
    "user_id": "discord_user_id",
    "title": string,
    "content": string,
    "tags": array,
    "created_at": timestamp,
    "updated_at": timestamp,
    "metadata": {
        "category": string,
        "version": string
    }
}
```

## Query Patterns

### Common Queries
1. Get user's LLM usage for date range
2. Calculate total costs per user/guild
3. Fetch prompts by tag
4. Get Copilot efficiency metrics

### Performance Optimization
- Use partition keys effectively
- Implement caching for frequent queries
- Batch operations when possible
- Use change feed for real-time updates

## Data Models

### Python Classes
```python
@dataclass
class User:
    id: str
    guild_id: str
    username: str
    settings: Dict[str, Any]
    created_at: datetime
    updated_at: datetime

@dataclass
class LLMUsage:
    id: str
    user_id: str
    llm_type: str
    tokens_used: int
    cost: float
    timestamp: datetime
    metadata: Dict[str, Any]

# Additional models defined in database/models.py
