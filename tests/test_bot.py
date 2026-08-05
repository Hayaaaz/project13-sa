import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.bot import answer

def test_lockdown():
    resp = answer("What is the lockdown procedure?")
    assert "lockdown" in resp.lower()

def test_fire_drill():
    resp = answer("What do we do in a fire drill?")
    assert "fire drill" in resp.lower()

def test_late_policy():
    resp = answer("What is the policy for late students?")
    assert "late" in resp.lower() or "office" in resp.lower()

def test_unknown():
    resp = answer("What is the lunch menu?")
    assert "don't know" in resp.lower()
