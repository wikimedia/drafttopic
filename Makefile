.DELETE_ON_ERROR:

drafttopic_major_minor = 1.4

models: \
	articletopic_models \
	drafttopic_models

drafttopic_models: \
	models/hywiki.drafttopic.gradient_boosting.model

articletopic_models: \
	models/arwiki.articletopic.gradient_boosting.model \
	models/cswiki.articletopic.gradient_boosting.model \
	models/enwiki.articletopic.gradient_boosting.model \
	models/kowiki.articletopic.gradient_boosting.model \
	models/viwiki.articletopic.gradient_boosting.model \
	models/wikidata.articletopic.gradient_boosting.model \
	models/hywiki.articletopic.gradient_boosting.model

tuning_models: \
	tuning_reports/hywiki.articletopic.md \
	tuning_reports/hywiki.drafttopic.md


################## Common datasets #################################

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

################## Chinese Wikipedia #################################

datasets/zhwiki.balanced_article_sample.json: \
		datasets/enwiki.labeled_article_items.json.bz2
	bzcat $< | ./utility balance_sample zh -n 1000 > $@

datasets/zhwiki.balanced_article_sample.w_draft_text.json: \
		datasets/zhwiki.balanced_article_sample.json
	./utility fetch_draft_text \
	  --api-host=https://zh.wikipedia.org \
	  --tok_strategy=CJK \
	  --input=$< \
	  --output=$@ \
	  --threads=1 \
	  --debug

datasets/zhwiki.balanced_article_sample.w_article_text.json: \
		datasets/zhwiki.balanced_article_sample.json
	./utility fetch_article_text \
	  --api-host=https://zh.wikipedia.org \
          --tok_strategy=CJK \
          --input=$< \
          --output=$@ \
          --threads=1 \
          --debug

word2vec/zhwiki-20200501-learned_vectors.50_cell.10k.kv:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/zhwiki-20200501-learned_vectors.50_cell.10k.kv -qO- > $@

datasets/zhwiki.balanced_article_sample.w_draft_cache.json: \
		datasets/zhwiki.balanced_article_sample.w_draft_text.json \
		word2vec/zhwiki-20200501-learned_vectors.50_cell.10k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.zhwiki.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

datasets/zhwiki.balanced_article_sample.w_article_cache.json: \
		datasets/zhwiki.balanced_article_sample.w_article_text.json \
		word2vec/zhwiki-20200501-learned_vectors.50_cell.10k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.zhwiki.articletopic \
		--input=$< \
		--output=$@ \
		--verbose


models/zhwiki.drafttopic.gradient_boosting.model: \
		datasets/zhwiki.balanced_article_sample.w_draft_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.zhwiki.drafttopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@

	revscoring model_info $@ > model_info/zhwiki.drafttopic.md

models/zhwiki.articletopic.gradient_boosting.model: \
		datasets/zhwiki.balanced_article_sample.w_article_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.zhwiki.articletopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	 	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@

	revscoring model_info $@ > model_info/zhwiki.articletopic.md


tuning_reports/zhwiki.drafttopic.md: \
		datasets/zhwiki.balanced_article_sample.w_draft_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.zhwiki.drafttopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.json \
	   	--folds=3 > $@

tuning_reports/zhwiki.articletopic.md: \
		datasets/zhwiki.balanced_article_sample.w_article_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.zhwiki.articletopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.json \
	   	--folds=3 > $@

################## Japanese Wikipedia #################################

datasets/jawiki.balanced_article_sample.json: \
		datasets/enwiki.labeled_article_items.json.bz2
	bzcat $< | ./utility balance_sample ja -n 1000 > $@

datasets/jawiki.balanced_article_sample.w_draft_text.json: \
		datasets/jawiki.balanced_article_sample.json
	./utility fetch_draft_text \
	  --api-host=https://ja.wikipedia.org \
	  --tok_strategy=CJK \
	  --input=$< \
	  --output=$@ \
	  --threads=1 \
	  --debug

datasets/jawiki.balanced_article_sample.w_article_text.json: \
		datasets/jawiki.balanced_article_sample.json
	./utility fetch_article_text \
          --api-host=https://ja.wikipedia.org \
          --tok_strategy=CJK \
          --input=$< \
          --output=$@ \
          --threads=1 \
          --debug

word2vec/jawiki-20200501-learned_vectors.50_cell.10k.kv:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/jawiki-20200501-learned_vectors.50_cell.10k.kv -qO- > $@

datasets/jawiki.balanced_article_sample.w_draft_cache.json: \
		datasets/jawiki.balanced_article_sample.w_draft_text.json \
		word2vec/jawiki-20200501-learned_vectors.50_cell.10k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.jawiki.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

datasets/jawiki.balanced_article_sample.w_article_cache.json: \
		datasets/jawiki.balanced_article_sample.w_article_text.json \
		word2vec/jawiki-20200501-learned_vectors.50_cell.10k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.jawiki.articletopic \
		--input=$< \
		--output=$@ \
		--verbose


models/jawiki.drafttopic.gradient_boosting.model: \
		datasets/jawiki.balanced_article_sample.w_draft_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.jawiki.drafttopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@

	revscoring model_info $@ > model_info/jawiki.drafttopic.md

models/jawiki.articletopic.gradient_boosting.model: \
		datasets/jawiki.balanced_article_sample.w_article_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.jawiki.articletopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	 	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@

	revscoring model_info $@ > model_info/jawiki.articletopic.md


tuning_reports/jawiki.drafttopic.md: \
		datasets/jawiki.balanced_article_sample.w_draft_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.jawiki.drafttopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.json \
	   	--folds=3 > $@

tuning_reports/jawiki.articletopic.md: \
		datasets/jawiki.balanced_article_sample.w_article_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.jawiki.articletopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.json \
	   	--folds=3 > $@


################## Korean Wikipedia #################################

datasets/kowiki.balanced_article_sample.json: \
		datasets/enwiki.labeled_article_items.json.bz2
	bzcat $< | ./utility balance_sample ko -n 1000 > $@

datasets/kowiki.balanced_article_sample.w_draft_text.json: \
		datasets/kowiki.balanced_article_sample.json
	./utility fetch_draft_text \
	  --api-host=https://ko.wikipedia.org \
	  --tok_strategy=CJK \
	  --input=$< \
	  --output=$@ \
	  --threads=1 \
	  --debug

datasets/kowiki.balanced_article_sample.w_article_text.json: \
		datasets/kowiki.balanced_article_sample.json
	./utility fetch_article_text \
	  --api-host=https://ko.wikipedia.org \
	  --tok_strategy=CJK \
	  --input=$< \
	  --output=$@ \
	  --threads=1 \
	  --debug

word2vec/kowiki-20200501-learned_vectors.50_cell.10k.kv:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/kowiki-20200501-learned_vectors.50_cell.10k.kv -qO- > $@
datasets/kowiki.balanced_article_sample.w_draft_cache.json: \
		datasets/kowiki.balanced_article_sample.w_draft_text.json \
		word2vec/kowiki-20200501-learned_vectors.50_cell.10k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.kowiki.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

datasets/kowiki.balanced_article_sample.w_article_cache.json: \
		datasets/kowiki.balanced_article_sample.w_article_text.json \
		word2vec/kowiki-20200501-learned_vectors.50_cell.10k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.kowiki.articletopic \
		--input=$< \
		--output=$@ \
		--verbose


models/kowiki.drafttopic.gradient_boosting.model: \
		datasets/kowiki.balanced_article_sample.w_draft_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.kowiki.drafttopic taxo_labels \
		--debug \
		--labels-config=labels-config.json \
		-p 'n_estimators=150' \
		-p 'max_depth=5' \
		-p 'max_features="log2"' \
		-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
		--folds=5 \
		--multilabel > $@

	revscoring model_info $@ > model_info/kowiki.drafttopic.md

models/kowiki.articletopic.gradient_boosting.model: \
		datasets/kowiki.balanced_article_sample.w_article_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.kowiki.articletopic taxo_labels \
		--debug \
		--labels-config=labels-config.json \
		-p 'n_estimators=150' \
		-p 'max_depth=5' \
		-p 'max_features="log2"' \
		-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
		--folds=5 \
		--multilabel > $@

	revscoring model_info $@ > model_info/kowiki.articletopic.md


tuning_reports/kowiki.drafttopic.md: \
		datasets/kowiki.balanced_article_sample.w_draft_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.kowiki.drafttopic \
		taxo_labels pr_auc.macro \
		--debug \
		--verbose \
		--multilabel \
		--labels-config=labels-config.json \
		--folds=3 > $@

tuning_reports/kowiki.articletopic.md: \
		datasets/kowiki.balanced_article_sample.w_article_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.kowiki.articletopic \
		taxo_labels pr_auc.macro \
		--debug \
		--verbose \
		--multilabel \
		--labels-config=labels-config.json \
		--folds=3 > $@

#####################  English Wikipedia #############################

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

word2vec/enwiki-20200501-learned_vectors.50_cell.10k.kv:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/enwiki-20200501-learned_vectors.50_cell.10k.kv -qO- > $@

datasets/enwiki.balanced_article_sample.w_draft_cache.json: \
		datasets/enwiki.balanced_article_sample.w_draft_text.json \
		word2vec/enwiki-20200501-learned_vectors.50_cell.10k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.enwiki.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

datasets/enwiki.balanced_article_sample.w_article_cache.json: \
		datasets/enwiki.balanced_article_sample.w_article_text.json \
		word2vec/enwiki-20200501-learned_vectors.50_cell.10k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.enwiki.articletopic \
		--input=$< \
		--output=$@ \
		--verbose


models/enwiki.drafttopic.gradient_boosting.model: \
		datasets/enwiki.balanced_article_sample.w_draft_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.enwiki.drafttopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@

	revscoring model_info $@ > model_info/enwiki.drafttopic.md

models/enwiki.articletopic.gradient_boosting.model: \
		datasets/enwiki.balanced_article_sample.w_article_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.enwiki.articletopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@

	revscoring model_info $@ > model_info/enwiki.articletopic.md


tuning_reports/enwiki.drafttopic.md: \
		datasets/enwiki.balanced_article_sample.w_draft_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.enwiki.drafttopic \
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
		drafttopic.feature_lists.enwiki.articletopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.yaml \
	   	--folds=3 > $@

################## Armenian Wikipedia #################################

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

word2vec/hywiki-20200501-learned_vectors.50_cell.10k.kv:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/hywiki-20200501-learned_vectors.50_cell.10k.kv -qO- > $@

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


###################### Vietnamese Wikipedia #########################

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

word2vec/viwiki-20200501-learned_vectors.50_cell.10k.kv:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/viwiki-20200501-learned_vectors.50_cell.10k.kv -qO- > $@

datasets/viwiki.balanced_article_sample.w_draft_cache.json: \
		datasets/viwiki.balanced_article_sample.w_draft_text.json \
		word2vec/viwiki-20200501-learned_vectors.50_cell.10k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.viwiki.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

datasets/viwiki.balanced_article_sample.w_article_cache.json: \
		datasets/viwiki.balanced_article_sample.w_article_text.json \
		word2vec/viwiki-20200501-learned_vectors.50_cell.10k.kv
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


###################### Wikidata #########################

datasets/wikidata.balanced_article_sample.json: \
		datasets/enwiki.labeled_article_items.json.bz2
	bzcat $< | ./utility balance_sample wikidata -n 1000 > $@

datasets/wikidata.balanced_article_sample.w_article_text.json: \
		datasets/wikidata.balanced_article_sample.json
	./utility fetch_article_text \
	  --api-host=https://www.wikidata.org \
	  --input=$< \
	  --output=$@ \
	  --debug

word2vec/wikidata-20200501-learned_vectors.50_cell.10k.kv:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/wikidata-20200501-learned_vectors.50_cell.10k.kv -qO- > $@

datasets/wikidata.balanced_article_sample.w_article_cache.json: \
		datasets/wikidata.balanced_article_sample.w_article_text.json \
		word2vec/wikidata-20200501-learned_vectors.50_cell.10k.kv
	./utility extract_from_text \
		drafttopic.feature_lists.wikidata.articletopic \
		--input=$< \
		--output=$@ \
		--verbose


models/wikidata.articletopic.gradient_boosting.model: \
		datasets/wikidata.balanced_article_sample.w_article_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.wikidata.articletopic taxo_labels \
		--debug \
		--labels-config=labels-config.json \
		-p 'n_estimators=150' \
		-p 'max_depth=5' \
		-p 'max_features="log2"' \
		-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
		--folds=5 \
		--multilabel > $@

	revscoring model_info $@ > model_info/wikidata.articletopic.md


tuning_reports/wikidata.articletopic.md: \
		datasets/wikidata.balanced_article_sample.w_article_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.wikidata.articletopic \
		taxo_labels pr_auc.macro \
		--debug \
		--verbose \
		--multilabel \
		--labels-config=labels-config.yaml \
		--folds=3 > $@
