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
def _(conn, mo, olist_customers):
    _df = mo.sql(
        f"""
        SELECT * FROM olist_customers limit 10
        """,
        engine=conn
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


if __name__ == "__main__":
    app.run()
