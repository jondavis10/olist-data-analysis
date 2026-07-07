import marimo

__generated_with = "0.23.9"
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
        SELECT table_catalog, table_name, FROM information_schema.tables
        """,
        engine=conn
    )
    return


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        SELECT table_catalog, table_name, column_name, data_type, FROM information_schema.columns WHERE table_name = 'Olist_customers'
        """,
        engine=conn
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    "\"7-7-2026"\"
    table "Olist_customers" unique key customer_id links to table "Olist_orders_dataset" customer_id.
        -explore data and create Entity relationship diagram (ERD)
        -
    """)
    return


@app.cell
def _(conn, mo, olist_customers):
    _df = mo.sql(
        f"""
        SELECT customer_id, customer_unique_id FROM Olist_customers LIMIT 25
        """,
        engine=conn
    )
    return


@app.cell
def _(conn, mo, olist_customers):
    _df = mo.sql(
        f"""
        SELECT
            COUNT(DISTINCT customer_id) as distinct_customer_id,
            COUNT(DISTINCT customer_unique_id) as distinct_customer_unique_id,
            COUNT(*) as total
        FROM
        	Olist_customers 
            ;
        """,
        engine=conn
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        SELECT table_catalog, table_name, column_name, data_type, FROM information_schema.columns WHERE table_name = 'Olist_orders_dataset'
        """,
        engine=conn
    )
    return


if __name__ == "__main__":
    app.run()
