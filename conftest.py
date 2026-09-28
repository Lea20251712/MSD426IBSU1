import os

# Use an in-memory database for all tests, before app.py is imported
os.environ["DATABASE_URL"] = "sqlite:///:memory:"