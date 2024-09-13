from tabulate import tabulate

from metrics_query import get_top_cities_by_sales, get_top_countries_by_sales, get_out_of_stock_products, get_inventory_levels, get_payment_metrics, get_order_metrics, get_this_month_top_selling_products, get_revenue_by_city, get_total_revenue, get_revenue_by_product

def tabulate_sql_data(data):
    if len(data) <= 0:
        print("No data found.")
        return

    header = data[0].keys()
    rows =  [x.values() for x in data]
    print(tabulate(rows, header))

def print_total_revenue():
    tabulate_sql_data(get_total_revenue())

def print_revenue_by_city():
    tabulate_sql_data(get_revenue_by_city())

def print_revenue_by_product():
    tabulate_sql_data(get_revenue_by_product())

def print_this_month_top_selling_products():
    tabulate_sql_data(get_this_month_top_selling_products())

def print_order_metrics():
    tabulate_sql_data(get_order_metrics())

def print_payment_metrics():
    tabulate_sql_data(get_payment_metrics())

def print_inventory_levels():
    tabulate_sql_data(get_inventory_levels())

def print_out_of_stock_products():
    tabulate_sql_data(get_out_of_stock_products())

def print_top_cities_by_sales():
    tabulate_sql_data(get_top_cities_by_sales())

def print_top_countries_by_sales():
    tabulate_sql_data(get_top_countries_by_sales())
