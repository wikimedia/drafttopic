datasets/enwiki.labeled_wikiprojects.json:
	wget https://ndownloader.figshare.com/files/9828517 -qO- > $@

models/enwiki.drafttopic.gradient_boosting.model: \
	datasets/enwiki.labeled_wikiprojects.w_cache.json
	cat $< | \
	revscoring cv_train revscoring.scoring.models.GradientBoosting \
		drafttopic.feature_lists.word2vec.drafttopic mid_level_categories \
		--debug \
	   	--labels-config=labels-config.yaml \
	   	-p 'n_estimators=50' \
		-p 'max_depth=3' \
	   	-p 'max_features="log2"' \
	   	-p 'learning_rate=0.1' \
	   	--folds=3 \
	   	--model-file=models/enwiki.drafttopic.gb.model \
		--multilabel > $@


tuning_reports/enwiki.drafttopic.md: \
	datasets/enwiki.labeled_wikiprojects.w_cache.json
	cat $< | \
	revscoring tune config/gradient_boosting.params.yaml \
		drafttopic.feature_lists.word2vec.drafttopic \
	   	mid_level_categories pr_auc.macro \
	   	--debug \
	   	--observations=datasets/enwiki.labeled_wikiprojects.w_cache.json \
	   	--verbose \
	   	--multilabel \
	   	--labels-config=labels-config.yaml \
	   	--folds=3 > $@
