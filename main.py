from database.database import engine, SessionLocal
from models import models
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)


# Kept for later (FastAPI uses this as a dependency). Not used below.
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# --- Open a session (a "conversation" with the database) ---
db: Session = SessionLocal()

# --- 0. Start clean, so every run of this script gives the same output ---
db.query(models.Test).delete()
db.commit()

# --- 1. Add rows ---
row1 = models.Test(title="Buy milk", description="2 liters", priority=2)
row2 = models.Test(title="Read Telegram", description="catch up on channels", priority=1)
row3 = models.Test(title="Write digest", description="summarize the day", priority=3, complete=True)

db.add(row1)
db.add(row2)
db.add(row3)
db.commit()  # nothing is saved to the file until commit()

# --- 2. Query and print all rows ---
print("After insert:")
rows = db.query(models.Test).all()
for row in rows:
    print(f"  id={row.id} title={row.title!r} priority={row.priority} complete={row.complete}")

# --- 3. Delete one row ---
to_delete = db.query(models.Test).filter(models.Test.title == "Buy milk").first()
db.delete(to_delete)
db.commit()

# --- 4. Query and print what is left ---
print("After delete:")
rows = db.query(models.Test).all()
for row in rows:
    print(f"  id={row.id} title={row.title!r} priority={row.priority} complete={row.complete}")

# --- Close the session ---
db.close()
