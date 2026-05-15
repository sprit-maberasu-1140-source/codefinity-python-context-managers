class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        # TODO: Implement connection opening logic
        print(f"Connecting to database:{self.db_name}")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        # TODO: Implement connection closing logic
        print(f"Disconnecting from database:{self.db_name}") 

# Sample usage
with DatabaseConnection("TestDB") as conn:
    print("Performing database operations...")
