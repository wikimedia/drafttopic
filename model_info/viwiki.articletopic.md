Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'warm_start': False, 'min_samples_split': 2, 'center': False, 'max_leaf_nodes': None, 'population_rates': None, 'n_estimators': 150, 'verbose': 0, 'multilabel': True, 'ccp_alpha': 0.0, 'learning_rate': 0.1, 'label_weights': {}, 'max_features': 'log2', 'validation_fraction': 0.1, 'min_samples_leaf': 1, 'scale': False, 'min_impurity_decrease': 0.0, 'presort': 'deprecated', 'max_depth': 5, 'tol': 0.0001, 'init': None, 'random_state': None, 'criterion': 'friedman_mse', 'min_weight_fraction_leaf': 0.0, 'min_impurity_split': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'subsample': 1.0, 'n_iter_no_change': None, 'loss': 'deviance'}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-11-amd64-x86_64-with-debian-9.12'
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
	counts (n=60772):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14137  -->  12709  1428   876  45759
			'Culture.Biography.Women'                       5142  -->   4194   948   751  54879
			'Culture.Food and drink'                        1375  -->   1047   328   105  59292
			'Culture.Internet culture'                      3515  -->   3044   471   202  57055
			'Culture.Linguistics'                           1516  -->   1196   320    63  59193
			'Culture.Literature'                            5607  -->   4416  1191   421  54744
			'Culture.Media.Books'                           1469  -->   1158   311    86  59217
			'Culture.Media.Entertainment'                   2061  -->   1370   691   164  58547
			'Culture.Media.Films'                           2705  -->   2240   465   160  57907
			'Culture.Media.Media*'                         13367  -->  11796  1571  1215  46190
			'Culture.Media.Music'                           2924  -->   2560   364   189  57659
			'Culture.Media.Radio'                            295  -->    203    92    41  60436
			'Culture.Media.Software'                        2323  -->   1989   334   249  58200
			'Culture.Media.Television'                      1981  -->   1506   475   103  58688
			'Culture.Media.Video games'                     2075  -->   1956   119    46  58651
			'Culture.Performing arts'                       1379  -->   1052   327   109  59284
			'Culture.Philosophy and religion'               3075  -->   1804  1271   257  57440
			'Culture.Sports'                                3998  -->   3508   490   137  56637
			'Culture.Visual arts.Architecture'              1850  -->   1367   483   157  58765
			'Culture.Visual arts.Comics and Anime'          2212  -->   2059   153    82  58478
			'Culture.Visual arts.Fashion'                   1501  -->   1276   225    77  59194
			'Culture.Visual arts.Visual arts*'              6060  -->   4796  1264   393  54319
			'Geography.Geographical'                        3991  -->   2629  1362   545  56236
			'Geography.Regions.Africa.Africa*'              5657  -->   4590  1067   450  54665
			'Geography.Regions.Africa.Central Africa'       1209  -->    591   618   151  59412
			'Geography.Regions.Africa.Eastern Africa'        458  -->    318   140    42  60272
			'Geography.Regions.Africa.Northern Africa'      1477  -->   1147   330    88  59207
			'Geography.Regions.Africa.Southern Africa'      1164  -->    857   307    49  59559
			'Geography.Regions.Africa.Western Africa'        673  -->    567   106    64  60035
			'Geography.Regions.Americas.Central America'    1627  -->   1119   508   115  59030
			'Geography.Regions.Americas.North America'      5424  -->   3769  1655   586  54762
			'Geography.Regions.Americas.South America'      2177  -->   1724   453   167  58428
			'Geography.Regions.Asia.Asia*'                 13958  -->  11902  2056  1112  45702
			'Geography.Regions.Asia.Central Asia'           1238  -->   1022   216    74  59460
			'Geography.Regions.Asia.East Asia'              5592  -->   4632   960   439  54741
			'Geography.Regions.Asia.North Asia'             1701  -->   1396   305   185  58886
			'Geography.Regions.Asia.South Asia'             2039  -->   1636   403    69  58664
			'Geography.Regions.Asia.Southeast Asia'         2665  -->   2052   613   214  57893
			'Geography.Regions.Asia.West Asia'              2204  -->   1840   364    91  58477
			'Geography.Regions.Europe.Eastern Europe'       3570  -->   2996   574   293  56909
			'Geography.Regions.Europe.Europe*'             12480  -->  10296  2184  1142  47150
			'Geography.Regions.Europe.Northern Europe'      2837  -->   1946   891   234  57701
			'Geography.Regions.Europe.Southern Europe'      2732  -->   2130   602   165  57875
			'Geography.Regions.Europe.Western Europe'       3927  -->   3116   811   199  56646
			'Geography.Regions.Oceania'                     2276  -->   1706   570   115  58381
			'History and Society.Business and economics'    3310  -->   2130  1180   327  57135
			'History and Society.Education'                 1628  -->   1024   604    92  59052
			'History and Society.History'                   4534  -->   2662  1872   550  55688
			'History and Society.Military and warfare'      4949  -->   3970   979   449  55374
			'History and Society.Politics and government'   4591  -->   2618  1973   515  55666
			'History and Society.Society'                   6015  -->   3148  2867   511  54246
			'History and Society.Transportation'            3570  -->   3340   230    78  57124
			'STEM.Biology'                                  7201  -->   6706   495   175  53396
			'STEM.Chemistry'                                1455  -->   1160   295   162  59155
			'STEM.Computing'                                2470  -->   2114   356   241  58061
			'STEM.Earth and environment'                    1591  -->   1111   480   132  59049
			'STEM.Engineering'                              3007  -->   2535   472   120  57645
			'STEM.Libraries & Information'                   486  -->    373   113    28  60258
			'STEM.Mathematics'                               933  -->    806   127    38  59801
			'STEM.Medicine & Health'                        1821  -->   1395   426   141  58810
			'STEM.Physics'                                  1376  -->   1078   298   143  59253
			'STEM.STEM*'                                   20635  -->  18993  1642   803  39334
			'STEM.Space'                                    1656  -->   1536   120    38  59078
			'STEM.Technology'                               4274  -->   3314   960   523  55975
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.233         0.123
		Culture.Biography.Women                         0.085         0.015
		Culture.Food and drink                          0.023         0.002
		Culture.Internet culture                        0.058         0.003
		Culture.Linguistics                             0.025         0.007
		Culture.Literature                              0.092         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.034         0.004
		Culture.Media.Films                             0.045         0.011
		Culture.Media.Media*                            0.22          0.058
		Culture.Media.Music                             0.048         0.024
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.034         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.051         0.011
		Culture.Sports                                  0.066         0.071
		Culture.Visual arts.Architecture                0.03          0.011
		Culture.Visual arts.Comics and Anime            0.036         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.1           0.018
		Geography.Geographical                          0.066         0.024
		Geography.Regions.Africa.Africa*                0.093         0.008
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.027         0.003
		Geography.Regions.Americas.North America        0.089         0.064
		Geography.Regions.Americas.South America        0.036         0.006
		Geography.Regions.Asia.Asia*                    0.23          0.045
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.092         0.011
		Geography.Regions.Asia.North Asia               0.028         0.001
		Geography.Regions.Asia.South Asia               0.034         0.015
		Geography.Regions.Asia.Southeast Asia           0.044         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.059         0.013
		Geography.Regions.Europe.Europe*                0.205         0.076
		Geography.Regions.Europe.Northern Europe        0.047         0.031
		Geography.Regions.Europe.Southern Europe        0.045         0.013
		Geography.Regions.Europe.Western Europe         0.065         0.019
		Geography.Regions.Oceania                       0.037         0.015
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.027         0.007
		History and Society.History                     0.075         0.011
		History and Society.Military and warfare        0.081         0.014
		History and Society.Politics and government     0.076         0.028
		History and Society.Society                     0.099         0.013
		History and Society.Transportation              0.059         0.015
		STEM.Biology                                    0.118         0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.049         0.005
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.015         0
		STEM.Medicine & Health                          0.03          0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.34          0.069
		STEM.Space                                      0.027         0.006
		STEM.Technology                                 0.07          0.005
	match_rate (micro=0.052, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.127
		Culture.Biography.Women                      0.025
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.065
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.014
		Geography.Regions.Africa.Central Africa      0.003
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.055
		Geography.Regions.Americas.South America     0.008
		Geography.Regions.Asia.Asia*                 0.061
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.017
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.008
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.016
		Geography.Regions.Europe.Europe*             0.085
		Geography.Regions.Europe.Northern Europe     0.025
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.019
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.016
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.025
		History and Society.Society                  0.016
		History and Society.Transportation           0.015
		STEM.Biology                                 0.034
		STEM.Chemistry                               0.004
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.082
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.948, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.935
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.986
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.945
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.939
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.983
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.992
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.915
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.984
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.975
		History and Society.Society                  0.984
		History and Society.Transportation           0.985
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.918
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.811, macro=0.781):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.899
		Culture.Biography.Women                      0.816
		Culture.Food and drink                       0.761
		Culture.Internet culture                     0.866
		Culture.Linguistics                          0.789
		Culture.Literature                           0.788
		Culture.Media.Books                          0.788
		Culture.Media.Entertainment                  0.665
		Culture.Media.Films                          0.828
		Culture.Media.Media*                         0.882
		Culture.Media.Music                          0.876
		Culture.Media.Radio                          0.688
		Culture.Media.Software                       0.856
		Culture.Media.Television                     0.76
		Culture.Media.Video games                    0.943
		Culture.Performing arts                      0.763
		Culture.Philosophy and religion              0.587
		Culture.Sports                               0.877
		Culture.Visual arts.Architecture             0.739
		Culture.Visual arts.Comics and Anime         0.931
		Culture.Visual arts.Fashion                  0.85
		Culture.Visual arts.Visual arts*             0.791
		Geography.Geographical                       0.659
		Geography.Regions.Africa.Africa*             0.811
		Geography.Regions.Africa.Central Africa      0.489
		Geography.Regions.Africa.Eastern Africa      0.694
		Geography.Regions.Africa.Northern Africa     0.777
		Geography.Regions.Africa.Southern Africa     0.736
		Geography.Regions.Africa.Western Africa      0.842
		Geography.Regions.Americas.Central America   0.688
		Geography.Regions.Americas.North America     0.695
		Geography.Regions.Americas.South America     0.792
		Geography.Regions.Asia.Asia*                 0.853
		Geography.Regions.Asia.Central Asia          0.826
		Geography.Regions.Asia.East Asia             0.828
		Geography.Regions.Asia.North Asia            0.821
		Geography.Regions.Asia.South Asia            0.802
		Geography.Regions.Asia.Southeast Asia        0.77
		Geography.Regions.Asia.West Asia             0.835
		Geography.Regions.Europe.Eastern Europe      0.839
		Geography.Regions.Europe.Europe*             0.825
		Geography.Regions.Europe.Northern Europe     0.686
		Geography.Regions.Europe.Southern Europe     0.78
		Geography.Regions.Europe.Western Europe      0.793
		Geography.Regions.Oceania                    0.75
		History and Society.Business and economics   0.644
		History and Society.Education                0.629
		History and Society.History                  0.587
		History and Society.Military and warfare     0.802
		History and Society.Politics and government  0.57
		History and Society.Society                  0.523
		History and Society.Transportation           0.936
		STEM.Biology                                 0.931
		STEM.Chemistry                               0.797
		STEM.Computing                               0.856
		STEM.Earth and environment                   0.698
		STEM.Engineering                             0.843
		STEM.Libraries & Information                 0.767
		STEM.Mathematics                             0.864
		STEM.Medicine & Health                       0.766
		STEM.Physics                                 0.783
		STEM.STEM*                                   0.92
		STEM.Space                                   0.928
		STEM.Technology                              0.775
		-------------------------------------------  -----
	!recall (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.992
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.974
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.989
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.976
		Geography.Regions.Europe.Northern Europe     0.996
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.99
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.991
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.98
		STEM.Space                                   0.999
		STEM.Technology                              0.991
		-------------------------------------------  -----
	precision (micro=0.749, macro=0.601):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.87
		Culture.Biography.Women                      0.472
		Culture.Food and drink                       0.515
		Culture.Internet culture                     0.463
		Culture.Linguistics                          0.846
		Culture.Literature                           0.619
		Culture.Media.Books                          0.687
		Culture.Media.Entertainment                  0.461
		Culture.Media.Films                          0.762
		Culture.Media.Media*                         0.681
		Culture.Media.Music                          0.868
		Culture.Media.Radio                          0.687
		Culture.Media.Software                       0.211
		Culture.Media.Television                     0.794
		Culture.Media.Video games                    0.759
		Culture.Performing arts                      0.546
		Culture.Philosophy and religion              0.586
		Culture.Sports                               0.965
		Culture.Visual arts.Architecture             0.748
		Culture.Visual arts.Comics and Anime         0.594
		Culture.Visual arts.Fashion                  0.346
		Culture.Visual arts.Visual arts*             0.672
		Geography.Geographical                       0.624
		Geography.Regions.Africa.Africa*             0.438
		Geography.Regions.Africa.Central Africa      0.109
		Geography.Regions.Africa.Eastern Africa      0.312
		Geography.Regions.Africa.Northern Africa     0.391
		Geography.Regions.Africa.Southern Africa     0.513
		Geography.Regions.Africa.Western Africa      0.351
		Geography.Regions.Americas.Central America   0.539
		Geography.Regions.Americas.North America     0.818
		Geography.Regions.Americas.South America     0.638
		Geography.Regions.Asia.Asia*                 0.631
		Geography.Regions.Asia.Central Asia          0.365
		Geography.Regions.Asia.East Asia             0.546
		Geography.Regions.Asia.North Asia            0.195
		Geography.Regions.Asia.South Asia            0.913
		Geography.Regions.Asia.Southeast Asia        0.558
		Geography.Regions.Asia.West Asia             0.856
		Geography.Regions.Europe.Eastern Europe      0.68
		Geography.Regions.Europe.Europe*             0.742
		Geography.Regions.Europe.Northern Europe     0.843
		Geography.Regions.Europe.Southern Europe     0.784
		Geography.Regions.Europe.Western Europe      0.816
		Geography.Regions.Oceania                    0.854
		History and Society.Business and economics   0.535
		History and Society.Education                0.75
		History and Society.History                  0.397
		History and Society.Military and warfare     0.587
		History and Society.Politics and government  0.643
		History and Society.Society                  0.417
		History and Society.Transportation           0.913
		STEM.Biology                                 0.908
		STEM.Chemistry                               0.313
		STEM.Computing                               0.358
		STEM.Earth and environment                   0.588
		STEM.Engineering                             0.681
		STEM.Libraries & Information                 0.507
		STEM.Mathematics                             0.362
		STEM.Medicine & Health                       0.673
		STEM.Physics                                 0.217
		STEM.STEM*                                   0.774
		STEM.Space                                   0.897
		STEM.Technology                              0.302
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     1
		Culture.Linguistics                          0.998
		Culture.Literature                           0.997
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.999
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.991
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
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.993
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.998
		Geography.Regions.Europe.Europe*             0.985
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.997
		History and Society.Politics and government  0.988
		History and Society.Society                  0.994
		History and Society.Transportation           0.999
		STEM.Biology                                 0.998
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.994
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.772, macro=0.659):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.884
		Culture.Biography.Women                      0.598
		Culture.Food and drink                       0.615
		Culture.Internet culture                     0.603
		Culture.Linguistics                          0.816
		Culture.Literature                           0.693
		Culture.Media.Books                          0.734
		Culture.Media.Entertainment                  0.544
		Culture.Media.Films                          0.793
		Culture.Media.Media*                         0.769
		Culture.Media.Music                          0.872
		Culture.Media.Radio                          0.687
		Culture.Media.Software                       0.338
		Culture.Media.Television                     0.777
		Culture.Media.Video games                    0.841
		Culture.Performing arts                      0.637
		Culture.Philosophy and religion              0.587
		Culture.Sports                               0.919
		Culture.Visual arts.Architecture             0.743
		Culture.Visual arts.Comics and Anime         0.725
		Culture.Visual arts.Fashion                  0.492
		Culture.Visual arts.Visual arts*             0.727
		Geography.Geographical                       0.641
		Geography.Regions.Africa.Africa*             0.569
		Geography.Regions.Africa.Central Africa      0.178
		Geography.Regions.Africa.Eastern Africa      0.431
		Geography.Regions.Africa.Northern Africa     0.52
		Geography.Regions.Africa.Southern Africa     0.605
		Geography.Regions.Africa.Western Africa      0.496
		Geography.Regions.Americas.Central America   0.605
		Geography.Regions.Americas.North America     0.752
		Geography.Regions.Americas.South America     0.707
		Geography.Regions.Asia.Asia*                 0.725
		Geography.Regions.Asia.Central Asia          0.506
		Geography.Regions.Asia.East Asia             0.658
		Geography.Regions.Asia.North Asia            0.315
		Geography.Regions.Asia.South Asia            0.854
		Geography.Regions.Asia.Southeast Asia        0.647
		Geography.Regions.Asia.West Asia             0.845
		Geography.Regions.Europe.Eastern Europe      0.752
		Geography.Regions.Europe.Europe*             0.781
		Geography.Regions.Europe.Northern Europe     0.756
		Geography.Regions.Europe.Southern Europe     0.782
		Geography.Regions.Europe.Western Europe      0.804
		Geography.Regions.Oceania                    0.798
		History and Society.Business and economics   0.584
		History and Society.Education                0.684
		History and Society.History                  0.473
		History and Society.Military and warfare     0.678
		History and Society.Politics and government  0.605
		History and Society.Society                  0.464
		History and Society.Transportation           0.924
		STEM.Biology                                 0.92
		STEM.Chemistry                               0.45
		STEM.Computing                               0.505
		STEM.Earth and environment                   0.638
		STEM.Engineering                             0.753
		STEM.Libraries & Information                 0.61
		STEM.Mathematics                             0.51
		STEM.Medicine & Health                       0.717
		STEM.Physics                                 0.339
		STEM.STEM*                                   0.841
		STEM.Space                                   0.912
		STEM.Technology                              0.434
		-------------------------------------------  -----
	!f1 (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.999
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.983
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.984
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.989
		History and Society.Society                  0.992
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.987
		STEM.Space                                   0.999
		STEM.Technology                              0.995
		-------------------------------------------  -----
	accuracy (micro=0.982, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.971
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.997
		Culture.Literature                           0.989
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.969
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.991
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.986
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.979
		History and Society.Society                  0.985
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.976
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	fpr (micro=0.011, macro=0.005):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.019
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.008
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.026
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.004
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.004
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.008
		Geography.Regions.Africa.Central Africa      0.003
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.011
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.024
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.024
		Geography.Regions.Europe.Northern Europe     0.004
		Geography.Regions.Europe.Southern Europe     0.003
		Geography.Regions.Europe.Western Europe      0.004
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.01
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.009
		History and Society.Society                  0.009
		History and Society.Transportation           0.001
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.004
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.02
		STEM.Space                                   0.001
		STEM.Technology                              0.009
		-------------------------------------------  -----
	roc_auc (micro=0.979, macro=0.981):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.984
		Culture.Internet culture                     0.99
		Culture.Linguistics                          0.979
		Culture.Literature                           0.981
		Culture.Media.Books                          0.987
		Culture.Media.Entertainment                  0.98
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.987
		Culture.Media.Radio                          0.967
		Culture.Media.Software                       0.987
		Culture.Media.Television                     0.983
		Culture.Media.Video games                    0.993
		Culture.Performing arts                      0.982
		Culture.Philosophy and religion              0.964
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.982
		Culture.Visual arts.Comics and Anime         0.99
		Culture.Visual arts.Fashion                  0.987
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.969
		Geography.Regions.Africa.Africa*             0.982
		Geography.Regions.Africa.Central Africa      0.978
		Geography.Regions.Africa.Eastern Africa      0.973
		Geography.Regions.Africa.Northern Africa     0.983
		Geography.Regions.Africa.Southern Africa     0.979
		Geography.Regions.Africa.Western Africa      0.986
		Geography.Regions.Americas.Central America   0.98
		Geography.Regions.Americas.North America     0.971
		Geography.Regions.Americas.South America     0.983
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.988
		Geography.Regions.Asia.East Asia             0.983
		Geography.Regions.Asia.North Asia            0.988
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.98
		Geography.Regions.Asia.West Asia             0.983
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.973
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.98
		Geography.Regions.Europe.Western Europe      0.982
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.972
		History and Society.Education                0.98
		History and Society.History                  0.961
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.961
		History and Society.Society                  0.946
		History and Society.Transportation           0.99
		STEM.Biology                                 0.987
		STEM.Chemistry                               0.988
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.98
		STEM.Engineering                             0.986
		STEM.Libraries & Information                 0.974
		STEM.Mathematics                             0.989
		STEM.Medicine & Health                       0.981
		STEM.Physics                                 0.988
		STEM.STEM*                                   0.983
		STEM.Space                                   0.994
		STEM.Technology                              0.981
		-------------------------------------------  -----
	pr_auc (micro=0.826, macro=0.684):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.931
		Culture.Biography.Women                      0.604
		Culture.Food and drink                       0.621
		Culture.Internet culture                     0.789
		Culture.Linguistics                          0.825
		Culture.Literature                           0.758
		Culture.Media.Books                          0.775
		Culture.Media.Entertainment                  0.53
		Culture.Media.Films                          0.843
		Culture.Media.Media*                         0.872
		Culture.Media.Music                          0.902
		Culture.Media.Radio                          0.501
		Culture.Media.Software                       0.381
		Culture.Media.Television                     0.791
		Culture.Media.Video games                    0.937
		Culture.Performing arts                      0.595
		Culture.Philosophy and religion              0.575
		Culture.Sports                               0.958
		Culture.Visual arts.Architecture             0.743
		Culture.Visual arts.Comics and Anime         0.801
		Culture.Visual arts.Fashion                  0.45
		Culture.Visual arts.Visual arts*             0.791
		Geography.Geographical                       0.655
		Geography.Regions.Africa.Africa*             0.659
		Geography.Regions.Africa.Central Africa      0.097
		Geography.Regions.Africa.Eastern Africa      0.258
		Geography.Regions.Africa.Northern Africa     0.441
		Geography.Regions.Africa.Southern Africa     0.496
		Geography.Regions.Africa.Western Africa      0.396
		Geography.Regions.Americas.Central America   0.585
		Geography.Regions.Americas.North America     0.822
		Geography.Regions.Americas.South America     0.745
		Geography.Regions.Asia.Asia*                 0.818
		Geography.Regions.Asia.Central Asia          0.498
		Geography.Regions.Asia.East Asia             0.683
		Geography.Regions.Asia.North Asia            0.29
		Geography.Regions.Asia.South Asia            0.898
		Geography.Regions.Asia.Southeast Asia        0.685
		Geography.Regions.Asia.West Asia             0.895
		Geography.Regions.Europe.Eastern Europe      0.828
		Geography.Regions.Europe.Europe*             0.86
		Geography.Regions.Europe.Northern Europe     0.823
		Geography.Regions.Europe.Southern Europe     0.829
		Geography.Regions.Europe.Western Europe      0.847
		Geography.Regions.Oceania                    0.852
		History and Society.Business and economics   0.594
		History and Society.Education                0.7
		History and Society.History                  0.456
		History and Society.Military and warfare     0.755
		History and Society.Politics and government  0.645
		History and Society.Society                  0.462
		History and Society.Transportation           0.95
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.502
		STEM.Computing                               0.58
		STEM.Earth and environment                   0.671
		STEM.Engineering                             0.81
		STEM.Libraries & Information                 0.553
		STEM.Mathematics                             0.572
		STEM.Medicine & Health                       0.757
		STEM.Physics                                 0.406
		STEM.STEM*                                   0.938
		STEM.Space                                   0.957
		STEM.Technology                              0.538
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}}}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}}}

