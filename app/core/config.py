import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    #usuario:password@localhost:5432/nombre_BD
    "postgresql://postgres:2005@localhost:5432/System_Orders"
) 