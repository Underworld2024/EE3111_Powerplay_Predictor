from io import StringIO
import pandas as pd

def predict(match_data, ball_by_ball_data):
    df = pd.read_csv(StringIO(ball_by_ball_data))
    df["runs_off_bat"] = pd.to_numeric(df["runs_off_bat"], errors="coerce").fillna(0)
    df["extras"] = pd.to_numeric(df["extras"], errors="coerce").fillna(0)
    runs = int((df["runs_off_bat"] + df["extras"]).sum())
    fours = (df["runs_off_bat"] == 4).sum()
    sixes = (df["runs_off_bat"] == 6).sum()
    wickets = df['wicket_type'].count()
    year = 2026

    return -981.520895 + 0.499013*year + 1.079282*runs + -1.822510*wickets + -0.338091*fours + 0.289348*sixes

