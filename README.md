# Analyzing the Relationship Between Goalkeeper Skill Level/Performance & Team League Position in Serie A Football: 22/23 Season

## Abstract

This report presents an analysis to ascertain the correlation between various goalkeeper performance metrics and their respective team's position in the Serie A standings. Goalkeepers, intrinsically interlinked with team dynamics, are dissected to isolate their distinct influence. The primary objective is to determine the causal influence of a goalkeeper's performance metrics on their team's league position. Although similar to my assignment 1, I carefully selected this topic for this specific assignment. The reason behind this choice being the great amount of confounders that are present in the analysis of goalkeeper skill. Analysts around the world struggle to understand which keepers really are the best in the world, and which simply have a good defence in front of them, or which simply have unskilled opponents. The reality of the situation is, there are so many confounders, its hard to come to a definitive conclusion without statistics. In this project, I do my best to isolate goalkeepers' performances from the rest of their team, using specifically chosen statistics.

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

### Statistics Taken Into Consideration
- **Non Penalty Goals Allowed (NPGa):** Simply the total number of non penalty goals allowed by the goalkeeper.
- **Non Penalty Save Percentage (NPSpct):** The percentage of non-penalty shots taken on a goalkeeper that were saved.
- **Clean Sheets** The amount of matches played in which the team did not concede a single goal (the total number of matches played for each team were 38).
- **Expected Goals (xG):** Represents the probability that a shot will result in a goal based on several variables such as shot angle, type of pass leading to it, distance from goal, etc. This value is derived from decades of film data that shows the results of previous shots taken from similar positions
- **Post-shot Expected Goals (PsxG):** An extension of xG, taking into account the shot's placement, thus factoring in the goalkeeper's potential influence on preventing the goal.
  
### Important Context Regarding Expected Goals (xG) vs. Post-shot Expected Goals (PsxG):
Given the above, PsxG is an optimal metric to gauge a goalkeeper's influence as it filters out the quality of shots, focusing only on shot placement, which directly pertains to the goalkeeper's intervention.

As such, a very important, and final data point can be calculated:
- **Post-shot Expected Goals - Goals Allowed ):** Simply the difference between PsxG and GA. This value essentially tells us how skilled (or lucky) a keeper is in stopping shots that are rated highly to go in.

### Analysis & Addressing Data Confounders
The plan for analysis is to create a ranking system of each team's goalkeeping statistics, ranking them from 1-20, and comparing that to the final league table.

To better isolate a goalkeeper's performance, it's imperative to consider metrics that are less influenced by the broader team's dynamics. Metrics like PsxG - GA, PSxG, and Save Percentage serve this purpose since they hone in on a goalkeeper's response to shots, regardless of the defensive context. By assigning more significant weightage to PsxG and Save Percentage in our analysis, we prioritize metrics that epitomize a goalkeeper's isolated impact.

```python
# Weighting system
df['total_score'] = (df['NPGA_norm'] * 0.15 +
                     df['NPSP_norm'] * 0.25 +
                     df['CleanSheets_norm'] * 0.15 +
                     df['PSxG_norm'] * 0.10 +
                     df['PSxG_GA_norm'] * 0.35)
```

### Normalization 

Normalizing data is crucial for bringing diverse metrics onto a common scale, allowing for a more balanced and equitable comparison. Otherwise, the above equation makes no sense! The normalization equations used in this analysis are:

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


### Addressing Football Confounders
Although in this project we attempted to do our best in tackling the problem of isolating a goalkeeper's performance rating from his team's, there were certain factors that could not be accounted for. For instance, we only had access to team data - not player data. This meant that certain teams may have played with multiple goalkeepers in a season for a variety of resasons, but this would have thrown off our ratings, as different goalkeepers have different skill levels. Moreover, football is a chaotic sport. There are plenty of situations leading to goals that are totally random - nothing a keeper could do, regardless of his skill level. As such, this will certainly affect the validity of our data. 

More specifically, Mike Maignan, who is considered to be one of the best goalkeepers in the world, plays for Milan. Yet Milan finished close to the bottom in the goalkeeper rankings. The cause: Maignan only played about 50% of games in the 22/23 season analyzed, due to injury.

### Colliders in our Analysis:

Given the interconnected nature of football metrics, it's plausible to encounter colliders. For instance, let's consider a team's defensive strategy and a goalkeeper's save percentage. Both of these factors might influence the number of clean sheets a team achieves in a season. If we were to control for clean sheets (the collider) while analyzing the relationship between defensive strategy and save percentage, we could inadvertently introduce bias.

In our study, we  selected metrics to minimize the risk of introducing colliders. By applying more weight to certain metrics to isolate a goalkeeper's performance, such as PsxG and Save Percentage, rather than Clean Sheets, we aimed to mitigate the risk of confounding due to colliders.



## Results and Discussion

### Correlation Analysis:

Our primary quantitative finding was a correlation value of \(-0.70\) between goalkeeper rankings and final league position. This negative correlation suggests that as the goalkeeper ranking improves (with a lower rank being better), the final league position also improves (with a lower position indicating a higher league standing). Such a strong negative correlation underscores the pivotal role of a goalkeeper in determining the fate of a team in the league. While correlation doesn't imply causation, this significant relationship suggests that teams with better-ranked goalkeepers tend to finish higher in the league standings.

### Scatterplot and Line of Best Fit:

![ScatterPlotGoalieRankings](https://github.com/raphk33/Goalkeeper-Performance-League-Performance/assets/144087440/7aaa4d7d-9131-4f3c-a9b9-490e0ab86993)

The scatterplot offers a visual representation of individual data points, showcasing the relationship between two quantitative variables - in this case, goalkeeper ranking and final league position. By visualizing these data points, one can discern patterns or trends in the data.

The line of best fit, often a linear regression line, provides a summarized trend of the data. In our analysis, this line serves to highlight the general direction of the relationship between our two variables. The negative slope of our line corroborates the negative correlation value, reinforcing the inverse relationship between goalkeeper ranking and league position.

### Distribution of Goalkeeper Rankings:

To understand the distribution of goalkeeper rankings, we visualized the data using a distribution plot. This plot provides insights into the frequency and spread of the rankings across goalkeepers in the Serie A league. Specifically, it indicates:

- **Central Tendency:** Where the majority of goalkeepers lie in terms of ranking.
- **Spread:** How wide the range of rankings is, suggesting the level of parity or disparity among goalkeepers.
- **Outliers:** Any extreme values that stand out from the bulk of the distribution.

Our distribution plot suggested certain nuances about the goalkeepers' performance metrics. It allows for both a macro (overall distribution shape) and micro (specific peaks or troughs) understanding of how goalkeepers compared with each other.

In conclusion, our results, both quantitative and visual, bring forth compelling insights about the importance of goalkeeping performance in Serie A. Future analyses might delve deeper into individual metrics, dissect specific matches, or even compare across different leagues to generalize or challenge our findings.

## Operational Implications 

The findings of this analysis have direct implications for football club management, particularly in their strategic and operational decisions. Here's a breakdown of the potential impact:

1. **Recruitment and Investment:** The strong correlation between goalkeeper performance and league standings suggests that investments in high-caliber goalkeepers can have a tangible impact on a club's success. Clubs might consider allocating a larger portion of their budget for scouting, recruiting, or retaining elite goalkeepers, acknowledging the substantial influence they wield on match outcomes.

2. **Training and Development:** Identifying areas where a goalkeeper excels or needs improvement is pivotal. Regular assessments, using metrics such as those analyzed in this study, can guide personalized training regimes. Emphasizing consistent performance on the key metrics identified can ensure goalkeepers remain at the pinnacle of their capabilities.

3. **Tactical Adjustments:** A strong goalkeeper can allow a team to adopt more aggressive outfield tactics, knowing there's reliability at the back. Conversely, if a goalkeeper's performance metrics dip, a more conservative approach might be warranted. 

4. **Stakeholder Communication:** For club stakeholders, be it fans, sponsors, or board members, understanding the performance metrics and their implications can foster informed discussions. It paints a clearer picture of the team's strengths and areas of opportunity, guiding future expectations.


## Conclusion

In conclusion, this analysis underscores the significance of goalkeeping in Serie A's competitive landscape. While the metrics and their interplay with league outcomes are intricate, the overarching takeaway is clear: goalkeeping performance is pivotal. As football continues to evolve, with matches often won or lost on fine margins, clubs would be well-served to recognize and act upon the insights gleaned from such data-driven analyses. This study provides a robust foundation for more granular analyses in the future and emphasizes the importance of a nuanced approach to quantifying player performances in team sports.





