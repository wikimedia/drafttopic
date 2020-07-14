Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'min_samples_split': 2, 'random_state': None, 'presort': 'deprecated', 'criterion': 'friedman_mse', 'init': None, 'n_estimators': 150, 'label_weights': {}, 'min_weight_fraction_leaf': 0.0, 'min_impurity_split': None, 'scale': False, 'max_leaf_nodes': None, 'tol': 0.0001, 'min_impurity_decrease': 0.0, 'learning_rate': 0.1, 'ccp_alpha': 0.0, 'loss': 'deviance', 'warm_start': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'n_iter_no_change': None, 'min_samples_leaf': 1, 'subsample': 1.0, 'population_rates': None, 'validation_fraction': 0.1, 'max_features': 'log2', 'max_depth': 5, 'multilabel': True, 'center': False, 'verbose': 0}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-12-amd64-x86_64-with-debian-9.12'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.210-1+deb9u1 (2020-06-07)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-12-amd64'
	
	Statistics:
	counts (n=63880):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16539  -->  14663  1876  1218  46123
			'Culture.Biography.Women'                       4162  -->   3180   982   812  58906
			'Culture.Food and drink'                        1301  -->    916   385    69  62510
			'Culture.Internet culture'                      2969  -->   2307   662   200  60711
			'Culture.Linguistics'                           1367  -->   1027   340   104  62409
			'Culture.Literature'                            5298  -->   3939  1359   433  58149
			'Culture.Media.Books'                           1906  -->   1355   551   198  61776
			'Culture.Media.Entertainment'                   1825  -->    917   908   173  61882
			'Culture.Media.Films'                           2347  -->   1940   407   145  61388
			'Culture.Media.Media*'                         14457  -->  12411  2046  1445  47978
			'Culture.Media.Music'                           2665  -->   2162   503   292  60923
			'Culture.Media.Radio'                           1191  -->    963   228    28  62661
			'Culture.Media.Software'                        1784  -->   1028   756   349  61747
			'Culture.Media.Television'                      2224  -->   1694   530   179  61477
			'Culture.Media.Video games'                     2114  -->   1904   210    36  61730
			'Culture.Performing arts'                       1324  -->    854   470   101  62455
			'Culture.Philosophy and religion'               2712  -->   1579  1133   339  60829
			'Culture.Sports'                                5901  -->   5302   599   306  57673
			'Culture.Visual arts.Architecture'              2571  -->   1906   665   250  61059
			'Culture.Visual arts.Comics and Anime'          1509  -->   1231   278    91  62280
			'Culture.Visual arts.Fashion'                   1173  -->    805   368    46  62661
			'Culture.Visual arts.Visual arts*'              5989  -->   4575  1414   521  57370
			'Geography.Geographical'                        3518  -->   2284  1234   278  60084
			'Geography.Regions.Africa.Africa*'              6484  -->   5678   806   359  57037
			'Geography.Regions.Africa.Central Africa'       1155  -->    887   268    35  62690
			'Geography.Regions.Africa.Eastern Africa'       1100  -->    901   199    36  62744
			'Geography.Regions.Africa.Northern Africa'      1309  -->    999   310    94  62477
			'Geography.Regions.Africa.Southern Africa'      1260  -->   1011   249    43  62577
			'Geography.Regions.Africa.Western Africa'       1151  -->    958   193    65  62664
			'Geography.Regions.Americas.Central America'    1302  -->    931   371    88  62490
			'Geography.Regions.Americas.North America'      7482  -->   5303  2179  1251  55147
			'Geography.Regions.Americas.South America'      1575  -->   1156   419   134  62171
			'Geography.Regions.Asia.Asia*'                 11206  -->   9648  1558   824  51850
			'Geography.Regions.Asia.Central Asia'           1133  -->    889   244    45  62702
			'Geography.Regions.Asia.East Asia'              2749  -->   2089   660   256  60875
			'Geography.Regions.Asia.North Asia'             1369  -->    929   440   183  62328
			'Geography.Regions.Asia.South Asia'             2428  -->   2104   324   118  61334
			'Geography.Regions.Asia.Southeast Asia'         1726  -->   1358   368   103  62051
			'Geography.Regions.Asia.West Asia'              2301  -->   1897   404   124  61455
			'Geography.Regions.Europe.Eastern Europe'       3088  -->   2460   628   292  60500
			'Geography.Regions.Europe.Europe*'             12265  -->   9544  2721  1743  49872
			'Geography.Regions.Europe.Northern Europe'      4099  -->   2867  1232   637  59144
			'Geography.Regions.Europe.Southern Europe'      2397  -->   1720   677   297  61186
			'Geography.Regions.Europe.Western Europe'       3062  -->   2119   943   444  60374
			'Geography.Regions.Oceania'                     2535  -->   2103   432   146  61199
			'History and Society.Business and economics'    3458  -->   1651  1807   561  59861
			'History and Society.Education'                 2204  -->   1073  1131   244  61432
			'History and Society.History'                   3307  -->   1380  1927   513  60060
			'History and Society.Military and warfare'      4048  -->   2928  1120   380  59452
			'History and Society.Politics and government'   4604  -->   2919  1685   468  58808
			'History and Society.Society'                   4009  -->   1667  2342   407  59464
			'History and Society.Transportation'            3601  -->   3115   486   196  60083
			'STEM.Biology'                                  2951  -->   2421   530   146  60783
			'STEM.Chemistry'                                1319  -->    933   386   152  62409
			'STEM.Computing'                                2102  -->   1394   708   427  61351
			'STEM.Earth and environment'                    1619  -->   1156   463   123  62138
			'STEM.Engineering'                              2361  -->   1704   657   184  61335
			'STEM.Libraries & Information'                  1165  -->    691   474    80  62635
			'STEM.Mathematics'                              1136  -->    766   370    69  62675
			'STEM.Medicine & Health'                        1784  -->   1200   584   167  61929
			'STEM.Physics'                                  1173  -->    766   407   135  62572
			'STEM.STEM*'                                   16613  -->  14497  2116  1062  46205
			'STEM.Space'                                    1412  -->   1219   193    50  62418
			'STEM.Technology'                               3691  -->   2310  1381   611  59578
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.259         0.123
		Culture.Biography.Women                         0.065         0.015
		Culture.Food and drink                          0.02          0.002
		Culture.Internet culture                        0.046         0.003
		Culture.Linguistics                             0.021         0.007
		Culture.Literature                              0.083         0.015
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.029         0.004
		Culture.Media.Films                             0.037         0.011
		Culture.Media.Media*                            0.226         0.058
		Culture.Media.Music                             0.042         0.024
		Culture.Media.Radio                             0.019         0.002
		Culture.Media.Software                          0.028         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.033         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.011
		Culture.Sports                                  0.092         0.071
		Culture.Visual arts.Architecture                0.04          0.011
		Culture.Visual arts.Comics and Anime            0.024         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.094         0.018
		Geography.Geographical                          0.055         0.024
		Geography.Regions.Africa.Africa*                0.102         0.008
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.017         0
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.02          0.003
		Geography.Regions.Americas.North America        0.117         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.175         0.045
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.043         0.011
		Geography.Regions.Asia.North Asia               0.021         0.001
		Geography.Regions.Asia.South Asia               0.038         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.048         0.013
		Geography.Regions.Europe.Europe*                0.192         0.076
		Geography.Regions.Europe.Northern Europe        0.064         0.031
		Geography.Regions.Europe.Southern Europe        0.038         0.013
		Geography.Regions.Europe.Western Europe         0.048         0.019
		Geography.Regions.Oceania                       0.04          0.015
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.035         0.007
		History and Society.History                     0.052         0.011
		History and Society.Military and warfare        0.063         0.014
		History and Society.Politics and government     0.072         0.028
		History and Society.Society                     0.063         0.013
		History and Society.Transportation              0.056         0.015
		STEM.Biology                                    0.046         0.034
		STEM.Chemistry                                  0.021         0.002
		STEM.Computing                                  0.033         0.003
		STEM.Earth and environment                      0.025         0.005
		STEM.Engineering                                0.037         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.028         0.006
		STEM.Physics                                    0.018         0.001
		STEM.STEM*                                      0.26          0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.058         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.132
		Culture.Biography.Women                      0.025
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.019
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.078
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.069
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.02
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.066
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.054
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.015
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.09
		Geography.Regions.Europe.Northern Europe     0.032
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.02
		Geography.Regions.Oceania                    0.015
		History and Society.Business and economics   0.014
		History and Society.Education                0.008
		History and Society.History                  0.013
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.026
		History and Society.Society                  0.012
		History and Society.Transportation           0.016
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.081
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.868
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.981
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.922
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.931
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.98
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.934
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.946
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.91
		Geography.Regions.Europe.Northern Europe     0.968
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.987
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.974
		History and Society.Society                  0.988
		History and Society.Transportation           0.984
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.919
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.783, macro=0.732):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.887
		Culture.Biography.Women                      0.764
		Culture.Food and drink                       0.704
		Culture.Internet culture                     0.777
		Culture.Linguistics                          0.751
		Culture.Literature                           0.743
		Culture.Media.Books                          0.711
		Culture.Media.Entertainment                  0.502
		Culture.Media.Films                          0.827
		Culture.Media.Media*                         0.858
		Culture.Media.Music                          0.811
		Culture.Media.Radio                          0.809
		Culture.Media.Software                       0.576
		Culture.Media.Television                     0.762
		Culture.Media.Video games                    0.901
		Culture.Performing arts                      0.645
		Culture.Philosophy and religion              0.582
		Culture.Sports                               0.898
		Culture.Visual arts.Architecture             0.741
		Culture.Visual arts.Comics and Anime         0.816
		Culture.Visual arts.Fashion                  0.686
		Culture.Visual arts.Visual arts*             0.764
		Geography.Geographical                       0.649
		Geography.Regions.Africa.Africa*             0.876
		Geography.Regions.Africa.Central Africa      0.768
		Geography.Regions.Africa.Eastern Africa      0.819
		Geography.Regions.Africa.Northern Africa     0.763
		Geography.Regions.Africa.Southern Africa     0.802
		Geography.Regions.Africa.Western Africa      0.832
		Geography.Regions.Americas.Central America   0.715
		Geography.Regions.Americas.North America     0.709
		Geography.Regions.Americas.South America     0.734
		Geography.Regions.Asia.Asia*                 0.861
		Geography.Regions.Asia.Central Asia          0.785
		Geography.Regions.Asia.East Asia             0.76
		Geography.Regions.Asia.North Asia            0.679
		Geography.Regions.Asia.South Asia            0.867
		Geography.Regions.Asia.Southeast Asia        0.787
		Geography.Regions.Asia.West Asia             0.824
		Geography.Regions.Europe.Eastern Europe      0.797
		Geography.Regions.Europe.Europe*             0.778
		Geography.Regions.Europe.Northern Europe     0.699
		Geography.Regions.Europe.Southern Europe     0.718
		Geography.Regions.Europe.Western Europe      0.692
		Geography.Regions.Oceania                    0.83
		History and Society.Business and economics   0.477
		History and Society.Education                0.487
		History and Society.History                  0.417
		History and Society.Military and warfare     0.723
		History and Society.Politics and government  0.634
		History and Society.Society                  0.416
		History and Society.Transportation           0.865
		STEM.Biology                                 0.82
		STEM.Chemistry                               0.707
		STEM.Computing                               0.663
		STEM.Earth and environment                   0.714
		STEM.Engineering                             0.722
		STEM.Libraries & Information                 0.593
		STEM.Mathematics                             0.674
		STEM.Medicine & Health                       0.673
		STEM.Physics                                 0.653
		STEM.STEM*                                   0.873
		STEM.Space                                   0.863
		STEM.Technology                              0.626
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.992
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.998
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.978
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.711, macro=0.58):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.829
		Culture.Biography.Women                      0.454
		Culture.Food and drink                       0.612
		Culture.Internet culture                     0.454
		Culture.Linguistics                          0.769
		Culture.Literature                           0.613
		Culture.Media.Books                          0.474
		Culture.Media.Entertainment                  0.393
		Culture.Media.Films                          0.788
		Culture.Media.Media*                         0.646
		Culture.Media.Music                          0.806
		Culture.Media.Radio                          0.796
		Culture.Media.Software                       0.12
		Culture.Media.Television                     0.7
		Culture.Media.Video games                    0.802
		Culture.Performing arts                      0.536
		Culture.Philosophy and religion              0.531
		Culture.Sports                               0.929
		Culture.Visual arts.Architecture             0.66
		Culture.Visual arts.Comics and Anime         0.552
		Culture.Visual arts.Fashion                  0.431
		Culture.Visual arts.Visual arts*             0.613
		Geography.Geographical                       0.773
		Geography.Regions.Africa.Africa*             0.524
		Geography.Regions.Africa.Central Africa      0.465
		Geography.Regions.Africa.Eastern Africa      0.394
		Geography.Regions.Africa.Northern Africa     0.384
		Geography.Regions.Africa.Southern Africa     0.579
		Geography.Regions.Africa.Western Africa      0.355
		Geography.Regions.Americas.Central America   0.627
		Geography.Regions.Americas.North America     0.687
		Geography.Regions.Americas.South America     0.684
		Geography.Regions.Asia.Asia*                 0.724
		Geography.Regions.Asia.Central Asia          0.487
		Geography.Regions.Asia.East Asia             0.677
		Geography.Regions.Asia.North Asia            0.176
		Geography.Regions.Asia.South Asia            0.874
		Geography.Regions.Asia.Southeast Asia        0.742
		Geography.Regions.Asia.West Asia             0.819
		Geography.Regions.Europe.Eastern Europe      0.683
		Geography.Regions.Europe.Europe*             0.655
		Geography.Regions.Europe.Northern Europe     0.674
		Geography.Regions.Europe.Southern Europe     0.662
		Geography.Regions.Europe.Western Europe      0.649
		Geography.Regions.Oceania                    0.843
		History and Society.Business and economics   0.344
		History and Society.Education                0.477
		History and Society.History                  0.351
		History and Society.Military and warfare     0.619
		History and Society.Politics and government  0.7
		History and Society.Society                  0.439
		History and Society.Transportation           0.803
		STEM.Biology                                 0.923
		STEM.Chemistry                               0.312
		STEM.Computing                               0.206
		STEM.Earth and environment                   0.622
		STEM.Engineering                             0.559
		STEM.Libraries & Information                 0.224
		STEM.Mathematics                             0.204
		STEM.Medicine & Health                       0.617
		STEM.Physics                                 0.205
		STEM.STEM*                                   0.743
		STEM.Space                                   0.867
		STEM.Technology                              0.241
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.98
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.993
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.989
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.741, macro=0.632):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.857
		Culture.Biography.Women                      0.569
		Culture.Food and drink                       0.655
		Culture.Internet culture                     0.573
		Culture.Linguistics                          0.76
		Culture.Literature                           0.672
		Culture.Media.Books                          0.568
		Culture.Media.Entertainment                  0.441
		Culture.Media.Films                          0.807
		Culture.Media.Media*                         0.737
		Culture.Media.Music                          0.809
		Culture.Media.Radio                          0.802
		Culture.Media.Software                       0.199
		Culture.Media.Television                     0.73
		Culture.Media.Video games                    0.848
		Culture.Performing arts                      0.586
		Culture.Philosophy and religion              0.555
		Culture.Sports                               0.913
		Culture.Visual arts.Architecture             0.698
		Culture.Visual arts.Comics and Anime         0.658
		Culture.Visual arts.Fashion                  0.529
		Culture.Visual arts.Visual arts*             0.68
		Geography.Geographical                       0.706
		Geography.Regions.Africa.Africa*             0.656
		Geography.Regions.Africa.Central Africa      0.579
		Geography.Regions.Africa.Eastern Africa      0.532
		Geography.Regions.Africa.Northern Africa     0.511
		Geography.Regions.Africa.Southern Africa     0.673
		Geography.Regions.Africa.Western Africa      0.497
		Geography.Regions.Americas.Central America   0.668
		Geography.Regions.Americas.North America     0.698
		Geography.Regions.Americas.South America     0.708
		Geography.Regions.Asia.Asia*                 0.787
		Geography.Regions.Asia.Central Asia          0.601
		Geography.Regions.Asia.East Asia             0.716
		Geography.Regions.Asia.North Asia            0.28
		Geography.Regions.Asia.South Asia            0.87
		Geography.Regions.Asia.Southeast Asia        0.763
		Geography.Regions.Asia.West Asia             0.822
		Geography.Regions.Europe.Eastern Europe      0.735
		Geography.Regions.Europe.Europe*             0.711
		Geography.Regions.Europe.Northern Europe     0.687
		Geography.Regions.Europe.Southern Europe     0.689
		Geography.Regions.Europe.Western Europe      0.67
		Geography.Regions.Oceania                    0.836
		History and Society.Business and economics   0.4
		History and Society.Education                0.482
		History and Society.History                  0.381
		History and Society.Military and warfare     0.667
		History and Society.Politics and government  0.665
		History and Society.Society                  0.427
		History and Society.Transportation           0.833
		STEM.Biology                                 0.868
		STEM.Chemistry                               0.433
		STEM.Computing                               0.314
		STEM.Earth and environment                   0.665
		STEM.Engineering                             0.63
		STEM.Libraries & Information                 0.325
		STEM.Mathematics                             0.313
		STEM.Medicine & Health                       0.644
		STEM.Physics                                 0.312
		STEM.STEM*                                   0.802
		STEM.Space                                   0.865
		STEM.Technology                              0.348
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.989
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.974
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.991
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.984
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.963
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.997
		Culture.Literature                           0.989
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.964
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.979
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.952
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.985
		History and Society.Military and warfare     0.99
		History and Society.Politics and government  0.982
		History and Society.Society                  0.986
		History and Society.Transportation           0.995
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.97
		STEM.Space                                   0.998
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.026
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.002
		Culture.Literature                           0.007
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.029
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.005
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.022
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.016
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.034
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.008
		History and Society.Military and warfare     0.006
		History and Society.Politics and government  0.008
		History and Society.Society                  0.007
		History and Society.Transportation           0.003
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.002
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.022
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.976, macro=0.978):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.982
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.978
		Culture.Literature                           0.977
		Culture.Media.Books                          0.981
		Culture.Media.Entertainment                  0.968
		Culture.Media.Films                          0.983
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.987
		Culture.Media.Software                       0.98
		Culture.Media.Television                     0.981
		Culture.Media.Video games                    0.993
		Culture.Performing arts                      0.981
		Culture.Philosophy and religion              0.964
		Culture.Sports                               0.984
		Culture.Visual arts.Architecture             0.983
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.983
		Culture.Visual arts.Visual arts*             0.976
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.988
		Geography.Regions.Africa.Eastern Africa      0.984
		Geography.Regions.Africa.Northern Africa     0.981
		Geography.Regions.Africa.Southern Africa     0.985
		Geography.Regions.Africa.Western Africa      0.983
		Geography.Regions.Americas.Central America   0.982
		Geography.Regions.Americas.North America     0.966
		Geography.Regions.Americas.South America     0.983
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.987
		Geography.Regions.Asia.East Asia             0.981
		Geography.Regions.Asia.North Asia            0.985
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.982
		Geography.Regions.Asia.West Asia             0.986
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.977
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.958
		History and Society.Education                0.96
		History and Society.History                  0.944
		History and Society.Military and warfare     0.978
		History and Society.Politics and government  0.965
		History and Society.Society                  0.929
		History and Society.Transportation           0.986
		STEM.Biology                                 0.981
		STEM.Chemistry                               0.984
		STEM.Computing                               0.981
		STEM.Earth and environment                   0.978
		STEM.Engineering                             0.98
		STEM.Libraries & Information                 0.975
		STEM.Mathematics                             0.981
		STEM.Medicine & Health                       0.978
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.977
		STEM.Space                                   0.987
		STEM.Technology                              0.969
		-------------------------------------------  -----
	pr_auc (micro=0.788, macro=0.656):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.909
		Culture.Biography.Women                      0.567
		Culture.Food and drink                       0.625
		Culture.Internet culture                     0.739
		Culture.Linguistics                          0.785
		Culture.Literature                           0.742
		Culture.Media.Books                          0.597
		Culture.Media.Entertainment                  0.415
		Culture.Media.Films                          0.844
		Culture.Media.Media*                         0.847
		Culture.Media.Music                          0.853
		Culture.Media.Radio                          0.85
		Culture.Media.Software                       0.187
		Culture.Media.Television                     0.77
		Culture.Media.Video games                    0.902
		Culture.Performing arts                      0.593
		Culture.Philosophy and religion              0.538
		Culture.Sports                               0.947
		Culture.Visual arts.Architecture             0.749
		Culture.Visual arts.Comics and Anime         0.74
		Culture.Visual arts.Fashion                  0.513
		Culture.Visual arts.Visual arts*             0.756
		Geography.Geographical                       0.757
		Geography.Regions.Africa.Africa*             0.718
		Geography.Regions.Africa.Central Africa      0.627
		Geography.Regions.Africa.Eastern Africa      0.459
		Geography.Regions.Africa.Northern Africa     0.422
		Geography.Regions.Africa.Southern Africa     0.654
		Geography.Regions.Africa.Western Africa      0.446
		Geography.Regions.Americas.Central America   0.672
		Geography.Regions.Americas.North America     0.767
		Geography.Regions.Americas.South America     0.745
		Geography.Regions.Asia.Asia*                 0.841
		Geography.Regions.Asia.Central Asia          0.714
		Geography.Regions.Asia.East Asia             0.739
		Geography.Regions.Asia.North Asia            0.223
		Geography.Regions.Asia.South Asia            0.896
		Geography.Regions.Asia.Southeast Asia        0.74
		Geography.Regions.Asia.West Asia             0.875
		Geography.Regions.Europe.Eastern Europe      0.775
		Geography.Regions.Europe.Europe*             0.768
		Geography.Regions.Europe.Northern Europe     0.713
		Geography.Regions.Europe.Southern Europe     0.711
		Geography.Regions.Europe.Western Europe      0.684
		Geography.Regions.Oceania                    0.86
		History and Society.Business and economics   0.345
		History and Society.Education                0.436
		History and Society.History                  0.319
		History and Society.Military and warfare     0.706
		History and Society.Politics and government  0.709
		History and Society.Society                  0.398
		History and Society.Transportation           0.877
		STEM.Biology                                 0.915
		STEM.Chemistry                               0.459
		STEM.Computing                               0.301
		STEM.Earth and environment                   0.691
		STEM.Engineering                             0.652
		STEM.Libraries & Information                 0.356
		STEM.Mathematics                             0.385
		STEM.Medicine & Health                       0.655
		STEM.Physics                                 0.325
		STEM.STEM*                                   0.897
		STEM.Space                                   0.904
		STEM.Technology                              0.365
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'type': 'object', 'properties': {'History and Society.Education': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}}}

