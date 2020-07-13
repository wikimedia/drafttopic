
.DELETE_ON_ERROR:

drafttopic_major_minor = 1.2

models: \
	articletopic_models \
	drafttopic_models

drafttopic_models: \
	models/viwiki.drafttopic.gradient_boosting.model

articletopic_models: \
	models/viwiki.articletopic.gradient_boosting.model

datasets/viwiki.balanced_article_sample.json: \
		datasets/enwiki.labeled_article_items.json.bz2
	bzcat $< | ./utility balance_sample vi -n 1000 > $@

datasets/viwiki.balanced_article_sample.w_draft_text.json: \
		datasets/viwiki.balanced_article_sample.json
	./utility fetch_draft_text \
	  --api-host=https://vi.wikipedia.org \
	  --input=$< \
	  --output=$@ \
	  --debug

datasets/viwiki.balanced_article_sample.w_article_text.json: \
		datasets/viwiki.balanced_article_sample.json
	./utility fetch_article_text \
	  --api-host=https://vi.wikipedia.org \
	  --input=$< \
	  --output=$@ \
	  --debug

word2vec/viwiki-20191201-learned_vectors.50_cell.100k.kv:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/viwiki-20191201-learned_vectors.50_cell.100k.kv -qO- > $@

datasets/viwiki.balanced_article_sample.w_draft_cache.json: \
		datasets/viwiki.balanced_article_sample.w_draft_text.json \
		word2vec/viwiki-20191201-learned_vectors.50_cell.100k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.viwiki.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

datasets/viwiki.balanced_article_sample.w_article_cache.json: \
		datasets/viwiki.balanced_article_sample.w_article_text.json \
		word2vec/viwiki-20191201-learned_vectors.50_cell.100k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.viwiki.articletopic \
		--input=$< \
		--output=$@ \
		--verbose

models/viwiki.drafttopic.gradient_boosting.model: \
		datasets/viwiki.balanced_article_sample.w_draft_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.viwiki.drafttopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@

	revscoring model_info $@ > model_info/viwiki.drafttopic.md

models/viwiki.articletopic.gradient_boosting.model: \
		datasets/viwiki.balanced_article_sample.w_article_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.viwiki.articletopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@

	revscoring model_info $@ > model_info/viwiki.articletopic.md

tuning_reports/viwiki.drafttopic.md: \
		datasets/viwiki.balanced_article_sample.w_draft_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.viwiki.drafttopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.yaml \
	   	--folds=3 > $@

tuning_reports/viwiki.articletopic.md: \
		datasets/viwiki.balanced_article_sample.w_article_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.viwiki.articletopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.yaml \
	   	--folds=3 > $@
