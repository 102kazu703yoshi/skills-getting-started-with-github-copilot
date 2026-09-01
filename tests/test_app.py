"""
Tests for the High School Activity Management System API.

This module contains basic integration tests for the FastAPI application,
covering core functionality and happy-path scenarios.
"""

from fastapi.testclient import TestClient
from src.app import app


client = TestClient(app)


class TestActivityManagement:
    """Test suite for activity management endpoints."""

    def test_get_activities_returns_list(self):
        """Test that GET /activities returns a dictionary of all available activities."""
        response = client.get("/activities")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) > 0
        # Verify structure of activity objects
        first_activity = next(iter(data.values()))
        assert "description" in first_activity
        assert "schedule" in first_activity
        assert "max_participants" in first_activity
        assert "participants" in first_activity

    def test_activity_signup_success(self):
        """Test that a new user can successfully sign up for an activity."""
        activity_name = "Programming Class"
        test_email = "student123@school.edu"
        
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": test_email}
        )
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert test_email in data["message"]
        
        # Verify participant was added by checking activities
        activities_response = client.get("/activities")
        participants = activities_response.json()[activity_name]["participants"]
        assert test_email in participants

    def test_activity_signup_duplicate_prevention(self):
        """Test that duplicate signup attempts are rejected."""
        activity_name = "Programming Class"
        test_email = "programmer@school.edu"
        
        # First signup succeeds
        response1 = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": test_email}
        )
        assert response1.status_code == 200
        
        # Duplicate signup should fail
        response2 = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": test_email}
        )
        assert response2.status_code == 400
        assert "already signed up" in response2.json().get("detail", "").lower()

    def test_activity_withdrawal_success(self):
        """Test that a user can successfully withdraw from an activity."""
        activity_name = "Art Studio"
        test_email = "artist@school.edu"
        
        # First, sign up
        client.post(
            f"/activities/{activity_name}/signup",
            params={"email": test_email}
        )
        
        # Then withdraw
        response = client.post(
            f"/activities/{activity_name}/withdraw",
            params={"email": test_email}
        )
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        
        # Verify participant was removed by checking activities
        activities_response = client.get("/activities")
        participants = activities_response.json()[activity_name]["participants"]
        assert test_email not in participants

    def test_activity_withdrawal_nonexistent_user(self):
        """Test that withdrawal fails when user is not enrolled."""
        activity_name = "Soccer Club"
        test_email = "notsignedupstudent@school.edu"
        
        response = client.post(
            f"/activities/{activity_name}/withdraw",
            params={"email": test_email}
        )
        assert response.status_code == 400
        assert "not signed up" in response.json().get("detail", "").lower()

    def test_nonexistent_activity_returns_404(self):
        """Test that requests to non-existent activities return 404."""
        fake_activity = "Nonexistent Activity"
        
        # Test GET - verify it's not in the activities list
        response_get = client.get("/activities")
        activity_names = list(response_get.json().keys())
        assert fake_activity not in activity_names
        
        # Test POST signup to non-existent activity
        response_signup = client.post(
            f"/activities/{fake_activity}/signup",
            params={"email": "test@school.edu"}
        )
        assert response_signup.status_code == 404

    def test_root_redirects_to_static(self):
        """Test that GET / redirects to the static content."""
        response = client.get("/", follow_redirects=False)
        assert response.status_code in [301, 302, 303, 307, 308]  # Redirect status codes
        assert "static" in response.headers.get("location", "").lower()
