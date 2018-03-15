# Model tuning report
- Revscoring version: 2.2.0
- Features: drafttopic.feature_lists.word2vec.drafttopic
- Date: 2018-03-15T03:12:16.771318
- Observations: 93392
- Labels: ["STEM.Time", "STEM.Physics", "STEM.Space", "STEM.Mathematics", "Culture.Crafts and hobbies", "History_And_Society.Transportation", "Geography.Maps", "Culture.Internet culture", "History_And_Society.Business and economics", "Assistance.Article improvement and grading", "STEM.Biology", "STEM.Science", "STEM.Technology", "Geography.Countries", "Culture.Media", "History_And_Society.History and society", "Assistance.Contents systems", "Culture.Broadcasting", "Assistance.Maintenance", "Culture.Food and drink", "History_And_Society.Military and warfare", "Culture.Philosophy and religion", "Geography.Oceania", "Culture.Plastic arts", "History_And_Society.Education", "STEM.Engineering", "Culture.Visual arts", "STEM.Meteorology", "Culture.Language and literature", "Geography.Landforms", "Culture.Entertainment", "STEM.Medicine", "Geography.Bodies of water", "STEM.Information science", "Culture.Sports", "Geography.Europe", "History_And_Society.Politics and government", "Geography.Cities", "STEM.Geosciences", "Culture.Performing arts", "Culture.Arts", "STEM.Chemistry", "Assistance.Files"]
- Statistic: pr_auc.macro (maximize)
- Folds: 3

# Top scoring configurations
| model            |   pr_auc.macro | params                                                                |
|:-----------------|---------------:|:----------------------------------------------------------------------|
| GradientBoosting |         0.7142 | max_features="log2", max_depth=5, learning_rate=0.1, n_estimators=50  |
| GradientBoosting |         0.6923 | max_features="log2", max_depth=4, learning_rate=0.1, n_estimators=50  |
| GradientBoosting |         0.6647 | max_features="log2", max_depth=3, learning_rate=0.1, n_estimators=50  |
| GradientBoosting |         0.6545 | max_features="log2", max_depth=5, learning_rate=0.01, n_estimators=50 |
| GradientBoosting |         0.624  | max_features="log2", max_depth=4, learning_rate=0.01, n_estimators=50 |
| GradientBoosting |         0.5869 | max_features="log2", max_depth=3, learning_rate=0.01, n_estimators=50 |

# Models
## GradientBoosting
|   pr_auc.macro | params                                                                |
|---------------:|:----------------------------------------------------------------------|
|         0.7142 | max_features="log2", max_depth=5, learning_rate=0.1, n_estimators=50  |
|         0.6923 | max_features="log2", max_depth=4, learning_rate=0.1, n_estimators=50  |
|         0.6647 | max_features="log2", max_depth=3, learning_rate=0.1, n_estimators=50  |
|         0.6545 | max_features="log2", max_depth=5, learning_rate=0.01, n_estimators=50 |
|         0.624  | max_features="log2", max_depth=4, learning_rate=0.01, n_estimators=50 |
|         0.5869 | max_features="log2", max_depth=3, learning_rate=0.01, n_estimators=50 |

