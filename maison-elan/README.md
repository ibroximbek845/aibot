# Maison Élan

Luxury clothing storefront with an admin dashboard.

## Required environment variables

Set these in Render → your service → Environment (or in a local, untracked `.env` file):

- `DATABASE_URL` — PostgreSQL connection string.
- `JWT_SECRET` — long, random secret used to sign admin sessions.
- `ADMIN_EMAIL` — admin login email.
- `ADMIN_PASSWORD` — strong, unique admin password.

Do not hard-code credentials in source files and do not commit `.env`. The `.env.example` file contains placeholders only.

## Run

```bash
npm install
npm start
```

The storefront is served at `/` and the admin dashboard at `/admin`.
