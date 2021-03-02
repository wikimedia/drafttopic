# Model tuning report
- Revscoring version: 2.9.2
- Features: drafttopic.feature_lists.zhwiki.articletopic
- Date: 2021-03-01T20:38:55.235072
- Observations: 62675
- Labels: ["Culture.Biography.Biography*", "Culture.Biography.Women", "Culture.Food and drink", "Culture.Internet culture", "Culture.Linguistics", "Culture.Literature", "Culture.Media.Books", "Culture.Media.Entertainment", "Culture.Media.Films", "Culture.Media.Media*", "Culture.Media.Music", "Culture.Media.Radio", "Culture.Media.Software", "Culture.Media.Television", "Culture.Media.Video games", "Culture.Performing arts", "Culture.Philosophy and religion", "Culture.Sports", "Culture.Visual arts.Architecture", "Culture.Visual arts.Comics and Anime", "Culture.Visual arts.Fashion", "Culture.Visual arts.Visual arts*", "Geography.Geographical", "Geography.Regions.Africa.Africa*", "Geography.Regions.Africa.Central Africa", "Geography.Regions.Africa.Eastern Africa", "Geography.Regions.Africa.Northern Africa", "Geography.Regions.Africa.Southern Africa", "Geography.Regions.Africa.Western Africa", "Geography.Regions.Americas.Central America", "Geography.Regions.Americas.North America", "Geography.Regions.Americas.South America", "Geography.Regions.Asia.Asia*", "Geography.Regions.Asia.Central Asia", "Geography.Regions.Asia.East Asia", "Geography.Regions.Asia.North Asia", "Geography.Regions.Asia.South Asia", "Geography.Regions.Asia.Southeast Asia", "Geography.Regions.Asia.West Asia", "Geography.Regions.Europe.Eastern Europe", "Geography.Regions.Europe.Europe*", "Geography.Regions.Europe.Northern Europe", "Geography.Regions.Europe.Southern Europe", "Geography.Regions.Europe.Western Europe", "Geography.Regions.Oceania", "History and Society.Business and economics", "History and Society.Education", "History and Society.History", "History and Society.Military and warfare", "History and Society.Politics and government", "History and Society.Society", "History and Society.Transportation", "STEM.Biology", "STEM.Chemistry", "STEM.Computing", "STEM.Earth and environment", "STEM.Engineering", "STEM.Libraries & Information", "STEM.Mathematics", "STEM.Medicine & Health", "STEM.Physics", "STEM.STEM*", "STEM.Space", "STEM.Technology"]
- Statistic: pr_auc.macro (maximize)
- Folds: 3

# Top scoring configurations
| model            |   pr_auc.macro | params                                                                |
|:-----------------|---------------:|:----------------------------------------------------------------------|
| GradientBoosting |         0.5652 | max_features="log2", learning_rate=0.1, max_depth=5, n_estimators=50  |
| GradientBoosting |         0.5578 | max_features="log2", learning_rate=0.1, max_depth=4, n_estimators=50  |
| GradientBoosting |         0.5348 | max_features="log2", learning_rate=0.1, max_depth=3, n_estimators=50  |
| GradientBoosting |         0.5216 | max_features="log2", learning_rate=0.01, max_depth=5, n_estimators=50 |
| GradientBoosting |         0.487  | max_features="log2", learning_rate=0.01, max_depth=4, n_estimators=50 |
| GradientBoosting |         0.445  | max_features="log2", learning_rate=0.01, max_depth=3, n_estimators=50 |

# Models
## GradientBoosting
|   pr_auc.macro | params                                                                |
|---------------:|:----------------------------------------------------------------------|
|         0.5652 | max_features="log2", learning_rate=0.1, max_depth=5, n_estimators=50  |
|         0.5578 | max_features="log2", learning_rate=0.1, max_depth=4, n_estimators=50  |
|         0.5348 | max_features="log2", learning_rate=0.1, max_depth=3, n_estimators=50  |
|         0.5216 | max_features="log2", learning_rate=0.01, max_depth=5, n_estimators=50 |
|         0.487  | max_features="log2", learning_rate=0.01, max_depth=4, n_estimators=50 |
|         0.445  | max_features="log2", learning_rate=0.01, max_depth=3, n_estimators=50 |

