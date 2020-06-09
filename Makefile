.DELETE_ON_ERROR:

drafttopic_major_minor = 1.2

models: \
	articletopic_models \
	drafttopic_models

drafttopic_models: \
	models/arwiki.drafttopic.gradient_boosting.model \
	models/cswiki.drafttopic.gradient_boosting.model \
	models/enwiki.drafttopic.gradient_boosting.model \
	models/kowiki.drafttopic.gradient_boosting.model \
	models/viwiki.drafttopic.gradient_boosting.model

articletopic_models: \
	models/arwiki.articletopic.gradient_boosting.model \
	models/cswiki.articletopic.gradient_boosting.model \
	models/enwiki.articletopic.gradient_boosting.model \
	models/kowiki.articletopic.gradient_boosting.model \
	models/viwiki.articletopic.gradient_boosting.model


# Johnson, Isaac; Halfaker, Aaron (2019):
# Wikipedia Articles and Associated WikiProject Templates. figshare. Dataset.
# https://doi.org/10.6084/m9.figshare.10248344.v3
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


###################### Arabic Wikipedia ##########################

datasets/arwiki.balanced_article_sample.json: \
		datasets/enwiki.labeled_article_items.json.bz2
	bzcat $< | ./utility balance_sample ar -n 1000 > $@

datasets/arwiki.balanced_article_sample.w_draft_text.json: \
		datasets/arwiki.balanced_article_sample.json
	./utility fetch_draft_text \
	  --api-host=https://ar.wikipedia.org \
	  --input=$< \
	  --output=$@ \
	  --debug

datasets/arwiki.balanced_article_sample.w_article_text.json: \
		datasets/arwiki.balanced_article_sample.json
	./utility fetch_article_text \
	  --api-host=https://ar.wikipedia.org \
	  --input=$< \
	  --output=$@ \
	  --debug


word2vec/arwiki-20191201-learned_vectors.50_cell.100k.kv:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/arwiki-20191201-learned_vectors.50_cell.100k.kv -qO- > $@

datasets/arwiki.balanced_article_sample.w_draft_cache.json: \
		datasets/arwiki.balanced_article_sample.w_draft_text.json \
		word2vec/arwiki-20191201-learned_vectors.100_cell.300k.vec.bz2
	./utility extract_from_text \
		drafttopic.feature_lists.arwiki.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

datasets/arwiki.balanced_article_sample.w_article_cache.json: \
		datasets/arwiki.balanced_article_sample.w_article_text.json \
		word2vec/arwiki-20191201-learned_vectors.100_cell.300k.vec.bz2
	./utility extract_from_text \
		drafttopic.feature_lists.arwiki.articletopic \
		--input=$< \
		--output=$@ \
		--verbose

models/arwiki.drafttopic.gradient_boosting.model: \
		datasets/arwiki.balanced_article_sample.w_draft_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.arwiki.drafttopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@
	
	revscoring model_info $@ > model_info/arwiki.drafttopic.md

models/arwiki.articletopic.gradient_boosting.model: \
		datasets/arwiki.balanced_article_sample.w_article_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.arwiki.articletopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@
	
	revscoring model_info $@ > model_info/arwiki.articletopic.md


tuning_reports/arwiki.drafttopic.md: \
		datasets/arwiki.balanced_article_sample.w_draft_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.arwiki.drafttopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.yaml \
	   	--folds=3 > $@

tuning_reports/arwiki.articletopic.md: \
		datasets/arwiki.balanced_article_sample.w_article_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.arwiki.articletopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.yaml \
	   	--folds=3 > $@


################### Czech Wikipedia #############################

datasets/cswiki.balanced_article_sample.json: \
		datasets/enwiki.labeled_article_items.json.bz2
	bzcat $< | ./utility balance_sample cs -n 1000 > $@

datasets/cswiki.balanced_article_sample.w_draft_text.json: \
		datasets/cswiki.balanced_article_sample.json
	./utility fetch_draft_text \
	  --api-host=https://cs.wikipedia.org \
	  --input=$< \
	  --output=$@ \
	  --debug

datasets/cswiki.balanced_article_sample.w_article_text.json: \
		datasets/cswiki.balanced_article_sample.json
	./utility fetch_article_text \
	  --api-host=https://cs.wikipedia.org \
	  --input=$< \
	  --output=$@ \
	  --debug


word2vec/cswiki-20191201-learned_vectors.50_cell.100k.kv:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/cswiki-20191201-learned_vectors.50_cell.100k.kv -qO- > $@

datasets/cswiki.balanced_article_sample.w_draft_cache.json: \
		datasets/cswiki.balanced_article_sample.w_draft_text.json \
		word2vec/cswiki-20191201-learned_vectors.100_cell.300k.vec.bz2
	./utility extract_from_text \
		drafttopic.feature_lists.cswiki.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

datasets/cswiki.balanced_article_sample.w_article_cache.json: \
		datasets/cswiki.balanced_article_sample.w_article_text.json \
		word2vec/cswiki-20191201-learned_vectors.100_cell.300k.vec.bz2
	./utility extract_from_text \
		drafttopic.feature_lists.cswiki.articletopic \
		--input=$< \
		--output=$@ \
		--verbose

models/cswiki.drafttopic.gradient_boosting.model: \
		datasets/cswiki.balanced_article_sample.w_draft_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.cswiki.drafttopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@
	
	revscoring model_info $@ > model_info/cswiki.drafttopic.md

models/cswiki.articletopic.gradient_boosting.model: \
		datasets/cswiki.balanced_article_sample.w_article_cache.json \
		labels-config.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.cswiki.articletopic taxo_labels \
		--debug \
	   	--labels-config=labels-config.json \
	   	-p 'n_estimators=150' \
		-p 'max_depth=5' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
		--version=$(drafttopic_major_minor).0 \
	   	--folds=5 \
		--multilabel > $@
	
	revscoring model_info $@ > model_info/cswiki.articletopic.md


tuning_reports/cswiki.drafttopic.md: \
		datasets/cswiki.balanced_article_sample.w_draft_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.cswiki.drafttopic \
	   	taxo_labels pr_auc.macro \
	   	--debug \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.json \
	   	--folds=3 > $@

tuning_reports/cswiki.articletopic.md: \
		datasets/cswiki.balanced_article_sample.w_article_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.cswiki.articletopic \
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

word2vec/enwiki-20191201-learned_vectors.50_cell.100k.kv:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/enwiki-20191201-learned_vectors.50_cell.100k.kv -qO- > $@

datasets/enwiki.balanced_article_sample.w_draft_cache.json: \
		datasets/enwiki.balanced_article_sample.w_draft_text.json \
		word2vec/enwiki-20191201-learned_vectors.100_cell.300k.vec.bz2
	./utility extract_from_text \
		drafttopic.feature_lists.enwiki.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

datasets/enwiki.balanced_article_sample.w_article_cache.json: \
		datasets/enwiki.balanced_article_sample.w_article_text.json \
		word2vec/enwiki-20191201-learned_vectors.100_cell.300k.vec.bz2
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

################## Korean Wikipedia #################################

datasets/kowiki.balanced_article_sample.json: \
		datasets/enwiki.labeled_article_items.json.bz2
	bzcat $< | ./utility balance_sample ko -n 1000 > $@

datasets/kowiki.balanced_article_sample.w_draft_text.json: \
		datasets/kowiki.balanced_article_sample.json
	./utility fetch_draft_text \
	  --api-host=https://ko.wikipedia.org \
	  --input=$< \
	  --output=$@ \
	  --debug

datasets/kowiki.balanced_article_sample.w_article_text.json: \
		datasets/kowiki.balanced_article_sample.json
	./utility fetch_article_text \
	  --api-host=https://ko.wikipedia.org \
	  --input=$< \
	  --output=$@ \
	  --debug

word2vec/kowiki-20191201-learned_vectors.50_cell.100k.kv:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/kowiki-20191201-learned_vectors.50_cell.100k.kv -qO- > $@

datasets/kowiki.balanced_article_sample.w_draft_cache.json: \
		datasets/kowiki.balanced_article_sample.w_draft_text.json \
		word2vec/kowiki-20191201-learned_vectors.100_cell.300k.vec.bz2
	./utility extract_from_text \
		drafttopic.feature_lists.kowiki.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

datasets/kowiki.balanced_article_sample.w_article_cache.json: \
		datasets/kowiki.balanced_article_sample.w_article_text.json \
		word2vec/kowiki-20191201-learned_vectors.100_cell.300k.vec.bz2
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

word2vec/viwiki-20191201-learned_vectors.50_cell.100k.kv:
	wget https://analytics.wikimedia.org/datasets/archive/public-datasets/all/ores/topic/vectors/viwiki-20191201-learned_vectors.50_cell.100k.kv -qO- > $@

datasets/viwiki.balanced_article_sample.w_draft_cache.json: \
		datasets/viwiki.balanced_article_sample.w_draft_text.json \
		word2vec/viwiki-20191201-learned_vectors.100_cell.300k.vec.bz2
	./utility extract_from_text \
		drafttopic.feature_lists.viwiki.drafttopic \
		--input=$< \
		--output=$@ \
		--verbose

datasets/viwiki.balanced_article_sample.w_article_cache.json: \
		datasets/viwiki.balanced_article_sample.w_article_text.json \
		word2vec/viwiki-20191201-learned_vectors.100_cell.300k.vec.bz2
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
