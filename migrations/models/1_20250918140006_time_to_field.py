from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "tasks" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(100),
    "question" TEXT,
    "answer" TEXT
);
CREATE TABLE IF NOT EXISTS "stations" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "time" INT DEFAULT 10,
    "points" INT DEFAULT 10,
    "name" VARCHAR(100) NOT NULL,
    "description" TEXT,
    "image" VARCHAR(255),
    "assignment" TEXT,
    "task_id" INT REFERENCES "tasks" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "station_orders" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "eighth_id" INT REFERENCES "stations" ("id") ON DELETE CASCADE,
    "fifth_id" INT REFERENCES "stations" ("id") ON DELETE CASCADE,
    "first_id" INT REFERENCES "stations" ("id") ON DELETE CASCADE,
    "fourth_id" INT REFERENCES "stations" ("id") ON DELETE CASCADE,
    "ninth_id" INT REFERENCES "stations" ("id") ON DELETE CASCADE,
    "second_id" INT REFERENCES "stations" ("id") ON DELETE CASCADE,
    "seventh_id" INT REFERENCES "stations" ("id") ON DELETE CASCADE,
    "sixth_id" INT REFERENCES "stations" ("id") ON DELETE CASCADE,
    "tenth_id" INT REFERENCES "stations" ("id") ON DELETE CASCADE,
    "third_id" INT REFERENCES "stations" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "username" VARCHAR(150) NOT NULL UNIQUE,
    "email" VARCHAR(255) UNIQUE,
    "hash_password" VARCHAR(128) NOT NULL,
    "first_name" VARCHAR(30),
    "last_name" VARCHAR(150),
    "is_active" BOOL NOT NULL DEFAULT True,
    "is_superuser" BOOL NOT NULL DEFAULT False
);
CREATE TABLE IF NOT EXISTS "curators" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(100),
    "station_id" INT REFERENCES "stations" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL UNIQUE REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "player_teams" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "team_name" VARCHAR(100) NOT NULL,
    "start_time" TIMESTAMPTZ,
    "score" INT DEFAULT 0,
    "current_station" INT NOT NULL DEFAULT 1,
    "stations_id" INT REFERENCES "station_orders" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL UNIQUE REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""



async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
