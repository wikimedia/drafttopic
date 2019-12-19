.DELETE_ON_ERROR:

drafttopic_major_minor = 1.0

models: \
	models/enwiki.drafttopic.gradient_boosting.model \
	models/enwiki.articletopic.gradient_boosting.model


# Johnson, Isaac; Halfaker, Aaron (2019):
# Wikipedia Articles and Associated WikiProject Templates. figshare. Dataset.
# https://doi.org/10.6084/m9.figshare.10248344.v3
datasets/enwiki.article_items_with_wikiproject_templates.20191201.json.bz2:
	wget https://ndownloader.figshare.com/files/20183063 -qO- > $@

datasets/wikiproject_to_template.halfak_20191202.yaml:
	wget https://ndownloader.figshare.com/files/20205702 -qO- > $@

datasets/wikiproject_taxonomy.halfak_20191202.yaml:
	wget https://ndownloader.figshare.com/files/20205654 -qO- > $@

datasets/enwiki.labeled_article_items.json.bz2: \
		datasets/enwiki.article_items_with_wikiproject_templates.20191201.json.bz2 \
		datasets/wikiproject_taxonomy.halfak_20191202.yaml \
		datasets/wikiproject_to_template.halfak_20191202.yaml
	bzcat $< | ./utility taxo_label \
	  datasets/wikiproject_taxonomy.halfak_20191202.yaml \
	  datasets/wikiproject_to_template.halfak_20191202.yaml | \
	bzip2 -c > $@


labels-config.json: \
		datasets/enwiki.labeled_article_items.json.bz2
	bzcat $< | ./utility write_labels taxo_labels > $@

datasets/enwiki.balanced_article_sample.json: \
		datasets/enwiki.labeled_article_items.json.bz2
	bzcat $< | ./utility balance_sample en -n 1000 > $@


datasets/enwiki.balanced_article_sample.w_draft_text.json: \
		datasets/enwiki.balanced_article_sample.json
	./utility fetch_draft_text \
	  --api-host=https://en.wikipedia.org \
	  --input=$< \
	  --output=$@ \
	  --debug

datasets/enwiki.balanced_article_sample.w_article_text.json: \
		datasets/enwiki.balanced_article_sample.json
	./utility fetch_article_text \
	  --api-host=https://en.wikipedia.org \
	  --input=$< \
	  --output=$@ \
	  --debug


word2vec/GoogleNews-vectors-negative300.bin.gz:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/assets/GoogleNews-vectors-negative300.bin.gz -qO- > $@

datasets/enwiki.balanced_article_sample.w_draft_cache.json: \
		datasets/enwiki.balanced_article_sample.w_draft_text.json \
		word2vec/GoogleNews-vectors-negative300.bin.gz
	./utility extract_from_text \
		drafttopic.feature_lists.wordvectors.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

datasets/enwiki.balanced_article_sample.w_article_cache.json: \
		datasets/enwiki.balanced_article_sample.w_article_text.json \
		word2vec/GoogleNews-vectors-negative300.bin.gz
	./utility extract_from_text \
		drafttopic.feature_lists.wordvectors.articletopic \
		--input=$< \
		--output=$@ \
		--verbose

models/enwiki.drafttopic.gradient_boosting.model: \
		datasets/enwiki.balanced_article_sample.w_draft_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.wordvectors.drafttopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor) \
	   	--folds=5 \
		--multilabel > $@
	
	revscoring model_info $@ > model_info/enwiki.drafttopic.md

models/enwiki.articletopic.gradient_boosting.model: \
		datasets/enwiki.balanced_article_sample.w_article_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.wordvectors.articletopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor) \
	   	--folds=5 \
		--multilabel > $@
	
	revscoring model_info $@ > model_info/enwiki.articletopic.md


tuning_reports/enwiki.drafttopic.md: \
		datasets/enwiki.balanced_article_sample.w_draft_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.wordvectors.drafttopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.yaml \
	   	--folds=3 > $@

tuning_reports/enwiki.articletopic.md: \
		datasets/enwiki.balanced_article_sample.w_article_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.wordvectors.articletopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.yaml \
	   	--folds=3 > $@
