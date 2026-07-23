# Contributing to Open Video Automation Toolkit

Thank you for your interest in contributing to Open Video Automation Toolkit.

Contributions are welcome in many forms, including:

- Bug fixes
- New features
- Documentation improvements
- Example workflows
- Tests
- Security improvements
- Performance improvements
- Translation improvements

## Before You Start

Please check the existing issues before opening a new one.

For major changes, open an issue first and explain:

- The problem
- The proposed solution
- The expected behavior
- Possible alternatives
- Any compatibility concerns

This helps avoid duplicated work and makes it easier to discuss the proposed change before implementation.

## Development Process

1. Fork the repository.
2. Create a new branch.
3. Make focused and clear changes.
4. Test your changes.
5. Update the documentation when needed.
6. Commit your changes with a descriptive message.
7. Push the branch to your fork.
8. Open a pull request.

Example branch name:

```text
feature/add-subtitle-provider
```

Example commit message:

```text
feat: add subtitle provider support
```

## Branch Naming

Use clear and descriptive branch names.

Examples:

```text
feature/add-youtube-upload
fix/render-timeout
docs/update-installation-guide
test/add-api-tests
```

Recommended prefixes:

- `feature/` for new features
- `fix/` for bug fixes
- `docs/` for documentation changes
- `test/` for tests
- `refactor/` for code improvements
- `security/` for security-related changes

## Commit Message Guidelines

Use short and descriptive commit messages.

Examples:

```text
feat: add automatic subtitle generation
fix: prevent empty rendering jobs
docs: improve Docker installation guide
test: add rendering API tests
refactor: simplify media processing
security: remove sensitive values from logs
```

Avoid unclear commit messages such as:

```text
update
changes
fix stuff
new code
```

## Pull Request Guidelines

A pull request should:

- Explain what changed
- Explain why it changed
- Include testing details
- Include screenshots when relevant
- Mention related issues
- Avoid unrelated changes
- Keep credentials and secrets out of the repository
- Update documentation when behavior changes

A good pull request description should include:

```text
Summary:
What was changed?

Reason:
Why was this change needed?

Testing:
How was the change tested?

Related issue:
Which issue does this pull request address?
```

## Code Quality

Please keep changes:

- Focused
- Readable
- Documented
- Backward-compatible when possible
- Easy to test
- Easy to review

Avoid adding unnecessary dependencies.

Use clear function, variable and file names.

Add comments only when they improve understanding.

## Testing

Before opening a pull request:

- Confirm the application starts correctly
- Test the changed feature
- Check for error messages
- Confirm existing features still work
- Add tests when possible
- Verify that no credentials are included

For rendering-related changes, test at least:

- One vertical video
- One horizontal video
- Subtitle-enabled rendering
- Subtitle-disabled rendering
- Invalid input handling

## Documentation

Update the documentation when you change:

- Installation steps
- Environment variables
- API endpoints
- Configuration options
- Workflow behavior
- External service integrations

Do not add real credentials to documentation examples.

Use placeholder values such as:

```env
OPENAI_API_KEY=your_api_key_here
YOUTUBE_CLIENT_ID=your_client_id_here
API_AUTH_TOKEN=your_secure_token_here
```

## Security

Never commit:

- API keys
- Access tokens
- Passwords
- Private URLs
- Private IP addresses
- Service account credentials
- OAuth refresh tokens
- Personal information
- Customer data
- Private workflow exports
- Production configuration files

Use environment variables for sensitive values.

Only add placeholder values to `.env.example`.

Before committing, review your changes carefully:

```bash
git diff
git status
```

If a secret is committed accidentally, remove it immediately and rotate the exposed credential.

## Reporting Security Issues

Do not publish sensitive security vulnerabilities in a public issue.

For security-related reports, provide:

- A clear description
- Steps to reproduce
- Possible impact
- A suggested fix, when available

Do not include real credentials, personal data or production system information.

## Feature Requests

Feature requests should explain:

- The problem being solved
- The proposed feature
- The expected benefit
- Possible alternatives
- Any required external services

## Bug Reports

Bug reports should include:

- A clear title
- Steps to reproduce
- Expected behavior
- Actual behavior
- Relevant logs
- Operating system
- Docker version
- Python version
- FFmpeg version
- n8n version, when relevant

Remove all sensitive information from logs before sharing them.

## Code of Conduct

Be respectful, constructive and professional.

The following behavior is not accepted:

- Harassment
- Discrimination
- Personal attacks
- Threats
- Abusive language
- Spam
- Deliberate disruption
- Publishing private information

Disagreements should remain focused on the project and the technical issue.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.
