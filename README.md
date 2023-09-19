# Goalkeeper Performance Analysis in Serie A

## Abstract

This report presents an analysis to ascertain the correlation between various goalkeeper performance metrics and their respective team's position in the Serie A standings. Goalkeepers, intrinsically interlinked with team dynamics, are dissected to isolate their distinct influence. The primary objective is to determine the causal influence of a goalkeeper's performance metrics on their team's league position.

## Data Collection

### Sources:
- **FBref:** Utilized for extracting detailed metrics encompassing goalkeeper performances throughout the Serie A season.
- **Official Serie A League Charts:** Provides the end-of-season standings for Serie A teams.

### Methodology:
Data from FBref, enriched with performance metrics, was merged with the league standings data from the official Serie A charts to facilitate a multifaceted analysis.

```python
import pandas as pd

# Read the data from the Excel file
df = pd.read_excel('GoalkeepingDataExcel.xlsx')
```

## Metrics and Statistical Significance

### Expected Goals (xG) vs. Post-shot Expected Goals (PsxG):

- **Expected Goals (xG):** Represents the probability that a shot will result in a goal based on several variables such as shot angle, type of pass leading to it, distance from goal, etc.
- **Post-shot Expected Goals (PsxG):** An extension of xG, taking into account the shot's placement, thus factoring in the goalkeeper's potential influence on preventing the goal.

Given the above, PsxG is an optimal metric to gauge a goalkeeper's influence as it filters out the quality of shots, focusing only on shot placement, which directly pertains to the goalkeeper's intervention.

### Addressing Confounders

To better isolate a goalkeeper's performance, it's imperative to consider metrics that are less influenced by the broader team's dynamics. Metrics like PsxG and Save Percentage serve this purpose since they hone in on a goalkeeper's response to shots, regardless of the defensive context. By assigning more significant weightage to PsxG and Save Percentage in our analysis, we prioritize metrics that epitomize a goalkeeper's isolated impact.

```python
# Weighting system
df['total_score'] = (df['NPGA_norm'] * 0.15 +
                     df['NPSP_norm'] * 0.25 +
                     df['CleanSheets_norm'] * 0.15 +
                     df['PSxG_norm'] * 0.10 +
                     df['PSxG_GA_norm'] * 0.35)
```

### Normalization 

Normalizing data is crucial for bringing diverse metrics onto a common scale, allowing for a more balanced and equitable comparison. The normalization equations used in this analysis are:

- For metrics where a higher value is better:
    \( \text{Normalized Value} = \frac{\text{Value} - \text{Min Value}}{\text{Max Value} - \text{Min Value}} \)

- For metrics where a lower value is better:
    \( \text{Normalized Value} = 1 - \frac{\text{Value} - \text{Min Value}}{\text{Max Value} - \text{Min Value}} \)

```python
def normalize_higher_is_better(column):
    return (column - column.min()) / (column.max() - column.min())

def normalize_lower_is_better(column):
    return 1 - (column - column.min()) / (column.max() - column.min())
```

## Conclusion

The multifaceted metrics chosen and their respective weightages aim to capture a holistic view of a goalkeeper's influence. By analyzing these metrics and juxtaposing them with Serie A standings, we sought to discern patterns that could elucidate the often nebulous realm of goalkeeper analytics. This study provides a robust foundation for more granular analyses in the future and emphasizes the importance of a nuanced approach to quantifying player performances in team sports.
