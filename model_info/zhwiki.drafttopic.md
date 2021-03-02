Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'tol': 0.0001, 'n_estimators': 150, 'init': None, 'population_rates': None, 'loss': 'deviance', 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_impurity_decrease': 0.0, 'max_depth': 5, 'multilabel': True, 'learning_rate': 0.1, 'ccp_alpha': 0.0, 'subsample': 1.0, 'max_features': 'log2', 'min_weight_fraction_leaf': 0.0, 'presort': 'deprecated', 'criterion': 'friedman_mse', 'n_iter_no_change': None, 'min_impurity_split': None, 'verbose': 0, 'validation_fraction': 0.1, 'random_state': None, 'label_weights': {}, 'scale': False, 'min_samples_leaf': 1, 'center': False, 'min_samples_split': 2, 'max_leaf_nodes': None, 'warm_start': False}
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
	counts (n=60821):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13231  -->  10905  2326  1063  46527
			'Culture.Biography.Women'                       3158  -->   1854  1304   407  57256
			'Culture.Food and drink'                        1331  -->    750   581   102  59388
			'Culture.Internet culture'                      3323  -->   2295  1028   266  57232
			'Culture.Linguistics'                           1478  -->    960   518   103  59240
			'Culture.Literature'                            5376  -->   3695  1681   682  54763
			'Culture.Media.Books'                           1614  -->   1054   560   201  59006
			'Culture.Media.Entertainment'                   1853  -->    695  1158   226  58742
			'Culture.Media.Films'                           2386  -->   1651   735   212  58223
			'Culture.Media.Media*'                         13361  -->  10680  2681  1602  45858
			'Culture.Media.Music'                           2460  -->   1706   754   208  58153
			'Culture.Media.Radio'                            747  -->    424   323    80  59994
			'Culture.Media.Software'                        2060  -->   1219   841   392  58369
			'Culture.Media.Television'                      1993  -->   1214   779   184  58644
			'Culture.Media.Video games'                     2332  -->   1824   508   111  58378
			'Culture.Performing arts'                       1307  -->    638   669   128  59386
			'Culture.Philosophy and religion'               3511  -->   1782  1729   417  56893
			'Culture.Sports'                                4122  -->   3321   801   160  56539
			'Culture.Visual arts.Architecture'              2397  -->   1597   800   305  58119
			'Culture.Visual arts.Comics and Anime'          2306  -->   1683   623   245  58270
			'Culture.Visual arts.Fashion'                   1137  -->    649   488   113  59571
			'Culture.Visual arts.Visual arts*'              6313  -->   4175  2138   742  53766
			'Geography.Geographical'                        5388  -->   3576  1812   623  54810
			'Geography.Regions.Africa.Africa*'              5466  -->   4134  1332   369  54986
			'Geography.Regions.Africa.Central Africa'       1185  -->    898   287    82  59554
			'Geography.Regions.Africa.Eastern Africa'        959  -->    735   224    37  59825
			'Geography.Regions.Africa.Northern Africa'      1355  -->    887   468   107  59359
			'Geography.Regions.Africa.Southern Africa'      1155  -->    860   295    37  59629
			'Geography.Regions.Africa.Western Africa'        448  -->    246   202    50  60323
			'Geography.Regions.Americas.Central America'    1260  -->    781   479    39  59522
			'Geography.Regions.Americas.North America'      5583  -->   3249  2334   819  54419
			'Geography.Regions.Americas.South America'      1466  -->   1081   385    81  59274
			'Geography.Regions.Asia.Asia*'                 16494  -->  12966  3528  1895  42432
			'Geography.Regions.Asia.Central Asia'           1191  -->    722   469    84  59546
			'Geography.Regions.Asia.East Asia'              8341  -->   6083  2258  1134  51346
			'Geography.Regions.Asia.North Asia'             2681  -->   1755   926   195  57945
			'Geography.Regions.Asia.South Asia'             1759  -->   1284   475    82  58980
			'Geography.Regions.Asia.Southeast Asia'         2007  -->   1274   733   136  58678
			'Geography.Regions.Asia.West Asia'              1925  -->   1260   665   144  58752
			'Geography.Regions.Europe.Eastern Europe'       3923  -->   2742  1181   261  56637
			'Geography.Regions.Europe.Europe*'             13222  -->   9988  3234  1457  46142
			'Geography.Regions.Europe.Northern Europe'      3278  -->   1966  1312   365  57178
			'Geography.Regions.Europe.Southern Europe'      2874  -->   2026   848   223  57724
			'Geography.Regions.Europe.Western Europe'       3721  -->   2545  1176   338  56762
			'Geography.Regions.Oceania'                     1901  -->   1256   645   121  58799
			'History and Society.Business and economics'    3508  -->   1638  1870   440  56873
			'History and Society.Education'                 1830  -->    934   896   146  58845
			'History and Society.History'                   3966  -->   1798  2168   513  56342
			'History and Society.Military and warfare'      3605  -->   2006  1599   397  56819
			'History and Society.Politics and government'   3646  -->   1695  1951   490  56685
			'History and Society.Society'                   4309  -->   1340  2969   340  56172
			'History and Society.Transportation'            3605  -->   2932   673   190  57026
			'STEM.Biology'                                  3042  -->   2283   759   179  57600
			'STEM.Chemistry'                                1413  -->    906   507   155  59253
			'STEM.Computing'                                2429  -->   1629   800   440  57952
			'STEM.Earth and environment'                    2379  -->   1846   533   148  58294
			'STEM.Engineering'                              2395  -->   1524   871   153  58273
			'STEM.Libraries & Information'                  1148  -->    760   388    74  59599
			'STEM.Mathematics'                              1122  -->    743   379    76  59623
			'STEM.Medicine & Health'                        1745  -->   1013   732   175  58901
			'STEM.Physics'                                  1275  -->    760   515   164  59382
			'STEM.STEM*'                                   17854  -->  15142  2712  1242  41725
			'STEM.Space'                                    1687  -->   1421   266    55  59079
			'STEM.Technology'                               4108  -->   2387  1721   719  55994
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.218         0.121
		Culture.Biography.Women                         0.052         0.015
		Culture.Food and drink                          0.022         0.003
		Culture.Internet culture                        0.055         0.004
		Culture.Linguistics                             0.024         0.008
		Culture.Literature                              0.088         0.015
		Culture.Media.Books                             0.027         0.004
		Culture.Media.Entertainment                     0.03          0.004
		Culture.Media.Films                             0.039         0.012
		Culture.Media.Media*                            0.22          0.055
		Culture.Media.Music                             0.04          0.021
		Culture.Media.Radio                             0.012         0.002
		Culture.Media.Software                          0.034         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.038         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.058         0.01
		Culture.Sports                                  0.068         0.061
		Culture.Visual arts.Architecture                0.039         0.011
		Culture.Visual arts.Comics and Anime            0.038         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.104         0.018
		Geography.Geographical                          0.089         0.021
		Geography.Regions.Africa.Africa*                0.09          0.009
		Geography.Regions.Africa.Central Africa         0.019         0.001
		Geography.Regions.Africa.Eastern Africa         0.016         0.001
		Geography.Regions.Africa.Northern Africa        0.022         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.007         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.092         0.064
		Geography.Regions.Americas.South America        0.024         0.007
		Geography.Regions.Asia.Asia*                    0.271         0.053
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.137         0.012
		Geography.Regions.Asia.North Asia               0.044         0.006
		Geography.Regions.Asia.South Asia               0.029         0.017
		Geography.Regions.Asia.Southeast Asia           0.033         0.006
		Geography.Regions.Asia.West Asia                0.032         0.012
		Geography.Regions.Europe.Eastern Europe         0.065         0.018
		Geography.Regions.Europe.Europe*                0.217         0.082
		Geography.Regions.Europe.Northern Europe        0.054         0.029
		Geography.Regions.Europe.Southern Europe        0.047         0.014
		Geography.Regions.Europe.Western Europe         0.061         0.021
		Geography.Regions.Oceania                       0.031         0.017
		History and Society.Business and economics      0.058         0.01
		History and Society.Education                   0.03          0.008
		History and Society.History                     0.065         0.011
		History and Society.Military and warfare        0.059         0.015
		History and Society.Politics and government     0.06          0.016
		History and Society.Society                     0.071         0.008
		History and Society.Transportation              0.059         0.016
		STEM.Biology                                    0.05          0.035
		STEM.Chemistry                                  0.023         0.002
		STEM.Computing                                  0.04          0.003
		STEM.Earth and environment                      0.039         0.005
		STEM.Engineering                                0.039         0.006
		STEM.Libraries & Information                    0.019         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.021         0.001
		STEM.STEM*                                      0.294         0.066
		STEM.Space                                      0.028         0.004
		STEM.Technology                                 0.068         0.005
	match_rate (micro=0.05, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.12
		Culture.Biography.Women                      0.016
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.022
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.018
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.013
		Culture.Sports                               0.052
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.006
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.025
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.051
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.082
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.03
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.01
		Geography.Regions.Europe.Eastern Europe      0.017
		Geography.Regions.Europe.Europe*             0.09
		Geography.Regions.Europe.Northern Europe     0.024
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.02
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.014
		History and Society.Military and warfare     0.015
		History and Society.Politics and government  0.016
		History and Society.Society                  0.009
		History and Society.Transportation           0.017
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.083
		STEM.Space                                   0.005
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.95, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.88
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.978
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.948
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.994
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.975
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.918
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.97
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.99
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.91
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.986
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.984
		History and Society.Society                  0.991
		History and Society.Transportation           0.983
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.917
		STEM.Space                                   0.995
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.711, macro=0.652):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.824
		Culture.Biography.Women                      0.587
		Culture.Food and drink                       0.563
		Culture.Internet culture                     0.691
		Culture.Linguistics                          0.65
		Culture.Literature                           0.687
		Culture.Media.Books                          0.653
		Culture.Media.Entertainment                  0.375
		Culture.Media.Films                          0.692
		Culture.Media.Media*                         0.799
		Culture.Media.Music                          0.693
		Culture.Media.Radio                          0.568
		Culture.Media.Software                       0.592
		Culture.Media.Television                     0.609
		Culture.Media.Video games                    0.782
		Culture.Performing arts                      0.488
		Culture.Philosophy and religion              0.508
		Culture.Sports                               0.806
		Culture.Visual arts.Architecture             0.666
		Culture.Visual arts.Comics and Anime         0.73
		Culture.Visual arts.Fashion                  0.571
		Culture.Visual arts.Visual arts*             0.661
		Geography.Geographical                       0.664
		Geography.Regions.Africa.Africa*             0.756
		Geography.Regions.Africa.Central Africa      0.758
		Geography.Regions.Africa.Eastern Africa      0.766
		Geography.Regions.Africa.Northern Africa     0.655
		Geography.Regions.Africa.Southern Africa     0.745
		Geography.Regions.Africa.Western Africa      0.549
		Geography.Regions.Americas.Central America   0.62
		Geography.Regions.Americas.North America     0.582
		Geography.Regions.Americas.South America     0.737
		Geography.Regions.Asia.Asia*                 0.786
		Geography.Regions.Asia.Central Asia          0.606
		Geography.Regions.Asia.East Asia             0.729
		Geography.Regions.Asia.North Asia            0.655
		Geography.Regions.Asia.South Asia            0.73
		Geography.Regions.Asia.Southeast Asia        0.635
		Geography.Regions.Asia.West Asia             0.655
		Geography.Regions.Europe.Eastern Europe      0.699
		Geography.Regions.Europe.Europe*             0.755
		Geography.Regions.Europe.Northern Europe     0.6
		Geography.Regions.Europe.Southern Europe     0.705
		Geography.Regions.Europe.Western Europe      0.684
		Geography.Regions.Oceania                    0.661
		History and Society.Business and economics   0.467
		History and Society.Education                0.51
		History and Society.History                  0.453
		History and Society.Military and warfare     0.556
		History and Society.Politics and government  0.465
		History and Society.Society                  0.311
		History and Society.Transportation           0.813
		STEM.Biology                                 0.75
		STEM.Chemistry                               0.641
		STEM.Computing                               0.671
		STEM.Earth and environment                   0.776
		STEM.Engineering                             0.636
		STEM.Libraries & Information                 0.662
		STEM.Mathematics                             0.662
		STEM.Medicine & Health                       0.581
		STEM.Physics                                 0.596
		STEM.STEM*                                   0.848
		STEM.Space                                   0.842
		STEM.Technology                              0.581
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.988
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.957
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.978
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.969
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.992
		History and Society.Education                0.998
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.971
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.675, macro=0.53):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.836
		Culture.Biography.Women                      0.561
		Culture.Food and drink                       0.459
		Culture.Internet culture                     0.361
		Culture.Linguistics                          0.754
		Culture.Literature                           0.46
		Culture.Media.Books                          0.457
		Culture.Media.Entertainment                  0.281
		Culture.Media.Films                          0.692
		Culture.Media.Media*                         0.581
		Culture.Media.Music                          0.808
		Culture.Media.Radio                          0.501
		Culture.Media.Software                       0.105
		Culture.Media.Television                     0.638
		Culture.Media.Video games                    0.548
		Culture.Performing arts                      0.412
		Culture.Philosophy and religion              0.425
		Culture.Sports                               0.949
		Culture.Visual arts.Architecture             0.584
		Culture.Visual arts.Comics and Anime         0.297
		Culture.Visual arts.Fashion                  0.215
		Culture.Visual arts.Visual arts*             0.475
		Geography.Geographical                       0.563
		Geography.Regions.Africa.Africa*             0.495
		Geography.Regions.Africa.Central Africa      0.281
		Geography.Regions.Africa.Eastern Africa      0.386
		Geography.Regions.Africa.Northern Africa     0.332
		Geography.Regions.Africa.Southern Africa     0.613
		Geography.Regions.Africa.Western Africa      0.333
		Geography.Regions.Americas.Central America   0.768
		Geography.Regions.Americas.North America     0.727
		Geography.Regions.Americas.South America     0.79
		Geography.Regions.Asia.Asia*                 0.507
		Geography.Regions.Asia.Central Asia          0.257
		Geography.Regions.Asia.East Asia             0.296
		Geography.Regions.Asia.North Asia            0.526
		Geography.Regions.Asia.South Asia            0.899
		Geography.Regions.Asia.Southeast Asia        0.635
		Geography.Regions.Asia.West Asia             0.762
		Geography.Regions.Europe.Eastern Europe      0.741
		Geography.Regions.Europe.Europe*             0.687
		Geography.Regions.Europe.Northern Europe     0.74
		Geography.Regions.Europe.Southern Europe     0.722
		Geography.Regions.Europe.Western Europe      0.709
		Geography.Regions.Oceania                    0.844
		History and Society.Business and economics   0.376
		History and Society.Education                0.624
		History and Society.History                  0.357
		History and Society.Military and warfare     0.557
		History and Society.Politics and government  0.476
		History and Society.Society                  0.303
		History and Society.Transportation           0.804
		STEM.Biology                                 0.897
		STEM.Chemistry                               0.296
		STEM.Computing                               0.203
		STEM.Earth and environment                   0.595
		STEM.Engineering                             0.586
		STEM.Libraries & Information                 0.27
		STEM.Mathematics                             0.195
		STEM.Medicine & Health                       0.562
		STEM.Physics                                 0.17
		STEM.STEM*                                   0.673
		STEM.Space                                   0.796
		STEM.Technology                              0.193
		-------------------------------------------  -----
	!precision (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.988
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.972
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.978
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.989
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.683, macro=0.564):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.83
		Culture.Biography.Women                      0.574
		Culture.Food and drink                       0.506
		Culture.Internet culture                     0.474
		Culture.Linguistics                          0.698
		Culture.Literature                           0.551
		Culture.Media.Books                          0.538
		Culture.Media.Entertainment                  0.322
		Culture.Media.Films                          0.692
		Culture.Media.Media*                         0.673
		Culture.Media.Music                          0.746
		Culture.Media.Radio                          0.532
		Culture.Media.Software                       0.178
		Culture.Media.Television                     0.623
		Culture.Media.Video games                    0.645
		Culture.Performing arts                      0.447
		Culture.Philosophy and religion              0.462
		Culture.Sports                               0.871
		Culture.Visual arts.Architecture             0.623
		Culture.Visual arts.Comics and Anime         0.422
		Culture.Visual arts.Fashion                  0.312
		Culture.Visual arts.Visual arts*             0.553
		Geography.Geographical                       0.609
		Geography.Regions.Africa.Africa*             0.598
		Geography.Regions.Africa.Central Africa      0.41
		Geography.Regions.Africa.Eastern Africa      0.514
		Geography.Regions.Africa.Northern Africa     0.44
		Geography.Regions.Africa.Southern Africa     0.673
		Geography.Regions.Africa.Western Africa      0.415
		Geography.Regions.Americas.Central America   0.686
		Geography.Regions.Americas.North America     0.647
		Geography.Regions.Americas.South America     0.763
		Geography.Regions.Asia.Asia*                 0.617
		Geography.Regions.Asia.Central Asia          0.361
		Geography.Regions.Asia.East Asia             0.421
		Geography.Regions.Asia.North Asia            0.583
		Geography.Regions.Asia.South Asia            0.806
		Geography.Regions.Asia.Southeast Asia        0.635
		Geography.Regions.Asia.West Asia             0.704
		Geography.Regions.Europe.Eastern Europe      0.72
		Geography.Regions.Europe.Europe*             0.72
		Geography.Regions.Europe.Northern Europe     0.663
		Geography.Regions.Europe.Southern Europe     0.714
		Geography.Regions.Europe.Western Europe      0.696
		Geography.Regions.Oceania                    0.741
		History and Society.Business and economics   0.417
		History and Society.Education                0.562
		History and Society.History                  0.4
		History and Society.Military and warfare     0.557
		History and Society.Politics and government  0.47
		History and Society.Society                  0.307
		History and Society.Transportation           0.808
		STEM.Biology                                 0.817
		STEM.Chemistry                               0.405
		STEM.Computing                               0.311
		STEM.Earth and environment                   0.674
		STEM.Engineering                             0.61
		STEM.Libraries & Information                 0.383
		STEM.Mathematics                             0.302
		STEM.Medicine & Health                       0.571
		STEM.Physics                                 0.265
		STEM.STEM*                                   0.751
		STEM.Space                                   0.819
		STEM.Technology                              0.29
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.977
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.972
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.974
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.98
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.959
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.995
		Culture.Literature                           0.983
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.993
		Culture.Media.Media*                         0.957
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.995
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.948
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.975
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.952
		Geography.Regions.Europe.Northern Europe     0.982
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.987
		History and Society.Education                0.994
		History and Society.History                  0.985
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.983
		History and Society.Society                  0.988
		History and Society.Transportation           0.994
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.963
		STEM.Space                                   0.998
		STEM.Technology                              0.985
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.022
		Culture.Biography.Women                      0.007
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.012
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.004
		Culture.Media.Media*                         0.034
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.002
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.014
		Geography.Geographical                       0.011
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.043
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.022
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.031
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.006
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.008
		History and Society.Education                0.002
		History and Society.History                  0.009
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.009
		History and Society.Society                  0.006
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.029
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.964, macro=0.966):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.97
		Culture.Biography.Women                      0.967
		Culture.Food and drink                       0.97
		Culture.Internet culture                     0.972
		Culture.Linguistics                          0.969
		Culture.Literature                           0.967
		Culture.Media.Books                          0.975
		Culture.Media.Entertainment                  0.949
		Culture.Media.Films                          0.974
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.973
		Culture.Media.Radio                          0.956
		Culture.Media.Software                       0.977
		Culture.Media.Television                     0.971
		Culture.Media.Video games                    0.982
		Culture.Performing arts                      0.964
		Culture.Philosophy and religion              0.944
		Culture.Sports                               0.974
		Culture.Visual arts.Architecture             0.973
		Culture.Visual arts.Comics and Anime         0.981
		Culture.Visual arts.Fashion                  0.967
		Culture.Visual arts.Visual arts*             0.957
		Geography.Geographical                       0.966
		Geography.Regions.Africa.Africa*             0.97
		Geography.Regions.Africa.Central Africa      0.981
		Geography.Regions.Africa.Eastern Africa      0.977
		Geography.Regions.Africa.Northern Africa     0.969
		Geography.Regions.Africa.Southern Africa     0.966
		Geography.Regions.Africa.Western Africa      0.965
		Geography.Regions.Americas.Central America   0.968
		Geography.Regions.Americas.North America     0.952
		Geography.Regions.Americas.South America     0.978
		Geography.Regions.Asia.Asia*                 0.953
		Geography.Regions.Asia.Central Asia          0.969
		Geography.Regions.Asia.East Asia             0.965
		Geography.Regions.Asia.North Asia            0.961
		Geography.Regions.Asia.South Asia            0.976
		Geography.Regions.Asia.Southeast Asia        0.966
		Geography.Regions.Asia.West Asia             0.968
		Geography.Regions.Europe.Eastern Europe      0.963
		Geography.Regions.Europe.Europe*             0.954
		Geography.Regions.Europe.Northern Europe     0.959
		Geography.Regions.Europe.Southern Europe     0.971
		Geography.Regions.Europe.Western Europe      0.966
		Geography.Regions.Oceania                    0.968
		History and Society.Business and economics   0.947
		History and Society.Education                0.961
		History and Society.History                  0.936
		History and Society.Military and warfare     0.955
		History and Society.Politics and government  0.94
		History and Society.Society                  0.894
		History and Society.Transportation           0.98
		STEM.Biology                                 0.974
		STEM.Chemistry                               0.979
		STEM.Computing                               0.98
		STEM.Earth and environment                   0.977
		STEM.Engineering                             0.968
		STEM.Libraries & Information                 0.973
		STEM.Mathematics                             0.973
		STEM.Medicine & Health                       0.964
		STEM.Physics                                 0.979
		STEM.STEM*                                   0.971
		STEM.Space                                   0.989
		STEM.Technology                              0.963
		-------------------------------------------  -----
	pr_auc (micro=0.722, macro=0.562):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.89
		Culture.Biography.Women                      0.56
		Culture.Food and drink                       0.413
		Culture.Internet culture                     0.563
		Culture.Linguistics                          0.702
		Culture.Literature                           0.586
		Culture.Media.Books                          0.486
		Culture.Media.Entertainment                  0.216
		Culture.Media.Films                          0.704
		Culture.Media.Media*                         0.765
		Culture.Media.Music                          0.78
		Culture.Media.Radio                          0.445
		Culture.Media.Software                       0.13
		Culture.Media.Television                     0.634
		Culture.Media.Video games                    0.69
		Culture.Performing arts                      0.349
		Culture.Philosophy and religion              0.398
		Culture.Sports                               0.911
		Culture.Visual arts.Architecture             0.586
		Culture.Visual arts.Comics and Anime         0.482
		Culture.Visual arts.Fashion                  0.242
		Culture.Visual arts.Visual arts*             0.567
		Geography.Geographical                       0.661
		Geography.Regions.Africa.Africa*             0.654
		Geography.Regions.Africa.Central Africa      0.345
		Geography.Regions.Africa.Eastern Africa      0.481
		Geography.Regions.Africa.Northern Africa     0.39
		Geography.Regions.Africa.Southern Africa     0.634
		Geography.Regions.Africa.Western Africa      0.268
		Geography.Regions.Americas.Central America   0.659
		Geography.Regions.Americas.North America     0.71
		Geography.Regions.Americas.South America     0.8
		Geography.Regions.Asia.Asia*                 0.671
		Geography.Regions.Asia.Central Asia          0.234
		Geography.Regions.Asia.East Asia             0.45
		Geography.Regions.Asia.North Asia            0.548
		Geography.Regions.Asia.South Asia            0.844
		Geography.Regions.Asia.Southeast Asia        0.583
		Geography.Regions.Asia.West Asia             0.713
		Geography.Regions.Europe.Eastern Europe      0.73
		Geography.Regions.Europe.Europe*             0.791
		Geography.Regions.Europe.Northern Europe     0.709
		Geography.Regions.Europe.Southern Europe     0.744
		Geography.Regions.Europe.Western Europe      0.724
		Geography.Regions.Oceania                    0.76
		History and Society.Business and economics   0.335
		History and Society.Education                0.535
		History and Society.History                  0.349
		History and Society.Military and warfare     0.57
		History and Society.Politics and government  0.422
		History and Society.Society                  0.238
		History and Society.Transportation           0.848
		STEM.Biology                                 0.868
		STEM.Chemistry                               0.399
		STEM.Computing                               0.257
		STEM.Earth and environment                   0.683
		STEM.Engineering                             0.624
		STEM.Libraries & Information                 0.506
		STEM.Mathematics                             0.281
		STEM.Medicine & Health                       0.552
		STEM.Physics                                 0.279
		STEM.STEM*                                   0.861
		STEM.Space                                   0.872
		STEM.Technology                              0.265
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'items': {'type': 'string'}, 'type': 'array', 'description': 'The most likely labels predicted by the estimator'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

