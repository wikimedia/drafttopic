Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'loss': 'deviance', 'validation_fraction': 0.1, 'min_weight_fraction_leaf': 0.0, 'ccp_alpha': 0.0, 'population_rates': None, 'presort': 'deprecated', 'center': False, 'min_samples_leaf': 1, 'min_samples_split': 2, 'warm_start': False, 'n_iter_no_change': None, 'criterion': 'friedman_mse', 'min_impurity_split': None, 'multilabel': True, 'learning_rate': 0.1, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'init': None, 'n_estimators': 150, 'subsample': 1.0, 'verbose': 0, 'max_depth': 5, 'scale': False, 'tol': 0.0001, 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'label_weights': {}, 'random_state': None, 'max_features': 'log2'}
	Environment:
	 - revscoring_version: '2.8.2'
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
	counts (n=59164):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16062  -->  14427  1635   889  42213
			'Culture.Biography.Women'                       3473  -->   2380  1093   349  55342
			'Culture.Food and drink'                        1497  -->    949   548   170  57497
			'Culture.Internet culture'                      3248  -->   2722   526   205  55711
			'Culture.Linguistics'                           1605  -->   1139   466   108  57451
			'Culture.Literature'                            5508  -->   4091  1417   518  53138
			'Culture.Media.Books'                           1634  -->   1301   333   121  57409
			'Culture.Media.Entertainment'                   2283  -->    929  1354   270  56611
			'Culture.Media.Films'                           2945  -->   2474   471   164  56055
			'Culture.Media.Media*'                         14272  -->  12658  1614  1265  43627
			'Culture.Media.Music'                           3213  -->   2699   514   265  55686
			'Culture.Media.Radio'                            310  -->    138   172    31  58823
			'Culture.Media.Software'                        2144  -->   1735   409   284  56736
			'Culture.Media.Television'                      2543  -->   2034   509   164  56457
			'Culture.Media.Video games'                     2140  -->   1962   178    67  56957
			'Culture.Performing arts'                       1472  -->    833   639   123  57569
			'Culture.Philosophy and religion'               3931  -->   2281  1650   418  54815
			'Culture.Sports'                                6366  -->   5673   693   231  52567
			'Culture.Visual arts.Architecture'              2014  -->   1394   620   255  56895
			'Culture.Visual arts.Comics and Anime'          1888  -->   1586   302    85  57191
			'Culture.Visual arts.Fashion'                    790  -->    473   317    68  58306
			'Culture.Visual arts.Visual arts*'              5332  -->   3722  1610   474  53358
			'Geography.Geographical'                        3781  -->   2468  1313   607  54776
			'Geography.Regions.Africa.Africa*'              4003  -->   2648  1355   365  54796
			'Geography.Regions.Africa.Central Africa'        850  -->    518   332    79  58235
			'Geography.Regions.Africa.Eastern Africa'        330  -->    186   144    58  58776
			'Geography.Regions.Africa.Northern Africa'      1500  -->    877   623   124  57540
			'Geography.Regions.Africa.Southern Africa'       665  -->    456   209    51  58448
			'Geography.Regions.Africa.Western Africa'        158  -->     77    81    49  58957
			'Geography.Regions.Americas.Central America'    1345  -->    700   645   115  57704
			'Geography.Regions.Americas.North America'      5707  -->   3667  2040   928  52529
			'Geography.Regions.Americas.South America'      1566  -->    993   573   146  57452
			'Geography.Regions.Asia.Asia*'                 11315  -->   8974  2341   967  46882
			'Geography.Regions.Asia.Central Asia'           1049  -->    595   454    86  58029
			'Geography.Regions.Asia.East Asia'              3337  -->   2588   749   239  55588
			'Geography.Regions.Asia.North Asia'             2979  -->   2187   792   256  55929
			'Geography.Regions.Asia.South Asia'             1683  -->   1108   575   100  57381
			'Geography.Regions.Asia.Southeast Asia'         1580  -->    873   707   115  57469
			'Geography.Regions.Asia.West Asia'              2267  -->   1543   724   192  56705
			'Geography.Regions.Europe.Eastern Europe'       5812  -->   4396  1416   594  52758
			'Geography.Regions.Europe.Europe*'             17938  -->  14647  3291  2351  38875
			'Geography.Regions.Europe.Northern Europe'      3606  -->   2420  1186   423  55135
			'Geography.Regions.Europe.Southern Europe'      4063  -->   2986  1077   385  54716
			'Geography.Regions.Europe.Western Europe'       5296  -->   4062  1234   602  53266
			'Geography.Regions.Oceania'                     1308  -->    753   555   112  57744
			'History and Society.Business and economics'    3052  -->   1610  1442   350  55762
			'History and Society.Education'                 1566  -->    627   939   161  57437
			'History and Society.History'                   5704  -->   3472  2232   791  52669
			'History and Society.Military and warfare'      4317  -->   2925  1392   433  54414
			'History and Society.Politics and government'   3186  -->   1637  1549   362  55616
			'History and Society.Society'                   4069  -->   1186  2883   246  54849
			'History and Society.Transportation'            4200  -->   3795   405   190  54774
			'STEM.Biology'                                  4703  -->   4077   626   164  54297
			'STEM.Chemistry'                                1590  -->   1282   308   143  57431
			'STEM.Computing'                                2426  -->   1980   446   293  56445
			'STEM.Earth and environment'                    1840  -->   1252   588   147  57177
			'STEM.Engineering'                              2415  -->   1712   703   174  56575
			'STEM.Libraries & Information'                   489  -->    258   231    42  58633
			'STEM.Mathematics'                               956  -->    765   191    59  58149
			'STEM.Medicine & Health'                        1930  -->   1366   564   165  57069
			'STEM.Physics'                                  1411  -->    948   463   175  57578
			'STEM.STEM*'                                   18294  -->  16383  1911   940  39930
			'STEM.Space'                                    2265  -->   2098   167    31  56868
			'STEM.Technology'                               4794  -->   3614  1180   564  53806
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.271         0.13
		Culture.Biography.Women                         0.059         0.015
		Culture.Food and drink                          0.025         0.003
		Culture.Internet culture                        0.055         0.004
		Culture.Linguistics                             0.027         0.008
		Culture.Literature                              0.093         0.015
		Culture.Media.Books                             0.028         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.05          0.012
		Culture.Media.Media*                            0.241         0.056
		Culture.Media.Music                             0.054         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.036         0.001
		Culture.Media.Television                        0.043         0.009
		Culture.Media.Video games                       0.036         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.066         0.011
		Culture.Sports                                  0.108         0.061
		Culture.Visual arts.Architecture                0.034         0.011
		Culture.Visual arts.Comics and Anime            0.032         0.002
		Culture.Visual arts.Fashion                     0.013         0.001
		Culture.Visual arts.Visual arts*                0.09          0.018
		Geography.Geographical                          0.064         0.021
		Geography.Regions.Africa.Africa*                0.068         0.009
		Geography.Regions.Africa.Central Africa         0.014         0.001
		Geography.Regions.Africa.Eastern Africa         0.006         0.001
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.023         0.004
		Geography.Regions.Americas.North America        0.096         0.064
		Geography.Regions.Americas.South America        0.026         0.007
		Geography.Regions.Asia.Asia*                    0.191         0.053
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.056         0.012
		Geography.Regions.Asia.North Asia               0.05          0.006
		Geography.Regions.Asia.South Asia               0.028         0.017
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.038         0.012
		Geography.Regions.Europe.Eastern Europe         0.098         0.019
		Geography.Regions.Europe.Europe*                0.303         0.082
		Geography.Regions.Europe.Northern Europe        0.061         0.029
		Geography.Regions.Europe.Southern Europe        0.069         0.014
		Geography.Regions.Europe.Western Europe         0.09          0.021
		Geography.Regions.Oceania                       0.022         0.005
		History and Society.Business and economics      0.052         0.01
		History and Society.Education                   0.026         0.008
		History and Society.History                     0.096         0.011
		History and Society.Military and warfare        0.073         0.016
		History and Society.Politics and government     0.054         0.017
		History and Society.Society                     0.069         0.008
		History and Society.Transportation              0.071         0.016
		STEM.Biology                                    0.079         0.035
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.031         0.005
		STEM.Engineering                                0.041         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.016         0
		STEM.Medicine & Health                          0.033         0.007
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.309         0.066
		STEM.Space                                      0.038         0.004
		STEM.Technology                                 0.081         0.005
	match_rate (micro=0.056, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.134
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.005
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.008
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.013
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.014
		Culture.Sports                               0.059
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.057
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.061
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.014
		Geography.Regions.Asia.North Asia            0.009
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.025
		Geography.Regions.Europe.Europe*             0.119
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.017
		Geography.Regions.Europe.Western Europe      0.027
		Geography.Regions.Oceania                    0.005
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.021
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.015
		History and Society.Society                  0.007
		History and Society.Transportation           0.018
		STEM.Biology                                 0.033
		STEM.Chemistry                               0.004
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.081
		STEM.Space                                   0.005
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.944, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.866
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.995
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.992
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.987
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.941
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.943
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.939
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.991
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.975
		Geography.Regions.Europe.Europe*             0.881
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.983
		Geography.Regions.Europe.Western Europe      0.973
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.979
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.985
		History and Society.Society                  0.993
		History and Society.Transportation           0.982
		STEM.Biology                                 0.967
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.919
		STEM.Space                                   0.995
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.772, macro=0.693):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.898
		Culture.Biography.Women                      0.685
		Culture.Food and drink                       0.634
		Culture.Internet culture                     0.838
		Culture.Linguistics                          0.71
		Culture.Literature                           0.743
		Culture.Media.Books                          0.796
		Culture.Media.Entertainment                  0.407
		Culture.Media.Films                          0.84
		Culture.Media.Media*                         0.887
		Culture.Media.Music                          0.84
		Culture.Media.Radio                          0.445
		Culture.Media.Software                       0.809
		Culture.Media.Television                     0.8
		Culture.Media.Video games                    0.917
		Culture.Performing arts                      0.566
		Culture.Philosophy and religion              0.58
		Culture.Sports                               0.891
		Culture.Visual arts.Architecture             0.692
		Culture.Visual arts.Comics and Anime         0.84
		Culture.Visual arts.Fashion                  0.599
		Culture.Visual arts.Visual arts*             0.698
		Geography.Geographical                       0.653
		Geography.Regions.Africa.Africa*             0.662
		Geography.Regions.Africa.Central Africa      0.609
		Geography.Regions.Africa.Eastern Africa      0.564
		Geography.Regions.Africa.Northern Africa     0.585
		Geography.Regions.Africa.Southern Africa     0.686
		Geography.Regions.Africa.Western Africa      0.487
		Geography.Regions.Americas.Central America   0.52
		Geography.Regions.Americas.North America     0.643
		Geography.Regions.Americas.South America     0.634
		Geography.Regions.Asia.Asia*                 0.793
		Geography.Regions.Asia.Central Asia          0.567
		Geography.Regions.Asia.East Asia             0.776
		Geography.Regions.Asia.North Asia            0.734
		Geography.Regions.Asia.South Asia            0.658
		Geography.Regions.Asia.Southeast Asia        0.553
		Geography.Regions.Asia.West Asia             0.681
		Geography.Regions.Europe.Eastern Europe      0.756
		Geography.Regions.Europe.Europe*             0.817
		Geography.Regions.Europe.Northern Europe     0.671
		Geography.Regions.Europe.Southern Europe     0.735
		Geography.Regions.Europe.Western Europe      0.767
		Geography.Regions.Oceania                    0.576
		History and Society.Business and economics   0.528
		History and Society.Education                0.4
		History and Society.History                  0.609
		History and Society.Military and warfare     0.678
		History and Society.Politics and government  0.514
		History and Society.Society                  0.291
		History and Society.Transportation           0.904
		STEM.Biology                                 0.867
		STEM.Chemistry                               0.806
		STEM.Computing                               0.816
		STEM.Earth and environment                   0.68
		STEM.Engineering                             0.709
		STEM.Libraries & Information                 0.528
		STEM.Mathematics                             0.8
		STEM.Medicine & Health                       0.708
		STEM.Physics                                 0.672
		STEM.STEM*                                   0.896
		STEM.Space                                   0.926
		STEM.Technology                              0.754
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.943
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.985
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.994
		History and Society.Society                  0.996
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.977
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.688, macro=0.545):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.867
		Culture.Biography.Women                      0.628
		Culture.Food and drink                       0.358
		Culture.Internet culture                     0.465
		Culture.Linguistics                          0.756
		Culture.Literature                           0.541
		Culture.Media.Books                          0.625
		Culture.Media.Entertainment                  0.256
		Culture.Media.Films                          0.773
		Culture.Media.Media*                         0.65
		Culture.Media.Music                          0.794
		Culture.Media.Radio                          0.666
		Culture.Media.Software                       0.178
		Culture.Media.Television                     0.715
		Culture.Media.Video games                    0.698
		Culture.Performing arts                      0.452
		Culture.Philosophy and religion              0.449
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.632
		Culture.Visual arts.Comics and Anime         0.579
		Culture.Visual arts.Fashion                  0.319
		Culture.Visual arts.Visual arts*             0.597
		Geography.Geographical                       0.566
		Geography.Regions.Africa.Africa*             0.465
		Geography.Regions.Africa.Central Africa      0.243
		Geography.Regions.Africa.Eastern Africa      0.226
		Geography.Regions.Africa.Northern Africa     0.271
		Geography.Regions.Africa.Southern Africa     0.511
		Geography.Regions.Africa.Western Africa      0.308
		Geography.Regions.Americas.Central America   0.479
		Geography.Regions.Americas.North America     0.716
		Geography.Regions.Americas.South America     0.636
		Geography.Regions.Asia.Asia*                 0.688
		Geography.Regions.Asia.Central Asia          0.237
		Geography.Regions.Asia.East Asia             0.693
		Geography.Regions.Asia.North Asia            0.479
		Geography.Regions.Asia.South Asia            0.866
		Geography.Regions.Asia.Southeast Asia        0.638
		Geography.Regions.Asia.West Asia             0.708
		Geography.Regions.Europe.Eastern Europe      0.562
		Geography.Regions.Europe.Europe*             0.561
		Geography.Regions.Europe.Northern Europe     0.727
		Geography.Regions.Europe.Southern Europe     0.6
		Geography.Regions.Europe.Western Europe      0.593
		Geography.Regions.Oceania                    0.579
		History and Society.Business and economics   0.457
		History and Society.Education                0.537
		History and Society.History                  0.314
		History and Society.Military and warfare     0.575
		History and Society.Politics and government  0.572
		History and Society.Society                  0.356
		History and Society.Transportation           0.814
		STEM.Biology                                 0.913
		STEM.Chemistry                               0.358
		STEM.Computing                               0.312
		STEM.Earth and environment                   0.561
		STEM.Engineering                             0.575
		STEM.Libraries & Information                 0.339
		STEM.Mathematics                             0.27
		STEM.Medicine & Health                       0.617
		STEM.Physics                                 0.174
		STEM.STEM*                                   0.733
		STEM.Space                                   0.881
		STEM.Technology                              0.276
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.983
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.995
		History and Society.History                  0.996
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.992
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.993
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.721, macro=0.594):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.882
		Culture.Biography.Women                      0.655
		Culture.Food and drink                       0.458
		Culture.Internet culture                     0.598
		Culture.Linguistics                          0.732
		Culture.Literature                           0.626
		Culture.Media.Books                          0.7
		Culture.Media.Entertainment                  0.314
		Culture.Media.Films                          0.805
		Culture.Media.Media*                         0.75
		Culture.Media.Music                          0.816
		Culture.Media.Radio                          0.534
		Culture.Media.Software                       0.291
		Culture.Media.Television                     0.755
		Culture.Media.Video games                    0.792
		Culture.Performing arts                      0.502
		Culture.Philosophy and religion              0.506
		Culture.Sports                               0.91
		Culture.Visual arts.Architecture             0.661
		Culture.Visual arts.Comics and Anime         0.686
		Culture.Visual arts.Fashion                  0.416
		Culture.Visual arts.Visual arts*             0.643
		Geography.Geographical                       0.606
		Geography.Regions.Africa.Africa*             0.546
		Geography.Regions.Africa.Central Africa      0.347
		Geography.Regions.Africa.Eastern Africa      0.322
		Geography.Regions.Africa.Northern Africa     0.371
		Geography.Regions.Africa.Southern Africa     0.585
		Geography.Regions.Africa.Western Africa      0.377
		Geography.Regions.Americas.Central America   0.499
		Geography.Regions.Americas.North America     0.677
		Geography.Regions.Americas.South America     0.635
		Geography.Regions.Asia.Asia*                 0.737
		Geography.Regions.Asia.Central Asia          0.334
		Geography.Regions.Asia.East Asia             0.732
		Geography.Regions.Asia.North Asia            0.58
		Geography.Regions.Asia.South Asia            0.748
		Geography.Regions.Asia.Southeast Asia        0.592
		Geography.Regions.Asia.West Asia             0.694
		Geography.Regions.Europe.Eastern Europe      0.645
		Geography.Regions.Europe.Europe*             0.665
		Geography.Regions.Europe.Northern Europe     0.698
		Geography.Regions.Europe.Southern Europe     0.661
		Geography.Regions.Europe.Western Europe      0.669
		Geography.Regions.Oceania                    0.577
		History and Society.Business and economics   0.49
		History and Society.Education                0.459
		History and Society.History                  0.414
		History and Society.Military and warfare     0.622
		History and Society.Politics and government  0.541
		History and Society.Society                  0.32
		History and Society.Transportation           0.857
		STEM.Biology                                 0.889
		STEM.Chemistry                               0.496
		STEM.Computing                               0.451
		STEM.Earth and environment                   0.615
		STEM.Engineering                             0.635
		STEM.Libraries & Information                 0.412
		STEM.Mathematics                             0.404
		STEM.Medicine & Health                       0.659
		STEM.Physics                                 0.276
		STEM.STEM*                                   0.806
		STEM.Space                                   0.903
		STEM.Technology                              0.404
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.982
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.99
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.993
		History and Society.Society                  0.995
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.999
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.985
		STEM.Space                                   1
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.977, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.933
		Geography.Regions.Europe.Northern Europe     0.983
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.989
		History and Society.Education                0.992
		History and Society.History                  0.981
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.986
		History and Society.Society                  0.99
		History and Society.Transportation           0.995
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.021
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.028
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.011
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.017
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.02
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.011
		Geography.Regions.Europe.Europe*             0.057
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.007
		Geography.Regions.Europe.Western Europe      0.011
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.003
		History and Society.History                  0.015
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.006
		History and Society.Society                  0.004
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.023
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.972, macro=0.972):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.972
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.976
		Culture.Literature                           0.977
		Culture.Media.Books                          0.985
		Culture.Media.Entertainment                  0.962
		Culture.Media.Films                          0.984
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.936
		Culture.Media.Software                       0.985
		Culture.Media.Television                     0.983
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.975
		Culture.Philosophy and religion              0.956
		Culture.Sports                               0.98
		Culture.Visual arts.Architecture             0.978
		Culture.Visual arts.Comics and Anime         0.987
		Culture.Visual arts.Fashion                  0.97
		Culture.Visual arts.Visual arts*             0.97
		Geography.Geographical                       0.968
		Geography.Regions.Africa.Africa*             0.969
		Geography.Regions.Africa.Central Africa      0.982
		Geography.Regions.Africa.Eastern Africa      0.954
		Geography.Regions.Africa.Northern Africa     0.973
		Geography.Regions.Africa.Southern Africa     0.974
		Geography.Regions.Africa.Western Africa      0.906
		Geography.Regions.Americas.Central America   0.967
		Geography.Regions.Americas.North America     0.962
		Geography.Regions.Americas.South America     0.976
		Geography.Regions.Asia.Asia*                 0.966
		Geography.Regions.Asia.Central Asia          0.974
		Geography.Regions.Asia.East Asia             0.979
		Geography.Regions.Asia.North Asia            0.976
		Geography.Regions.Asia.South Asia            0.974
		Geography.Regions.Asia.Southeast Asia        0.969
		Geography.Regions.Asia.West Asia             0.974
		Geography.Regions.Europe.Eastern Europe      0.973
		Geography.Regions.Europe.Europe*             0.956
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.974
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.97
		History and Society.Business and economics   0.954
		History and Society.Education                0.953
		History and Society.History                  0.956
		History and Society.Military and warfare     0.972
		History and Society.Politics and government  0.952
		History and Society.Society                  0.909
		History and Society.Transportation           0.986
		STEM.Biology                                 0.982
		STEM.Chemistry                               0.986
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.975
		STEM.Engineering                             0.977
		STEM.Libraries & Information                 0.962
		STEM.Mathematics                             0.987
		STEM.Medicine & Health                       0.976
		STEM.Physics                                 0.983
		STEM.STEM*                                   0.977
		STEM.Space                                   0.994
		STEM.Technology                              0.976
		-------------------------------------------  -----
	pr_auc (micro=0.768, macro=0.595):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.94
		Culture.Biography.Women                      0.639
		Culture.Food and drink                       0.391
		Culture.Internet culture                     0.662
		Culture.Linguistics                          0.72
		Culture.Literature                           0.7
		Culture.Media.Books                          0.779
		Culture.Media.Entertainment                  0.233
		Culture.Media.Films                          0.82
		Culture.Media.Media*                         0.854
		Culture.Media.Music                          0.874
		Culture.Media.Radio                          0.323
		Culture.Media.Software                       0.33
		Culture.Media.Television                     0.769
		Culture.Media.Video games                    0.87
		Culture.Performing arts                      0.461
		Culture.Philosophy and religion              0.498
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.698
		Culture.Visual arts.Comics and Anime         0.757
		Culture.Visual arts.Fashion                  0.324
		Culture.Visual arts.Visual arts*             0.676
		Geography.Geographical                       0.623
		Geography.Regions.Africa.Africa*             0.54
		Geography.Regions.Africa.Central Africa      0.238
		Geography.Regions.Africa.Eastern Africa      0.151
		Geography.Regions.Africa.Northern Africa     0.296
		Geography.Regions.Africa.Southern Africa     0.43
		Geography.Regions.Africa.Western Africa      0.186
		Geography.Regions.Americas.Central America   0.445
		Geography.Regions.Americas.North America     0.745
		Geography.Regions.Americas.South America     0.625
		Geography.Regions.Asia.Asia*                 0.796
		Geography.Regions.Asia.Central Asia          0.273
		Geography.Regions.Asia.East Asia             0.779
		Geography.Regions.Asia.North Asia            0.613
		Geography.Regions.Asia.South Asia            0.779
		Geography.Regions.Asia.Southeast Asia        0.535
		Geography.Regions.Asia.West Asia             0.704
		Geography.Regions.Europe.Eastern Europe      0.705
		Geography.Regions.Europe.Europe*             0.766
		Geography.Regions.Europe.Northern Europe     0.742
		Geography.Regions.Europe.Southern Europe     0.718
		Geography.Regions.Europe.Western Europe      0.713
		Geography.Regions.Oceania                    0.531
		History and Society.Business and economics   0.441
		History and Society.Education                0.381
		History and Society.History                  0.472
		History and Society.Military and warfare     0.667
		History and Society.Politics and government  0.558
		History and Society.Society                  0.258
		History and Society.Transportation           0.902
		STEM.Biology                                 0.935
		STEM.Chemistry                               0.515
		STEM.Computing                               0.5
		STEM.Earth and environment                   0.634
		STEM.Engineering                             0.661
		STEM.Libraries & Information                 0.198
		STEM.Mathematics                             0.507
		STEM.Medicine & Health                       0.661
		STEM.Physics                                 0.21
		STEM.STEM*                                   0.896
		STEM.Space                                   0.94
		STEM.Technology                              0.534
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Culture.Media.Books': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

