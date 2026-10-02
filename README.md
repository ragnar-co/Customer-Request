# Customer Request Follow-up Dashboard

Weekly follow-up dashboard for cybersecurity customer requests. Uploads a
validated CSV, stores the accepted snapshot in DuckDB, and shows Total /
Completed / Overdue counts, a breakdown by service type, and an overdue
detail table with owner and days-overdue.

Full specification: [`docs/ddd-bundle/`](docs/ddd-bundle/) (see `README.md`
and `00-DDD-SCOPE.md` there for the original requirements). Metric formulas
must only ever be changed by editing `app/metrics.py` — never reimplemented
in the UI.

## Project Structure

```
app/                   Application source
  app.py               Streamlit dashboard (UI)
  config.py            Fixed reference_date, DB path, value contracts
  validate.py          CSV schema/value validation
  db.py                DuckDB snapshot loader
  metrics.py           Canonical metric queries (single source of truth)
  tests/               pytest suite (validation + golden-fixture metrics)
docs/
  ddd-bundle/          Project specification (DDD documents)
  ddd-blueprints/      Generic doc-generator blueprint templates (reference only)
input/                 Drop source CSVs here (gitignored, folder tracked via .gitkeep)
output/                DuckDB snapshot file lives here (gitignored, folder tracked via .gitkeep)
requirements.txt
.env.example
Dockerfile
.dockerignore
.gitignore
```

## Setup (local, no Docker)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # optional — edit APP_REFERENCE_DATE if needed
```

## Run

```bash
source .venv/bin/activate
streamlit run app/app.py
```

Open the printed local URL, upload a CSV matching the schema in
`docs/ddd-bundle/DATA_MODEL_SPEC.md`, and the dashboard populates after
validation passes.

## Run with Docker

```bash
docker build -t customer-request-dashboard .
docker run -p 8501:8501 --env-file .env -v "$(pwd)/output:/app/output" customer-request-dashboard
```

Open http://localhost:8501. The DuckDB snapshot persists on the host via the
mounted `output/` volume.

## Environment Variables

| Variable            | Default                                    | Purpose                                      |
|---------------------|---------------------------------------------|-----------------------------------------------|
| `APP_REFERENCE_DATE` | `2026-10-02`                                | Fixed date used for all overdue calculations. |
| `APP_DB_PATH`        | `<project_root>/output/customer_requests.duckdb` | DuckDB snapshot file location.          |

`APP_REFERENCE_DATE` is always an explicit, configured value — the app never
falls back to the live system clock.

## Tests

```bash
source .venv/bin/activate
pytest -q app/tests
```
