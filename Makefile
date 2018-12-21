drafttopic_major_minor = 0.2

models: \
	models/enwiki.drafttopic.gradient_boosting.model

datasets/enwiki.labeled_wikiprojects.json:
	wget https://ndownloader.figshare.com/files/9828517 -qO- > $@

labels-config.json: \
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

word2vec/GoogleNews-vectors-negative300.bin.gz:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/assets/GoogleNews-vectors-negative300.bin.gz -qO- > $@

datasets/enwiki.labeled_wikiprojects.w_cache.json: \
		datasets/enwiki.labeled_wikiprojects.w_text.json \
		word2vec/GoogleNews-vectors-negative300.bin.gz
	./utility extract_from_text \
		drafttopic.feature_lists.wordvectors.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

models/enwiki.drafttopic.gradient_boosting.model: \
		datasets/enwiki.labeled_wikiprojects.w_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.wordvectors.drafttopic mid_level_categories \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor) \
	   	--folds=5 \
	   	--model-file=models/enwiki.drafttopic.gradient_boosting.model \
		--multilabel > $@
	
	revscoring model_info $@ > model_info/enwiki.drafttopic.md

tuning_reports/enwiki.drafttopic.md: \
	datasets/enwiki.labeled_wikiprojects.w_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.wordvectors.drafttopic \
	   	mid_level_categories pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.yaml \
	   	--folds=3 > $@
