from backend.app.database import Base, engine
from backend.app.models import Decision

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
