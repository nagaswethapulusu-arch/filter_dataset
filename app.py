import pandas as pd
import streamlit as st

st.set_page_config(page_title="Filter Dataset Records", page_icon="🔍", layout="wide")
st.title("🔍 Filter Dataset Records with Pandas")
st.caption("Upload a CSV or use the sample Student Performance dataset, then build filters with one or more conditions.")

uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
try:
    df = pd.read_csv(uploaded) if uploaded is not None else pd.read_csv("student_performance.csv")
except Exception as e:
    st.error(f"Could not load the dataset: {e}")
    st.stop()

st.write(f"Total records: **{len(df)}**")

num_cols = df.select_dtypes("number").columns.tolist()
cat_cols = df.select_dtypes(exclude="number").columns.tolist()

st.sidebar.header("Filters")
combine = st.sidebar.radio("Combine conditions with", ["AND (&)", "OR (|)"])
masks, parts = [], []

for col in num_cols:
    lo, hi = float(df[col].min()), float(df[col].max())
    if lo == hi:
        continue
    use = st.sidebar.checkbox(f"Filter {col}", key=f"use_{col}")
    if use:
        a, b = st.sidebar.slider(col, lo, hi, (lo, hi), key=f"s_{col}")
        masks.append((df[col] >= a) & (df[col] <= b))
        parts.append(f"({col} >= {a} & {col} <= {b})")

for col in cat_cols:
    options = df[col].dropna().unique().tolist()
    if len(options) > 15:
        continue
    use = st.sidebar.checkbox(f"Filter {col}", key=f"use_{col}")
    if use:
        chosen = st.sidebar.multiselect(col, options, default=options[:1], key=f"m_{col}")
        masks.append(df[col].isin(chosen))
        parts.append(f"{col}.isin({chosen})")

if masks:
    result_mask = masks[0]
    for m in masks[1:]:
        result_mask = (result_mask & m) if combine.startswith("AND") else (result_mask | m)
    filtered = df[result_mask]
    joiner = " & " if combine.startswith("AND") else " | "
    st.subheader("Condition used")
    st.code("df[" + joiner.join(parts) + "]")
else:
    filtered = df
    st.info("Tick a filter in the sidebar to start filtering.")

c1, c2, c3 = st.columns(3)
c1.metric("Total records", len(df))
c2.metric("Matching records", len(filtered))
c3.metric("Share of data", f"{len(filtered) / len(df) * 100:.0f}%")

st.subheader("Filtered DataFrame")
st.dataframe(filtered, use_container_width=True)
