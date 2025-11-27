"""Tests for the FastAPI application"""

import pytest
from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_cities_spain():
    """Test getting cities for Spain"""
    response = client.get("/countries/Spain")
    assert response.status_code == 200
    assert sorted(response.json()) == sorted(["Madrid", "Barcelona", "Seville", "Valencia"])


def test_countries_with_invalid_country():
    """Test getting cities for a country that doesn't exist"""
    response = client.get("/countries/InvalidCountry")
    assert response.status_code == 404


def test_get_activities():
    """Test getting all activities"""
    response = client.get("/activities")
    assert response.status_code == 200
    assert "Chess Club" in response.json()
