Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'n_iter_no_change': None, 'init': None, 'max_features': 'log2', 'random_state': None, 'min_samples_leaf': 1, 'min_impurity_decrease': 0.0, 'ccp_alpha': 0.0, 'tol': 0.0001, 'criterion': 'friedman_mse', 'min_samples_split': 2, 'validation_fraction': 0.1, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'scale': False, 'warm_start': False, 'multilabel': True, 'loss': 'deviance', 'presort': 'deprecated', 'n_estimators': 150, 'verbose': 0, 'max_leaf_nodes': None, 'max_depth': 5, 'population_rates': None, 'min_impurity_split': None, 'subsample': 1.0, 'label_weights': {}, 'min_weight_fraction_leaf': 0.0, 'center': False, 'learning_rate': 0.1}
	Environment:
	 - revscoring_version: '2.9.2'
	 - platform: 'Linux-4.19.0-0.bpo.14-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.19.171-2~deb9u1 (2021-02-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Nov 18 2020 21:09:16')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.19.0-0.bpo.14-amd64'
	
	Statistics:
	counts (n=62675):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13546  -->  11832  1714   925  48204
			'Culture.Biography.Women'                       3220  -->   2217  1003   371  59084
			'Culture.Food and drink'                        1436  -->    965   471   126  61113
			'Culture.Internet culture'                      3439  -->   2626   813   250  58986
			'Culture.Linguistics'                           1584  -->   1143   441   102  60989
			'Culture.Literature'                            5572  -->   4209  1363   627  56476
			'Culture.Media.Books'                           1666  -->   1126   540   184  60825
			'Culture.Media.Entertainment'                   1898  -->    801  1097   237  60540
			'Culture.Media.Films'                           2465  -->   1851   614   194  60016
			'Culture.Media.Media*'                         13819  -->  11733  2086  1525  47331
			'Culture.Media.Music'                           2528  -->   1966   562   185  59962
			'Culture.Media.Radio'                            787  -->    496   291    58  61830
			'Culture.Media.Software'                        2173  -->   1455   718   417  60085
			'Culture.Media.Television'                      2058  -->   1445   613   164  60453
			'Culture.Media.Video games'                     2391  -->   2035   356    94  60190
			'Culture.Performing arts'                       1355  -->    774   581   146  61174
			'Culture.Philosophy and religion'               3678  -->   2102  1576   443  58554
			'Culture.Sports'                                4181  -->   3538   643   172  58322
			'Culture.Visual arts.Architecture'              2461  -->   1646   815   332  59882
			'Culture.Visual arts.Comics and Anime'          2382  -->   1969   413   208  60085
			'Culture.Visual arts.Fashion'                   1197  -->    860   337    96  61382
			'Culture.Visual arts.Visual arts*'              6520  -->   4775  1745   733  55422
			'Geography.Geographical'                        5476  -->   3674  1802   690  56509
			'Geography.Regions.Africa.Africa*'              5584  -->   4405  1179   344  56747
			'Geography.Regions.Africa.Central Africa'       1206  -->    934   272    73  61396
			'Geography.Regions.Africa.Eastern Africa'        974  -->    780   194    31  61670
			'Geography.Regions.Africa.Northern Africa'      1389  -->    977   412   119  61167
			'Geography.Regions.Africa.Southern Africa'      1182  -->    905   277    40  61453
			'Geography.Regions.Africa.Western Africa'        456  -->    257   199    42  62177
			'Geography.Regions.Americas.Central America'    1278  -->    857   421    46  61351
			'Geography.Regions.Americas.North America'      5704  -->   3642  2062   793  56178
			'Geography.Regions.Americas.South America'      1475  -->   1123   352    73  61127
			'Geography.Regions.Asia.Asia*'                 17067  -->  14106  2961  1816  43792
			'Geography.Regions.Asia.Central Asia'           1243  -->    839   404    82  61350
			'Geography.Regions.Asia.East Asia'              8724  -->   6976  1748  1125  52826
			'Geography.Regions.Asia.North Asia'             2736  -->   1844   892   215  59724
			'Geography.Regions.Asia.South Asia'             1809  -->   1376   433    73  60793
			'Geography.Regions.Asia.Southeast Asia'         2061  -->   1426   635   109  60505
			'Geography.Regions.Asia.West Asia'              1985  -->   1354   631   157  60533
			'Geography.Regions.Europe.Eastern Europe'       3992  -->   2895  1097   256  58427
			'Geography.Regions.Europe.Europe*'             13452  -->  10646  2806  1439  47784
			'Geography.Regions.Europe.Northern Europe'      3334  -->   2125  1209   361  58980
			'Geography.Regions.Europe.Southern Europe'      2935  -->   2137   798   233  59507
			'Geography.Regions.Europe.Western Europe'       3782  -->   2725  1057   321  58572
			'Geography.Regions.Oceania'                     1940  -->   1337   603   125  60610
			'History and Society.Business and economics'    3669  -->   1958  1711   460  58546
			'History and Society.Education'                 1908  -->   1129   779   161  60606
			'History and Society.History'                   4145  -->   2110  2035   567  57963
			'History and Society.Military and warfare'      3714  -->   2381  1333   397  58564
			'History and Society.Politics and government'   3796  -->   2043  1753   547  58332
			'History and Society.Society'                   4561  -->   1754  2807   387  57727
			'History and Society.Transportation'            3707  -->   3263   444   192  58776
			'STEM.Biology'                                  3139  -->   2513   626   173  59363
			'STEM.Chemistry'                                1487  -->   1104   383   133  61055
			'STEM.Computing'                                2560  -->   1942   618   452  59663
			'STEM.Earth and environment'                    2428  -->   1973   455   144  60103
			'STEM.Engineering'                              2496  -->   1764   732   203  59976
			'STEM.Libraries & Information'                  1183  -->    835   348    61  61431
			'STEM.Mathematics'                              1181  -->    886   295    92  61402
			'STEM.Medicine & Health'                        1847  -->   1213   634   186  60642
			'STEM.Physics'                                  1366  -->    929   437   179  61130
			'STEM.STEM*'                                   18516  -->  16514  2002  1101  43058
			'STEM.Space'                                    1718  -->   1544   174    48  60909
			'STEM.Technology'                               4322  -->   2882  1440   770  57583
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.216         0.121
		Culture.Biography.Women                         0.051         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.055         0.004
		Culture.Linguistics                             0.025         0.008
		Culture.Literature                              0.089         0.015
		Culture.Media.Books                             0.027         0.004
		Culture.Media.Entertainment                     0.03          0.004
		Culture.Media.Films                             0.039         0.012
		Culture.Media.Media*                            0.22          0.055
		Culture.Media.Music                             0.04          0.021
		Culture.Media.Radio                             0.013         0.002
		Culture.Media.Software                          0.035         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.038         0.003
		Culture.Performing arts                         0.022         0.003
		Culture.Philosophy and religion                 0.059         0.01
		Culture.Sports                                  0.067         0.061
		Culture.Visual arts.Architecture                0.039         0.011
		Culture.Visual arts.Comics and Anime            0.038         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.104         0.018
		Geography.Geographical                          0.087         0.021
		Geography.Regions.Africa.Africa*                0.089         0.009
		Geography.Regions.Africa.Central Africa         0.019         0.001
		Geography.Regions.Africa.Eastern Africa         0.016         0.001
		Geography.Regions.Africa.Northern Africa        0.022         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.007         0.001
		Geography.Regions.Americas.Central America      0.02          0.003
		Geography.Regions.Americas.North America        0.091         0.064
		Geography.Regions.Americas.South America        0.024         0.007
		Geography.Regions.Asia.Asia*                    0.272         0.053
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.139         0.012
		Geography.Regions.Asia.North Asia               0.044         0.006
		Geography.Regions.Asia.South Asia               0.029         0.017
		Geography.Regions.Asia.Southeast Asia           0.033         0.006
		Geography.Regions.Asia.West Asia                0.032         0.012
		Geography.Regions.Europe.Eastern Europe         0.064         0.018
		Geography.Regions.Europe.Europe*                0.215         0.082
		Geography.Regions.Europe.Northern Europe        0.053         0.029
		Geography.Regions.Europe.Southern Europe        0.047         0.014
		Geography.Regions.Europe.Western Europe         0.06          0.021
		Geography.Regions.Oceania                       0.031         0.017
		History and Society.Business and economics      0.059         0.01
		History and Society.Education                   0.03          0.008
		History and Society.History                     0.066         0.011
		History and Society.Military and warfare        0.059         0.015
		History and Society.Politics and government     0.061         0.016
		History and Society.Society                     0.073         0.008
		History and Society.Transportation              0.059         0.016
		STEM.Biology                                    0.05          0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.039         0.005
		STEM.Engineering                                0.04          0.006
		STEM.Libraries & Information                    0.019         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.022         0.001
		STEM.STEM*                                      0.295         0.066
		STEM.Space                                      0.027         0.004
		STEM.Technology                                 0.069         0.005
	match_rate (micro=0.051, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.123
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.008
		Culture.Literature                           0.022
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.019
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.008
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.013
		Culture.Sports                               0.054
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.005
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.026
		Geography.Geographical                       0.026
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.054
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.082
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.03
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.018
		Geography.Regions.Europe.Europe*             0.091
		Geography.Regions.Europe.Northern Europe     0.025
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.02
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.015
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.018
		History and Society.Society                  0.01
		History and Society.Transportation           0.018
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.003
		STEM.Computing                               0.01
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.082
		STEM.Space                                   0.005
		STEM.Technology                              0.017
		-------------------------------------------  -----
	filter_rate (micro=0.949, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.877
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.992
		Culture.Literature                           0.978
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.946
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.995
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.974
		Geography.Geographical                       0.974
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.946
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.918
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.97
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.909
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.985
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.982
		History and Society.Society                  0.99
		History and Society.Transportation           0.982
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.997
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.918
		STEM.Space                                   0.995
		STEM.Technology                              0.983
		-------------------------------------------  -----
	recall (micro=0.761, macro=0.71):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.689
		Culture.Food and drink                       0.672
		Culture.Internet culture                     0.764
		Culture.Linguistics                          0.722
		Culture.Literature                           0.755
		Culture.Media.Books                          0.676
		Culture.Media.Entertainment                  0.422
		Culture.Media.Films                          0.751
		Culture.Media.Media*                         0.849
		Culture.Media.Music                          0.778
		Culture.Media.Radio                          0.63
		Culture.Media.Software                       0.67
		Culture.Media.Television                     0.702
		Culture.Media.Video games                    0.851
		Culture.Performing arts                      0.571
		Culture.Philosophy and religion              0.572
		Culture.Sports                               0.846
		Culture.Visual arts.Architecture             0.669
		Culture.Visual arts.Comics and Anime         0.827
		Culture.Visual arts.Fashion                  0.718
		Culture.Visual arts.Visual arts*             0.732
		Geography.Geographical                       0.671
		Geography.Regions.Africa.Africa*             0.789
		Geography.Regions.Africa.Central Africa      0.774
		Geography.Regions.Africa.Eastern Africa      0.801
		Geography.Regions.Africa.Northern Africa     0.703
		Geography.Regions.Africa.Southern Africa     0.766
		Geography.Regions.Africa.Western Africa      0.564
		Geography.Regions.Americas.Central America   0.671
		Geography.Regions.Americas.North America     0.638
		Geography.Regions.Americas.South America     0.761
		Geography.Regions.Asia.Asia*                 0.827
		Geography.Regions.Asia.Central Asia          0.675
		Geography.Regions.Asia.East Asia             0.8
		Geography.Regions.Asia.North Asia            0.674
		Geography.Regions.Asia.South Asia            0.761
		Geography.Regions.Asia.Southeast Asia        0.692
		Geography.Regions.Asia.West Asia             0.682
		Geography.Regions.Europe.Eastern Europe      0.725
		Geography.Regions.Europe.Europe*             0.791
		Geography.Regions.Europe.Northern Europe     0.637
		Geography.Regions.Europe.Southern Europe     0.728
		Geography.Regions.Europe.Western Europe      0.721
		Geography.Regions.Oceania                    0.689
		History and Society.Business and economics   0.534
		History and Society.Education                0.592
		History and Society.History                  0.509
		History and Society.Military and warfare     0.641
		History and Society.Politics and government  0.538
		History and Society.Society                  0.385
		History and Society.Transportation           0.88
		STEM.Biology                                 0.801
		STEM.Chemistry                               0.742
		STEM.Computing                               0.759
		STEM.Earth and environment                   0.813
		STEM.Engineering                             0.707
		STEM.Libraries & Information                 0.706
		STEM.Mathematics                             0.75
		STEM.Medicine & Health                       0.657
		STEM.Physics                                 0.68
		STEM.STEM*                                   0.892
		STEM.Space                                   0.899
		STEM.Technology                              0.667
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.989
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.969
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.988
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.986
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.96
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.979
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.971
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.992
		History and Society.Education                0.997
		History and Society.History                  0.99
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.699, macro=0.558):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.865
		Culture.Biography.Women                      0.629
		Culture.Food and drink                       0.457
		Culture.Internet culture                     0.406
		Culture.Linguistics                          0.779
		Culture.Literature                           0.512
		Culture.Media.Books                          0.495
		Culture.Media.Entertainment                  0.302
		Culture.Media.Films                          0.733
		Culture.Media.Media*                         0.615
		Culture.Media.Music                          0.845
		Culture.Media.Radio                          0.613
		Culture.Media.Software                       0.114
		Culture.Media.Television                     0.701
		Culture.Media.Video games                    0.616
		Culture.Performing arts                      0.426
		Culture.Philosophy and religion              0.446
		Culture.Sports                               0.949
		Culture.Visual arts.Architecture             0.572
		Culture.Visual arts.Comics and Anime         0.367
		Culture.Visual arts.Fashion                  0.294
		Culture.Visual arts.Visual arts*             0.511
		Geography.Geographical                       0.548
		Geography.Regions.Africa.Africa*             0.531
		Geography.Regions.Africa.Central Africa      0.317
		Geography.Regions.Africa.Eastern Africa      0.447
		Geography.Regions.Africa.Northern Africa     0.331
		Geography.Regions.Africa.Southern Africa     0.609
		Geography.Regions.Africa.Western Africa      0.386
		Geography.Regions.Americas.Central America   0.758
		Geography.Regions.Americas.North America     0.757
		Geography.Regions.Americas.South America     0.816
		Geography.Regions.Asia.Asia*                 0.538
		Geography.Regions.Asia.Central Asia          0.289
		Geography.Regions.Asia.East Asia             0.323
		Geography.Regions.Asia.North Asia            0.517
		Geography.Regions.Asia.South Asia            0.915
		Geography.Regions.Asia.Southeast Asia        0.709
		Geography.Regions.Asia.West Asia             0.759
		Geography.Regions.Europe.Eastern Europe      0.758
		Geography.Regions.Europe.Europe*             0.707
		Geography.Regions.Europe.Northern Europe     0.76
		Geography.Regions.Europe.Southern Europe     0.726
		Geography.Regions.Europe.Western Europe      0.736
		Geography.Regions.Oceania                    0.849
		History and Society.Business and economics   0.404
		History and Society.Education                0.643
		History and Society.History                  0.368
		History and Society.Military and warfare     0.599
		History and Society.Politics and government  0.492
		History and Society.Society                  0.327
		History and Society.Transportation           0.819
		STEM.Biology                                 0.909
		STEM.Chemistry                               0.369
		STEM.Computing                               0.224
		STEM.Earth and environment                   0.62
		STEM.Engineering                             0.55
		STEM.Libraries & Information                 0.33
		STEM.Mathematics                             0.19
		STEM.Medicine & Health                       0.584
		STEM.Physics                                 0.181
		STEM.STEM*                                   0.715
		STEM.Space                                   0.831
		STEM.Technology                              0.209
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.99
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.992
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.993
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.992
		STEM.Space                                   1
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.72, macro=0.604):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.869
		Culture.Biography.Women                      0.657
		Culture.Food and drink                       0.544
		Culture.Internet culture                     0.53
		Culture.Linguistics                          0.749
		Culture.Literature                           0.61
		Culture.Media.Books                          0.572
		Culture.Media.Entertainment                  0.352
		Culture.Media.Films                          0.742
		Culture.Media.Media*                         0.713
		Culture.Media.Music                          0.81
		Culture.Media.Radio                          0.621
		Culture.Media.Software                       0.195
		Culture.Media.Television                     0.702
		Culture.Media.Video games                    0.715
		Culture.Performing arts                      0.488
		Culture.Philosophy and religion              0.501
		Culture.Sports                               0.895
		Culture.Visual arts.Architecture             0.617
		Culture.Visual arts.Comics and Anime         0.508
		Culture.Visual arts.Fashion                  0.417
		Culture.Visual arts.Visual arts*             0.602
		Geography.Geographical                       0.603
		Geography.Regions.Africa.Africa*             0.635
		Geography.Regions.Africa.Central Africa      0.449
		Geography.Regions.Africa.Eastern Africa      0.574
		Geography.Regions.Africa.Northern Africa     0.45
		Geography.Regions.Africa.Southern Africa     0.678
		Geography.Regions.Africa.Western Africa      0.458
		Geography.Regions.Americas.Central America   0.712
		Geography.Regions.Americas.North America     0.693
		Geography.Regions.Americas.South America     0.788
		Geography.Regions.Asia.Asia*                 0.651
		Geography.Regions.Asia.Central Asia          0.405
		Geography.Regions.Asia.East Asia             0.46
		Geography.Regions.Asia.North Asia            0.585
		Geography.Regions.Asia.South Asia            0.831
		Geography.Regions.Asia.Southeast Asia        0.7
		Geography.Regions.Asia.West Asia             0.719
		Geography.Regions.Europe.Eastern Europe      0.741
		Geography.Regions.Europe.Europe*             0.747
		Geography.Regions.Europe.Northern Europe     0.693
		Geography.Regions.Europe.Southern Europe     0.727
		Geography.Regions.Europe.Western Europe      0.728
		Geography.Regions.Oceania                    0.761
		History and Society.Business and economics   0.46
		History and Society.Education                0.616
		History and Society.History                  0.427
		History and Society.Military and warfare     0.619
		History and Society.Politics and government  0.514
		History and Society.Society                  0.353
		History and Society.Transportation           0.848
		STEM.Biology                                 0.851
		STEM.Chemistry                               0.493
		STEM.Computing                               0.346
		STEM.Earth and environment                   0.703
		STEM.Engineering                             0.619
		STEM.Libraries & Information                 0.45
		STEM.Mathematics                             0.303
		STEM.Medicine & Health                       0.618
		STEM.Physics                                 0.285
		STEM.STEM*                                   0.794
		STEM.Space                                   0.864
		STEM.Technology                              0.318
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.981
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.976
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.992
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.984
		STEM.Space                                   0.999
		STEM.Technology                              0.992
		-------------------------------------------  -----
	accuracy (micro=0.978, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.968
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.986
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.962
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.982
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.964
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.953
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.977
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.956
		Geography.Regions.Europe.Northern Europe     0.983
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.985
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.983
		History and Society.Society                  0.988
		History and Society.Transportation           0.995
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.999
		STEM.Technology                              0.985
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.019
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.011
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.031
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.002
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.006
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.013
		Geography.Geographical                       0.012
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.014
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.04
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.021
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.029
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.005
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.008
		History and Society.Education                0.003
		History and Society.History                  0.01
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.009
		History and Society.Society                  0.007
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.025
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.973, macro=0.976):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.981
		Culture.Internet culture                     0.983
		Culture.Linguistics                          0.979
		Culture.Literature                           0.977
		Culture.Media.Books                          0.981
		Culture.Media.Entertainment                  0.963
		Culture.Media.Films                          0.98
		Culture.Media.Media*                         0.976
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.971
		Culture.Media.Software                       0.983
		Culture.Media.Television                     0.979
		Culture.Media.Video games                    0.988
		Culture.Performing arts                      0.975
		Culture.Philosophy and religion              0.962
		Culture.Sports                               0.98
		Culture.Visual arts.Architecture             0.978
		Culture.Visual arts.Comics and Anime         0.988
		Culture.Visual arts.Fashion                  0.983
		Culture.Visual arts.Visual arts*             0.97
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.978
		Geography.Regions.Africa.Central Africa      0.983
		Geography.Regions.Africa.Eastern Africa      0.984
		Geography.Regions.Africa.Northern Africa     0.978
		Geography.Regions.Africa.Southern Africa     0.979
		Geography.Regions.Africa.Western Africa      0.969
		Geography.Regions.Americas.Central America   0.977
		Geography.Regions.Americas.North America     0.964
		Geography.Regions.Americas.South America     0.981
		Geography.Regions.Asia.Asia*                 0.964
		Geography.Regions.Asia.Central Asia          0.978
		Geography.Regions.Asia.East Asia             0.976
		Geography.Regions.Asia.North Asia            0.973
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.98
		Geography.Regions.Asia.West Asia             0.977
		Geography.Regions.Europe.Eastern Europe      0.973
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.968
		Geography.Regions.Europe.Southern Europe     0.977
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.975
		History and Society.Business and economics   0.959
		History and Society.Education                0.972
		History and Society.History                  0.952
		History and Society.Military and warfare     0.969
		History and Society.Politics and government  0.958
		History and Society.Society                  0.921
		History and Society.Transportation           0.985
		STEM.Biology                                 0.982
		STEM.Chemistry                               0.987
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.983
		STEM.Engineering                             0.979
		STEM.Libraries & Information                 0.982
		STEM.Mathematics                             0.985
		STEM.Medicine & Health                       0.976
		STEM.Physics                                 0.984
		STEM.STEM*                                   0.978
		STEM.Space                                   0.992
		STEM.Technology                              0.973
		-------------------------------------------  -----
	pr_auc (micro=0.77, macro=0.621):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.932
		Culture.Biography.Women                      0.657
		Culture.Food and drink                       0.556
		Culture.Internet culture                     0.651
		Culture.Linguistics                          0.778
		Culture.Literature                           0.677
		Culture.Media.Books                          0.586
		Culture.Media.Entertainment                  0.26
		Culture.Media.Films                          0.78
		Culture.Media.Media*                         0.816
		Culture.Media.Music                          0.861
		Culture.Media.Radio                          0.548
		Culture.Media.Software                       0.133
		Culture.Media.Television                     0.702
		Culture.Media.Video games                    0.824
		Culture.Performing arts                      0.474
		Culture.Philosophy and religion              0.477
		Culture.Sports                               0.936
		Culture.Visual arts.Architecture             0.621
		Culture.Visual arts.Comics and Anime         0.693
		Culture.Visual arts.Fashion                  0.349
		Culture.Visual arts.Visual arts*             0.621
		Geography.Geographical                       0.664
		Geography.Regions.Africa.Africa*             0.721
		Geography.Regions.Africa.Central Africa      0.385
		Geography.Regions.Africa.Eastern Africa      0.564
		Geography.Regions.Africa.Northern Africa     0.35
		Geography.Regions.Africa.Southern Africa     0.694
		Geography.Regions.Africa.Western Africa      0.264
		Geography.Regions.Americas.Central America   0.706
		Geography.Regions.Americas.North America     0.759
		Geography.Regions.Americas.South America     0.81
		Geography.Regions.Asia.Asia*                 0.716
		Geography.Regions.Asia.Central Asia          0.315
		Geography.Regions.Asia.East Asia             0.518
		Geography.Regions.Asia.North Asia            0.619
		Geography.Regions.Asia.South Asia            0.881
		Geography.Regions.Asia.Southeast Asia        0.685
		Geography.Regions.Asia.West Asia             0.756
		Geography.Regions.Europe.Eastern Europe      0.787
		Geography.Regions.Europe.Europe*             0.82
		Geography.Regions.Europe.Northern Europe     0.739
		Geography.Regions.Europe.Southern Europe     0.767
		Geography.Regions.Europe.Western Europe      0.775
		Geography.Regions.Oceania                    0.805
		History and Society.Business and economics   0.4
		History and Society.Education                0.639
		History and Society.History                  0.408
		History and Society.Military and warfare     0.644
		History and Society.Politics and government  0.497
		History and Society.Society                  0.316
		History and Society.Transportation           0.878
		STEM.Biology                                 0.91
		STEM.Chemistry                               0.541
		STEM.Computing                               0.286
		STEM.Earth and environment                   0.704
		STEM.Engineering                             0.669
		STEM.Libraries & Information                 0.388
		STEM.Mathematics                             0.393
		STEM.Medicine & Health                       0.634
		STEM.Physics                                 0.234
		STEM.STEM*                                   0.895
		STEM.Space                                   0.924
		STEM.Technology                              0.327
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'STEM.Engineering': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}}}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}}}

