import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import duckdb
    import marimo as mo
    import sqlglot

    return duckdb, mo


@app.cell
def _(duckdb):
    conn = duckdb.connect(str("Olist_dataset.duckdb"))
    return (conn,)


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM information_schema.tables
        """,
        engine=conn
    )
    return


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        create table if not exists Olist_customers as select * from 'olist_customers_dataset.csv';
        """,
        engine=conn
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        create table if not exists Olist_geolocation as select * from 'olist_geolocation_dataset.csv';
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        create table if not exists Olist_order_items as select * from 'olist_order_items_dataset.csv';
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        create table if not exists Olist_order_payments as select * from 'olist_order_payments_dataset.csv';
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        create table if not exists Olist_order_reviews as select * from 'olist_order_reviews_dataset.csv';
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        create table if not exists Olist_orders_dataset as select * from 'olist_orders_dataset.csv';
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        create table if not exists Olist_products as select * from 'olist_products_dataset.csv';
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        create table if not exists Olist_sellers as select * from 'olist_sellers_dataset.csv';
        """
    )
    return


@app.cell
def _(mo, olist_sellers):
    _df = mo.sql(
        f"""
        SELECT * FROM Olist_sellers limit 20
        """
    )
    return


if __name__ == "__main__":
    app.run()
