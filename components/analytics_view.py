"""
Analytics view: KPI cards + auto charts + custom chart builder.
Only shown when at least one tabular file is loaded.
"""

import streamlit as st
import pandas as pd

from utils.analytics import compute_kpis, auto_charts, correlation_heatmap, custom_chart


def render_analytics():
    dataframes: dict = st.session_state.get("dataframes", {})
    if not dataframes:
        st.info("Upload a CSV or Excel file to see analytics here.")
        return

    # File selector
    selected_file = st.selectbox("Select dataset", list(dataframes.keys()))
    df: pd.DataFrame = dataframes[selected_file]

    st.markdown(f"**{selected_file}** — {len(df):,} rows × {len(df.columns)} columns")

    # KPI cards
    kpis = compute_kpis(df)
    if kpis:
        st.markdown("#### Key metrics")
        cols = st.columns(min(len(kpis), 3))
        for i, (col_name, stats) in enumerate(kpis.items()):
            with cols[i % 3]:
                st.metric(
                    label=col_name,
                    value=stats["total"],
                    delta=f"avg {stats['mean']}",
                    help=f"Min: {stats['min']} | Max: {stats['max']}",
                )

    st.divider()

    # Auto charts
    st.markdown("#### Auto-generated charts")
    charts = auto_charts(df)
    if charts:
        chart_cols = st.columns(2)
        for i, fig in enumerate(charts):
            chart_cols[i % 2].plotly_chart(fig, use_container_width=True)
    else:
        st.info("No numeric columns found for charting.")

    # Correlation heatmap
    heatmap = correlation_heatmap(df)
    if heatmap:
        st.divider()
        st.markdown("#### Correlation matrix")
        st.plotly_chart(heatmap, use_container_width=True)

    # Custom chart builder
    st.divider()
    st.markdown("#### Build a custom chart")
    all_cols = df.columns.tolist()
    c1, c2, c3 = st.columns(3)
    x_col = c1.selectbox("X axis", all_cols, key="custom_x")
    y_col = c2.selectbox("Y axis", [c for c in all_cols if c != x_col], key="custom_y")
    chart_type = c3.selectbox("Chart type", ["Bar", "Line", "Scatter", "Area"], key="custom_type")

    if st.button("Generate chart", type="primary"):
        try:
            fig = custom_chart(df, x_col, y_col, chart_type)
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Could not generate chart: {e}")

    # Raw data preview
    st.divider()
    with st.expander("Preview raw data"):
        st.dataframe(df.head(100), use_container_width=True)
