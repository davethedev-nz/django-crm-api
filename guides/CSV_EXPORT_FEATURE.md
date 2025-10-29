# CSV Export Feature for Companies

## Overview
The Companies page now includes a CSV export feature that allows you to download company data based on your current filtered view, with timestamps and filter documentation.

## How to Use

### Via Dashboard UI

1. **Navigate to Companies Page**
   - Go to the Companies page in your CRM dashboard

2. **Apply Filters (Optional)**
   - Use the search box to filter by name, industry, or email
   - Use the milestone dropdown to filter by sales stage

3. **Export Data**
   - Click the "📥 Export Filtered Results" button at the top right
   - Your browser will download a timestamped CSV file (e.g., `companies_export_20251030_143022.csv`)
   - The export includes:
     - Current search filters
     - Current milestone filters
     - Filter metadata at the top of the CSV file

### Via REST API

```bash
GET /api/companies/export_csv/

# With filters
GET /api/companies/export_csv/?milestone=first_call
GET /api/companies/export_csv/?search=technology
GET /api/companies/export_csv/?milestone=successful&search=tech
```

## Export Format

### File Naming

Exported files follow this naming convention:
- **Format**: `companies_export_YYYYMMDD_HHMMSS.csv`
- **Example**: `companies_export_20251030_143022.csv`
- The timestamp helps you track when the export was generated

### CSV Structure

Each CSV export includes:

1. **Metadata Section** (commented rows at top)
   - Export title
   - Generation timestamp
   - Total number of records
   - Applied filters (if any)

2. **Data Section**
   - Column headers
   - Company data rows, grouped by industry

### CSV Columns

The exported CSV includes the following columns:

1. **Industry** - Company industry (grouped)
2. **Company Name** - Name of the company
3. **Website** - Company website URL
4. **Email** - Company email address
5. **Phone** - Company phone number
6. **Address** - Company physical address
7. **Milestone** - Current milestone code (e.g., `first_call`)
8. **Milestone Status** - Human-readable milestone (e.g., "First Call")
9. **Notes** - Additional notes about the company
10. **Created Date** - When the company was added to the system
11. **Updated Date** - Last update timestamp

### Industry Grouping

Companies are automatically grouped by industry in the export:

- **Sorted by Industry**: Companies are ordered alphabetically by industry, then by name
- **Visual Separation**: Blank rows separate different industry groups
- **Unspecified Industries**: Companies without an industry are listed under "No Industry Specified"

## Example Export

```csv
# Companies Export
# Generated: 2025-10-30 14:30:22
# Total Records: 8
# Filters Applied:
#   - Milestone: First Call
#   - Search: "tech"

Industry,Company Name,Website,Email,Phone,Address,Milestone,Milestone Status,Notes,Created Date,Updated Date
Consulting,Global Tech Services,https://globaltechservices.com,hello@globaltechservices.com,+1-555-0300,"789 Pine Rd, Chicago, IL",first_call,First Call,Technology consulting firm,2025-10-15 10:30:00,2025-10-15 10:30:00

Technology,Acme Tech Corp,https://acmetech.com,contact@acmetech.com,+1-555-0100,"123 Main St, New York, NY",first_call,First Call,Potential client,2025-10-13 14:20:00,2025-10-13 14:20:00
Technology,Tech Startup Co,https://techstartup.co,team@techstartup.co,+1-555-0400,"321 Elm St, Austin, TX",first_call,First Call,Innovative startup,2025-10-16 11:45:00,2025-10-16 11:45:00
```

## Features

### Smart Filtering
- Export respects current page filters
- Search terms are applied to the export
- Milestone filters are honored
- Only visible companies are exported

### Data Integrity
- All dates are in ISO format (YYYY-MM-DD HH:MM:SS)
- Empty fields are exported as blank (not NULL)
- Special characters are properly escaped
- UTF-8 encoding ensures international characters work correctly

### Industry Analytics
The grouped format makes it easy to:
- Analyze company distribution by industry
- Create industry-specific mailing lists
- Generate industry reports in spreadsheet software
- Import into other CRM systems

## Use Cases

### Sales Analytics
```
1. Click "📥 Export CSV" button
2. Select industry: "Technology"
3. Export to CSV
4. Open in Excel/Google Sheets
5. Analyze technology sector performance
```

### Marketing Campaigns
```
1. Filter by milestone: "first_call"
2. Click "📥 Export CSV"
3. Select industry: "Healthcare"
4. Export to CSV
5. Import into email marketing tool
6. Send targeted healthcare industry campaigns
```

### Industry Comparison
```
1. Export "Technology" industry to CSV
2. Export "Manufacturing" industry to CSV
3. Compare company counts and milestones
4. Identify which industries have more successful deals
```

### Reporting
```
1. Click "📥 Export CSV"
2. Select "All Industries"
3. Export to CSV
4. Share with management
5. Grouped view shows market coverage
6. Easy to spot industry gaps
```

## Tips

- **Use Filters First**: Apply filters before exporting to get exactly the data you need
- **Industry Blank Rows**: The blank rows between industries make it easy to separate groups in Excel
- **Date Format**: Dates are exported in a standard format that Excel recognizes
- **Reimport**: The export format is compatible with the CSV upload feature

## Integration with Upload Feature

The export format is compatible with the CSV upload feature:

1. Export companies to CSV
2. Modify the CSV file (add/update companies)
3. Re-upload using the "📤 Upload CSV" button
4. System will update existing companies and create new ones

**Note**: When uploading an exported CSV, you can simplify it to just the columns you need:
- Remove `Created Date` and `Updated Date` columns (system generates these)
- Keep `Milestone` column OR `Milestone Status` column (not both)
- Remove blank separator rows

## Technical Details

### Dashboard Endpoint
```
GET /companies/export-csv/
Query Parameters:
  - industry: Filter by specific industry (or "none" for no industry)
  - milestone: Filter by milestone
  - search: Filter by search term
```

### REST API Endpoint
```
GET /api/companies/export_csv/
Query Parameters:
  - industry: Filter by specific industry
  - milestone: Filter by milestone
  - search: Filter by search term
```

### Performance
- Efficient database query with `.order_by('industry', 'name')`
- Streams response for large datasets
- No pagination required for exports
- Handles thousands of companies efficiently

## Troubleshooting

**Issue**: Export button downloads empty file
- **Solution**: Make sure you have companies in the database

**Issue**: Industries not grouped correctly
- **Solution**: Check that companies have the industry field populated

**Issue**: Special characters look wrong
- **Solution**: Open the CSV with UTF-8 encoding in your spreadsheet software

**Issue**: Dates show as text in Excel
- **Solution**: This is normal - you can format them as dates in Excel if needed

## Future Enhancements

Potential improvements for future versions:
- [ ] Export to Excel format (.xlsx)
- [ ] Export to PDF report format
- [ ] Custom column selection
- [ ] Industry summary statistics in export
- [ ] Scheduled automatic exports
- [ ] Email export to specified recipients
