def generate_sales_summary(df):
    summary = ""

    # Total sales by region
    region_sales = df.groupby("Region")["Sales"].sum()
    summary += "Total Sales by Region:\n"
    summary += region_sales.to_string()
    summary += "\n\n"

    # Total profit by category
    category_profit = df.groupby("Category")["Profit"].sum()
    summary += "Total Profit by Category:\n"
    summary += category_profit.to_string()
    summary += "\n\n"

    # Yearly sales trend
    df['Year'] = df['Order Date'].dt.year
    yearly_sales = df.groupby("Year")["Sales"].sum()
    summary += "Yearly Sales Trend:\n"
    summary += yearly_sales.to_string()

    return summary
