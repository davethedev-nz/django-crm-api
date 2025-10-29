# CSV Upload Feature for Companies

## Overview
The Companies page now includes a CSV upload feature that allows you to bulk import or update company records.

## How to Use

1. **Access the Upload Feature**
   - Navigate to the Companies page in the dashboard
   - Click the "📤 Upload CSV" button at the top right of the page

2. **Prepare Your CSV File**
   - Use the template file: `seed_data/companies_template.csv`
   - Required column: `name`
   - Optional columns: `website`, `email`, `phone`, `address`, `industry`, `milestone`, `notes`

3. **Upload Process**
   - Click "Choose CSV File" in the modal
   - Select your prepared CSV file
   - Click "Upload" to start the import
   - The system will show you the results:
     - Number of new companies created
     - Number of existing companies updated
     - Any errors encountered during import

## CSV Format

### Column Descriptions

| Column | Required | Description | Example |
|--------|----------|-------------|---------|
| `name` | ✅ Yes | Company name (must be unique) | Acme Corporation |
| `website` | No | Company website URL | https://acme.com |
| `email` | No | Company email address | contact@acme.com |
| `phone` | No | Company phone number | +1-555-0100 |
| `address` | No | Company physical address | 123 Main St, New York, NY |
| `industry` | No | Company industry/sector | Technology |
| `milestone` | No | Current sales milestone | not_contacted |
| `notes` | No | Additional notes | Potential client for software services |

### Valid Milestone Values

- `not_contacted` - Not yet contacted
- `first_call` - First Call
- `not_interested` - Not interested
- `email_sent` - Email sent
- `meeting_arranged` - Meeting arranged
- `waiting_on_contact` - Waiting on Contact
- `successful` - Successful

## Behavior

### Creating New Companies
- If a company name doesn't exist in the database, a new company record will be created

### Updating Existing Companies
- If a company name already exists, the record will be updated with new information
- Only non-empty fields will update the existing data
- Empty fields in the CSV will not overwrite existing data

## Example CSV

```csv
name,website,email,phone,address,industry,milestone,notes
Acme Corporation,https://acme.com,contact@acme.com,+1-555-0100,"123 Main St, New York, NY",Technology,not_contacted,Potential client for software services
Widget Inc,https://widget.com,info@widget.com,+1-555-0200,"456 Oak Ave, San Francisco, CA",Manufacturing,first_call,Initial discussion held
```

## Error Handling

The upload process will:
- Validate that a file is provided
- Check that the file is a CSV
- Skip rows with missing company names
- Report any errors encountered during processing
- Continue processing other rows even if some rows have errors

## Tips

- **Backup First**: Always backup your database before large imports
- **Test Small**: Try uploading a small CSV first to verify the format
- **Check Results**: Review the upload results message for any errors
- **Page Refresh**: The page will automatically refresh after a successful upload to show the new data

## Troubleshooting

**Issue**: Upload button does nothing
- **Solution**: Make sure you're logged in and have proper permissions

**Issue**: "Company name is required" errors
- **Solution**: Ensure all rows have a value in the `name` column

**Issue**: Invalid milestone warnings
- **Solution**: Use only the valid milestone values listed above

**Issue**: Special characters look wrong
- **Solution**: Save your CSV file with UTF-8 encoding

## API Endpoint (for developers)

The upload functionality is also available via REST API:

```bash
POST /api/companies/upload_csv/
Content-Type: multipart/form-data

# Include CSV file in form data with key 'file'
```

Response:
```json
{
  "message": "CSV upload completed",
  "created": 5,
  "updated": 2,
  "errors": []
}
```
