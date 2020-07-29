.DELETE_ON_ERROR:

drafttopic_major_minor = 1.3

models: \
	articletopic_models \
	drafttopic_models

drafttopic_models: \
	models/hywiki.drafttopic.gradient_boosting.model

articletopic_models: \
	models/hywiki.articletopic.gradient_boosting.model

tuning_models: \
	tuning_reports/hywiki.articletopic.md \
	tuning_reports/hywiki.drafttopic.md

datasets/enwiki.article_items_with_wikiproject_templates.20191201.json.bz2:
	wget https://ndownloader.figshare.com/files/20183063 -qO- > $@

datasets/wikiproject_to_template.halfak_20191202.yaml:
	wget https://ndownloader.figshare.com/files/20205702 -qO- > $@

datasets/wikiproject_taxonomy.halfak_20191202.yaml:
	wget https://ndownloader.figshare.com/files/20205654 -qO- > $@

datasets/enwiki.labeled_article_items.wo_central_africa.json.bz2: \
		datasets/enwiki.article_items_with_wikiproject_templates.20191201.json.bz2 \
		datasets/wikiproject_taxonomy.halfak_20191202.yaml \
		datasets/wikiproject_to_template.halfak_20191202.yaml
	bzcat $< | ./utility taxo_label \
	  datasets/wikiproject_taxonomy.halfak_20191202.yaml \
	  datasets/wikiproject_to_template.halfak_20191202.yaml | \
	bzip2 -c > $@


# From https://quarry.wmflabs.org/query/45568
datasets/enwiki.central_africa_titles.txt:
	wget https://quarry.wmflabs.org/run/472620/output/0/tsv -qO- | \
	tail -n+2 | sed 's/_/ /g' > $@

datasets/enwiki.labeled_article_items.json.bz2: \
		datasets/enwiki.labeled_article_items.wo_central_africa.json.bz2 \
		datasets/enwiki.central_africa_titles.txt
	bzcat $< | ./utility add_central_africa --verbose | bzip2 -c > $@

labels-config.json: \
		datasets/enwiki.labeled_article_items.json.bz2
	bzcat $< | ./utility write_labels taxo_labels > $@

datasets/hywiki.balanced_article_sample.json: \
		datasets/enwiki.labeled_article_items.json.bz2
	bzcat $< | ./utility balance_sample hy -n 1000 > $@

datasets/hywiki.balanced_article_sample.w_draft_text.json: \
		datasets/hywiki.balanced_article_sample.json
	./utility fetch_draft_text \
	  --api-host=https://hy.wikipedia.org \
	  --input=$< \
	  --output=$@ \
	  --debug

datasets/hywiki.balanced_article_sample.w_article_text.json: \
		datasets/hywiki.balanced_article_sample.json
	./utility fetch_article_text \
	  --api-host=https://hy.wikipedia.org \
	  --input=$< \
	  --output=$@ \
	  --debug

#word2vec/hywiki-20200501-learned_vectors.50_cell.10k.kv:
#	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/hywiki-20200501-learned_vectors.50_cell.10k.kv -qO- > $@

datasets/hywiki.balanced_article_sample.w_draft_cache.json: \
		datasets/hywiki.balanced_article_sample.w_draft_text.json \
		word2vec/hywiki-20200501-learned_vectors.50_cell.10k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.hywiki.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

datasets/hywiki.balanced_article_sample.w_article_cache.json: \
		datasets/hywiki.balanced_article_sample.w_article_text.json \
		word2vec/hywiki-20200501-learned_vectors.50_cell.10k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.hywiki.articletopic \
		--input=$< \
		--output=$@ \
		--verbose


models/hywiki.drafttopic.gradient_boosting.model: \
		datasets/hywiki.balanced_article_sample.w_draft_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.hywiki.drafttopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@

	revscoring model_info $@ > model_info/hywiki.drafttopic.md

models/hywiki.articletopic.gradient_boosting.model: \
		datasets/hywiki.balanced_article_sample.w_article_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.hywiki.articletopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@

	revscoring model_info $@ > model_info/hywiki.articletopic.md


tuning_reports/hywiki.drafttopic.md: \
		datasets/hywiki.balanced_article_sample.w_draft_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.hywiki.drafttopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.json \
	   	--folds=3 > $@

tuning_reports/hywiki.articletopic.md: \
		datasets/hywiki.balanced_article_sample.w_article_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.hywiki.articletopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.json \
	   	--folds=3 > $@
