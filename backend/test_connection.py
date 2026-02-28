import os
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables
load_dotenv()

# Get Supabase credentials
supabase_url = os.getenv("SUPABASE_URL")
supabase_anon_key = os.getenv("SUPABASE_ANON_KEY")
supabase_service_key = os.getenv("SUPABASE_SERVICE_KEY")

print("=== Testing Supabase Connection ===")
print(f"Supabase URL: {supabase_url}")
print(f"Anon Key: {supabase_anon_key[:20]}...{supabase_anon_key[-10:]}")
print(f"Service Key: {supabase_service_key[:20]}...{supabase_service_key[-10:]}")

try:
    # Test with anon key (public access)
    print("\nTesting anonymous client...")
    anon_client = create_client(supabase_url, supabase_anon_key)
    
    # Try to get a simple query - check if profiles table exists
    response = anon_client.table("profiles").select("id").limit(1).execute()
    print(f"✓ Anonymous client connected successfully!")
    print(f"  Found {len(response.data)} profile records")
    
except Exception as e:
    print(f"✗ Anonymous client failed: {e}")

try:
    # Test with service key (admin access)
    print("\nTesting service client...")
    service_client = create_client(supabase_url, supabase_service_key)
    
    # Try to get books table count
    response = service_client.table("books").select("id").limit(1).execute()
    print(f"✓ Service client connected successfully!")
    print(f"  Found {len(response.data)} book records")
    
except Exception as e:
    print(f"✗ Service client failed: {e}")

print("\n=== Connection Test Complete ===")