# Changelog

## 28/09/2026

### Added
- config.py: the app reads SECRET_KEY and DATABASE_URL from environment variables
- .env.example: template of the settings
- .env added to .gitignore so real settings are not committed

### Changed
- app.py now loads its settings from config.py
- conftest.py sets DATABASE_URL so tests use an in-memory database

### Fixed
- Tests were running against the real database and wiping it
- Member registration code was removed from main after a merge, and was restored through PR #3

## 21/09/2026 - 23/09/2026

### Added
- Basic Flask app with a home route
- Member and Registration models, connected to SQLite
- Registration form and /registrations/new route
- Automated test for registration (pytest)
- README with setup, run and test instructions