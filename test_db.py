from sqlalchemy import create_engine
import sys

# The exact string the user has in Render
URL = "postgresql://postgres.ajnguaopifbeippmojbi:Gelman%26050897@aws-1-eu-west-1.pooler.supabase.com:6543/postgres"

try:
    print("Testing connection...")
    engine = create_engine(URL)
    with engine.connect() as conn:
        print("Success!")
except Exception as e:
    print(f"Error: {e}")
