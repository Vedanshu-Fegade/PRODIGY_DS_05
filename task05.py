"""Task 05 — analyse the official Kaggle US Accidents dataset in chunks.

Download US_Accidents_March23.csv from:
https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents
and place it in this task's data directory before running.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "US_Accidents_March23.csv"
OUT = ROOT / "outputs"
USECOLS = ["Severity", "Start_Time", "Start_Lat", "Start_Lng", "Weather_Condition", "Junction", "Crossing", "Traffic_Signal"]


def main() -> None:
    if not DATA.exists():
        raise FileNotFoundError(
            f"Required dataset not found: {DATA}\nDownload US_Accidents_March23.csv from Kaggle and place it there."
        )
    sns.set_theme(style="whitegrid")
    OUT.mkdir(exist_ok=True)
    hour_counts = pd.Series(dtype="int64")
    weather_counts = pd.Series(dtype="int64")
    road_severity = pd.DataFrame()
    points: list[pd.DataFrame] = []
    rows = 0
    for chunk in pd.read_csv(DATA, usecols=USECOLS, chunksize=200_000, low_memory=False):
        rows += len(chunk)
        starts = pd.to_datetime(chunk["Start_Time"], errors="coerce")
        hour_counts = hour_counts.add(starts.dt.hour.value_counts(), fill_value=0)
        weather_counts = weather_counts.add(chunk["Weather_Condition"].fillna("Unknown").value_counts(), fill_value=0)
        road = chunk.melt(id_vars="Severity", value_vars=["Junction", "Crossing", "Traffic_Signal"],
                          var_name="road_context", value_name="present")
        road = road[road["present"].fillna(False).astype(bool)]
        part = pd.crosstab(road["road_context"], road["Severity"])
        road_severity = road_severity.add(part, fill_value=0)
        valid_points = chunk.dropna(subset=["Start_Lat", "Start_Lng", "Severity"])
        points.append(valid_points.sample(n=min(2_000, len(valid_points)), random_state=42))

    sampled_points = pd.concat(points, ignore_index=True)
    if len(sampled_points) > 50_000:
        sampled_points = sampled_points.sample(50_000, random_state=42)
    hour_counts = hour_counts.reindex(range(24), fill_value=0).sort_index()
    weather_top = weather_counts.nlargest(10).sort_values()

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].bar(hour_counts.index, hour_counts.values, color="#4C78A8")
    axes[0].set(title="Accidents by Hour of Day", xlabel="Hour", ylabel="Accident records", xticks=range(0, 24, 2))
    axes[1].barh(weather_top.index, weather_top.values, color="#72B7B2")
    axes[1].set(title="Ten Most Common Weather Conditions", xlabel="Accident records", ylabel="")
    fig.tight_layout()
    fig.savefig(OUT / "time_and_weather_patterns.png", dpi=180)
    plt.close(fig)

    plt.figure(figsize=(7, 4))
    sns.heatmap(road_severity.sort_index().fillna(0).astype(int), annot=True, fmt="d", cmap="YlOrRd")
    plt.title("Accident Severity by Road Context")
    plt.xlabel("Severity")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(OUT / "road_context_severity.png", dpi=180)
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.hexbin(sampled_points["Start_Lng"], sampled_points["Start_Lat"], gridsize=70,
               mincnt=1, cmap="magma")
    plt.colorbar(label="Sampled accident records per hexagon")
    plt.title("US Accident Hotspots — Geographic Density (Random Sample)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.tight_layout()
    plt.savefig(OUT / "accident_hotspots.png", dpi=180)
    plt.close()

    peak = int(hour_counts.idxmax())
    (OUT / "findings.txt").write_text(
        f"Records processed: {rows:,}\nPeak accident-record hour: {peak:02d}:00 ({int(hour_counts.loc[peak]):,} records).\n"
        f"Most common recorded weather condition: {weather_counts.idxmax()} ({int(weather_counts.max()):,} records).\n"
        "The hotspot plot shows reported-record density, not risk adjusted for traffic volume or population.\n",
        encoding="utf-8",
    )
    print(f"Task 05 complete — processed {rows:,} real records; figures saved in {OUT}")


if __name__ == "__main__":
    main()
