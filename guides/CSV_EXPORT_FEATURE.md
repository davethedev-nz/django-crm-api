# CSV Export Feature for Companies

## Overview
The Companies page now includes a CSV export feature that allows you to download company data grouped by industry.

## How to Use

### Via Dashboard UI

1. **Navigate to Companies Page**
   - Go to http://127.0.0.1:8000/companies/

2. **Apply Filters (Optional)**
   - Use the search box to filter by name, industry, or email
   - Use the milestone dropdown to filter by sales stage

3. **Export Data**
   - Click the "📥 Export CSV" button at the top right
   - Your browser will download a file named `companies_export.csv`
   - The export includes only the companies visible in your current filtered view

### Via REST API

```bash
GET /api/companies/export_csv/

# With filters
GET /api/companies/export_csv/?milestone=first_call
GET /api/companies/export_csv/?search=technology
```

## Export Format

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
Industry,Company Name,Website,Email,Phone,Address,Milestone,Milestone Status,Notes,Created Date,Updated Date
Consulting,Global Services Ltd,https://globalservices.com,hello@globalservices.com,+1-555-0300,"789 Pine Rd, Chicago, IL",email_sent,Email sent,Sent proposal on 2025-10-15,2025-10-15 10:30:00,2025-10-15 10:30:00

Manufacturing,Widget Inc,https://widget.com,info@widget.com,+1-555-0200,"456 Oak Ave, San Francisco, CA",first_call,First Call,Initial discussion held,2025-10-14 09:15:00,2025-10-14 09:15:00

Technology,Acme Corporation,https://acme.com,contact@acme.com,+1-555-0100,"123 Main St, New York, NY",not_contacted,Not yet contacted,Potential client,2025-10-13 14:20:00,2025-10-13 14:20:00
Technology,Tech Startup Co,https://techstartup.co,team@techstartup.co,+1-555-0400,"321 Elm St, Austin, TX",meeting_arranged,Meeting arranged,Meeting next week,2025-10-16 11:45:00,2025-10-16 11:45:00
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
1. Filter by milestone: "successful"
2. Export to CSV
3. Open in Excel/Google Sheets
4. Create pivot tables by industry
5. Identify highest-performing industries
```

### Marketing Campaigns
```
1. Filter by industry: "Technology"
2. Export to CSV
3. Import into email marketing tool
4. Send targeted industry-specific campaigns
```

### Reporting
```
1. Export all companies (no filters)
2. Share with management
3. Grouped view shows market coverage
4. Easy to spot industry gaps
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
  - milestone: Filter by milestone
  - search: Filter by search term
```

### REST API Endpoint
```
GET /api/companies/export_csv/
Query Parameters:
  - milestone: Filter by milestone
  - search: Filter by search term
  - industry: Filter by industry
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
