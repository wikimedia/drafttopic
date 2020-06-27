Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'validation_fraction': 0.1, 'n_estimators': 150, 'scale': False, 'init': None, 'warm_start': False, 'max_leaf_nodes': None, 'learning_rate': 0.1, 'min_samples_split': 2, 'min_impurity_decrease': 0.0, 'center': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'min_weight_fraction_leaf': 0.0, 'criterion': 'friedman_mse', 'population_rates': None, 'label_weights': {}, 'min_samples_leaf': 1, 'random_state': None, 'subsample': 1.0, 'tol': 0.0001, 'loss': 'deviance', 'verbose': 0, 'max_depth': 5, 'n_iter_no_change': None, 'min_impurity_split': None, 'presort': 'auto', 'max_features': 'log2'}
	Environment:
	 - revscoring_version: '2.6.9'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.144-3.1 (2019-02-19)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=60648):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15939  -->  14325  1614   840  43869
			'Culture.Biography.Women'                       4348  -->   3174  1174   467  55833
			'Culture.Food and drink'                        1776  -->   1357   419    95  58777
			'Culture.Internet culture'                      3458  -->   2714   744   212  56978
			'Culture.Linguistics'                           1656  -->   1050   606   114  58878
			'Culture.Literature'                            5841  -->   4242  1599   542  54265
			'Culture.Media.Books'                           1589  -->   1153   436   123  58936
			'Culture.Media.Entertainment'                   2260  -->   1059  1201   246  58142
			'Culture.Media.Films'                           2960  -->   2428   532   123  57565
			'Culture.Media.Media*'                         14981  -->  12783  2198  1601  44066
			'Culture.Media.Music'                           3125  -->   2469   656   326  57197
			'Culture.Media.Radio'                            637  -->    347   290    50  59961
			'Culture.Media.Software'                        2292  -->   1700   592   382  57974
			'Culture.Media.Television'                      2514  -->   1755   759   191  57943
			'Culture.Media.Video games'                     2351  -->   2051   300    88  58209
			'Culture.Performing arts'                       1526  -->    832   694   166  58956
			'Culture.Philosophy and religion'               3817  -->   1934  1883   367  56464
			'Culture.Sports'                                5312  -->   4551   761   193  55143
			'Culture.Visual arts.Architecture'              2049  -->   1304   745   218  58381
			'Culture.Visual arts.Comics and Anime'          2460  -->   2060   400   157  58031
			'Culture.Visual arts.Fashion'                   1350  -->    912   438   103  59195
			'Culture.Visual arts.Visual arts*'              6338  -->   4435  1903   540  53770
			'Geography.Geographical'                        3969  -->   2571  1398   549  56130
			'Geography.Regions.Africa.Africa*'              4244  -->   3145  1099   272  56132
			'Geography.Regions.Africa.Central Africa'        823  -->    590   233    62  59763
			'Geography.Regions.Africa.Eastern Africa'        483  -->    347   136    62  60103
			'Geography.Regions.Africa.Northern Africa'      1455  -->   1031   424   112  59081
			'Geography.Regions.Africa.Southern Africa'       668  -->    460   208    47  59933
			'Geography.Regions.Africa.Western Africa'        279  -->    189    90    35  60334
			'Geography.Regions.Americas.Central America'    1364  -->    829   535    70  59214
			'Geography.Regions.Americas.North America'      6439  -->   4375  2064  1226  52983
			'Geography.Regions.Americas.South America'      1577  -->   1116   461   113  58958
			'Geography.Regions.Asia.Asia*'                 16007  -->  13302  2705  1587  43054
			'Geography.Regions.Asia.Central Asia'           1281  -->    861   420    79  59288
			'Geography.Regions.Asia.East Asia'              7663  -->   6202  1461   875  52110
			'Geography.Regions.Asia.North Asia'             3000  -->   2145   855   231  57417
			'Geography.Regions.Asia.South Asia'             1739  -->   1311   428    77  58832
			'Geography.Regions.Asia.Southeast Asia'         1910  -->   1360   550    97  58641
			'Geography.Regions.Asia.West Asia'              2217  -->   1611   606   166  58265
			'Geography.Regions.Europe.Eastern Europe'       4128  -->   3097  1031   295  56225
			'Geography.Regions.Europe.Europe*'             13972  -->  11254  2718  1652  45024
			'Geography.Regions.Europe.Northern Europe'      3743  -->   2641  1102   409  56496
			'Geography.Regions.Europe.Southern Europe'      3189  -->   2323   866   321  57138
			'Geography.Regions.Europe.Western Europe'       3913  -->   2932   981   426  56309
			'Geography.Regions.Oceania'                     1695  -->   1184   511    62  58891
			'History and Society.Business and economics'    3833  -->   2020  1813   400  56415
			'History and Society.Education'                 1935  -->   1139   796   125  58588
			'History and Society.History'                   5195  -->   2873  2322   667  54786
			'History and Society.Military and warfare'      4461  -->   2868  1593   391  55796
			'History and Society.Politics and government'   3960  -->   1938  2022   493  56195
			'History and Society.Society'                   4538  -->   1253  3285   307  55803
			'History and Society.Transportation'            3804  -->   3291   513   164  56680
			'STEM.Biology'                                  3489  -->   2725   764   187  56972
			'STEM.Chemistry'                                1482  -->   1121   361   132  59034
			'STEM.Computing'                                2790  -->   2168   622   451  57407
			'STEM.Earth and environment'                    1865  -->   1133   732   149  58634
			'STEM.Engineering'                              2634  -->   1847   787   180  57834
			'STEM.Libraries & Information'                   741  -->    506   235    46  59861
			'STEM.Mathematics'                              1151  -->    843   308    89  59408
			'STEM.Medicine & Health'                        2009  -->   1277   732   159  58480
			'STEM.Physics'                                  1500  -->    995   505   183  58965
			'STEM.STEM*'                                   17860  -->  15582  2278  1079  41709
			'STEM.Space'                                    1699  -->   1477   222    40  58909
			'STEM.Technology'                               4588  -->   3135  1453   709  55351
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.263         0.121
		Culture.Biography.Women                         0.072         0.015
		Culture.Food and drink                          0.029         0.003
		Culture.Internet culture                        0.057         0.004
		Culture.Linguistics                             0.027         0.008
		Culture.Literature                              0.096         0.015
		Culture.Media.Books                             0.026         0.004
		Culture.Media.Entertainment                     0.037         0.004
		Culture.Media.Films                             0.049         0.012
		Culture.Media.Media*                            0.247         0.055
		Culture.Media.Music                             0.052         0.021
		Culture.Media.Radio                             0.011         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.041         0.009
		Culture.Media.Video games                       0.039         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.063         0.01
		Culture.Sports                                  0.088         0.061
		Culture.Visual arts.Architecture                0.034         0.011
		Culture.Visual arts.Comics and Anime            0.041         0.002
		Culture.Visual arts.Fashion                     0.022         0.001
		Culture.Visual arts.Visual arts*                0.105         0.018
		Geography.Geographical                          0.065         0.021
		Geography.Regions.Africa.Africa*                0.07          0.009
		Geography.Regions.Africa.Central Africa         0.014         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0.001
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.005         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.106         0.064
		Geography.Regions.Americas.South America        0.026         0.007
		Geography.Regions.Asia.Asia*                    0.264         0.053
		Geography.Regions.Asia.Central Asia             0.021         0.001
		Geography.Regions.Asia.East Asia                0.126         0.012
		Geography.Regions.Asia.North Asia               0.049         0.006
		Geography.Regions.Asia.South Asia               0.029         0.017
		Geography.Regions.Asia.Southeast Asia           0.031         0.006
		Geography.Regions.Asia.West Asia                0.037         0.012
		Geography.Regions.Europe.Eastern Europe         0.068         0.018
		Geography.Regions.Europe.Europe*                0.23          0.082
		Geography.Regions.Europe.Northern Europe        0.062         0.029
		Geography.Regions.Europe.Southern Europe        0.053         0.014
		Geography.Regions.Europe.Western Europe         0.065         0.021
		Geography.Regions.Oceania                       0.028         0.017
		History and Society.Business and economics      0.063         0.01
		History and Society.Education                   0.032         0.008
		History and Society.History                     0.086         0.011
		History and Society.Military and warfare        0.074         0.015
		History and Society.Politics and government     0.065         0.016
		History and Society.Society                     0.075         0.008
		History and Society.Transportation              0.063         0.016
		STEM.Biology                                    0.058         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.046         0.003
		STEM.Earth and environment                      0.031         0.005
		STEM.Engineering                                0.043         0.006
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.033         0.006
		STEM.Physics                                    0.025         0.001
		STEM.STEM*                                      0.294         0.066
		STEM.Space                                      0.028         0.004
		STEM.Technology                                 0.076         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.126
		Culture.Biography.Women                      0.019
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.08
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.008
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.055
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.005
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.023
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.064
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.078
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.026
		Geography.Regions.Asia.North Asia            0.008
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.019
		Geography.Regions.Europe.Europe*             0.098
		Geography.Regions.Europe.Northern Europe     0.028
		Geography.Regions.Europe.Southern Europe     0.016
		Geography.Regions.Europe.Western Europe      0.023
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.018
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.017
		History and Society.Society                  0.008
		History and Society.Transportation           0.017
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.004
		STEM.Computing                               0.01
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.081
		STEM.Space                                   0.004
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.92
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.945
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.995
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.936
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.922
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.974
		Geography.Regions.Asia.North Asia            0.992
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.981
		Geography.Regions.Europe.Europe*             0.902
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.983
		History and Society.Society                  0.992
		History and Society.Transportation           0.983
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.996
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.919
		STEM.Space                                   0.996
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.766, macro=0.704):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.899
		Culture.Biography.Women                      0.73
		Culture.Food and drink                       0.764
		Culture.Internet culture                     0.785
		Culture.Linguistics                          0.634
		Culture.Literature                           0.726
		Culture.Media.Books                          0.726
		Culture.Media.Entertainment                  0.469
		Culture.Media.Films                          0.82
		Culture.Media.Media*                         0.853
		Culture.Media.Music                          0.79
		Culture.Media.Radio                          0.545
		Culture.Media.Software                       0.742
		Culture.Media.Television                     0.698
		Culture.Media.Video games                    0.872
		Culture.Performing arts                      0.545
		Culture.Philosophy and religion              0.507
		Culture.Sports                               0.857
		Culture.Visual arts.Architecture             0.636
		Culture.Visual arts.Comics and Anime         0.837
		Culture.Visual arts.Fashion                  0.676
		Culture.Visual arts.Visual arts*             0.7
		Geography.Geographical                       0.648
		Geography.Regions.Africa.Africa*             0.741
		Geography.Regions.Africa.Central Africa      0.717
		Geography.Regions.Africa.Eastern Africa      0.718
		Geography.Regions.Africa.Northern Africa     0.709
		Geography.Regions.Africa.Southern Africa     0.689
		Geography.Regions.Africa.Western Africa      0.677
		Geography.Regions.Americas.Central America   0.608
		Geography.Regions.Americas.North America     0.679
		Geography.Regions.Americas.South America     0.708
		Geography.Regions.Asia.Asia*                 0.831
		Geography.Regions.Asia.Central Asia          0.672
		Geography.Regions.Asia.East Asia             0.809
		Geography.Regions.Asia.North Asia            0.715
		Geography.Regions.Asia.South Asia            0.754
		Geography.Regions.Asia.Southeast Asia        0.712
		Geography.Regions.Asia.West Asia             0.727
		Geography.Regions.Europe.Eastern Europe      0.75
		Geography.Regions.Europe.Europe*             0.805
		Geography.Regions.Europe.Northern Europe     0.706
		Geography.Regions.Europe.Southern Europe     0.728
		Geography.Regions.Europe.Western Europe      0.749
		Geography.Regions.Oceania                    0.699
		History and Society.Business and economics   0.527
		History and Society.Education                0.589
		History and Society.History                  0.553
		History and Society.Military and warfare     0.643
		History and Society.Politics and government  0.489
		History and Society.Society                  0.276
		History and Society.Transportation           0.865
		STEM.Biology                                 0.781
		STEM.Chemistry                               0.756
		STEM.Computing                               0.777
		STEM.Earth and environment                   0.608
		STEM.Engineering                             0.701
		STEM.Libraries & Information                 0.683
		STEM.Mathematics                             0.732
		STEM.Medicine & Health                       0.636
		STEM.Physics                                 0.663
		STEM.STEM*                                   0.872
		STEM.Space                                   0.869
		STEM.Technology                              0.683
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.964
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.983
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.993
		History and Society.Education                0.998
		History and Society.History                  0.988
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.689, macro=0.555):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.869
		Culture.Biography.Women                      0.574
		Culture.Food and drink                       0.55
		Culture.Internet culture                     0.445
		Culture.Linguistics                          0.728
		Culture.Literature                           0.528
		Culture.Media.Books                          0.604
		Culture.Media.Entertainment                  0.308
		Culture.Media.Films                          0.819
		Culture.Media.Media*                         0.588
		Culture.Media.Music                          0.751
		Culture.Media.Radio                          0.606
		Culture.Media.Software                       0.13
		Culture.Media.Television                     0.658
		Culture.Media.Video games                    0.63
		Culture.Performing arts                      0.375
		Culture.Philosophy and religion              0.454
		Culture.Sports                               0.941
		Culture.Visual arts.Architecture             0.653
		Culture.Visual arts.Comics and Anime         0.429
		Culture.Visual arts.Fashion                  0.261
		Culture.Visual arts.Visual arts*             0.567
		Geography.Geographical                       0.593
		Geography.Regions.Africa.Africa*             0.571
		Geography.Regions.Africa.Central Africa      0.329
		Geography.Regions.Africa.Eastern Africa      0.261
		Geography.Regions.Africa.Northern Africa     0.338
		Geography.Regions.Africa.Southern Africa     0.537
		Geography.Regions.Africa.Western Africa      0.468
		Geography.Regions.Americas.Central America   0.643
		Geography.Regions.Americas.North America     0.671
		Geography.Regions.Americas.South America     0.72
		Geography.Regions.Asia.Asia*                 0.567
		Geography.Regions.Asia.Central Asia          0.289
		Geography.Regions.Asia.East Asia             0.379
		Geography.Regions.Asia.North Asia            0.504
		Geography.Regions.Asia.South Asia            0.907
		Geography.Regions.Asia.Southeast Asia        0.732
		Geography.Regions.Asia.West Asia             0.754
		Geography.Regions.Europe.Eastern Europe      0.73
		Geography.Regions.Europe.Europe*             0.669
		Geography.Regions.Europe.Northern Europe     0.747
		Geography.Regions.Europe.Southern Europe     0.648
		Geography.Regions.Europe.Western Europe      0.678
		Geography.Regions.Oceania                    0.918
		History and Society.Business and economics   0.426
		History and Society.Education                0.69
		History and Society.History                  0.338
		History and Society.Military and warfare     0.592
		History and Society.Politics and government  0.485
		History and Society.Society                  0.298
		History and Society.Transportation           0.834
		STEM.Biology                                 0.896
		STEM.Chemistry                               0.367
		STEM.Computing                               0.222
		STEM.Earth and environment                   0.535
		STEM.Engineering                             0.569
		STEM.Libraries & Information                 0.381
		STEM.Mathematics                             0.186
		STEM.Medicine & Health                       0.605
		STEM.Physics                                 0.169
		STEM.STEM*                                   0.708
		STEM.Space                                   0.847
		STEM.Technology                              0.22
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.99
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.982
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.992
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.991
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.718, macro=0.601):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.883
		Culture.Biography.Women                      0.643
		Culture.Food and drink                       0.64
		Culture.Internet culture                     0.568
		Culture.Linguistics                          0.678
		Culture.Literature                           0.611
		Culture.Media.Books                          0.659
		Culture.Media.Entertainment                  0.372
		Culture.Media.Films                          0.82
		Culture.Media.Media*                         0.696
		Culture.Media.Music                          0.77
		Culture.Media.Radio                          0.574
		Culture.Media.Software                       0.222
		Culture.Media.Television                     0.677
		Culture.Media.Video games                    0.731
		Culture.Performing arts                      0.444
		Culture.Philosophy and religion              0.479
		Culture.Sports                               0.897
		Culture.Visual arts.Architecture             0.645
		Culture.Visual arts.Comics and Anime         0.567
		Culture.Visual arts.Fashion                  0.376
		Culture.Visual arts.Visual arts*             0.626
		Geography.Geographical                       0.619
		Geography.Regions.Africa.Africa*             0.645
		Geography.Regions.Africa.Central Africa      0.451
		Geography.Regions.Africa.Eastern Africa      0.383
		Geography.Regions.Africa.Northern Africa     0.458
		Geography.Regions.Africa.Southern Africa     0.604
		Geography.Regions.Africa.Western Africa      0.554
		Geography.Regions.Americas.Central America   0.625
		Geography.Regions.Americas.North America     0.675
		Geography.Regions.Americas.South America     0.714
		Geography.Regions.Asia.Asia*                 0.674
		Geography.Regions.Asia.Central Asia          0.404
		Geography.Regions.Asia.East Asia             0.516
		Geography.Regions.Asia.North Asia            0.591
		Geography.Regions.Asia.South Asia            0.823
		Geography.Regions.Asia.Southeast Asia        0.722
		Geography.Regions.Asia.West Asia             0.74
		Geography.Regions.Europe.Eastern Europe      0.74
		Geography.Regions.Europe.Europe*             0.731
		Geography.Regions.Europe.Northern Europe     0.726
		Geography.Regions.Europe.Southern Europe     0.686
		Geography.Regions.Europe.Western Europe      0.712
		Geography.Regions.Oceania                    0.793
		History and Society.Business and economics   0.471
		History and Society.Education                0.635
		History and Society.History                  0.42
		History and Society.Military and warfare     0.616
		History and Society.Politics and government  0.487
		History and Society.Society                  0.287
		History and Society.Transportation           0.849
		STEM.Biology                                 0.835
		STEM.Chemistry                               0.494
		STEM.Computing                               0.345
		STEM.Earth and environment                   0.569
		STEM.Engineering                             0.628
		STEM.Libraries & Information                 0.489
		STEM.Mathematics                             0.297
		STEM.Medicine & Health                       0.62
		STEM.Physics                                 0.269
		STEM.STEM*                                   0.782
		STEM.Space                                   0.858
		STEM.Technology                              0.333
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.977
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.973
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.978, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.971
		Culture.Biography.Women                      0.988
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.986
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.959
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.958
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.957
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.981
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.952
		Geography.Regions.Europe.Northern Europe     0.984
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.988
		History and Society.Education                0.995
		History and Society.History                  0.983
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.983
		History and Society.Society                  0.989
		History and Society.Transportation           0.995
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.968
		STEM.Space                                   0.999
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.019
		Culture.Biography.Women                      0.008
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.035
		Culture.Media.Music                          0.006
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.002
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.023
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.036
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.017
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.035
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.007
		History and Society.Education                0.002
		History and Society.History                  0.012
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.009
		History and Society.Society                  0.005
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.025
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.972, macro=0.972):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.981
		Culture.Internet culture                     0.983
		Culture.Linguistics                          0.972
		Culture.Literature                           0.973
		Culture.Media.Books                          0.983
		Culture.Media.Entertainment                  0.963
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.974
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.967
		Culture.Media.Software                       0.984
		Culture.Media.Television                     0.978
		Culture.Media.Video games                    0.988
		Culture.Performing arts                      0.968
		Culture.Philosophy and religion              0.945
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.974
		Culture.Visual arts.Comics and Anime         0.988
		Culture.Visual arts.Fashion                  0.978
		Culture.Visual arts.Visual arts*             0.967
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.975
		Geography.Regions.Africa.Central Africa      0.984
		Geography.Regions.Africa.Eastern Africa      0.967
		Geography.Regions.Africa.Northern Africa     0.975
		Geography.Regions.Africa.Southern Africa     0.96
		Geography.Regions.Africa.Western Africa      0.953
		Geography.Regions.Americas.Central America   0.969
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.976
		Geography.Regions.Asia.Asia*                 0.963
		Geography.Regions.Asia.Central Asia          0.979
		Geography.Regions.Asia.East Asia             0.977
		Geography.Regions.Asia.North Asia            0.974
		Geography.Regions.Asia.South Asia            0.977
		Geography.Regions.Asia.Southeast Asia        0.975
		Geography.Regions.Asia.West Asia             0.977
		Geography.Regions.Europe.Eastern Europe      0.972
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.974
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.976
		History and Society.Business and economics   0.959
		History and Society.Education                0.971
		History and Society.History                  0.948
		History and Society.Military and warfare     0.968
		History and Society.Politics and government  0.949
		History and Society.Society                  0.899
		History and Society.Transportation           0.984
		STEM.Biology                                 0.978
		STEM.Chemistry                               0.984
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.97
		STEM.Engineering                             0.977
		STEM.Libraries & Information                 0.975
		STEM.Mathematics                             0.98
		STEM.Medicine & Health                       0.972
		STEM.Physics                                 0.982
		STEM.STEM*                                   0.976
		STEM.Space                                   0.989
		STEM.Technology                              0.969
		-------------------------------------------  -----
	pr_auc (micro=0.765, macro=0.612):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.945
		Culture.Biography.Women                      0.633
		Culture.Food and drink                       0.692
		Culture.Internet culture                     0.718
		Culture.Linguistics                          0.669
		Culture.Literature                           0.686
		Culture.Media.Books                          0.678
		Culture.Media.Entertainment                  0.329
		Culture.Media.Films                          0.86
		Culture.Media.Media*                         0.819
		Culture.Media.Music                          0.813
		Culture.Media.Radio                          0.494
		Culture.Media.Software                       0.227
		Culture.Media.Television                     0.694
		Culture.Media.Video games                    0.79
		Culture.Performing arts                      0.416
		Culture.Philosophy and religion              0.447
		Culture.Sports                               0.937
		Culture.Visual arts.Architecture             0.659
		Culture.Visual arts.Comics and Anime         0.729
		Culture.Visual arts.Fashion                  0.37
		Culture.Visual arts.Visual arts*             0.682
		Geography.Geographical                       0.629
		Geography.Regions.Africa.Africa*             0.68
		Geography.Regions.Africa.Central Africa      0.313
		Geography.Regions.Africa.Eastern Africa      0.245
		Geography.Regions.Africa.Northern Africa     0.402
		Geography.Regions.Africa.Southern Africa     0.509
		Geography.Regions.Africa.Western Africa      0.365
		Geography.Regions.Americas.Central America   0.532
		Geography.Regions.Americas.North America     0.727
		Geography.Regions.Americas.South America     0.714
		Geography.Regions.Asia.Asia*                 0.744
		Geography.Regions.Asia.Central Asia          0.366
		Geography.Regions.Asia.East Asia             0.565
		Geography.Regions.Asia.North Asia            0.618
		Geography.Regions.Asia.South Asia            0.856
		Geography.Regions.Asia.Southeast Asia        0.761
		Geography.Regions.Asia.West Asia             0.754
		Geography.Regions.Europe.Eastern Europe      0.766
		Geography.Regions.Europe.Europe*             0.789
		Geography.Regions.Europe.Northern Europe     0.772
		Geography.Regions.Europe.Southern Europe     0.705
		Geography.Regions.Europe.Western Europe      0.743
		Geography.Regions.Oceania                    0.84
		History and Society.Business and economics   0.425
		History and Society.Education                0.63
		History and Society.History                  0.375
		History and Society.Military and warfare     0.66
		History and Society.Politics and government  0.489
		History and Society.Society                  0.233
		History and Society.Transportation           0.882
		STEM.Biology                                 0.888
		STEM.Chemistry                               0.536
		STEM.Computing                               0.355
		STEM.Earth and environment                   0.575
		STEM.Engineering                             0.654
		STEM.Libraries & Information                 0.446
		STEM.Mathematics                             0.344
		STEM.Medicine & Health                       0.622
		STEM.Physics                                 0.259
		STEM.STEM*                                   0.891
		STEM.Space                                   0.883
		STEM.Technology                              0.36
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}}}}}

