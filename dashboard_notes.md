

## Dashboard Questions Answered
1. How many customers do we have, and what's our average spend and satisfaction?
2. Which segment has the highest spending vs overall average?
3. How does satisfaction vary by segment?
4. How does spending vary by city?
5. How are customer signups trending over time?

## Filters Built
- Segment filter (All / Corporate / Retail / SME)
- City filter (All + 7 cities)
- Live customer count shown after filtering

## Data Freshness
- Loaded from customer_data_cleaned.csv
- Timestamp shown at top of dashboard on every load

## User Test Note
Tested the dashboard myself by opening it in the browser after running streamlit. 
The three KPI tiles loaded correctly showing total customers, average purchase amount 
and average satisfaction score. When I changed the segment filter from "All" to 
"Corporate", all the numbers and charts updated instantly which confirmed the 
filters are working correctly.

## Hover Definitions
- Total Customers: shows note about customer_id reuse issue from Task 2
- Avg Purchase Amount: shows definition on hover
- Avg Satisfaction Score: shows baseline (2.89) for comparison

## Known Limitations
- Data is a static CSV snapshot, not a live database connection
- Filters apply to all tiles simultaneously — no tile-level independent filtering
- customer_id reuse issue (Task 2) means Total Customers is row-count based, not unique-ID based