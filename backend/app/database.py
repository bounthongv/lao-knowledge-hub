from supabase import create_client, Client
from app.config import settings

# Supabase client for general operations (uses service role key)
# This has full access to the database
supabase: Client = create_client(
    settings.supabase_url,
    settings.supabase_service_key
)

# Supabase client for auth operations (uses anon key)
# This respects RLS policies
supabase_auth: Client = create_client(
    settings.supabase_url,
    settings.supabase_anon_key
)

def get_supabase() -> Client:
    """
    Dependency for getting Supabase client.
    Use this in FastAPI routes if you need direct Supabase access.
    """
    return supabase
