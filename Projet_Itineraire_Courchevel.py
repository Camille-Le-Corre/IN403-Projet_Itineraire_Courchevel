###### 
## PROJET IN403 - Tout schuss a Courch !
## LE CORRE Camille, LEFEVRE Laura 
## LDDBI
######


### Import des librairies

import re
import tkinter as tk
from PIL import ImageTk, Image

### Définition des variables globales

## Définition des dictionnaires


# Dictionnaire associant à chaque numéro de sommet un nom

sommets = {
    1 : "R_signal_",
    2 : "P_rochers-grandes.bosses_1",
    3 : "B_rochers_1",
    4 : "B_rochers_2",
    5 : "TD_chapelets_",
    6 : "TF_ariondaz_",
    7 : "TF_granges_",
    8 : "P_granges-praline_1",
    9 : "P_carabosse-praline_1",
    10 : "P_carabosse-praline_2",
    11 : "TD_granges-stade_",
    12 : "TF_belvedere_",
    13 : "P_belvedere-praline_1",
    14 : "TF_mickey_",
    15 : "V_courchevel-1650_",
    16 : "P_indiens-marquis_1",
    17 : "TF_ste.agathe_",
    18 : "P_indiens-piste.bleue_1",
    19 : "TD_3.vallees_",
    20 : "TF_marquis_",
    21 : "TF_3.vallees_",
    22 : "TF_troika_",
    23 : "R_bosses_",
    24 : "TF_pte.bosse_",
    25 : "B_praline_1",
    26 : "P_grandes.bosses-praline_1",
    27 : "P_grandes.bosses-pyramide_1",
    28 : "P_grandes.bosses-pyramide_2",
    29 : "TF_combe_",
    30 : "P_mont.russes-grandes.bosses_",
    31 : "TF_roc.mugnier_",
    32 : "TD_pyramide_",
    33 : "B_roc.mugnier_1",
    34 : "P_mont.russes-plan.mugnier_1",
    35 : "B_pyramide_1",
    36 : "P_mont.russes-pyramide_1",
    37 : "TD_roc.merlet_",
    38 : "P_mont.russes-pyramide_2",
    39 : "P_mont.russes-plan.mugnier_2",
    40 : "TF_chanrossa-roc.merlet_",
    41 : "P_chanrossa-Jean.Pachod_1",
    42 : "TD_chanrossa-marmottes_",
    43 : "B_roc.mugnier_2",
    44 : "B_roc.mugnier_3",
    45 : "R_prameruel_",
    46 : "P_cave.des.creux-mur-prameruel_1",
    47 : "P_altiport-mur_1",
    48 : "TD_suisses_",
    49 : "TF_gravelles_",
    50 : "P_lac.creux-park.city_1",
    51 : "P_park.city-rama_1",
    52 : "P_lac.creux-rama_1",
    53 : "B_rama_1",
    54 : "P_lac.creux-rama_2",
    55 : "P_lac.creux-park.city-rama_1",
    56 : "TD_creux.noirs_",
    57 : "P_creux-lac.creux_1",
    58 : "P_rama-suisses-turcs_1",
    59 : "TF_aiguille.du.fruit_",
    60 : "P_suisses-turcs_1",
    61 : "R_vizelle_",
    62 : "P_creux-roches.grises_1",
    63 : "B_roches.grises_1",
    64 : "B_roches.grises_2",
    65 : "TF_creux.noirs_",
    66 : "B_rama_2",
    67 : "P_creux-rama_1",
    68 : "TF_saulire_",
    69 : "B_combe.saulire_1",
    70 : "B_combe.saulire_2",
    71 : "P_combe.pylones-combe.saulire_1",
    72 : "P_combe.saulire-m_1",
    73 : "P_combe.pylones-combe.saulire_2",
    74 : "B_combe.saulire_3",
    75 : "P_combe.saulire-grand.couloir_1",
    76 : "B_combe.saulire_4",
    77 : "P_combe.pylones-combe.saulire_3",
    78 : "TF_rocher.de.l.ombre_",
    79 : "P_combe.pylones-combe.saulire_4",
    80 : "TF_sources_",
    81 : "B_verdons_1",
    82 : "TD_saulire_",
    83 : "R_verdons_",
    84 : "B_verdons_2",
    85 : "P_biollay.verdons-m_1",
    86 : "P_biollay.verdons-m_2",
    87 : "B_m_1",
    88 : "TF_biollay-pralong_",
    89 : "P_biollay-biollay.verdons_1",
    90 : "P_biollay-marquetty_1",
    91 : "B_biollay_1",
    92 : "B_pralong_1",
    93 : "P_altiport-pralong_1",
    94 : "B_pralong_2",
    95 : "TF_altiport_",
    96 : "TF_ferme_",
    97 : "TD_altiport-ferme_",
    98 : "TF_cospillot_",
    99 : "R_pralong_",
    100 : "P_biollay-titi_1",
    101 : "P_biollay-titi_2",
    102 : "TF_jardin.alpin_",
    103 : "B_titi_1",
    104 : "TF_bellecote_",
    105 : "B_biollay_2",
    106 : "P_biollay-ryry_1",
    107 : "P_marquetty-ryry_1",
    108 : "P_marquetty-renard_1",
    109 : "P_biollay-renard_1",
    110 : "P_renard-titi_1",
    111 : "TD_cospillot_",
    112 : "T2_jardin.alpin_",
    113 : "B_renard_1",
    114 : "TF_etoiles",
    115 : "T1_jardin.alpin_",
    116 : "TD_etoiles_",
    117 : "TD_bellecote_",
    118 : "TD_jardin.alpin_",
    119 : "R_lac_",
    120 : "P_chenus-verdons_1",
    121 : "TD_rocher.de.l.ombre-sources_",
    122 : "P_renard-stade.descente-verdons_1",
    123 : "P_anemones-chenus-loze.est_1",
    124 : "P_renard-verdons_1",
    125 : "V_courchevel-1850_",
    126 : "TD_loze_",
    127 : "P_loze.est-jantzen_1",
    128 : "P_anemones-jantzen_1",
    129 : "P_anemones-chenus-loze.est_2",
    130 : "P_anemones-lac.bleu-loze.est_1",
    131 : "P_lac.bleu-loze.est_1",
    132 : "B_anemones_1",
    133 : "R_chenus_",
    134 : "TF_cretes_",
    135 : "R_loze_",
    136 : "TF_bouc.blanc_",
    137 : "B_dou.du.midi_1",
    138 : "TF_stade_",
    139 : "P_maumau-petit.dou_1",
    140 : "TD_stade_",
    141 : "TD_jardin.d.enfants_",
    142 : "P_maumau-proveres_1",
    143 : "TF_jardin.d.enfants_",
    144 : "B_proveres_1",
    145 : "B_stade_1",
    146 : "P_proveres-stade_1",
    147 : "TF_roys_",
    148 : "TD_roys_",
    149 : "V_courchevel-1550_",
    150 : "TD_tovets_",
    151 : "P_deviation.1550-dou.du.midi_1",
    152 : "P_brigues-deviation.1550_1",
    153 : "TD_epicea_",
    154 : "TD_plantrey_",
    155 : "P_dou.du.midi-maumau_1",
    156 : "P_dou.du.midi-maumau_2",
    157 : "TF_praz_",
    158 : "P_dou.du.midi-maumau_3",
    159 : "TF_epicea_",
    160 : "B_dou.du.midi_2",
    161 : "P_dou.du.midi-jean.blanc_1",
    162 : "TD_cretes_",
    163 : "P_arolles-bouc.blanc-lanches_1",
    164 : "TF_la.tania_",
    165 : "R_praz.juget_",
    166 : "B_dou.des.lanches_1",
    167 : "P_dou.des.lanches-lanches_1",
    168 : "B_dou.des.lanches_2",
    169 : "P_col.de.la.loze-dou.des.lanches_1",
    170 : "TF_col.de.la.loze-dou.des.lanches_",
    171 : "P_moretta.blanche-plan.fontaine_1",
    172 : "P_jockeys-murettes_1",
    173 : "P_moretta.blanche-murettes_1",
    174 : "TD_bouc.blanc_",
    175 : "TF_gros.murger_",
    176 : "B_folyeres_1",
    177 : "P_moretta.blanche-plan.fontaine_2",
    178 : "TD_gros.murger-la.tania_",
    179 : "V_la-tania-1400_",
    180 : "P_jockeys-murettes_2",
    181 : "V_courchevel-le-praz-1300_",
    182 : "B_brigues_1",
    183 : "B_brigues_2",
    184 : "P_brigues-jean.blanc_1",
    185 : "V_st-bon-1100_",
    186 : "B_jean.blanc_1",
    187 : "TF_stade_",
    188 : "TD_combe_",
    }


# Dictionnaire associant à chaque sommet un tuple de ses successeurs

# on retient qu'il faut proposer les 2 pistes bleues entre 39 et 34 (plan mugnier et mont russes)

successeurs = {
            1 : (2, 5),
            2 : (3, 27, 28),
            3 : (4, 6),
            4 : (5),
            5 : (1, 10),
            6 : (4, 5, 7, 188),
            7 : (8, 21),
            8 : (9, 11),
            9 : (5, 10),
            10 : (11),
            11 : (7, 13, 187),
            12 : (11, 13),
            13 : (15),
            14 : (15),
            15 : (6, 12, 14, 17, 20),
            16 : (15),
            17 : (16),
            18 : (17, 19),
            19 : (15, 21),
            20 : (8, 18),
            21 : (20, 23),
            22 : (179),
            23 : (1, 18, 20, 24),
            24 : (23, 45),
            25 : (23, 24),
            26 : (23, 25),
            27 : (6),
            28 : (27, 29),
            29 : (30, 33),
            30 : (26),
            31 : (28),
            32 : (29, 30, 33, 37),
            33 : (43),
            34 : (32),
            35 : (31, 32),
            36 : (35),
            37 : (36, 38, 40),
            38 : (36, 39),
            39 : (34),           # 2 pistes bleues possibles 
            40 : (37, 41),
            41 : (42),
            42 : (40, 45, 61),
            43 : (44),
            44 : (45),
            45 : (31, 49, 59),
            46 : (45),
            47 : (46, 93),
            48 : (47, 61),
            49 : (46, 48),
            50 : (49),
            51 : (50, 52),
            52 : (50, 53),
            53 : (42),
            54 : (52, 53),
            55 : (51, 54, 56),
            56 : (54, 65),
            57 : (42, 56),
            58 : (55, 59, 60),
            59 : (55, 60),
            60 : (48),
            61 : (58, 69, 70),
            62 : (57),
            63 : (62),
            64 : (63),
            65 : (64),
            66 : (61, 67),
            67 : (62),
            68 : (66, 67, 69, 75),
            69 : (74),
            70 : (69, 71),
            71 : (72, 73),
            72 : (73, 87),
            73 : (74, 77),
            74 : (75),
            75 : (76),
            76 : (77, 78),
            77 : (79),
            78 : (79, 122),
            79 : (80),
            80 : (81),
            81 : (82, 84),
            82 : (68, 83),
            83 : (61, 82, 84, 107, 108),
            84 : (122),
            85 : (83),
            86 : (85, 89),
            87 : (85, 86),
            88 : (48, 89, 92),
            89 : (90),
            90 : (91, 107),
            91 : (101, 106),
            92 : (48, 93),
            93 : (94, 101),
            94 : (95, 97),
            95 : (46),
            96 : (97),
            97 : (95, 96, 98),
            98 : (97, 99),
            99 : (88, 98),
            100 : (99),
            101 : (100, 104),
            102 : (101, 105),
            103 : (100, 118),
            104 : (103, 110),
            105 : (109),
            106 : (102, 105),
            107 : (106, 108),
            108 : (109, 122),
            109 : (110, 119),
            110 : (113),
            111 : (98, 118),
            112 : (102, 114),
            113 : (112, 119),
            114 : (116),
            115 : (112, 116),
            116 : (114, 115, 124),
            117 : (104, 118),
            118 : (111, 117, 115, 125),
            119 : (88, 133),
            120 : (124),
            121 : (78, 80, 120, 123),
            122 : (121),
            123 : (120, 127),
            124 : (125),
            125 : (83, 118, 126, 133, 141, 142),
            126 : (125, 135),
            127 : (126),
            128 : (123, 127),
            129 : (123, 128, 130),
            130 : (131),
            131 : (123),
            132 : (129, 130),
            133 : (129, 132, 134, 167, 170),
            134 : (135),
            135 : (126, 129, 136, 137, 161, 162),
            136 : (163),
            137 : (138, 160),
            138 : (139),
            139 : (140),
            140 : (125, 138, 156),
            141 : (125),
            142 : (144, 155),
            143 : (141),
            144 : (145, 147),
            145 : (146, 147),
            146 : (150),
            147 : (146, 148, 149),
            148 : (147),
            149 : (125),
            150 : (125),
            151 : (150),
            152 : (151, 184),
            153 : (152, 159),
            154 : (135, 153),
            155 : (143, 151, 154),
            156 : (154, 155),
            157 : (156),
            158 : (139, 156),
            159 : (153, 158),
            160 : (158),
            161 : (160, 186),
            162 : (134, 161, 163),
            163 : (164),
            164 : (171, 172, 174, 175),
            165 : (133, 170),
            166 : (165),
            167 : (163, 166),
            168 : (166, 167),
            169 : (133, 168),
            170 : (169),
            171 : (174),
            172 : (173, 180),
            173 : (177, 180),
            174 : (136, 173, 176, 177),
            175 : (174, 176),
            176 : (179),
            177 : (178, 179),
            178 : (164, 175),
            179 : (22, 178),
            180 : (181),
            181 : (157, 162),
            182 : (181, 185),
            183 : (181, 182),
            184 : (183),
            185 : (),           # pas de successeur
            186: (152, 184),
            187 : (11, 16, 18),
            188 : (26, 29),
            }


# Dictionnaire contenant les données du graphe
# Rappel : chaque arc est défini par ses 2 sommets, son type, sa longueur et son nom

graphe = {
        (1, 2, 'b') : [0.2, 'grandes bosses'],
        (1, 2, 'r') : [0.2, 'rochers'],
        (1, 5, 'r') : [2, 'chapelets'],
        (2, 3, 'r') : [1, 'rochers'],
        (2, 27, 'b') : [1, 'ariondaz'],
        (2, 28, 'b') : [0.7, 'grandes bosses'],
        (3, 4, 'r') : [0.2, 'rochers'],
        (3, 6, 'r') : [0.2, 'rochers'],
        (4, 5, 'r') : [1, 'rochers'],
        (5, 1, 'ts') : [2, 'chapelets'],
        (5, 10, 'v') : [1, 'praline'],
        (6, 4, 'r') : [0.2, 'rochers'],
        (6, 5, 'r') : [1, 'bel air'],
        (6, 7, 'b') : [0.5, 'ariondaz'],
        (6, 188, 'v') : [0.3, 'praline'],
        (7, 8, 'b') : [0.2, 'granges'],
        (7, 21, 'b') : [0.2, 'ariondaz'],
        (8, 9, 'v') : [0.2, 'praline'],
        (8, 11, 'b') : [0.6,'granges'],
        (9, 5, 'v') : [0.8, 'praline'],
        (9, 10, 'b') : [0.5, 'carabosse'],
        (10, 11, 'v') : [0.1, 'praline'],
        (11, 7, 'ts') : [1, 'granges'],
        (11, 13, 'v') : [0.5, 'praline'],
        (11, 187, 'tf') : [0.5, 'stade'],
        (12, 11, 'v') : [0.5, 'belvedere'],
        (12, 13, 'v') : [0.3, 'belvedere'],
        (13, 15, 'v') : [1, 'belvedere'],
        (14, 15, 'c') : [0.3, 'zen'],
        (15, 6, 'tc') : [3.5, 'ariondaz'],
        (15, 12, 'rg') : [1.5, 'belvedere'],
        (15, 14, 'rg') : [0.3, 'mickey'],
        (15, 17, 'tf') : [0.7, 'ste agathe'],
        (15, 20, 'tf') : [2, 'marquis'],
        (16, 15, 'b') : [0.4, 'marquis'],
        (17, 16, 'b') : [0.2, 'indiens'],
        (18, 17, 'b') : [0.1, 'indiens'],
        (18, 19, 'b') : [0.8, 'piste bleue'],
        (19, 15, 'v') : [0.2, 'chemin'],
        (19, 21, 'ts') : [2, '3 vallees'],
        (20, 8, 'v') : [0.1, 'praline'],
        (20, 18, 'b') : [1.5, 'piste bleue'],
        (21, 20, 'b') : [0.1, 'piste bleue'],
        (21, 23, 'b') : [0.1, 'ariondaz'],
        (22, 179, 'v') : [0.1, 'plan fontaine'],
        (23, 1, 'ts') : [2.1, 'signal'],
        (23, 18, 'b') : [1, 'indiens'],
        (23, 20, 'v') : [1, 'praline'],
        (23, 24, 'tf') : [0.6, 'pte bosse'],
        (24, 23, 'v') : [0.6, 'praline'],
        (24, 45, 'b') : [0.3, 'gravelles'],
        (25, 23, 'v') : [0.5, 'praline'],
        (25, 24, 'v') : [0.3, 'praline'],
        (26, 23, 'b') : [0.5, 'grandes bosses'],
        (26, 25, 'v') : [0.2, 'praline'],
        (27, 6, 'b') : [0.5, 'pyramide'],
        (28, 27, 'b') : [0.2, 'pyramide'],
        (28, 29, 'b') : [0.1, 'grandes bosses'],
        (29, 30, 'b') : [0.1, 'grandes bosses'],
        (29, 33, 'r') : [0.1, 'roc mugnier'],
        (30, 26, 'b') : [0.7, 'grandes bosses'],
        (31, 28, 'b') : [0.1, 'pyramide'],
        (32, 29, 'b') : [0.1, 'mont russes'],
        (32, 30, 'b') : [0.2, 'mont russes'],
        (32, 33, 'r') : [0.1, 'roc mugnier'],
        (32, 37, 'tf') : [1.5, 'pyramide'],
        (33, 43, 'r') : [0.7, 'roc mugnier'],
        (34, 32, 'b') : [0.1, 'mont russes'],
        (35, 31, 'b') : [0.8, 'pyramide'],
        (35, 32, 'b') : [0.8, 'pyramide'],
        (36, 35, 'b') : [0.4, 'pyramide'],
        (37, 36, 'b') : [0.3, 'pyramide'],
        (37, 38, 'b') : [0.2, 'mont russes'],
        (37, 40, 'ts') : [0.7, 'roc merlet'],
        (38, 36, 'b') : [0.1, 'mont russes'],
        (38, 39, 'b') : [0.4, 'mont russes'],
        (39, 34, 'b') : [0.7, 'plan mugnier'],
        (40, 37, 'r') : [0.7, 'roc merlet'],
        (40, 41, 'r') : [0.3, 'Jean Pachod'],
        (41, 42, 'r') : [1.7, 'Jean Pachod'],
        (41, 42, 'n') : [1.7, 'chanrossa'],
        (42, 40, 'ts') : [2.3, 'chanrossa'],
        (42, 45, 'r') : [1.5, 'creux'],
        (42, 61, 'ts') : [2.2, 'marmottes'],
        (43, 44, 'r') : [0.4, 'roc mugnier'],
        (44, 45, 'r') : [0.7, 'roc mugnier'],
        (45, 31, 'ts') : [2, 'roc mugnier'],
        (45, 49, 'ts') : [1.2, 'gravelles'],
        (45, 59, 'ts') : [2.4, 'aiguille du fruit'],
        (46, 45, 'b') : [0.5, 'prameruel'],
        (47, 46, 'r') : [1.1, 'mur'],
        (47, 93, 'b') : [0.6, 'altiport'],
        (48, 47, 'b') : [0.2, 'altiport'],
        (48, 61, 'ts') : [2.2, 'suisses'],
        (49, 46, 'r') : [1.2, 'cave des creux'],
        (49, 48, 'b') : [0.5, 'altiport'],
        (50, 49, 'r') : [0.4, 'park city'],
        (51, 50, 'r') : [0.5, 'park city'],
        (51, 52, 'r') : [0.2, 'rama'],
        (52, 50, 'r') : [0.5, 'lac creux'],
        (52, 53, 'r') : [0.4, 'rama'],
        (53, 42, 'r') : [0.2, 'rama'],
        (54, 52, 'r') : [0.2, 'lac creux'],
        (54, 53, 'r') : [0.4, 'rama'],
        (55, 51, 'r') : [0.4, 'park city'],
        (55, 54, 'r') : [0.4, 'rama'],
        (55, 56, 'r') : [0.5, 'rama'],
        (56, 54, 'r') : [0.5, 'lac creux'],
        (56, 65, 'ts') : [2, 'creux noirs'],
        (57, 42, 'r') : [1.5, 'creux'],
        (57, 56, 'r') : [0.7, 'lac creux'],
        (58, 55, 'r') : [1, 'rama'],
        (58, 59, 'n') : [0.8, 'turcs'],
        (58, 60, 'n') : [1, 'suisses'],
        (59, 55, 'r') : [0.5, 'park city'],
        (59, 60, 'n') : [0.3, 'turcs'],
        (60, 48, 'n') : [1.7, 'suisses'],
        (61, 58, 'r') : [0.3, 'rama'],
        (61, 69, 'r') : [0.2, 'combe saulire'],
        (61, 70, 'r') : [0.2, 'combe saulire'],
        (62, 57, 'r') : [0.9, 'creux'],
        (63, 62, 'r') : [0.7, 'roches grises'],
        (63, 62, 'n') : [0.5, 'roches grises'],
        (64, 63, 'r') : [0.5, 'roches grises'],
        (65, 64, 'r') : [0.2, 'roches grises'],
        (66, 61, 'r') : [0.2, 'rama'],
        (66, 67, 'r') : [0.2, 'rama'],
        (67, 62, 'r') : [1, 'creux'],
        (68, 66, 'r') : [0.3, 'rama'],
        (68, 67, 'r') : [0.3, 'creux'],
        (68, 69, 'r') : [0.6, 'combe saulire'],
        (68, 75, 'n') : [1.5, 'grand couloir'],
        (69, 74, 'r') : [0.6, 'combe saulire'],
        (70, 69, 'r') : [0.2, 'combe saulire'],
        (70, 71, 'r') : [0.1, 'combe saulire'],
        (71, 72, 'r') : [0.1, 'combe saulire'],
        (71, 73, 'n') : [0.3, 'combe pylones'],
        (72, 73, 'r') : [0.4, 'combe saulire'],
        (72, 87, 'n') : [1.2, 'm'],
        (73, 74, 'r') : [0.2, 'combe saulire'],
        (73, 77, 'n') : [1, 'combe pylones'],
        (74, 75, 'r') : [0.6, 'combe saulire'],
        (75, 76, 'r') : [0.3, 'combe saulire'],
        (76, 77, 'r') : [0.3, 'combe saulire'],
        (76, 78, 'r') : [0.3, 'combe saulire'],
        (77, 79, 'r') : [0.1, 'combe pylones'],
        (78, 79, 'r') : [0.1, 'combe saulire'],
        (78, 122, 'r') : [1.7, 'stade descente'],
        (79, 80, 'r') : [0.4, 'combe saulire'],
        (80, 81, 'v') : [0.1, 'verdons'],
        (81, 82, 'v') : [0.1, 'verdons'],
        (81, 84, 'v') : [0.2, 'verdons'],
        (82, 68, 'tp') : [2, 'saulire'],
        (82, 83, 'v') : [0.1, 'verdons'],
        (83, 61, 'tc') : [1.9, 'vizelle'],
        (83, 82, 'v') : [0.1, 'verdons'],
        (83, 84, 'v') : [0.2, 'verdons'],
        (83, 107, 'b') : [0.4, 'ryry'],
        (83, 108, 'v') : [0.6, 'renard'],
        (84, 122, 'v') : [0.8, 'verdons'],
        (85, 83, 'b') : [0.3, 'biollay verdons'],
        (86, 85, 'b') : [0.1, 'biollay verdons'],
        (86, 89, 'b') : [0.5, 'biollay verdons'],
        (87, 85, 'n') : [0.5, 'm'],
        (87, 86, 'n') : [0.4, 'm'],
        (88, 48, 'b') : [0.8, 'super pralong'],
        (88, 89, 'b') : [0.1, 'biollay'],
        (88, 92, 'b') : [0.3, 'pralong'],
        (89, 90, 'b') : [0.2, 'biollay'],
        (90, 91, 'b') : [0.4, 'biollay'],
        (90, 107, 'r') : [0.6, 'marquetty'],
        (91, 101, 'b') : [0.4, 'biollay'],
        (91, 106, 'b') : [0.4, 'biollay'],
        (92, 48, 'b') : [0.7, 'pralong'],
        (92, 93, 'b') : [0.6, 'pralong'],
        (93, 94, 'b') : [0.1, 'pralong'],
        (93, 101, 'b') : [0.6, 'altiport'],
        (94, 95, 'b') : [0.2, 'prameruel'],
        (94, 97, 'b') : [0.9, 'pralong'],
        (95, 46, 'b') : [1.2, 'prameruel'],
        (96, 97, 'c') : [0.4, 'zen'],
        (97, 95, 'tf') : [0.8, 'altiport'],
        (97, 96, 'tf') : [0.4, 'ferme'],
        (97, 98, 'c') : [0.2, 'chemin de pralong'],
        (98, 97, 'c') : [0.2, 'chemin de pralong'],
        (98, 99, 'c') : [0.1, 'chemin de pralong'],
        (99, 88, 'ts') : [2, 'pralong'],
        (99, 98, 'c') : [0.1, 'chemin de pralong'],
        (100, 99, 'v') : [0.3, "titi"],
        (101, 100, 'b') : [0.3, 'biollay'],
        (101, 104, 'v') : [0.3, 'titi'],
        (102, 101, 'v') : [0.1, 'titi'],
        (102, 105, 'b') : [0.2, 'biollay'],
        (103, 100, 'v') : [0.1, 'titi'],
        (103, 118, 'v') : [2, 'titi'],
        (104, 103, 'v') : [0.1, 'titi'],
        (104, 110, 'v') : [0.2, 'titi'],
        (105, 109, 'b') : [0.2, 'biollay'],
        (106, 102, 'b') : [0.1, 'ryry'],
        (106, 105, 'b') : [0.1, 'biollay'],
        (107, 106, 'b') : [0.7, 'ryry'],
        (107, 108, 'r') : [0.5, 'marquetty'],
        (108, 109, 'v') : [0.3, 'renard'],
        (108, 122, 'v') : [0.4, 'renard'],
        (109, 110, 'v') : [0.1, 'renard'],
        (109, 119, 'b') : [0.6, 'biollay'],
        (110, 113, 'v') : [0.3, 'renard'],
        (111, 98, 'rg') : [1.2, 'cospillot'],
        (111, 118, 'c') : [0.8, 'chemin de plaisouillet'],
        (112, 102, 'tc') : [1, 'jardin alpin'],
        (112, 114, 'v') : [0.1, 'renard'],
        (113, 112, 'v') : [0.1, 'renard'],
        (113, 119, 'v') : [0.3, 'renard'],
        (114, 116, 'v') : [0.3, 'renard'],
        (115, 112, 'tc') : [0.3, 'jardin alpin'],
        (115, 116, 'c') : [0.1, 'chemin du lac'],
        (116, 114, 'rg') : [0.3, 'etoiles'],
        (116, 115, 'c') : [0.1, 'chemin du lac'],
        (116, 124, 'v') : [0.8, 'renard'],
        (117, 104, 'rg') : [1.6, 'bellecote'],
        (117, 118, 'c') : [0.2, 'chemin de la foret'],
        (118, 111, 'c') : [0.8, 'chemin de plaisouillet'],
        (118, 117, 'c') : [0.2, 'chemin de la foret'],
        (118, 115, 'tc') : [0.7, 'jardin alpin'],
        (118, 125, 'c') : [0.1, 'chemin des etables'],
        (119, 88, 'ts') : [2.1, 'biollay'],
        (119, 133, 'ts') : [2, 'coqs'],
        (120, 124, 'v') : [0.5, 'verdons'],
        (121, 78, 'ts') : [1.5, "rocher de l ombre"],
        (121, 80, 'ts') : [1, 'sources'],
        (121, 120, 'v') : [0.1, 'verdons'],
        (121, 123, 'v') : [0.3, 'verdons'],
        (122, 121, 'v') : [0.1, 'verdons'],
        (123, 120, 'r') : [0.3, 'chenus'],
        (123, 127, 'b') : [0.5, 'loze est'],
        (124, 125, 'v') : [0.4, 'verdons'],
        (125, 83, 'tc') : [2, 'verdons'],
        (125, 118, 'c') : [0.1, 'chemin des etables'],
        (125, 126, 'c') : [0.1, 'chemin du stade'],
        (125, 133, 'tc') : [2.2, 'chenus'],
        (125, 141, 'c') : [0.1, 'chemin des jardins'],
        (125, 142, 'b') : [0.1, 'proveres'],
        (126, 125, 'c') : [0.1, 'chemin du stade'],
        (126, 135, 'ts') : [1.6, 'loze'],
        (127, 126, 'b') : [0.2, 'loze est'],
        (128, 123, 'b') : [0.5, 'anemones'],
        (128, 127, 'r') : [0.5, 'jantzen'],
        (129, 123, 'r') : [0.8, 'chenus'],
        (129, 128, 'b') : [0.7, 'anemones'],
        (129, 130, 'v') : [0.3, 'loze est'],
        (130, 131, 'b') : [0.3, 'lac bleu'],
        (130, 131, 'v') : [0.5, 'loze est'],
        (131, 123, 'v') : [0.6, 'loze est'],
        (132, 129, 'b') : [0.2, 'anemones'],
        (132, 130, 'b') : [0.3, 'anemones'],
        (133, 129, 'r') : [0.4, 'chenus'],
        (133, 132, 'b') : [0.3, 'anemones'],
        (133, 134, 'b') : [0.2, 'cretes'],
        (133, 167, 'r') : [1.5, 'lanches'],
        (133, 170, 'ts') : [1.3, 'col de la loze'],
        (134, 135, 'b') : [0.2, 'cretes'],
        (135, 126, 'r') : [1.8, 'loze'],
        (135, 129, 'v') : [0.5, 'loze est'],
        (135, 136, 'r') : [0.1, 'bouc blanc'],
        (135, 137, 'r') : [0.3, 'dou du midi'],
        (135, 161, 'n') : [0.8, 'jean blanc'],
        (135, 162, 'b') : [0.8, 'cretes'],
        (136, 163, 'r') : [0.9, 'bouc blanc'],
        (137, 138, 'r') : [0.3, 'petit dou'],
        (137, 160, 'r') : [0.3, 'dou du midi'],
        (138, 139, 'r') : [0.6, 'petit dou'],
        (139, 140, 'v') : [0.3, 'maumau'],
        (140, 125, 'v') : [0.4, 'maumau'],
        (140, 138, 'ts') : [1, 'stade'],
        (140, 156, 'b') : [0.8, 'maumau'],
        (141, 125, 'c') : [0.1, 'chemin des jardins'],
        (142, 144, 'b') : [0.2, 'proveres'],
        (142, 155, 'v') : [0.8, 'maumau'],
        (143, 141, 'ts') : [0.6, "jardin d enfants"],
        (143, 155, 'c') : [0.4, 'chemin des ours'],
        (144, 145, 'b') : [0.1, 'stade'],
        (144, 147, 'b') : [1, 'proveres'],
        (145, 146, 'b') : [0.6, 'stade'],
        (145, 147, 'b') : [0.5, 'tovets'],
        (146, 150, 'b') : [0.3, 'proveres'],
        (147, 146, 'b') : [0.4, 'proveres'],
        (147, 148, 'v') : [0.4, 'roys'],
        (147, 149, 'b') : [0.4, 'tovets'],
        (148, 147, 'rg') : [0.3, 'roys'],
        (149, 125, 'tc') : [1.2, 'grangettes'],
        (150, 125, 'ts') : [1.1, 'tovets'],
        (151, 150, 'r') : [0.4, 'deviation 1550'],
        (152, 151, 'r') : [0.9, 'deviation 1550'],
        (152, 184, 'r') : [0.6, 'brigues'],
        (153, 152, 'r') : [0.3, 'brigues'],
        (153, 159, 'ts') : [1, 'epicea'],
        (154, 135, 'ts') : [2.4, 'plantrey'],
        (154, 153, 'v') : [0.1, 'maumau'],
        (155, 143, 'c') : [0.4, 'chemin des ours'],
        (155, 151, 'r') : [0.8, 'dou du midi'],
        (155, 154, 'v') : [0.1, 'maumau'],
        (156, 154, 'b') : [0.1, 'maumau'],
        (156, 155, 'r') : [0.1, 'dou du midi'],
        (157, 156, 'b') : [0.4, 'maumau'],
        (158, 139, 'v') : [0.7, 'maumau'],
        (158, 156, 'r') : [0.8, 'dou du midi'],
        (159, 153, 'v') : [1, 'tothor'],
        (159, 158, 'v') : [0.3, 'maumau'],
        (160, 158, 'r') : [0.5, 'dou du midi'],
        (161, 160, 'r') : [0.5, 'dou du midi'],
        (161, 186, 'n') : [1.3, 'jean blanc'],
        (162, 134, 'ts') : [1.1, 'cretes'],
        (162, 161, 'r') : [0.1, 'dou du midi'],
        (162, 163, 'b') : [0.6, 'arolles'],
        (163, 164, 'b') : [0.5, 'arolles'],
        (163, 164, 'r') : [0.5, 'bouc blanc'],
        (164, 171, 'v') : [0.4, 'plan fontaine'],
        (164, 172, 'n') : [0.7, 'jockeys'],
        (164, 174, 'r') : [1, 'bouc blanc'],
        (164, 175, 'b') : [1, 'folyeres'],
        (165, 133, 'tf') : [1.8, 'praz juget'],
        (165, 170, 'ts') : [1.4, 'dou des lanches'],
        (166, 165, 'n') : [0.4, 'dou des lanches'],
        (167, 163, 'r') : [0.4, 'lanches'],
        (167, 166, 'n') : [0.2, 'dou des lanches'],
        (168, 166, 'n') : [0.3, 'dou des lanches'],
        (168, 167, 'n') : [0.2, 'dou des lanches'],
        (169, 133, 'b') : [0.7, 'col de la loze'],
        (169, 168, 'n') : [1, 'dou des lanches'],
        (170, 169, 'b') : [0.6, 'col de la loze'],
        (171, 174, 'r') : [0.7, 'moretta blanche'],
        (172, 173, 'r') : [0.7, 'murettes'],
        (172, 180, 'n') : [1.2, 'jockeys'],
        (173, 177, 'v') : [1.7, 'plan fontaine'],
        (173, 180, 'r') : [1.1, 'murettes'],
        (174, 136, 'tf') : [2, 'bouc blanc'],
        (174, 173, 'v') : [0.4, 'plan fontaine'],
        (174, 176, 'b') : [0.2, 'folyeres'],
        (174, 177, 'r') : [1, 'moretta blanche'],
        (175, 174, 'b') : [0.2, 'folyeres'],
        (175, 176, 'b') : [0.3, 'folyeres'],
        (176, 179, 'b') : [1.8, 'folyeres'],
        (177, 178, 'r') : [0.7, 'moretta blanche'],
        (177, 179, 'v') : [1, 'plan fontaine'],
        (178, 164, 'tc') : [2.5, 'la tania'],
        (178, 175, 'tf') : [1.6, 'gros murger'],
        (179, 22, 'tf') : [0.3, 'troika'],
        (179, 178, 'v') : [0.4, 'plan fontaine'],    #a verifier pour le nom
        (180, 181, 'r') : [0.8, 'murettes'],
        (181, 157, 'tc') : [2.4, 'praz'],
        (181, 162, 'tc') : [2.1, 'foret'],
        (182, 181, 'r') : [0.9, 'brigues'],
        (182, 185, 'r') : [2, 'saint bon'],
        (183, 181, 'r') : [0.8, 'amoureux'],
        (183, 182, 'r') : [0.3, 'brigues'],
        (184, 183, 'r') : [0.4, 'brigues'],
        (186, 152, 'r') : [0.4, 'deviation 1550'],
        (186, 184, 'n') : [0.8, 'jean blanc'],
        (187, 11, 'r') : [0.6, 'stade'],
        (187, 16, 'b') : [1.1, 'marquis'],
        (187, 18, 'b') : [1, 'piste bleue'],
        (188, 26, 'v') : [0.1, 'praline'],
        (188, 29, 'ts') : [0.9, 'combe']
        }


# Dictionnaire des temps de descente des pistes en fonction de leur couleur et du niveau du skieur
# Le 1er élément du tuple correspond au temps pour un skieur de niveau débutant,
# le 2ème élement pour un skieur de niveau intermédiaire et le dernier pour un skieur téméraire 

temps_pistes = {
        'v' : (4.5, 3, 2),      # piste verte
        'b' : (8, 4, 2),        # piste bleue
        'r' : (12.5, 5, 2),     # piste rouge
        'n' : (24.5, 7, 2)      # piste noire
        }


# Dictionnaire des temps des remontées mécaniques

temps_remontees = {
        'temps_moyen_attente' : 5,
        'tp' : 0.5,     # téléphérique
        'tc' : 1,       # télécabine
        'ts' : 1.5,     # télésiège
        'tf' : 2,       # téléski
        'rg' : 2,       # remontée gratuite
        'c' : 3         # à pied
        }


# Dictionnaire des abréviations

abreviations = {
        'v' : 'verte',
        'b' : 'bleue',
        'r' : 'rouge',
        'n' : 'noire',
        'tp' : 'téléphérique',
        'tc' : 'télécabine',
        'ts' : 'télésiège',
        'tf' : 'téléski',
        'rg' : 'remontée gratuite',
        'c' : 'à pied'
        }


## Définition des autres variables


# Liste des coordonées des sommets pour l'interface graphique
# La liste contient 188 tuples de 4 valeurs : un tuple regroupe
# les coordonnées d'un sommet (x1, y1, x2, y2)

CS = [(),
(38, 246, 54, 259),
(56, 255, 62, 261),
(116, 302, 122, 308),
(116, 314, 122, 320),
(82, 383, 92, 393),     #5
(135, 315, 145, 325),
(172, 343, 182, 353),
(177, 366, 183, 372),
(161, 373, 167, 379),
(168, 411, 174, 417),   #10
(179, 412, 189, 422),
(218, 406, 228, 416),
(231, 427, 241, 437),
(272, 463, 278, 469),
(295, 460, 316, 478),   #15
(272, 445, 278, 451),
(265, 431, 271, 437),
(274, 427, 280, 433),
(333, 450, 343, 460),
(190, 359, 196, 365),   #20
(186, 353, 192, 359),
(910, 464, 916, 470),
(199, 352, 209, 362),
(222, 321, 232, 331),
(194, 313, 200, 319),   #25
(180, 313, 186, 319),
(113, 276, 123, 286),
(109, 264, 115, 270),
(118, 265, 124, 271),
(130, 270, 136, 276),   #30
(108, 255, 114, 261),
(121, 255, 127, 261),
(135, 260, 141, 266),
(118, 247, 124, 253),
(76, 214, 82, 220),     #35
(54, 185, 60, 191),
(40, 154, 50, 164),
(58, 171, 64, 177),
(84, 194, 90, 200),
(98, 110, 108, 120),   #40
(131, 119, 137, 125),
(253, 191, 263, 201),
(192, 277, 198, 283),
(210, 285, 216, 291),
(247, 305, 257, 315),   #45
(286, 317, 292, 323),
(347, 257, 353, 263),
(345, 244, 355, 254),
(312, 236, 318, 242),
(301, 223, 307, 229),   #50
(313, 186, 323, 196),
(298, 191, 304, 197),
(268, 195, 274, 201),
(301, 180, 307, 186),
(328, 162, 334, 168),   #55
(300, 146, 310, 156),
(347, 126, 353, 132),
(390, 119, 396, 125),
(359, 156, 369, 166),
(375, 175, 381, 181),   #60
(431, 104, 441, 114),
(403, 103, 409, 109),
(406, 73, 412, 79),
(403, 50, 409, 56),
(398, 33, 408, 43),     #65
(449, 94, 455, 100),
(461, 79, 467, 85),
(482, 85, 492, 95),
(451, 113, 457, 119),
(439, 126, 445, 132),   #70
(435, 133, 441, 139),
(429, 145, 435, 151),
(454, 153, 460, 159),
(475, 151, 481, 157),
(498, 179, 504, 185),   #75
(512, 199, 518, 205),
(490, 207, 496, 213),
(500, 212, 510, 222),
(491, 219, 497, 225),
(497, 246, 507, 256),   #80
(491, 257, 497, 263),
(481, 255, 487, 261),
(469, 256, 479, 266),
(484, 269, 490, 275),
(458, 239, 464, 245),   #85
(449, 235, 455, 241),
(442, 209, 448, 215),
(410, 229, 420, 239),
(411, 241, 417, 247),
(416, 253, 422, 259),   #90
(408, 276, 418, 286),
(400, 253, 406, 259),
(374, 281, 380, 287),
(378, 289, 384, 295),
(368, 295, 374, 301),   #95
(364, 325, 370, 331),
(376, 347, 382, 353),
(386, 351, 392, 357),
(396, 351, 402, 357),
(410, 342, 416, 348),   #100
(414, 312, 420, 318),
(423, 307, 429, 313),
(418, 338, 424, 344),
(428, 327, 438, 337),
(434, 313, 440, 319),   #105
(429, 304, 435, 310),
(448, 281, 454, 287),
(461, 307, 467, 313),
(448, 323, 454, 329),
(450, 332, 456, 338),   #110
(437, 416, 447, 426),
(456, 355, 462, 361),
(458, 345, 464, 351),
(466, 358, 472, 364),
(466, 381, 472, 387),   #115
(458, 379, 464, 385),
(479, 399, 485, 405),
(493, 403, 499, 409),
(475, 349, 485, 359),
(486, 343, 492, 349),   #120
(482, 330, 488, 336),
(481, 321, 487, 327),
(507, 345, 513, 351),
(500, 383, 506, 389),
(502, 407, 512, 417),   #125
(513, 377, 519, 383),
(544, 347, 550, 353),
(570, 299, 576, 305),
(569, 300, 575, 306),
(544, 287, 550, 293),   #130
(518, 297, 524, 303),
(569, 279, 575, 285),
(597, 270, 607, 280),
(608, 287, 614, 293),
(608, 303, 618, 313),   #135
(628, 307, 638, 317),
(615, 328, 621, 334),
(594, 355, 600, 361),
(554, 391, 560, 397),
(533, 401, 539, 407),   #140
(515, 413, 521, 419),
(508, 419, 514, 425),
(538, 439, 544, 445),
(499, 436, 505, 442),
(500, 447, 506, 453),   #145
(498, 493, 504, 499),
(476, 474, 482, 480),
(485, 494, 495, 504),
(458, 489, 468, 499),
(516, 494, 526, 504),   #150
(535, 489, 541, 495),
(598, 457, 604, 463),
(581, 440, 587, 446),
(570, 439, 576, 445),
(562, 437, 568, 443),   #155
(567, 433, 573, 439),
(558, 412, 564, 418),
(596, 389, 602, 395),
(618, 378, 628, 388),
(612, 360, 618, 366),   #160
(644, 351, 650, 357),
(652, 344, 662, 354),
(686, 351, 692, 357),
(711, 365, 717, 371),
(712, 350, 722, 360),   #165
(692, 332, 698, 338),
(676, 330, 682, 336),
(673, 315, 679, 321),
(650, 261, 656, 267),
(695, 249, 705, 259),   #170
(728, 378, 738, 388),
(734, 409, 740, 415),
(774, 435, 780, 441),
(781, 406, 791, 416),
(777, 394, 787, 404),   #175
(804, 401, 810, 407),
(835, 459, 841, 465),
(888, 479, 898, 489),
(911, 475, 917, 481),
(759, 481, 769, 491),   #180
(726, 517, 736, 527),
(668, 521, 674, 527),
(651, 502, 657, 508),
(625, 493, 631, 499),
(576, 572, 586, 582),   #185
(618, 438, 624, 444),
(211, 377, 221, 387),
(166, 309, 176, 319),]


niveau_skieur = -1   # cette variable est initialisé à -1 et pourra prendre 3 valeurs :
                    # 0 (débutant), 1 (intermédiaire), 2 (téméraire)

sommets_selec = [0,0]   # liste de 2 éléments initialisés à 0, elle contiendra par la suite les
                        # numéros du sommet de départ et d'arrivée

premier_acces = 1   # variable initalisée à 1 signifiant que l'application n'a pour le moment
                    # pas été lancée, elle prendra ensuite la valeur 0 jusqu'à la fermeture de
                    # la fenêtre par l'utilisateur. Elle est utilisée pour savoir s'il faut
                    # afficher ou non l'image d'accueil

infini = 2**30

### Fonctions pour trouver le plus court chemin (algorithme de Dijkstra)


def calculTemps(sA, sB):
    ''' Calcule le temps nécessaire au skieur pour aller de sA à sB'''

    global graphe, niveau_skieur, temps_pistes, temps_remontees

    temps = infini
    # Recherche dans le dictionnaire les informations concernant l'arc (sA, sB)

    li_keys = [keys for keys in graphe.keys() if keys[0] == sA and keys[1] == sB]

    for key in li_keys:
        arc = (key, graphe[key])
        type_arc = arc[0][2]        # le type d'un arc est la couleur de la piste ou le type de remontée mécanique
        longueur_arc = arc[1][0]

        if type_arc in temps_pistes:
            # S'il s'agit d'une piste, le temps est calculé en fonction de
            # sa couleur, de sa longueur et du niveau du skieur
            nouveau_temps = longueur_arc * temps_pistes[type_arc][niveau_skieur]

        else:
            if type_arc == 'c':
                # S'il s'agit d'un arc de type chemin (à pied), il n'y a pas de temps d'attente
                nouveau_temps = longueur_arc * temps_remontees['c']
            else:
                # S'il s'agit d'une remontée mécanique, le temps est calculé en fonction du
                # temps moyen d'attente, du type de remontée et de sa longueur
                nouveau_temps = temps_remontees['temps_moyen_attente'] + (longueur_arc * temps_remontees[type_arc])

        if nouveau_temps < temps:
            temps = nouveau_temps

    return temps, type_arc 


def algoDijkstra(s_depart, s_arrivee):
    ''' Fonction realisant l'algorithme de Dijkstra afin de trouver le plus court
        chemin entre les sommets s_depart et s_arrivee dans le graphe represente
        dans un dictionnaire'''

    global successeurs

    nb_sommets = len(successeurs)

    # Création d'un dictionnaire pour stocker pour chaque sommet un tuple
    # contenant le sommet père et la distance jusqu'au sommet depuis le sommet de départ
    distances = {sommet: (None, infini) for sommet in range(1, nb_sommets+1)}
    distances[s_depart] = 0

    sommets_marques = [0]

    s_traitement = s_depart
    somme = 0

    while len(sommets_marques) < nb_sommets :   # Tant qu'on n'a pas marqué tous les sommets
        sommets_marques.append(s_traitement)    # Ajout du sommet en cours de traitement aux sommets marqués

        if type(successeurs[s_traitement]) == int :     # Regarde si le type est un int pour le cas où il n'y a qu'un successeur
            suc = [successeurs[s_traitement]]
        else:                                               # Sinon on recupère le tuple des successeurs
            suc = successeurs[s_traitement]

        for sommet in suc :                                 # Parcourt les successeurs pour calculer le nouveau temps
            temps, type_arc = calculTemps(s_traitement, sommet)
            if sommet not in sommets_marques :
                d = distances[sommet][1]                    # Recupère la distance jusqu'au sommet
                if somme + temps < d :                       # pour la comparer au nouveau temps calculé
                    distances[sommet] = ((s_traitement, type_arc), somme + temps)   #On stocke le sommet parent et le nouveau temps calculé

        # Recherche du prochain sommet à traiter parmi les sommets non marqués
        minimum = (None, infini)
        for sommet in range(1, nb_sommets+1):
            # Recherche du minimum pour trouver le prochain sommet à traiter
            if sommet not in sommets_marques and distances[sommet][1] <= minimum[1] :
                minimum = (sommet, distances[sommet][1])

        s_traitement, somme = minimum

    # Reconstruction du chemin de s_depart jusqu'à s_arrivee
    sommet = s_arrivee
    parcours = [s_arrivee]
    longueur = distances[s_arrivee][1]

    while sommet != s_depart:           # Remonte le graphe depuis le dernier sommet pour obtenir le plus court chemin
        parcours.append(distances[sommet][0][1])
        sommet = distances[sommet][0][0]
        parcours.append(sommet)

    parcours.reverse()      # Inverse l'ordre pour avoir le chemin dans le bon sens

    return parcours, longueur


### Fonctions pour donner l'itinéraire au skieur


def recupNomsFromSommet(nom_s):
    ''' Récupère le nom de la ou des listes ou remontées mécaniques
        à partir du nom du sommet'''
   
    while nom_s[0] != '_':     # suppression de la ou des lettres majuscules indiquant le type du sommet:
        nom_s = nom_s[1:]
    nom_s = nom_s[1:]

    # Création d'une regex récupérant les noms des pistes ou des remontées :
    # on veut récupérer ce qui est entouré des caractères '-' et/ou de '_'
    regex = re.compile("[-_]?([A-Za-z0-9\.]+)[-_]")
    # Séparation des pistes/remontées dans une liste
    liste_sans_espace = regex.findall(nom_s)

    # Les noms des pistes en plusieurs mots sont séparés par des points (exemple : dou.du.midi)
    # Il faut donc remplacer ces points par des espaces
    liste_avec_espace = []
    for n in liste_sans_espace:
        piste = ''
        for l in n:
            if l == '.':
                piste += ' '
            else:
                piste += l
        liste_avec_espace.append(piste)

    return liste_avec_espace


def recupTypeFromNom(nom_piste_ou_remontee, p_r):
    ''' Récupère le type d'une piste ou d'une remontée
        Exemple : verte, rouge, télécabine, téléski, ...
        Attention, un même nom peut être porté à la fois par un télésiège, une piste
        verte et une bleue par exemple.
        L'argument p_r précise si l'on cherche le nom d'une piste ou d'une remontée ('p' ou 'r')'''
    
    global graphe, abreviations, temps_pistes, temps_remontees
    
    arcs = graphe.items()
    t = []
    for a in arcs:        # on parcourt chaque arc du graphe
        if a[1][1] == nom_piste_ou_remontee:        # si le nom de l'arc est celui que l'on cherche
            type_a = a[0][2]
            if type_a not in t:                     # et qu'on ne l'a pas encore ajouté à la liste t,
                t.append(type_a)                    # on l'ajoute

    # Suppression des pistes si on cherche un type de remontée mécanique
    if p_r == 'r':
        for k in t:
            if k not in temps_remontees:
                t.remove(k)
    # Suppression des remontées si on cherche une couleur de piste
    else:
        for k in t:
            if k not in temps_pistes:
                t.remove(k)

    # Remplacement des abréviations            
    for k in range(len(t)):
        t[k] = abreviations[t[k]]

    return t


def recupNomFromArc(sA, sB, type_arc):
    ''' Récupère le nom d'un arc à partir des numéros
        des sommets de l'arc en question (et son type)'''
    # Cette fonction est utilisée dans la fonction itineraire
    
    global graphe

    arcs = graphe.items()
    for a in arcs:      # Parcourt de chaque arc du graphe
        if (a[0][0] == sA) and (a[0][1] == sB) and (a[0][2] == type_arc):         # s'il s'agit d'un arc (sA, sB)
            return a[1][1]                   # on renvoie son nom


def descriptionT(nom_s):
    ''' Décrit les sommets en lien avec une remontée mécanique.
        Cette fonction traite un des types de sommets possibles dans la fonction descriptionSommet'''

    description_s = ''
    noms = recupNomsFromSommet(nom_s)       # on récupère une liste des noms des remontées
    types_remontees = []

    for n in range(len(noms)):
        types_remontees.append(recupTypeFromNom(noms[n], 'r')[0])
    debut_fin = nom_s[1]

    if debut_fin == 'D':      # si le sommet est le début d'une remontée mécanique
        description_s += 'au début du '
        for k in range(len(noms)):
            if (k == (len(noms)-1)) and (k != 0):
                description_s += ' et du '
            elif k != 0:
                description_s += ', '
            description_s += str(types_remontees[k]) + ' ' + str(noms[k])

    elif debut_fin == 'F':     # si le sommet est la fin d'une remontée
        description_s += 'à la fin du '
        for k in range(len(noms)):
            if (k == (len(noms)-1)) and (k != 0):
                description_s += ' et du '
            elif k != 0:
                description_s += ', '
            description_s += str(types_remontees[k]) + ' ' + str(noms[k])
            
    else:                    # s'il s'agit d'un arrêt du télécabine jardin alpin
                                    # (c'est le seul à avoir plusieurs arrêts)            
        description_s += "à l'arrêt " + debut_fin + " du télécabine jardin alpin"

    return description_s


def descriptionP(nom_s):
    ''' Décrit les sommets des intersections entre plusieurs pistes.
        Cette fonction traite un des types de sommets possibles dans la fonction descriptionSommet'''

    description_s = ''
    description_s += "à l'intersection entre la piste "
    pistes = recupNomsFromSommet(nom_s)
    types_pistes = []
    for n in range(len(pistes)):
        types_pistes.append(recupTypeFromNom(pistes[n], 'p')[0])
    for k in range(len(pistes)):
        if (k == (len(pistes)-1)) and (k != 0):
            description_s += ' et la piste '
        elif k != 0:
            description_s += ', la piste '
        description_s += str(types_pistes[k]) + ' ' + str(pistes[k])

    return description_s


def descriptionSommet(s):
    ''' Retourne une description du sommet s pour que le skieur comprenne où il doit aller.
        Par exemple, le sommet 5 (TD_chapelets) sera décrit comme "le début du télésiege chapelets" '''
    
    global sommets
    
    nom_s = sommets[s]          # on récupère le nom du sommet
    type_s = nom_s[0]           # le type du sommet est sa lettre majuscule (1er caractère)
    description_s = ''
    nb = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    # Remontée mécanique
    if type_s == 'T':
        description_s = descriptionT(nom_s)

    # Intersection entre plusieurs pistes
    elif type_s == 'P':       
        description_s = descriptionP(nom_s)

    # Bifurcation d'une piste    
    elif type_s == 'B':       
        description_s += 'à la bifurcation de la piste ' + recupNomsFromSommet(nom_s)[0]

    # Point de rencontre
    elif type_s == 'R':       
        description_s += 'au point de rencontre '
        pt = recupNomsFromSommet(nom_s)[0]
        description_s += pt[0].upper() + pt[1:]

    # Village
    elif type_s == 'V':
        description_s += 'au village de '
        village = recupNomsFromSommet(nom_s)
        for v in village:
            if v[0] not in nb:
                description_s += v[0].upper() + v[1:]
                description_s += " "
            else :
                description_s += v


    return description_s


def affichageTempsIti(tps_en_minutes):
    ''' Retourne la phrase décrviant le temps nécessaire pour suivre l'itinéraire'''

    tps_en_minutes = int(tps_en_minutes) + 1    # arrondi supérieur du nombre de minutes
    nb_heures = tps_en_minutes // 60
    nb_minutes = tps_en_minutes % 60
    res = "Pour cet itinéraire, il vous faudra "

    # Affichage du nombre d'heures
    if nb_heures != 0:
        if nb_heures == 1:
            res += "1 heure"                    # s'il y a une heure
        else:
            res += str(nb_heures) + " heures"   # s'il y a plusieurs heures
        if nb_minutes != 0:
            res += " et "
    
    # Affichage du nombre de minutes
    if nb_minutes != 0:
        if nb_minutes == 1:                         # s'il y a une minute
            res += "1 minute"
        else:
            res += str(nb_minutes) + " minutes"     # s'il y a plusieurs minutes
    
    return res

def etape_iti(historique, depart, fin):
    '''Fonction permettant de décrire une étape de l'itinéraire lorsqu'il y a eu un changement dans 
    l'itinéraire (par exemple un changement de piste)'''

    type_arc = historique[depart][0]   #Recupère le type de l'arc

    if type_arc in temps_pistes:    #Si c'est une piste
        etape = 'Descendez la piste ' + str(abreviations[type_arc]) + ' ' + historique[depart][1]
        etape += " jusqu'" + descriptionSommet(historique[fin][2]) + '\n'
    elif type_arc == 'c':           #Si c'est un chemin
        etape = 'Prenez le ' + historique[fin][1] + '\n'
    elif type_arc == 'rg':          #Si c'est une remontée gratuite
        etape = 'Prenez la remontée gratuite ' + historique[fin][1] + '\n'
    else:                           #Si c'est une remontée
        etape = 'Prenez le ' + str(abreviations[type_arc]) + ' ' + historique[fin][1] + '\n'

    return etape

def itineraire(l_sommets):
    ''' Cette fonction prend en argument la liste des sommets correspondant
    au plus court chemin trouvé par l'algorithme de Dijkstra,
    puis elle retourne les indications sur l'itinéraire à suivre '''

    global temps_pistes, abreviations

    temps = l_sommets[1]        #On récupère le temps total du PCC
    l_sommets = l_sommets[0]    #On récupère le PCC
    historique = []

    iti = affichageTempsIti(temps) + '\n'   #Affichage du temps total estimé
    iti += 'Vous vous trouvez actuellement ' + descriptionSommet(l_sommets[0]) + '\n'

    #Constition de l'historique du PCC en ajoutant pour chaque arc : le type de l'arc, le nom de l'arc et le sommet d'arrivée de l'arc
    for s in range(0, len(l_sommets)-1, 2):
        sA = l_sommets[s]
        sB = l_sommets[s+2]
        type_a = l_sommets[s+1]
        historique.append((type_a, recupNomFromArc(sA, sB, type_a), sB))

    depart = 0      #Initialisation d'un point de départ

    for a in range(1, len(historique)):     
        #Si la condition suivante n'est pas remplie, alors cela signifie que l'arc 'a' de l'historique correspond à la suite
        #de l'arc stocké dans la variable départ (c'est la même piste), donc on parcourt les arcs de l'historique jusqu'à trouver 
        #un arc différent de l'arc départ (une intersection de piste)
        if (historique[a][0] != historique[depart][0]) or (historique[a][1] != historique[depart][1]):
            #On récupère l'étape de l'itinéraire correspondant à un changement de piste
            iti += etape_iti(historique, depart, a-1)
            depart = a      #On stocke le nouveau depart

    #On rappelle etape_iti pour obtenir la dernière étape de l'itinéraire
    #Cette instruction permet aussi de traiter le où l'itinéraire ne change jamais de piste du sommet de départ jusqu'au sommet d'arrivée
    iti += etape_iti(historique, depart, len(historique)-1)

    iti += 'Vous êtes arrivés ' + descriptionSommet(l_sommets[len(l_sommets)-1])

    return iti

### Interface graphique

## Définition des fonctions utilisées pour l'interface graphique


def recupNumSommetClique(event):
    ''' Cette fonction récupère les coordonnées de l'endroit où l'utilisateur a cliqué
        (clic gauche) puis elle compare ces coordonnées à celles des différents sommets.
        Elle renvoie le numéro du sommet correspondant, ou rien si aucun sommet n'a été cliqué
        Elle permet aussi de changer la couleur des sommets sélectionnés '''
    
    global CS, sommets_selec, canvas

    # Si les 2 sommets n'ont pas encore été sélectionnés
    if (sommets_selec[0] == 0) or (sommets_selec[1] == 0):
        # On récupère les coorodnnées du point cliqué
        x = event.x
        y = event.y
        # On parcourt les coordonnées de chaque sommet
        for s in range(1, 189):     
            x1 = CS[s][0]
            y1 = CS[s][1]
            x2 = CS[s][2]
            y2 = CS[s][3]
            # On regarde si les coordonnées du point cliqué se trouvent entre les
            # coordonnées du sommet, c'est-à-dire si l'utilisateur a cliqué sur ce sommet
            if (x1<=x) and (x<=x2) and (y1<=y) and (y<=y2):
                # Ce sommet devient rouge
                canvas.create_oval(x1, y1, x2, y2, fill='red')
                # Le numéro du sommet est ajouté à la liste sommets_selec
                if sommets_selec[0] != 0:
                    sommets_selec[1] = s
                else:
                    sommets_selec[0] = s
    return sommets_selec


def annulerSommetSelec(event):
    ''' Annule la sélection d'un sommet, fonction appelée
        suite à un clic droit sur un sommet '''

    global CS, sommets_selec

    # Si au moins un sommet a été sélectionné pour le moment
    if sommets_selec != [0,0]:
        # On récupère les coordonnées de l'endroit où l'utilisateur a cliqué
        x = event.x
        y = event.y
        # On parcourt les coordonnées de chaque sommet
        for s in range(1, 189):
            x1 = CS[s][0]
            y1 = CS[s][1]
            x2 = CS[s][2]
            y2 = CS[s][3]
            # On regarde si les coordonnées du point cliqué se trouvent entre les coordonnées du sommet,
            # c'est-à-dire si l'utilisateur a cliqué sur ce sommet, et que ce sommet était déjà sélectionné
            if (x1<=x) and (x<=x2) and (y1<=y) and (y<=y2) and s in sommets_selec:
                # Si c'est le cas, ce sommet redevient noir et la liste sommets_selec est modifiée
                canvas.create_oval(x1, y1, x2, y2, fill='black')
                sommets_selec.remove(s)
                sommets_selec.append(0)
    return sommets_selec


def nivDeb():
    ''' Met à jour la variable globale niveau_skieur en fonction du bouton cliqué.
        Ici elle prend la valeur 0 (niveau débutant) '''
    
    global niveau_skieur
    niveau_skieur = 0
    w_niveaux.destroy()


def nivInt():
    ''' Met à jour la variable globale niveau_skieur en fonction du bouton cliqué.
        Ici elle prend la valeur 1 (niveau intermédiaire) '''
    
    global niveau_skieur
    niveau_skieur = 1
    w_niveaux.destroy()


def nivTem():
    ''' Met à jour la variable globale niveau_skieur en fonction du bouton cliqué.
        Ici elle prend la valeur 2 (niveau téméraire) '''
    
    global niveau_skieur
    niveau_skieur = 2
    w_niveaux.destroy()


def affichageChoixNiveau():
    ''' Affiche la fenêtre permettant le choix du niveau'''
    global w_accueil, can, canvas, w_niveaux

    # Fermeture de la fenêtre affichant l'image d'accueil
    w_accueil.destroy()

    # Création de la fenêtre pour le choix du niveau
    w_niveaux = tk.Tk()
    w_niveaux.title("Tout schuss à Courch !")

    # Création des widgets
    demande_niveau = tk.Label(w_niveaux, text="Quel-est votre niveau ?", font=("helvetica", "30"))
    debutant = tk.Button(w_niveaux, text="Débutant", font=("helvetica", "25"), command=nivDeb)
    intermediaire = tk.Button(w_niveaux, text="Intermédiaire", font=("helvetica", "25"), command=nivInt)
    temeraire = tk.Button(w_niveaux, text="Téméraire", font=("helvetica", "25"), command=nivTem)

    # Placement des widgets
    demande_niveau.grid(row=0, column=0, columnspan=4)
    debutant.grid(row=1, column=0)
    intermediaire.grid(row=1, column=1)
    temeraire.grid(row=1, column=2)

    w_niveaux.mainloop()


def numeroteSommets(iti):
    ''' Affiche l'ordre des sommets à emprunter pour suivre l'itinéraire.
        Les sommets à suivre deviennent rouge et sont numérotés'''

    global CS, canvas

    num = 1
    for k in range(0, len(iti), 2):
        # Création d'un rond rouge au niveau du sommet pour le faire changer de couleur
        coord = CS[iti[k]]
        x1 = coord[0]
        y1 = coord[1]
        x2 = coord[2]
        y2 = coord[3]
        canvas.create_oval(x1, y1, x2, y2, fill='red', outline='red')
        # Création du texte pour numéroté le sommet en question
        x_num = (x1+x2)/2
        y_num = (y1+y2)/2
        canvas.create_text(x_num, y_num, text=str(num), font=("helvetica", "10"))
        num += 1


def retourNiveaux():
    ''' Permet de revenir au choix du niveau '''
    
    global w_plan_station

    w_plan_station.destroy()    # fermeture de la fenêtre actuelle
    application()               # la fonction principale est rappelée


def validerSommets():
    ''' Cette fonction vérifie que l'utilisateur a bien sélectionné 2 sommets.
        Si ce n'est pas le cas, elle affiche un message d'erreur.
        Si c'est le cas, elle utilise la fonction algoDijkstra et itineraire afin
        de trouver le plus court chemin et de l'afficher sous forme d'instructions
        claires pour le skieur'''

    sA = sommets_selec[0]
    sB = sommets_selec[1]

    if sA == 185:
        label_iti['text'] = "Aucun itinéraire n'est trouvé au départ de St Bon,\nveuillez vous renseigner au près des navettes à disposition"
        return

    if (sA != 0) and (sB != 0):     # si 2 sommets ont bien été sélectionnés
        label_iti['text'] = ""
        # Recherche du plus court chemin par l'algorithme de Dijkstra
        iti = algoDijkstra(sA, sB)
        # Affichage des sommets à suivre (ils deviennent rouges et sont numérotés)
        numeroteSommets(iti[0])
        # Affichage des instructions pour suivre l'itinéraire
        label_iti['text'] = itineraire(iti)
    else:
        # Affichage du message d'erreur
        label_iti['text'] = "Veuillez sélectionner 2 sommets"
    # Enlever la possibilité de déselectionner un sommet une fois qu'un itinéraire a été affiché
    canvas.unbind("<Button-3>")
    # Laisser la possibilité de masquer l'itinéraire pour mieux voir le plan de la station
    valider.grid_remove()
    masquer.grid(column=10, row=10)


def masquerIti():
    ''' Permet de masquer les instructions de l'itinéraire '''

    label_iti["text"] = ''
    # Ré-affichage du bouton pour valider les sommets et afficher l'itinéraire
    masquer.grid_remove()
    valider.grid(column=10, row=10)


def application():
    ''' Fonction principale du programme, permettant de lancer l'application.
        Elle gère l'ouverture et la fermeture des 3 fenêtres, ainsi que l'affichage
        et l'utilisation de tous les widgets, à l'aide des fonctions définies précedemment'''

    global niveau_skieur, sommets_selec, CS, premier_acces, can, w_accueil, w_plan_station, canvas, label_iti, valider, masquer
    
    # Initialistaion des variables globales (ou ré-initialisation si l'utilisateur revient
    # sur une fenêtre où il est déjà allé grâce au bouton 'Retour')
    niveau_skieur = 0
    sommets_selec = [0,0]

    # Création de la fenêtre d'accueil
    w_accueil = tk.Tk()
    w_accueil.title("Tout schuss à Courch !")

    # Si l'utilisateur vient de lancer l'application, il visionnera l'image d'accueil
    if premier_acces == 1:
        accueil_courch = Image.open("bienvenue_courchevel.png")
        #accueil_courch = Image.open("ProjetIN403-Courchevel/bienvenue_courchevel.png")
        img = ImageTk.PhotoImage(accueil_courch)
        can = tk.Canvas(w_accueil, width=img.width(), height=img.height())
        image_id = can.create_image(0, 0, anchor='nw', image=img)
        can.grid(row=0, column=0, rowspan=8, columnspan=8)

        # Après 2 secondes d'affichage, l'image disparait et la fenêtre pour choisir le niveau s'ouvre
        w_accueil.after(2000, affichageChoixNiveau)

        # La variable globale premier_acces est maintenant définie à 0 et le restera jusqu'à la
        # fermeture du programme. L'image d'accueil ne sera donc plus affichée
        premier_acces = 0

    # Sinon, il a cliqué sur le bouton 'Retour' et il revient directement au choix du niveau
    else:
        affichageChoixNiveau()

    w_accueil.mainloop()

    # Si un niveau a bien été sélectionné, il faut afficher le plan de la station
    if niveau_skieur != -1:

        # Création de la fenêtre du plan de la station
        w_plan_station = tk.Tk()
        w_plan_station.title("Tout schuss à Courch !")

        # Affichage du plan
        plan_station = Image.open("plan_station2.png")
        #plan_station = Image.open("ProjetIN403-Courchevel/plan_station2.png")
        img = ImageTk.PhotoImage(plan_station)
        canvas = tk.Canvas(w_plan_station, width=img.width(), height=img.height())
        canvas.create_image(0, 0, anchor='nw', image=img)
        canvas.grid(column=0, row=0, columnspan=12, rowspan=12)

        # Création des widgets correspondant aux sommets
        for s in range(1, 189):
            canvas.create_oval(CS[s][0], CS[s][1], CS[s][2], CS[s][3], fill='black')

        # Liaison des actions de l'utilisateur avec des commandes
        # Un clic gauche permet de sélectionner un sommet
        canvas.bind("<Button-1>", recupNumSommetClique)
        # Un clic droit permet d'annuler la sélection d'un sommet
        canvas.bind("<Button-3>", annulerSommetSelec)

        # Création des widgets
        retour = tk.Button(w_plan_station, text="Retour", font=("helvetica", "15"), command=retourNiveaux)
        valider = tk.Button(w_plan_station, text="Obtenir l'itinéraire", font=("helvetica", "15"), command=validerSommets)
        label_iti = tk.Label(w_plan_station, text="", font=("helvetica", "10"))
        masquer = tk.Button(w_plan_station, text="Masquer", font=("helvetica", "15"), command=masquerIti)

        # Placement des widgets
        retour.grid(column=11, row=10)
        valider.grid(column=10, row=10)
        label_iti.grid(column=9, columnspan=3, row=0, rowspan=2)

        w_plan_station.mainloop()


# Appel de la fonction principale, lancement de l'application
application()
