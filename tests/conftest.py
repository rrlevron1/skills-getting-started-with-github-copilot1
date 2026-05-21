import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_db


@pytest.fixture
def client():
    """Provide a TestClient instance for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore the in-memory activities database before each test."""
    original_activities = copy.deepcopy(activities_db)
    yield
    activities_db.clear()
    activities_db.update(copy.deepcopy(original_activities))
