# Seed Data Import Feature

## Overview
Automatic seed data import system that loads companies and contacts from CSV files on application startup.

## Management Command

### Command: `import_seed_data`

Imports company and contact data from a CSV file.

**Usage:**
```bash
python manage.py import_seed_data [options]
```

**Options:**
- `--clear` - Clear all existing companies and contacts before importing
- `--file PATH` - Specify custom CSV file path (default: `seed_data/test_data.csv`)

**Examples:**
```bash
# Import seed data (skips if data already exists)
python manage.py import_seed_data

# Force reimport (clears existing data first)
python manage.py import_seed_data --clear

# Import from custom file
python manage.py import_seed_data --file path/to/custom.csv
```

## CSV Format

The CSV file should have the following columns:

| Column Name | Required | Description |
|------------|----------|-------------|
| Company Name | Yes* | Name of the company |
| Contact Name | No | Full name of the contact person |
| Email | Yes* | Contact email address (must be unique) |
| Phone Number | No | Contact phone number |
| Notes | No | Additional notes |

*At least Company Name or Email must be provided


## Automatic Import on Startup

### Development Environment

**Local Development:**
Use the provided startup script that automatically runs migrations and imports seed data:

```bash
./dev_server.sh
```

This script:
1. Runs database migrations
2. Imports seed data (if not already present)
3. Starts the development server

**Manual Start:**
If you prefer to start manually:
```bash
python manage.py migrate
python manage.py import_seed_data
python manage.py runserver
```

### Production/Railway Environment

The seed data import runs automatically on every deployment via the `nixpacks.toml` start command:

```toml
[start]
cmd = "python manage.py migrate && python manage.py import_seed_data && gunicorn ..."
```

**Important:** The command is safe to run multiple times. It will:
- Skip import if data already exists
- Log a warning message and continue
- Not duplicate existing records

## Import Behavior

### Safety Features

1. **Duplicate Prevention:**
   - Checks if companies or contacts already exist
   - Skips import if database already has data
   - Use `--clear` flag to force reimport

2. **Error Handling:**
   - Continues processing if individual rows fail
   - Reports errors without stopping the entire import
   - Gracefully handles missing files

3. **Data Integrity:**
   - Email addresses must be unique (enforced by model)
   - Company-Contact relationships are preserved
   - All imported companies set to `not_contacted` milestone

### Import Logic

**For each CSV row:**

1. **Company Creation:**
   - Creates company with `milestone='not_contacted'`
   - Uses `get_or_create()` to avoid duplicates
   - Skips if company name already exists

2. **Contact Creation:**
   - Requires unique email address
   - Splits "Contact Name" into first and last name
   - Associates with created/existing company
   - Falls back to company name if contact name is empty

3. **Relationship:**
   - Each contact is linked to its company via ForeignKey
   - Company detail page shows all related contacts
   - Contacts can be created without a company (optional)

## Output Examples


### Data Already Exists:
```
Database already contains 9 companies. Skipping import. Use --clear to force reimport.
```

### File Not Found:
```
CSV file not found: /path/to/file.csv
Skipping seed data import.
```

## File Location

**Default seed data file:**
```
seed_data/test_data.csv
```

This file is version controlled and deployed with the application.

## Environment Variables

No environment variables required. The command detects the environment automatically:

- **Development:** Runs on every server start (via `dev_server.sh`)
- **Production:** Runs on Railway deployment (via `nixpacks.toml`)
- **Both:** Safe to run multiple times

## Troubleshooting

### Import Not Running Automatically

**Development:**
- Ensure you're using `./dev_server.sh` to start the server
- Or manually run `python manage.py import_seed_data`

**Production (Railway):**
- Check deployment logs: `railway logs`
- Command runs after migrations in start command
- Look for "Importing seed data" or "already contains" messages

### Duplicate Errors

If you get unique constraint errors:
```bash
# Clear and reimport
python manage.py import_seed_data --clear
```

### Custom Data

To use your own seed data:
1. Create a CSV file with the correct format
2. Place it in the `seed_data/` directory
3. Run: `python manage.py import_seed_data --file seed_data/your_file.csv`

### Testing Import

To test the import process:
```bash
# Clear and reimport with verbose output
python manage.py import_seed_data --clear -v 2
```

## Integration with Existing Features

### Companies
- All imported companies have `milestone='not_contacted'`
- Ready for progression through the sales pipeline
- Visible in company list and dashboard stats

### Contacts
- Each contact linked to its company
- Searchable and filterable in contact list
- Displayed on company detail pages

### Dashboard
- Imported data immediately appears in dashboard stats
- Milestone chart shows all companies in "Not Yet Contacted"
- Total counts update automatically

## Future Enhancements

Potential improvements:
- [ ] Support for multiple CSV files
- [ ] Import deals and opportunities
- [ ] Update existing records (instead of skip)
- [ ] Import validation and preview
- [ ] Bulk import via admin interface
- [ ] Import from Google Sheets/Excel
- [ ] Import activity history
- [ ] Custom field mapping
- [ ] Import scheduling/automation

## Related Files

```
contacts/management/commands/import_seed_data.py  - Management command
seed_data/test_data.csv                           - Default seed data
nixpacks.toml                                     - Railway startup config
dev_server.sh                                     - Local dev startup script
```

## Notes

- Import is idempotent (safe to run multiple times)
- No data loss risk - checks before importing
- Suitable for both development and production
- Performance: ~1-2 seconds for 100 records
- Memory efficient: processes row by row
