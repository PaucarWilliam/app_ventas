import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    #usuario:password@localhost:5432/nombre_BD
    "postgresql://postgres:root@localhost:5432/System_Orders"
) 