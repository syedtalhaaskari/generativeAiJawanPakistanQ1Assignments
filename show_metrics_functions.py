import pymysql
from tabulate import tabulate

from metrics_query import get_top_cities_by_sales, get_top_countries_by_sales, get_out_of_stock_products, get_inventory_levels, get_payment_metrics, get_order_metrics, get_this_month_top_selling_products, get_revenue_by_city, get_total_revenue, get_revenue_by_product
import db

db_conn = db.mysqlconnect()

def tabulate_sql_data(data):
    header = data[0].keys()
    rows =  [x.values() for x in data]
    print(tabulate(rows, header))

def print_total_revenue():
    tabulate_sql_data(get_total_revenue(db_conn))

def print_revenue_by_city():
    tabulate_sql_data(get_revenue_by_city(db_conn))

def print_revenue_by_product():
    tabulate_sql_data(get_revenue_by_product(db_conn))

def print_this_month_top_selling_products():
    tabulate_sql_data(get_this_month_top_selling_products(db_conn))

def print_order_metrics():
    tabulate_sql_data(get_order_metrics(db_conn))

def print_payment_metrics():
    tabulate_sql_data(get_payment_metrics(db_conn))

def print_inventory_levels():
    tabulate_sql_data(get_inventory_levels(db_conn))

def print_out_of_stock_products():
    tabulate_sql_data(get_out_of_stock_products(db_conn))

def print_top_cities_by_sales():
    tabulate_sql_data(get_top_cities_by_sales(db_conn))

def print_top_countries_by_sales():
    tabulate_sql_data(get_top_countries_by_sales(db_conn))

