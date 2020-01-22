Model Information:
	 - type: GradientBoosting
	 - version: 1.1.0
	 - params: {'random_state': None, 'learning_rate': 0.1, 'min_samples_split': 2, 'max_features': 'log2', 'center': False, 'min_impurity_decrease': 0.0, 'n_iter_no_change': None, 'subsample': 1.0, 'criterion': 'friedman_mse', 'warm_start': False, 'multilabel': True, 'max_leaf_nodes': None, 'verbose': 0, 'min_impurity_split': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'label_weights': {}, 'loss': 'deviance', 'validation_fraction': 0.1, 'n_estimators': 150, 'max_depth': 5, 'presort': 'auto', 'min_samples_leaf': 1, 'scale': False, 'init': None, 'min_weight_fraction_leaf': 0.0, 'population_rates': None, 'tol': 0.0001}
	Environment:
	 - revscoring_version: '2.6.3'
	 - platform: 'Linux-4.9.0-11-amd64-x86_64-with-debian-9.11'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.189-3+deb9u1 (2019-09-20)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-11-amd64'
	
	Statistics:
	counts (n=60036):
			label                                              n          TP    FP     FN     TN
			---------------------------------------------  -----  ---  -----  ----  -----  -----
			'Culture.Biography.Biography*'                 16215  -->  13804  2411   1294  42527
			'Culture.Biography.Women'                       4019  -->   2843  1176    750  55267
			'Culture.Food and drink'                        1229  -->    823   406     74  58733
			'Culture.Internet culture'                      2685  -->   2020   665    197  57154
			'Culture.Linguistics'                           1169  -->    790   379     70  58797
			'Culture.Literature'                            5060  -->   3470  1590    581  54395
			'Culture.Media.Books'                           1770  -->   1128   642    184  58082
			'Culture.Media.Entertainment'                   1661  -->    753   908    154  58221
			'Culture.Media.Films'                           2185  -->   1661   524    174  57677
			'Culture.Media.Media*'                         13423  -->  11089  2334   1576  45037
			'Culture.Media.Music'                           2499  -->   1906   593    287  57250
			'Culture.Media.Radio'                           1105  -->    846   259     37  58894
			'Culture.Media.Software'                        1665  -->    904   761    300  58071
			'Culture.Media.Television'                      2032  -->   1314   718    197  57807
			'Culture.Media.Video games'                     1899  -->   1649   250     61  58076
			'Culture.Performing arts'                       1270  -->    806   464    107  58659
			'Culture.Philosophy and religion'               2492  -->   1268  1224    304  57240
			'Culture.Sports'                                5757  -->   5137   620    347  53932
			'Culture.Visual arts.Architecture'              2428  -->   1681   747    286  57322
			'Culture.Visual arts.Comics and Anime'          1448  -->   1102   346    112  58476
			'Culture.Visual arts.Fashion'                   1115  -->    799   316     79  58842
			'Culture.Visual arts.Visual arts*'              5706  -->   4129  1577    578  53752
			'Geography.Geographical'                        3402  -->   2304  1098    283  56351
			'Geography.Regions.Africa.Africa*'              5506  -->   4581   925    242  54288
			'Geography.Regions.Africa.Central Africa'         65  -->     12    53  11616  48355
			'Geography.Regions.Africa.Eastern Africa'       1085  -->    842   243     28  58923
			'Geography.Regions.Africa.Northern Africa'      1267  -->    887   380     79  58690
			'Geography.Regions.Africa.Southern Africa'      1215  -->    897   318     62  58759
			'Geography.Regions.Africa.Western Africa'       1110  -->    876   234     57  58869
			'Geography.Regions.Americas.Central America'    1243  -->    793   450     67  58726
			'Geography.Regions.Americas.North America'      7148  -->   4538  2610   1108  51780
			'Geography.Regions.Americas.South America'      1497  -->   1066   431    146  58393
			'Geography.Regions.Asia.Asia*'                 10670  -->   8866  1804    867  48499
			'Geography.Regions.Asia.Central Asia'           1082  -->    795   287     45  58909
			'Geography.Regions.Asia.East Asia'              2586  -->   1931   655    266  57184
			'Geography.Regions.Asia.North Asia'             1337  -->    845   492    200  58499
			'Geography.Regions.Asia.South Asia'             2325  -->   1908   417    120  57591
			'Geography.Regions.Asia.Southeast Asia'         1610  -->   1169   441     92  58334
			'Geography.Regions.Asia.West Asia'              2198  -->   1657   541    134  57704
			'Geography.Regions.Europe.Eastern Europe'       2992  -->   2251   741    273  56771
			'Geography.Regions.Europe.Europe*'             12062  -->   8871  3191   1773  46201
			'Geography.Regions.Europe.Northern Europe'      4062  -->   2558  1504    596  55378
			'Geography.Regions.Europe.Southern Europe'      2316  -->   1508   808    259  57461
			'Geography.Regions.Europe.Western Europe'       3064  -->   1880  1184    361  56611
			'Geography.Regions.Oceania'                     2478  -->   1905   573    121  57437
			'History and Society.Business and economics'    3356  -->   1435  1921    502  56178
			'History and Society.Education'                 2059  -->    964  1095    257  57720
			'History and Society.History'                   3138  -->   1261  1877    443  56455
			'History and Society.Military and warfare'      3829  -->   2597  1232    410  55797
			'History and Society.Politics and government'   4372  -->   2542  1830    464  55200
			'History and Society.Society'                   3804  -->   1343  2461    372  55860
			'History and Society.Transportation'            3427  -->   2839   588    239  56370
			'STEM.Biology'                                  2702  -->   2156   546    126  57208
			'STEM.Chemistry'                                1241  -->    820   421    151  58644
			'STEM.Computing'                                1916  -->   1219   697    422  57698
			'STEM.Earth and environment'                    1542  -->   1044   498     84  58410
			'STEM.Engineering'                              2164  -->   1508   656    182  57690
			'STEM.Libraries & Information'                  1105  -->    594   511     64  58867
			'STEM.Mathematics'                              1077  -->    767   310     84  58875
			'STEM.Medicine & Health'                        1637  -->   1039   598    169  58230
			'STEM.Physics'                                  1152  -->    725   427    133  58751
			'STEM.STEM*'                                   15499  -->  13109  2390   1092  43445
			'STEM.Space'                                    1321  -->   1136   185     62  58653
			'STEM.Technology'                               3389  -->   1987  1402    559  56088
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.27          0.123
		Culture.Biography.Women                         0.067         0.015
		Culture.Food and drink                          0.02          0.002
		Culture.Internet culture                        0.045         0.004
		Culture.Linguistics                             0.019         0.007
		Culture.Literature                              0.084         0.016
		Culture.Media.Books                             0.029         0.004
		Culture.Media.Entertainment                     0.028         0.004
		Culture.Media.Films                             0.036         0.011
		Culture.Media.Media*                            0.224         0.059
		Culture.Media.Music                             0.042         0.024
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.028         0.001
		Culture.Media.Television                        0.034         0.009
		Culture.Media.Video games                       0.032         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.011
		Culture.Sports                                  0.096         0.071
		Culture.Visual arts.Architecture                0.04          0.011
		Culture.Visual arts.Comics and Anime            0.024         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.095         0.018
		Geography.Geographical                          0.057         0.024
		Geography.Regions.Africa.Africa*                0.092         0.008
		Geography.Regions.Africa.Central Africa         0.001         0
		Geography.Regions.Africa.Eastern Africa         0.018         0
		Geography.Regions.Africa.Northern Africa        0.021         0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.119         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.178         0.046
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.043         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.039         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.037         0.011
		Geography.Regions.Europe.Eastern Europe         0.05          0.013
		Geography.Regions.Europe.Europe*                0.201         0.076
		Geography.Regions.Europe.Northern Europe        0.068         0.031
		Geography.Regions.Europe.Southern Europe        0.039         0.013
		Geography.Regions.Europe.Western Europe         0.051         0.019
		Geography.Regions.Oceania                       0.041         0.015
		History and Society.Business and economics      0.056         0.01
		History and Society.Education                   0.034         0.007
		History and Society.History                     0.052         0.011
		History and Society.Military and warfare        0.064         0.014
		History and Society.Politics and government     0.073         0.028
		History and Society.Society                     0.063         0.013
		History and Society.Transportation              0.057         0.015
		STEM.Biology                                    0.045         0.034
		STEM.Chemistry                                  0.021         0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.036         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.027         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.258         0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.056         0.005
	match_rate (micro=0.053, macro=0.021):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.131
		Culture.Biography.Women                      0.023
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.08
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.07
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.024
		Geography.Geographical                       0.021
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.194
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.06
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.055
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.015
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.09
		Geography.Regions.Europe.Northern Europe     0.03
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.018
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.013
		History and Society.Education                0.008
		History and Society.History                  0.012
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.024
		History and Society.Society                  0.011
		History and Society.Transportation           0.017
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.081
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.979):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.869
		Culture.Biography.Women                      0.977
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.92
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.976
		Geography.Geographical                       0.979
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.806
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.94
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.91
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.982
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.987
		History and Society.Education                0.992
		History and Society.History                  0.988
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.976
		History and Society.Society                  0.989
		History and Society.Transportation           0.983
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.919
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.743, macro=0.682):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.851
		Culture.Biography.Women                      0.707
		Culture.Food and drink                       0.67
		Culture.Internet culture                     0.752
		Culture.Linguistics                          0.676
		Culture.Literature                           0.686
		Culture.Media.Books                          0.637
		Culture.Media.Entertainment                  0.453
		Culture.Media.Films                          0.76
		Culture.Media.Media*                         0.826
		Culture.Media.Music                          0.763
		Culture.Media.Radio                          0.766
		Culture.Media.Software                       0.543
		Culture.Media.Television                     0.647
		Culture.Media.Video games                    0.868
		Culture.Performing arts                      0.635
		Culture.Philosophy and religion              0.509
		Culture.Sports                               0.892
		Culture.Visual arts.Architecture             0.692
		Culture.Visual arts.Comics and Anime         0.761
		Culture.Visual arts.Fashion                  0.717
		Culture.Visual arts.Visual arts*             0.724
		Geography.Geographical                       0.677
		Geography.Regions.Africa.Africa*             0.832
		Geography.Regions.Africa.Central Africa      0.185
		Geography.Regions.Africa.Eastern Africa      0.776
		Geography.Regions.Africa.Northern Africa     0.7
		Geography.Regions.Africa.Southern Africa     0.738
		Geography.Regions.Africa.Western Africa      0.789
		Geography.Regions.Americas.Central America   0.638
		Geography.Regions.Americas.North America     0.635
		Geography.Regions.Americas.South America     0.712
		Geography.Regions.Asia.Asia*                 0.831
		Geography.Regions.Asia.Central Asia          0.735
		Geography.Regions.Asia.East Asia             0.747
		Geography.Regions.Asia.North Asia            0.632
		Geography.Regions.Asia.South Asia            0.821
		Geography.Regions.Asia.Southeast Asia        0.726
		Geography.Regions.Asia.West Asia             0.754
		Geography.Regions.Europe.Eastern Europe      0.752
		Geography.Regions.Europe.Europe*             0.735
		Geography.Regions.Europe.Northern Europe     0.63
		Geography.Regions.Europe.Southern Europe     0.651
		Geography.Regions.Europe.Western Europe      0.614
		Geography.Regions.Oceania                    0.769
		History and Society.Business and economics   0.428
		History and Society.Education                0.468
		History and Society.History                  0.402
		History and Society.Military and warfare     0.678
		History and Society.Politics and government  0.581
		History and Society.Society                  0.353
		History and Society.Transportation           0.828
		STEM.Biology                                 0.798
		STEM.Chemistry                               0.661
		STEM.Computing                               0.636
		STEM.Earth and environment                   0.677
		STEM.Engineering                             0.697
		STEM.Libraries & Information                 0.538
		STEM.Mathematics                             0.712
		STEM.Medicine & Health                       0.635
		STEM.Physics                                 0.629
		STEM.STEM*                                   0.846
		STEM.Space                                   0.86
		STEM.Technology                              0.586
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.97
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.989
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.806
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.992
		History and Society.Society                  0.993
		History and Society.Transportation           0.996
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.687, macro=0.547):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.802
		Culture.Biography.Women                      0.439
		Culture.Food and drink                       0.568
		Culture.Internet culture                     0.435
		Culture.Linguistics                          0.808
		Culture.Literature                           0.505
		Culture.Media.Books                          0.449
		Culture.Media.Entertainment                  0.382
		Culture.Media.Films                          0.729
		Culture.Media.Media*                         0.603
		Culture.Media.Music                          0.789
		Culture.Media.Radio                          0.725
		Culture.Media.Software                       0.123
		Culture.Media.Television                     0.629
		Culture.Media.Video games                    0.684
		Culture.Performing arts                      0.502
		Culture.Philosophy and religion              0.509
		Culture.Sports                               0.915
		Culture.Visual arts.Architecture             0.598
		Culture.Visual arts.Comics and Anime         0.467
		Culture.Visual arts.Fashion                  0.302
		Culture.Visual arts.Visual arts*             0.559
		Geography.Geographical                       0.766
		Geography.Regions.Africa.Africa*             0.596
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.427
		Geography.Regions.Africa.Northern Africa     0.39
		Geography.Regions.Africa.Southern Africa     0.452
		Geography.Regions.Africa.Western Africa      0.358
		Geography.Regions.Americas.Central America   0.65
		Geography.Regions.Americas.North America     0.676
		Geography.Regions.Americas.South America     0.645
		Geography.Regions.Asia.Asia*                 0.693
		Geography.Regions.Asia.Central Asia          0.455
		Geography.Regions.Asia.East Asia             0.651
		Geography.Regions.Asia.North Asia            0.146
		Geography.Regions.Asia.South Asia            0.859
		Geography.Regions.Asia.Southeast Asia        0.736
		Geography.Regions.Asia.West Asia             0.782
		Geography.Regions.Europe.Eastern Europe      0.671
		Geography.Regions.Europe.Europe*             0.621
		Geography.Regions.Europe.Northern Europe     0.651
		Geography.Regions.Europe.Southern Europe     0.657
		Geography.Regions.Europe.Western Europe      0.654
		Geography.Regions.Oceania                    0.849
		History and Society.Business and economics   0.33
		History and Society.Education                0.439
		History and Society.History                  0.361
		History and Society.Military and warfare     0.57
		History and Society.Politics and government  0.669
		History and Society.Society                  0.405
		History and Society.Transportation           0.75
		STEM.Biology                                 0.927
		STEM.Chemistry                               0.287
		STEM.Computing                               0.191
		STEM.Earth and environment                   0.682
		STEM.Engineering                             0.538
		STEM.Libraries & Information                 0.235
		STEM.Mathematics                             0.173
		STEM.Medicine & Health                       0.586
		STEM.Physics                                 0.192
		STEM.STEM*                                   0.719
		STEM.Space                                   0.831
		STEM.Technology                              0.235
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.992
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.978
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.988
		History and Society.Society                  0.992
		History and Society.Transportation           0.997
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.988
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.709, macro=0.589):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.826
		Culture.Biography.Women                      0.541
		Culture.Food and drink                       0.615
		Culture.Internet culture                     0.551
		Culture.Linguistics                          0.736
		Culture.Literature                           0.582
		Culture.Media.Books                          0.527
		Culture.Media.Entertainment                  0.415
		Culture.Media.Films                          0.744
		Culture.Media.Media*                         0.697
		Culture.Media.Music                          0.776
		Culture.Media.Radio                          0.745
		Culture.Media.Software                       0.201
		Culture.Media.Television                     0.638
		Culture.Media.Video games                    0.765
		Culture.Performing arts                      0.561
		Culture.Philosophy and religion              0.509
		Culture.Sports                               0.903
		Culture.Visual arts.Architecture             0.642
		Culture.Visual arts.Comics and Anime         0.579
		Culture.Visual arts.Fashion                  0.425
		Culture.Visual arts.Visual arts*             0.631
		Geography.Geographical                       0.719
		Geography.Regions.Africa.Africa*             0.694
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.551
		Geography.Regions.Africa.Northern Africa     0.501
		Geography.Regions.Africa.Southern Africa     0.561
		Geography.Regions.Africa.Western Africa      0.493
		Geography.Regions.Americas.Central America   0.644
		Geography.Regions.Americas.North America     0.655
		Geography.Regions.Americas.South America     0.677
		Geography.Regions.Asia.Asia*                 0.756
		Geography.Regions.Asia.Central Asia          0.562
		Geography.Regions.Asia.East Asia             0.695
		Geography.Regions.Asia.North Asia            0.238
		Geography.Regions.Asia.South Asia            0.839
		Geography.Regions.Asia.Southeast Asia        0.731
		Geography.Regions.Asia.West Asia             0.768
		Geography.Regions.Europe.Eastern Europe      0.71
		Geography.Regions.Europe.Europe*             0.674
		Geography.Regions.Europe.Northern Europe     0.64
		Geography.Regions.Europe.Southern Europe     0.654
		Geography.Regions.Europe.Western Europe      0.633
		Geography.Regions.Oceania                    0.807
		History and Society.Business and economics   0.372
		History and Society.Education                0.453
		History and Society.History                  0.381
		History and Society.Military and warfare     0.62
		History and Society.Politics and government  0.622
		History and Society.Society                  0.377
		History and Society.Transportation           0.787
		STEM.Biology                                 0.858
		STEM.Chemistry                               0.4
		STEM.Computing                               0.294
		STEM.Earth and environment                   0.68
		STEM.Engineering                             0.607
		STEM.Libraries & Information                 0.327
		STEM.Mathematics                             0.278
		STEM.Medicine & Health                       0.609
		STEM.Physics                                 0.294
		STEM.STEM*                                   0.777
		STEM.Space                                   0.845
		STEM.Technology                              0.335
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      0.893
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.97
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.982
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.976, macro=0.987):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.956
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.985
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.958
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.988
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.806
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.957
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.946
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.985
		History and Society.Education                0.992
		History and Society.History                  0.986
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.98
		History and Society.Society                  0.985
		History and Society.Transportation           0.993
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.967
		STEM.Space                                   0.998
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.009):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.03
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.011
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.034
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.011
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.004
		Geography.Regions.Africa.Central Africa      0.194
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.021
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.006
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.008
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.008
		History and Society.Society                  0.007
		History and Society.Transportation           0.004
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.001
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.025
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.97, macro=0.97):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.971
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.977
		Culture.Internet culture                     0.983
		Culture.Linguistics                          0.976
		Culture.Literature                           0.971
		Culture.Media.Books                          0.977
		Culture.Media.Entertainment                  0.965
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.988
		Culture.Media.Software                       0.978
		Culture.Media.Television                     0.976
		Culture.Media.Video games                    0.99
		Culture.Performing arts                      0.978
		Culture.Philosophy and religion              0.957
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.977
		Culture.Visual arts.Comics and Anime         0.981
		Culture.Visual arts.Fashion                  0.982
		Culture.Visual arts.Visual arts*             0.97
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.981
		Geography.Regions.Africa.Central Africa      0.731
		Geography.Regions.Africa.Eastern Africa      0.983
		Geography.Regions.Africa.Northern Africa     0.981
		Geography.Regions.Africa.Southern Africa     0.983
		Geography.Regions.Africa.Western Africa      0.987
		Geography.Regions.Americas.Central America   0.976
		Geography.Regions.Americas.North America     0.957
		Geography.Regions.Americas.South America     0.982
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.982
		Geography.Regions.Asia.East Asia             0.979
		Geography.Regions.Asia.North Asia            0.98
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.977
		Geography.Regions.Asia.West Asia             0.982
		Geography.Regions.Europe.Eastern Europe      0.981
		Geography.Regions.Europe.Europe*             0.955
		Geography.Regions.Europe.Northern Europe     0.965
		Geography.Regions.Europe.Southern Europe     0.972
		Geography.Regions.Europe.Western Europe      0.967
		Geography.Regions.Oceania                    0.977
		History and Society.Business and economics   0.946
		History and Society.Education                0.957
		History and Society.History                  0.939
		History and Society.Military and warfare     0.97
		History and Society.Politics and government  0.953
		History and Society.Society                  0.915
		History and Society.Transportation           0.985
		STEM.Biology                                 0.98
		STEM.Chemistry                               0.982
		STEM.Computing                               0.982
		STEM.Earth and environment                   0.977
		STEM.Engineering                             0.978
		STEM.Libraries & Information                 0.973
		STEM.Mathematics                             0.981
		STEM.Medicine & Health                       0.972
		STEM.Physics                                 0.982
		STEM.STEM*                                   0.972
		STEM.Space                                   0.991
		STEM.Technology                              0.968
		-------------------------------------------  -----
	pr_auc (micro=0.752, macro=0.605):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.89
		Culture.Biography.Women                      0.499
		Culture.Food and drink                       0.573
		Culture.Internet culture                     0.703
		Culture.Linguistics                          0.767
		Culture.Literature                           0.619
		Culture.Media.Books                          0.513
		Culture.Media.Entertainment                  0.351
		Culture.Media.Films                          0.774
		Culture.Media.Media*                         0.797
		Culture.Media.Music                          0.82
		Culture.Media.Radio                          0.8
		Culture.Media.Software                       0.14
		Culture.Media.Television                     0.637
		Culture.Media.Video games                    0.836
		Culture.Performing arts                      0.594
		Culture.Philosophy and religion              0.453
		Culture.Sports                               0.938
		Culture.Visual arts.Architecture             0.665
		Culture.Visual arts.Comics and Anime         0.603
		Culture.Visual arts.Fashion                  0.496
		Culture.Visual arts.Visual arts*             0.699
		Geography.Geographical                       0.765
		Geography.Regions.Africa.Africa*             0.74
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.48
		Geography.Regions.Africa.Northern Africa     0.555
		Geography.Regions.Africa.Southern Africa     0.556
		Geography.Regions.Africa.Western Africa      0.416
		Geography.Regions.Americas.Central America   0.587
		Geography.Regions.Americas.North America     0.728
		Geography.Regions.Americas.South America     0.657
		Geography.Regions.Asia.Asia*                 0.807
		Geography.Regions.Asia.Central Asia          0.601
		Geography.Regions.Asia.East Asia             0.713
		Geography.Regions.Asia.North Asia            0.177
		Geography.Regions.Asia.South Asia            0.856
		Geography.Regions.Asia.Southeast Asia        0.72
		Geography.Regions.Asia.West Asia             0.825
		Geography.Regions.Europe.Eastern Europe      0.706
		Geography.Regions.Europe.Europe*             0.733
		Geography.Regions.Europe.Northern Europe     0.684
		Geography.Regions.Europe.Southern Europe     0.671
		Geography.Regions.Europe.Western Europe      0.631
		Geography.Regions.Oceania                    0.84
		History and Society.Business and economics   0.295
		History and Society.Education                0.381
		History and Society.History                  0.327
		History and Society.Military and warfare     0.639
		History and Society.Politics and government  0.657
		History and Society.Society                  0.345
		History and Society.Transportation           0.837
		STEM.Biology                                 0.915
		STEM.Chemistry                               0.392
		STEM.Computing                               0.3
		STEM.Earth and environment                   0.713
		STEM.Engineering                             0.601
		STEM.Libraries & Information                 0.302
		STEM.Mathematics                             0.419
		STEM.Medicine & Health                       0.607
		STEM.Physics                                 0.277
		STEM.STEM*                                   0.857
		STEM.Space                                   0.894
		STEM.Technology                              0.351
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'items': {'type': 'string'}, 'type': 'array', 'description': 'The most likely labels predicted by the estimator'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}}}}}

