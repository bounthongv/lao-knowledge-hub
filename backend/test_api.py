"""Test script to verify FastAPI backend is running"""
import requests

try:
    # Test health endpoint
    response = requests.get("http://localhost:8000/health")
    print(f"✅ Health Check: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # Test books endpoint
    response = requests.get("http://localhost:8000/api/v1/books")
    print(f"\n✅ Books API: {response.status_code}")
    print(f"Response: {response.json()}")
    
except requests.exceptions.ConnectionError:
    print("❌ Error: Cannot connect to API at http://localhost:8000")
    print("\nMake sure the FastAPI server is running:")
    print("  cd backend")
    print("  python -m uvicorn app.main:app --reload --port 8000")
except Exception as e:
    print(f"❌ Error: {e}")
