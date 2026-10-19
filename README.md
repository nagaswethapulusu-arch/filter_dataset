# 🔍 Filter Dataset Records (Pandas)

Filter records from a dataset using one or more conditions with Pandas, with examples, filtered DataFrames and a short explanation of each condition.

## Objective
Learn how to retrieve relevant records from a dataset.

## Tools
- Python
- Pandas
- Jupyter Notebook
- Streamlit (for the deployed demo)

## Dataset
Sample Student Performance dataset (`student_performance.csv`, 50 rows, 7 columns):
`student_id, gender, hours_studied, attendance_pct, previous_score, final_score, result`
The notebook creates this file itself, so no download is needed.

## Project Structure
```
├── Filter_Dataset_Records.ipynb   # Main notebook
├── student_performance.csv        # Dataset
├── app.py                         # Streamlit web app
├── requirements.txt               # Dependencies
└── README.md
```

## Filtering Cheat Sheet

| Goal | Code |
|---|---|
| Single condition | `df[df['final_score'] > 70]` |
| Text condition | `df[df['result'] == 'Fail']` |
| AND | `df[(df['gender'] == 'Female') & (df['hours_studied'] >= 5)]` |
| OR | `df[(df['final_score'] > 60) \| (df['hours_studied'] > 6)]` |
| NOT | `df[~(df['result'] == 'Pass')]` |
| In a list | `df[df['student_id'].isin([1, 5, 10])]` |
| In a range | `df[df['final_score'].between(55, 65)]` |
| Query string | `df.query("final_score > 65 and attendance_pct >= 85")` |

**Always put each condition in parentheses** when using `&` or `|`, because `&` and `|` are evaluated before `>` or `==`.

## Run Locally
```bash
git clone https://github.com/<your-username>/pandas-filter-records.git
cd pandas-filter-records
pip install -r requirements.txt

jupyter notebook Filter_Dataset_Records.ipynb   # notebook
streamlit run app.py                            # web app
```

## Deploy (Streamlit Community Cloud)
1. Push this repo to GitHub (include `student_performance.csv`).
2. Go to share.streamlit.io and click **New app**.
3. Select the repo, branch `main`, main file `app.py`.
4. Click **Deploy**.

## Interview Questions
- **How do you filter rows in Pandas?** Use a Boolean condition: `df[df['col'] > value]`.
- **How do you combine multiple conditions?** Use `&` (and), `|` (or), `~` (not), with each condition in parentheses.
- **Why are parentheses important?** `&` and `|` have higher precedence than comparison operators, so without parentheses Pandas raises an error or returns the wrong rows.

## Author
Swetha, AI & ML Track, Veda Technology
