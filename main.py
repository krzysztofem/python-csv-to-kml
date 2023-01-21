from bs4 import BeautifulSoup as Soup
from modules.getKMLstyle import getKMLstyleList
from modules.createPlacemark import createPlacemark
import xml.dom.minidom
import pandas as pd
from datetime import datetime

fileCSV = open('_source-for-map/znaleziska.csv', 'r')

ICON_RED = 'https://lh3.googleusercontent.com/fife/AAbDypBM4T1CelQIu53wje0S8wF2_bpsV29AYsIy1uNOiwgTOUNe7CLcsqQPXE4Oa_IL5vgpL3825n2I12l9ZPNz5OaWb4aeud1EWygWB79U5zNONQ-GiuaBDUoU2qk_XC3FFTMC0i1zRIo7yPSyK1LyTiVPbgYV7D0rAnEwIprsAgSNm13A588xyymdAcNuRDb2V1vgSEajIcAp5AVkERsV6ESiTDbuUq9T6jStTTqLXPmlj0SbfxOpr9SBiE8Z3X4xqZFiO-SdIqBB-kYXK4Mk6tWJHppmOkxpVI2hale-yWwfqjfqZhwij8ESn5UMx6yz-hLkEVLTl9NBunb2ydMCG33B8NjK7UHS0uval7UqC_1gGUDPgkqsn2gCbWC16UEhPd99LEdOoQ2_oQ4_AQZONpSXHki6BaVC4I6yvN4UblfKHPyzZ4dIRb3ZZLS-2tfhScFYBB6VK1fnXSVJjLXUchqMsyoUHr0791OExdViWqYFqRE7k7Cv5Dc_aolu9esi3laau_RXoR66fggE7dIHIMTR0naRNRtc1R8tyk--vVVIHvWnDEbe1gAZ5SPV-vmXBXzefISQtnLW_SUeDBsX3q7v-VD3mr5YZ6aiIgocxPzJZd1-wPWiYqNBrMmekJKpflJCC8QdKv2vM7FvrkVsNOAeRgt8wq4WxGBchJ-faUI1hquh-otcIYfn8ZW6l9TKhKRt7v125CY9G2N1Yk-9AbhaGTWJ3U-S7SnU6sRTfiYQZjA6-yoHpWLV-AGUDKvVp-vPV1x-m-iblKliBaYadrJJ4kqcwDKauAbKEFk3Aq28_lNtUhZFVAcnCkGavSg-b6iudGcK5-TFmGWOM-pq5StG3fk5gcsm2x1uwjlT-7Bqdfqcr7S4bSLHo6iapvYGsYqHZ5582k_xikmUwI5nuoY4ZBhTcx_BD4xnVIl6eoRs1AK5clqaMlOTA_5tMx_OH5iSkxPshD-vlf8I1O6VpPMuF6XbrYkPkle5HDX6p_ZQT1vgYsI617wx_p0SaQNRnOTW6Gy-twp2GJdgVJoHImE_ZrL2KScVATM_WYZKVs925jnBpMNj9TB9XFfbr2P-maMBDizHAe9OlvzbEL-lAKnPKTOX_dKS1i1xsavYpZNek3I3I5LsQnrK1KoXCt8YJkYOLNPP22H03_VMSwKcp00teJTVzR2cPPn4mLGnDgs3HSKZVUFTxrlSqFHD-3gWg9Hxf3pcnYp5BdQ42HRsGxIueXZHMnJZ4s7BLAOFStGhSqd_LX4OIwPFhq1qgbQAUmgm3lBwUWqlam6LuQV1F7icau0WRHDU_srOLT-cNiQzl1of4CRRkVWZZWIy0f2TWeBFoH0bMCHQM-2ROU6dHIijCzbNTnfepRKMV65xGpU7GAHxnW7p6qERRBTwmZzEAaQuqp0KHxPDo_oX4XAszws8XMRj0Pa0gvzNw8XvKS-Qb-BDaXguqP656dmjnD6pksO5dkY9anHJPdGTbsySFOsjat-fnqAmlPAXiEEatnPxTHl36FJk65aSMzxcto0Jx_m9wflaIL9zmQPl3oz-7LuqcmgCzQ=w3714-h2128'
ICON_GREEN = 'https://lh3.googleusercontent.com/fife/AAbDypBRNQAhWSCI3_3nYw4qU5oLFDl9ejll7Ew86fJUrcxkl0mNCj4bgtWv5DksmNqQJN-0eYt6MLI7FK4rlnJaEdkZEB81E9Qpe3iZnazxjO7Ke_rav1ZZ2z3xdUjViJlhX1y2SN92Oo5ypyeIWy0PKkEo6bJapQDaf941SQK8DddJyniKRdgzWfdVjopl1GIiwo3Z0w6EAGFXaSEev9EATUGhchhdTDpnIqDNnbWnSiE7S59YsG54PwZH_EPl0GoeeLdYhODpOjeusj0av9v30ZrbbyCouajfyp5zc9UicoI-_ot0AYBSQrlCb60KnWcVa2dR3J1Sr_u2UNWrufytZGXLYu6kSeNQvcc4BL3nv3Xu863pS7jYrCNjp4qP6xvT_Ka1FD5_rYMGxJtZkG-goI8ov8LdhJhFT7pttnG_dUTn9mh2nJOavui79gv6bmfbtCTghwekG15EauajFLgFEszwB9IUpKOxhSHbIPSVU2hIwdRS33auzkNz-SU0nFOxZlHEsOTTTg-gw6xAKIYybv4LVY1apjP09a26RosQ-uv1fxeS0rMmi7ZTH5lHZiA05nHLIf-6p0NCzCek8pHj34c8kxZnKa7zt507n3UfSoXSS1uttb4e-cT107tudLmro2kktnigQbGOv2ja3Pee53bGn7C_M19vlJ0HzQU6wBeiDWMb7IxfJakLDPhiLfNijqpc26-e0sy8xQMmfr21q4bgCyQ6-NyzCNPumziiyD8bN6668dWtzV8we_eIIGfv-vkBjxusH0echVaeKYtmAII_ajtIEJ8bIF7Xk1tecQX-FhKywi6aHAP9xzXMnnf1YEqLypsG0eOLIZ6gsQW3I13wd12BLCilErqwc_Qwlv_07MhRj52wuJiJqbX33wtJqn99QtBtaFWKCSVlOh-gPS-8C1on625mP_HAs1Dk2NWi6BGMAjmkoDtXI0MxYEyGljK0arstZj1r217vRYI93RdM4bcmEK7KW8oRAlDhmEJAhraIv1vkmO6mpNOus-FpFss390Z2QTdXB7KAGyxdUqdAysOGqejuXSyiEuVPlaBb5gY6ey1e3Woe_v--IUPxdUtbsiO5ARHYf2prYQwr5n15Ec0UDxgBeoZwGxpNos5lcVom2fLBlPfOspuROqUn6p3l9vz6TQGAUC-9B8le65pi8E-CHnrTf6yvnKO1elozWbKLVVOd_pu5GvDEdz92hBzc9s5ZBcyPwK3wZLFpFid2UXSOfd0oStTNpKCzn4Q2i079kBYalrLA9U4T0CKXuhMcsWJ_bneSORBlS50SPdxn7BZ5Em5qzGW7SQUUZNslu9bAq3tdjnK4exmjATap4MPvJsVHVMExsuo0_KYgj0QpcpygH4XpCdM9gNMvZZm7rffrnkcLueG-ujccjQU-PrU7KP2w5r89Veob9N1h2x-jrS_JXFTzH52iBgTVnV2o1LYPbQ-_77dFVn-bD3jr32wv4-ZXkZ3oJdtMwVnMSObKA29nZbtD36vN0Cl4pPmmy4gV8Ck3v7_VxAlXwWrVfadfguptdEmr85PAiNY7Q-MM7ypc6A=w3714-h2128'
ICON_BLUE = 'https://lh3.googleusercontent.com/fife/AAbDypDM9LzQ62JQTe1qxb7CNccO1GdbUUEeGmjKZPucR6br3cSPHSwLjBXTTsuG-6y0oe-W82mmANKZUjw0NLEe_O4FQfWygzsUcPAn8RPplDszKz9ahp1rw-8z2FP3J-t4_iUMHsuNgLezkNc8aFqz4SMNYXwG5vw9F4d_YT95Dy113T8MfDDlbeoqibt7AuMdHi9-CNiYHbwp5Bjp2RzNMSOG9SDZHp1kNz_i3AZ00ORj2U_nK-9LuQpHAXqLnxptA75okZVGQlYUDTkxV1b9UdqyJ9n0rkVNyFshjVPVSvik99CswpKRdsEr7_ix9aL4Wb0A2l9pNKI7EfGFOK37_Eurcr3OsfXgiOeX7NvUKpsmrtUxnNNeIGOrNSvbXx_zrW26kXxh-SS_EHhYmkob-qqQ2Oz9RZ7q-HIBTUU67eiT1dzkPeIgoQjie-F7438bSYCLe7ei73MH7GPSaMBTyER5JyofXI0MMJbJHKRhWyPCjiXOswnxkZovrPGbhDfqedMmwMQ2qsksURqVACRFHuV7c1FtXv6TOPgdTgxtAisQurAHGKh23_hvhsQHwDiG8CSzF8terxcvY1ACpkoRZSL9m4kG4PP4VCIbWXIWy23bAyTS4TB_q903BEMrMiUuWwvtveGv4NdvUU32vFEhjtXlBe9HHdfWwohvAbEsjzRw6i0wfTTC47oPSFelcJubv7nuknFZaPbIVxp3CO_dSgIATji9Oim5EAoT86Eg6rUNpNmEW_OU-69EnwclFFUHymKy8OjeWv2Ub1YQ2U6QxcMS7jpwtW_6Kqlc9ZLOIKdrIPypCxrEWFs3m6qAQ98B_Txtf-6QPpJKv62Xs8Jl_SMUiPveLzRObIakBUEKsRuWj8oIhliVjdbvQEwPpO4nnSpJFfRnFUM0dggruoBoMnFbeM4ecpNVhq-NGGgSi1bxWdQBtPsosaGcUc3OlbsQUUaNCbYME4PrdkFwaaLeUdc5clNZxuJKD1y1ErAmWUCTHZqX-N-0pfIJ3DrScySnydbgymHROB9Xt9i3FyQtUuvcoObcIrOVv6Xl8CbtQkh_ZU-lmxmQgCThu0R3eUsOcd_k-zXGQRop3j_VDqKIxBtvugQDDbLsJ8Jjc9kqDgAnUZBponY2SICB-qZh2CQO2HnaWT12i-YNiMLmfD5yB8VrhpJsPyd06-PVZ5Hsgg-4ZkSdz4DtLYd8JlTSGapU1HCDkd20QUFLuozimvwckBUH3wlZDtOp7_Rj0KAFTKIbrayWw05e8HkRzhFIv2giX2ZoxWqCxBLaI5D-xf35HTGgQp62WVNzmhPxzbZ4ahP2PBDXpFOLWEwJri1fMiofurdLlIyaflpnC0PG0kj1KQEzmjz5IA1HGWG0UhrPo5SK07j99J6KnpNNiCWdW6WqmbuZcXzEuP41GKs0PvqvjkTAEtOrOeRbaSJPiih6OL5B18NGEe4J9hmF0b9IrtNYB9PIAK_vSlRKYx0Vw3eY8H6nUqievoPn7IYDxRmMZ-o4f-T8-1qvaFkpVujKq4VQXw01Xj1-uSfxrubv9xaedAYsmGh5Kg=w3714-h934'
ICON_YELLOW = 'https://lh3.googleusercontent.com/fife/AAbDypAVPm0KfZmtHCr9cGuXaKp_HqXbFIsPFNpRF1hHlNQ9piAbQ0-RpB-4vd2663SJPZvxPWqAiq1H960lbti2c-mxVrMqd2raV4YnuROxB-VOBT9qHsxUQKIyjWCYa7EjoWI4EwUxAL2GTQQXcCbsjjjhA-MwtTWYCw2_425NuTzthImv5PcRMoQ9W4Yjy2ay6ELLh2mVVwuMdyBCmrAV9XiSO7S3krZFcgVjwOvqfr1QPHaVlqUsvb1AWzhg9wnIUx2mMoaV4cRhb1bbVLYiE_lg6eBnEfRUokk5XOXUmoWXo_pgTK3PGzQ31NYwkFc_NPuroGGqcxfBeY5tkN7lnpVgq2ysoLW_zedY84m9Ktg0TEpkbatzMpOwS4F1XQ57u8QEVefBUqP8NNMkzgXc4tFn-irzTctVLsjLMbRuZ-3m-HiWfA0Lcdz7o88gW_CtcD5q5u3aDmmLaXwR7DgYjemuMvbFsLJf4j3FyOT7pzb1xe_jXZ8HkqTM88X2Xos5RxjCjNXQXokGleC59ccdoEDnj5wMtzih227UGIh7r-xI9LcAbCO_dneFOeDMroikTQZN_BmfXyvSPTBQB1KWZKAnjFFpmW9OZ0HfBpj-zpET-P9yDZQLFBngBrZgwIt4MkpWdzfAXAYe-FQQsvmlGSXuMIIRE3OFrkInkeV0vHvwA5eYtGdnSrblTR83_XCu7lUhOQFbiiTH9qvc5pXSwWpkA4IjG7QMieAlPOfK5TBAEUvnzNtsALpd6R9g_HjRRgAT17hkUDrDW_X68mqu71rLhZveZ7Jyjk5g2uQUt5SKtclXriW-8-dLRoAQmzJS7x9eKdsnF5IUPzpWWTtDNn35k7n541IKI9YaBel7w2ZExekFEYtv-6Gm6cT3W7JQRzAzm2hTN0yb6lq2tHW3kCovXeP1tK8wUN-qJmr621g2yUPXdL2hiMcLLdNwlw5t4ED9DAfprnjQo7aW6PVsF3JKjbozD2g84IG3rthocNKlH-K4tTSQdf8fotZver8acPKfaO0i5Pn6y9C-RpN8NmCW9FhcalRc2HQjniMQ_2ZXL9QgXSFPJa5rQ7c-PWwMnrCvca0QKzENU24rxZ9OhMJn36MpvWP8WPxar_ieOBnLNBoyLqv73chWdXVhM1siU_QJ2UT7t1C0y68s_JGeyW0y04qczkN-pTvmRVJTrJF6JtfP6mUwQ8i2VKJv7puBVK3ryHBAISxvBVg7d6udkVRkfdjY7CBNuIppSYFSQ1TEDqH51TffNauxJxhh0MFeUYDST3_sXVoxu84T4Kn4Z3_kxm2FEqrM6tQAYGSa_qWvaIwZxaf3WcBp6BaOR7gfNozf28SU5YIHcWwrtYsfh2ZrGef1UxIYot7aIOs8z_qLN9Ps7lgQ5oUFjr7kwkgPazjshX8fFpIcslM4gSdXGckkaMIKbMETGZL6cbfuEnVJZLgGuHyc3HNHtQ6BAHK-E_5T5ZSg0z-jLURQhWDrKQ7T3U1msOYuR6s6LFNdzog2MkRbqW5kukylhzoZFh296vI5I8LPnJxU5gPyEk-wJh4EXJcSIQ=w3714-h934'
ICON_BROWN = 'https://lh3.googleusercontent.com/fife/AAbDypAag5ygU4Bf99dj4bLrGuroBWKugHwrwkO7YWu0tYsjuct72h0TApUYoojtdR247nu7eWKOZoHSPncM6r0DxG_goUqI6S6VmktM-07zoWFMmboPYb6L37iLOL-gicSUjMzonSMmitxjXuvCpAg-0YDUIy-S22FF8reawECxOj0o77L719hIpMaQOzseMvHle9idKTpRw1MztZ_oa4d9TGMqVBwEnMuAhnC2JYyYReX_KTlhqI1ETBjYPalPnsIJvyB-caT_bCYwTWlm2KBexbq18a79eTSMk0pFyHaWwJ10J3Jrd4B1-CLYUTWsZdvjfZuqP4GKkrZOxtY7OB7tXZfOzarot6DoCtpzCNw0_MW5l5oDxFw2LfH6h1MVUN0yab1srEBgLPGf8Ck6EihxpeIpec9LxfOmwPFSog3sJq1euCJPLH6PZr-VBSMgQqTMx2sTi09vRV5bwpCcFEFSLkFr4ZOGEUxe-i3lLNEL3dSvgMz7wA7mUMgZxjHL41jHm2af0JL3sFPzq_wICs6RHn-Xo-Jz8sg83i5-K-x66KMou-J4yLZTZGoivFngUBBzgZ6oCseSRXGz-GbZIPsTiPpHs_HlGPAbXI2MblyH7dLg4a2GEYrVW_aIiahiCT6E0sSs9UQOthRt_NMWKsEYWr8Hf9HCqg8WfY4HWtty0PfqUpXrJaBhZBp5GmW2mQMQkctUkGkhixegbhmPo9mTTnZU3rBhDBL823q_lgkqAjNE13F-BqyAuyaAHsOYUuXGnEb1wPKXA_mloEnwDBuJ7_L6-tIlgMWGTSg-fz8q_HnE_92Iaf8NPU35CaaCQJNujFpGKNzE7O69Uj4CY3W1uHPhK1FdM9FvD3ynnJPYy0hRiSesfHxRA_XWxSta2qlT-Hc2w8Upfbw-vrsfnUs19rXNjnUn5sn_83i_0TSA1qSZpadi0aY5cx5ofYWXGjxSIwiQEUm13iDrwLzxbmppiPejHRVuoN2MxmtkIEiK2RrV-wLcGHYHeGrd6jEPAOoVbnlCVQMWJopdcl4sP_yWVIN8yQTrPmTXHoiqIR4JPb_chhVb29mVwtQd0VGCvEcoWd4ufanz66CoRj_2L54IpzM7BQEbuqhZmgKYtYFrVssqo9USJFz9vT5kIb71hJyRbkz_SEUTzyiWinixweoapYSDlFFXRyEo9u47CpSeWVgk818mRSNFeosn3H5FSSH4DtOdUqf80wY2oFpfwcozTPzXcwYyBhseRqv3zEOLRn7bjlJ31SbMi5HrpUssjfM-rRZYdWDFeMlvam8tdUqIfpdJQc5ZIHKFRG26tzQ1D6k7lPyUnxm0npbZuhdqIbDspGYwYVg4mvYWFWwEqGHkeh49bH7kbJzl84nSy1DpeURrkTvTZ3CZuqPsaC49RLzUEG1JpOWsT0HP3U2GWoLBhyNLV-WiXmSIQY1U-EaYeRRhTac8LPU-_E4F4cp6zJ-0VaCXkj7T6B-SaEOCVNW_qvFvSbPW7feWAWH_z4EHjfo8kSGbS_mW1yNjMdx1jrhwDRzsaP8DKXHTE6JLhphz2sGfrkAnDg=w3714-h934'
ICON_GREY = 'https://lh3.googleusercontent.com/fife/AAbDypDsd6-JchFGaszrPGMvzRacG6u4dwEOEwiwYXcRWgk8x73oWVKtO6bMvXwQucAelePPxAaaPuKH3K6fM-2EESjNxNClZwAlXCz09WWCDF7ncaLf2u1HnRG3PaKmd7GZkbFnZrF0xRSfhCUqhzV-ndIxSLPsYxCdGRKISLqsv4XkW4a5oU5TyCazU2XRyJkrx82MabUYIurwld-du9-Jb6YNkIMeiX5vxUw9Rs9n5TYYJRKH7_ygF_ac-Jzwtp_CR07RECzT8vQuK7ZUlXG09E-K01egTyqZ2zjDNJcndZA-LmIqlPZ3bZBNxzMedicPIhgRdZCgPSAeYk6MkPeIfDMS0cqZQrKyRcBB_zhd2KKM62pXKC9PkF4d_DIP9NZWfbjvPCw89WS8fEH_Y6SBg2YTgKol0WS9riDkC--Q-6T-Ml0kkaes8WGUEAhncPZjt59DcpWO7bxiLD1uCht_wJvkNB1hmfC94L-S74WAK182hK8uq8qFNAZAjfuUO1ShK4sq2X2l1crvFvDhrMXRnsNdaOVN3LQ-G4HxMVg1G8ND9ddRrLUdWOs-LK5AERDAV9RbKcdy2cpbEJ5hPdS9riCwf1DAob75E-nqOQeob-fANBH7e6fjgaQ46PDfT_6nspacvDz7-fCs7y8cxZ5TdNj4heXdIOwWj-G6NFdyiL7RYjtgjjJqRF-5HrNooecJ_aF9yBxl0EuUGcRTdoLReelnHonKqA33xpQju2Y8mrVZ0bJJ8R-Sthh6exA9J7U9eOQBYyV_kp738MjmOaT2ttRq0CpKeTNPAMFHreZ29iafz-fKhEy0JjKvKKcNyCezru0HSj7uOPRLSua6_X_Xg_N-Pl7kvpkQX13cXFWsK7EIau7W1SRcLtOGYK6t5Z1uKHR025X-xkxUkp0Fp753AVu3ZPNra0smsTKXHh0qoYnWzU4v94nd_Kt0Y36UxoPZp1bxSvSKR0jLHUJXCE0QTK-DOQUTA_4jWYtoG8s2e3IyY6VlvKE-t92nIhV9n1FrDkOk8k2-JeOIGYJzEdz6C5xO7oP3J-h9hiTsu4nbxwF1BcwZ97npjW1iglNnJbGX5-TwCDVlg5-YowpiuAbL-FUw6hYIwnWOfALEC-CZ7QzkpICkQQF56lCbC38Wy_-8JlcGJFQZHox7QVNrdZTQTS6Pm1MK6i2VQfdivwyL602-vZlZDLRDQ8Nguh6ys8e31zm-sqUEToXU_zjJzxPXkGjbIU0Mo83asTC3QPIz1n7sl3Uq3lDxll_eSqDwREtiKCkqT0y912OnrmxxPAvb9gk_w5enBzt5vSVkHiC64nG3O7GqUqvQYHvBTrOBkGHNVR3-6_o_yfU5iv5DlmPWGKVj0DIF35T_xDkRY0DCis1lpCxdlzk0v_YyJ9w-9Edk6Qkmm2nhaKuK2RExAW-L4pfwKqAws3YLTKp9h9ZCobGhOledUe4gkkWHG1pWDjixQINfuZyYcb3NpIHWRjvHZvb3BafW16R-pKAT_1aRh6FWdEYUjmQHxJiZRLFoOdO40n9f1IKzZINPBGlxxd-aJDPNW4GRzQ=w3714-h2128'

CONFIG = {
    'do V': {
        'iconUrl': ICON_RED,
        'styleId': 'iconRed'
    }, 
    'VI-XIII': {
        'iconUrl': ICON_GREEN,
        'styleId': 'iconGreen'
    },
    'XIV-XVI': {
        'iconUrl': ICON_BLUE,
        'styleId': 'iconBlue'
    }, 
    'XVII-1750': {
        'iconUrl': ICON_YELLOW,
        'styleId': 'iconYellow'
    }, 
    '1750-XIX': {
        'iconUrl': ICON_BROWN,
        'styleId': 'iconBrown'
    },
    'XX': {
        'iconUrl': ICON_GREY,
        'styleId': 'iconGrey'
    }, 
}

# load kml template file
with open('templates/kml-document.xml') as data:
    kml_document = Soup(data, 'lxml-xml')  

# find document
document = kml_document.find('Document')

# load points styles
for k,v in CONFIG.items():
    el = CONFIG.get(k)
    stylesList = getKMLstyleList(el.get('styleId'), el.get('iconUrl'))
    for el in stylesList:
        document.append(Soup(el, 'xml'))


data = pd.read_csv("_source-for-map/znaleziska.csv")

for key,value in CONFIG.items():
    # create google maps <Folder>
    newFolder = Soup('<Folder>', 'xml')
    # append <name> to <Folder>
    newFolder.Folder.append(Soup('<name>%s</name>' % key, 'xml'))

    # filter by period and iterate by period items
    df2 = data[data['Okres']==key]
    for index, row in df2.iterrows():
        config = CONFIG.get(row['Okres'])
        newPlacemark = Soup(createPlacemark(
                row['Numer'], row['Id znaleziska'], 
                row['Znalazca'], row['Okres'], 
                config.get('styleId'), 
                row['GPS E'], 
                row['GPS N']
            ), 'xml')
        newFolder.Folder.append(newPlacemark)
    
    # append <Folder> to <Document>        
    document.append(newFolder)


# convert to xml for google maps
xml = xml.dom.minidom.parseString(str(kml_document).replace("\n", ""))
xml_pretty_str = xml.toprettyxml()

# save kml document to file
dateTime = datetime.now().strftime("%Y_%m_%d-%I_%M_%S")

with open('_generated-maps/%s-map.kml' % dateTime , "w", encoding = 'utf-8') as file:    
    file.write(str(xml_pretty_str))
print('map ready')    