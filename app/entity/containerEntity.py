from sqlalchemy import Column, BINARY, INTEGER, TIMESTAMP, VARCHAR

from app.db.database import Base


class Container(Base):
    __tablename__ = "container"
    __table_args__ = {'extend_existing': True}

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    experiment_id = Column(BINARY(12), unique=True, index=True)
    user_id = Column(VARCHAR(50), index=True, nullable=False)
    data_name = Column(VARCHAR(100))
    model_name = Column(VARCHAR(100))
    created_at = Column(TIMESTAMP)
    X_TOKEN = Column(VARCHAR(10))
    TOKEN = Column(VARCHAR(10))
    # 11/8 Variable 추가로 인한 추가.
    status = Column(VARCHAR(10))
    python_source = Column(VARCHAR(300))
    accuracy = Column(VARCHAR(10))