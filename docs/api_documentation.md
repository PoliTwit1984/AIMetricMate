# AIMetricMate API Documentation

## Discord Bot Commands

### Analytics Commands
```
/metrics [timeframe] - Show AI usage metrics
/cost [service] - Display cost analysis
/report [type] - Generate detailed report
```

### Copilot Commands
```
/copilot stats - Show Copilot usage statistics
/copilot efficiency - Display acceptance rates
/copilot trends - Show usage trends
```

### Prompt Management
```
/prompt add <title> <content> - Add new prompt
/prompt list [tag] - List prompts
/prompt search <query> - Search prompts
/prompt edit <id> - Edit existing prompt
```

### Admin Commands
```
/admin setup - Initial bot setup
/admin config - Configure bot settings
/admin permissions - Manage access levels
```

## Event Handlers

### Discord Events
- on_ready(): Bot initialization
- on_guild_join(): New server setup
- on_message(): Message processing
- on_command_error(): Error handling

### Custom Events
- on_llm_usage(): Track LLM usage
- on_copilot_suggestion(): Track Copilot activity
- on_prompt_update(): Handle prompt changes

## Integration Points

### Azure Cosmos DB
- Connection management
- Query optimization
- Error handling
- Rate limiting

### GitHub API
- Authentication
- Copilot usage tracking
- Repository integration

## Rate Limits

### Discord API
- Commands: 120/minute
- Messages: 5/5s
- Bulk operations: 5/30s

### Database Operations
- Reads: 1000 RU/s
- Writes: 400 RU/s
- Queries: 200 RU/s

### Error Codes
- 429: Rate limit exceeded
- 403: Permission denied
- 404: Resource not found
- 500: Internal server error

## Security Considerations
- Token validation
- Permission checking
- Input sanitization
- Rate limit enforcement
