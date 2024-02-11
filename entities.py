import obj_class
import constants as cnst

# Maybe it would be better to convert this module to dictionary as in gamebook.py?
# Only problem is tha this operation requires a lot of time.

# /// declare entities
# self, name, entity_z_init, entity_z_count, entity_w_init, entity_w_count, state, esc_possible
# - - - - - - - - -
# - - - - - - - - -
# /// 002:
# /// GARAZAN
entity_002 = obj_class.Entity(f'{cnst.ENTITY_COLOR}GARAZAN{cnst.DEFAULT_COLOR}', 10, 10, True, True)
entity_002_z_init = entity_002_z_count = entity_002.entity_z_count
entity_002_w_init = entity_002_w_count = entity_002.entity_w_count
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# /// 032:
# /// WILKOLUDY
entity_032 = obj_class.Entity(f'{cnst.ENTITY_COLOR}WILKOLUDY{cnst.DEFAULT_COLOR}', 8, 7, True, False)
entity_032_z_init = entity_032_z_count = entity_032.entity_z_count
entity_032_w_init = entity_032_w_count = entity_032.entity_w_count
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# /// 069:
# /// UPIÓR(1)
entity_069_1 = obj_class.Entity(f'{cnst.ENTITY_COLOR}UPIÓR{cnst.DEFAULT_COLOR}', 5, 3, True, False)
entity_069_1_z_init = entity_069_1_z_count = entity_069_1.entity_z_count
entity_069_1_w_init = entity_069_1_w_count = entity_069_1.entity_w_count
# - - - - - - - - -
# /// UPIÓR(2)
entity_069_2 = obj_class.Entity(f'{cnst.ENTITY_COLOR}UPIÓR{cnst.DEFAULT_COLOR}', 5, 4, True, False)
entity_069_2_z_init = entity_069_2_z_count = entity_069_2.entity_z_count
entity_069_2_w_init = entity_069_2_w_count = entity_069_2.entity_w_count
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# /// 092:
# /// MINOTAUR
entity_092 = obj_class.Entity(f'{cnst.ENTITY_COLOR}MINOTAUR{cnst.DEFAULT_COLOR}', 10, 10, True, False)
entity_092_z_init = entity_092_z_count = entity_092.entity_z_count
entity_092_w_init = entity_092_w_count = entity_092.entity_w_count
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# /// 098:
# /// HERSZT GOBLINÓW
entity_098 = obj_class.Entity(f'{cnst.ENTITY_COLOR}HERSZT GOBLINÓW{cnst.DEFAULT_COLOR}', 9, 8, True,
                              False)
entity_098_z_init = entity_098_z_count = entity_098.entity_z_count
entity_098_w_init = entity_098_w_count = entity_098.entity_w_count
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# /// 107:
# /// STRAŻNIK TAJEMNICY
entity_107 = obj_class.Entity(f'{cnst.ENTITY_COLOR}STRAŻNIK TAJEMNICY{cnst.DEFAULT_COLOR}', 10, 14,
                              True, False)
entity_107_z_init = entity_107_z_count = entity_107.entity_z_count
entity_107_w_init = entity_107_w_count = entity_107.entity_w_count
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# /// 109:
# /// KARMAA
entity_109 = obj_class.Entity(f'{cnst.ENTITY_COLOR}KARMAA{cnst.DEFAULT_COLOR}', 7, 8, True, False)
entity_109_z_init = entity_109_z_count = entity_109.entity_z_count
entity_109_w_init = entity_109_w_count = entity_109.entity_w_count
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# /// 116:
# /// ORK
entity_116 = obj_class.Entity(f'{cnst.ENTITY_COLOR}ORK{cnst.DEFAULT_COLOR}', 6, 4, True, False)
entity_116_z_init = entity_116_z_count = entity_116.entity_z_count
entity_116_w_init = entity_116_w_count = entity_116.entity_w_count
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# /// 184:
# /// DEMON
entity_184 = obj_class.Entity(f'{cnst.ENTITY_COLOR}DEMON{cnst.DEFAULT_COLOR}', 7, 6, True, True)
entity_184_z_init = entity_184_z_count = entity_184.entity_z_count
entity_184_w_init = entity_184_w_count = entity_184.entity_w_count
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# /// 238:
# /// GREMLIN(1)
entity_238_1 = obj_class.Entity(f'{cnst.ENTITY_COLOR}GREMLIN{cnst.DEFAULT_COLOR}', 5, 3, True, False)
entity_238_1_z_init = entity_238_1_z_count = entity_238_1.entity_z_count
entity_238_1_w_init = entity_238_1_w_count = entity_238_1.entity_w_count
# - - - - - - - - -
# /// LICHA(2)
entity_238_2 = obj_class.Entity(f'{cnst.ENTITY_COLOR}LICHA{cnst.DEFAULT_COLOR}', 6, 5, True, False)
entity_238_2_z_init = entity_238_2_z_count = entity_238_2.entity_z_count
entity_238_2_w_init = entity_238_2_w_count = entity_238_2.entity_w_count
# - - - - - - - - -
# /// BRONGO(3)
entity_238_3 = obj_class.Entity(f'{cnst.ENTITY_COLOR}BRONGO{cnst.DEFAULT_COLOR}', 8, 4, True, False)
entity_238_3_z_init = entity_238_3_z_count = entity_238_3.entity_z_count
entity_238_3_w_init = entity_238_3_w_count = entity_238_3.entity_w_count
# - - - - - - - - -
# /// ORKONIK(4)
entity_238_4 = obj_class.Entity(f'{cnst.ENTITY_COLOR}ORKONIK{cnst.DEFAULT_COLOR}', 6, 4, True, False)
entity_238_4_z_init = entity_238_4_z_count = entity_238_4.entity_z_count
entity_238_4_w_init = entity_238_4_w_count = entity_238_4.entity_w_count
# - - - - - - - - -
# /// SAMASKÓRA(5)
entity_238_5 = obj_class.Entity(f'{cnst.ENTITY_COLOR}SAMASKÓRA{cnst.DEFAULT_COLOR}', 6, 5, True, False)
entity_238_5_z_init = entity_238_5_z_count = entity_238_5.entity_z_count
entity_238_5_w_init = entity_238_5_w_count = entity_238_5.entity_w_count
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# /// 317:
# /// OGRE
entity_317 = obj_class.Entity(f'{cnst.ENTITY_COLOR}OGRE{cnst.DEFAULT_COLOR}', 8, 10, True, False)
entity_317_z_init = entity_317_z_count = entity_317.entity_z_count
entity_317_w_init = entity_317_w_count = entity_317.entity_w_count
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# /// 332:
# /// TROLL
entity_332 = obj_class.Entity(f'{cnst.ENTITY_COLOR}TROLL{cnst.DEFAULT_COLOR}', 8, 8, True, False)
entity_332_z_init = entity_332_z_count = entity_332.entity_z_count
entity_332_w_init = entity_332_w_count = entity_332.entity_w_count
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# /// 344:
# /// STRAŻNIK TAJEMNICY
entity_344 = obj_class.Entity(f'{cnst.ENTITY_COLOR}STRAŻNIK TAJEMNICY{cnst.DEFAULT_COLOR}', 10, 16,
                              True, False)
entity_344_z_init = entity_344_z_count = entity_344.entity_z_count
entity_344_w_init = entity_344_w_count = entity_344.entity_w_count
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -

# /// declare rooms
# self, room_id, room_state, visit_in_turn
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
room_268 = obj_class.Room('268')
# - - - - - - - - -
room_310 = obj_class.Room('310')
# - - - - - - - - -
room_331 = obj_class.Room('331', True)
# - - - - - - - - -
room_336 = obj_class.Room('336')
# - - - - - - - - -
room_364 = obj_class.Room('364', False, 2)
# - - - - - - - - -
room_xxx = obj_class.Room('xxx')  # placeholder room for testing
