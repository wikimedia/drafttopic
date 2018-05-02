.PHONY: models

# Remove target files after command failure.
.DELETE_ON_ERROR:

models: \
		models/enwiki.drafttopic.gradient_boosting.model

# Generate machine-readable WikiProjects data.
datasets/enwiki.wikiprojects.json:
	./utility fetch_wikiprojects --output $@

# Generate a mapping of high-level topic categories to list of WikiProjects
# contained in them.
datasets/enwiki.midlevel_wikiprojects.json: \
		datasets/enwiki.wikiprojects.json
	./utility trim_wikiprojects --wikiprojects $< --output $@

datasets/enwiki.labeled_wikiprojects.json: \
		datasets/enwiki.midlevel_wikiprojects.json
	./utility fetch_project_content \
		--api-host=https://en.wikipedia.org/ \
		--mid-level-wp=$< \
		--output=$@

datasets/enwiki.labels-config.json: \
		datasets/enwiki.labeled_wikiprojects.json
	cat $< | \
	./utility write_labels \
		mid_level_categories > $@

datasets/enwiki.labeled_wikiprojects.w_text.json: \
		datasets/enwiki.labeled_wikiprojects.json
	./utility fetch_text \
		--api-host=https://en.wikipedia.org \
		--labelings=$< \
		--output=$@ \
		--verbose

datasets/enwiki.labeled_wikiprojects.w_cache.json: \
		datasets/enwiki.labeled_wikiprojects.json
	cat $< | \
	revscoring extract \
		drafttopic.feature_lists.wordvectors.drafttopic \
		--host=https://en.wikipedia.org/ \
		--input=datasets/enwiki.labeled_wikiprojects.json > $@

models/enwiki.drafttopic.gradient_boosting.model: \
		datasets/enwiki.labeled_wikiprojects.w_cache.json \
		datasets/enwiki.labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.wordvectors.drafttopic mid_level_categories \
		--debug \
		--labels-config=datasets/enwiki.labels-config.json \
		-p 'n_estimators=150' \
		-p 'max_depth=5' \
		-p 'max_features="log2"' \
		-p 'learning_rate=0.1' \
		--folds=5 \
		--model-file=models/enwiki.drafttopic.gradient_boosting.model \
		--multilabel > $@

tuning_reports/enwiki.drafttopic.md: \
		datasets/enwiki.labeled_wikiprojects.w_cache.json \
		datasets/enwiki.labels-config.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.wordvectors.drafttopic \
		mid_level_categories pr_auc.macro \
		--debug \
		--verbose \
		--multilabel \
		--labels-config=datasets/enwiki.labels-config.json \
		--folds=3 > $@
