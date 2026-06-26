"""
Analytics utilities: generate KPI cards and Plotly charts from a DataFrame.
Called by the Streamlit components when a tabular file is loaded.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import Optional


CHART_TEMPLATE = "plotly_white"
COLOR_SEQUENCE = ["#0F6E56", "#1D9E75", "#9FE1CB", "#3B8BD4", "#BA7517", "#D85A30"]


def compute_kpis(df: pd.DataFrame) -> dict:
    """Return a dict of KPI name -> (value_str, delta_str or None)."""
    kpis = {}
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    for col in numeric_cols[:6]:  # show max 6 KPIs
        total = df[col].sum()
        mean = df[col].mean()
        kpis[col] = {
            "total": f"{total:,.2f}",
            "mean": f"{mean:,.2f}",
            "min": f"{df[col].min():,.2f}",
            "max": f"{df[col].max():,.2f}",
        }
    return kpis


def auto_charts(df: pd.DataFrame) -> list[go.Figure]:
    """Auto-generate up to 4 relevant charts from the DataFrame."""
    charts = []
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    # 1. Bar chart: first categorical vs first numeric
    if categorical_cols and numeric_cols:
        cat_col = categorical_cols[0]
        num_col = numeric_cols[0]
        agg = df.groupby(cat_col)[num_col].sum().reset_index().sort_values(num_col, ascending=False).head(15)
        fig = px.bar(
            agg, x=cat_col, y=num_col,
            title=f"{num_col} by {cat_col}",
            color=cat_col,
            color_discrete_sequence=COLOR_SEQUENCE,
            template=CHART_TEMPLATE,
        )
        fig.update_layout(showlegend=False)
        charts.append(fig)

    # 2. Line chart: if there's a date/time column
    date_col = _detect_date_col(df)
    if date_col and numeric_cols:
        df_copy = df.copy()
        df_copy[date_col] = pd.to_datetime(df_copy[date_col], errors="coerce")
        df_copy = df_copy.dropna(subset=[date_col]).sort_values(date_col)
        num_col = numeric_cols[0]
        fig = px.line(
            df_copy, x=date_col, y=num_col,
            title=f"{num_col} over time",
            template=CHART_TEMPLATE,
            color_discrete_sequence=COLOR_SEQUENCE,
        )
        charts.append(fig)

    # 3. Histogram of first numeric
    if numeric_cols:
        fig = px.histogram(
            df, x=numeric_cols[0],
            title=f"Distribution of {numeric_cols[0]}",
            nbins=30,
            template=CHART_TEMPLATE,
            color_discrete_sequence=COLOR_SEQUENCE,
        )
        charts.append(fig)

    # 4. Scatter: first two numerics
    if len(numeric_cols) >= 2:
        fig = px.scatter(
            df, x=numeric_cols[0], y=numeric_cols[1],
            title=f"{numeric_cols[0]} vs {numeric_cols[1]}",
            template=CHART_TEMPLATE,
            color=categorical_cols[0] if categorical_cols else None,
            color_discrete_sequence=COLOR_SEQUENCE,
            opacity=0.7,
        )
        charts.append(fig)

    return charts


def correlation_heatmap(df: pd.DataFrame) -> Optional[go.Figure]:
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.shape[1] < 2:
        return None
    corr = numeric_df.corr()
    fig = go.Figure(data=go.Heatmap(
        z=corr.values,
        x=corr.columns.tolist(),
        y=corr.columns.tolist(),
        colorscale="Teal",
        zmid=0,
    ))
    fig.update_layout(title="Correlation Matrix", template=CHART_TEMPLATE)
    return fig


def custom_chart(df: pd.DataFrame, x_col: str, y_col: str, chart_type: str) -> go.Figure:
    """Build a user-specified chart."""
    kwargs = dict(x=df[x_col], y=df[y_col], template=CHART_TEMPLATE,
                  color_discrete_sequence=COLOR_SEQUENCE)
    if chart_type == "Bar":
        return px.bar(df, x=x_col, y=y_col, title=f"{y_col} by {x_col}",
                      template=CHART_TEMPLATE, color_discrete_sequence=COLOR_SEQUENCE)
    elif chart_type == "Line":
        return px.line(df, x=x_col, y=y_col, title=f"{y_col} over {x_col}",
                       template=CHART_TEMPLATE, color_discrete_sequence=COLOR_SEQUENCE)
    elif chart_type == "Scatter":
        return px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}",
                          template=CHART_TEMPLATE, color_discrete_sequence=COLOR_SEQUENCE, opacity=0.7)
    elif chart_type == "Area":
        return px.area(df, x=x_col, y=y_col, title=f"{y_col} over {x_col}",
                       template=CHART_TEMPLATE, color_discrete_sequence=COLOR_SEQUENCE)
    else:
        return px.bar(df, x=x_col, y=y_col, title=f"{y_col} by {x_col}",
                      template=CHART_TEMPLATE, color_discrete_sequence=COLOR_SEQUENCE)


def _detect_date_col(df: pd.DataFrame) -> Optional[str]:
    for col in df.columns:
        if any(kw in col.lower() for kw in ["date", "time", "month", "year", "day"]):
            return col
    return None
