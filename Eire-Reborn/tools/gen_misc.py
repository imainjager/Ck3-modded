"""Miscellaneous localization: army names and other small strings."""
from eir_lib import *


def build():
    L = Loc("eir_misc_l_english.yml")
    L.add("eir_viking_fleet_name", "Viking Fleet")
    L.add("eir_foreign_host_name", "Foreign Host")
    L.add("eir_clan_muster_name", "Clan Muster")
    L.add("eir_mercenary_company_name", "Mercenary Company")
    L.add("eir_bandit_warband_name", "Warband")
    L.add("eir_gallowglass_company_name", "Gallowglass Company")
    L.add("eir_book_of_kells_name", "The Gospel of Kells")
    L.add("eir_book_of_kells_desc", "A gospel book of astonishing beauty, the work of years of patient monks.")
    L.add("eir_ardagh_chalice_name", "The Silver Chalice")
    L.add("eir_ardagh_chalice_desc", "A silver and gold chalice, ornamented with interlace and set with amber.")
    L.add("eir_torc_of_tara_name", "The Torc of Tara")
    L.add("eir_torc_of_tara_desc", "A great twisted gold collar, older than any king of Ireland.")
    L.add("eir_caladbolg_name", "Caladbolg")
    L.add("eir_caladbolg_desc", "A sword the poets say struck three hills flat.")
    for k, n, d in (("iona_reliquary", "The Reliquary of Iona", "A bronze and silver box holding a scrap of Colmcille's cloak."),
                    ("poets_chain", "The High Poet's Chain", "A silver chain with small bells, given by the chief poet to a king he judged worthy."),
                    ("moot_horn", "The Moot Horn", "A carved drinking horn blown to call the thanes to their open-air moot."),
                    ("dimma", "The Little Gospel", "A pocket gospel book that can be carried in a satchel."),
                    ("bell_shrine", "The Bell Shrine", "A bronze and silver shrine for the iron bell of a saint."),
                    ("lunula", "The Gold Lunula", "A crescent of beaten gold, older than any king."),
                    ("ogham_blade", "The Ogham Blade", "A sword with a line of ogham letters along the spine."),
                    ("chieftain_torc", "The Chieftain's Torc", "A twisted gold collar worn by a line of lesser kings."),
                    ("cathach", "The Cathach", "A battle psalter said to have been copied by a saint, carried around armies before they fought."),
                    ("tara_brooch", "The Great Brooch", "A vast silver-gilt brooch, too big to be practical and too beautiful to leave off."),
                    ("cross_of_cong", "The Processional Cross", "An oak cross covered in bronze and silver, with a crystal at its heart.")):
        L.add("eir_%s_name" % k, n)
        L.add("eir_%s_desc" % k, d)
    # nicknames earned from the great decisions (flavor guide: every major decision leaves a memory)
    nicks = [
        ("nick_eir_convener", "the Convener", "Called the great assembly of the Gael, and every king came.", False),
        ("nick_eir_tara_builder", "the Builder of Tara", "Raised the Hall of Tara on the hill of the kings.", False),
        ("nick_eir_poet_king", "the Poet-King", "Gave the Filí their charter and made poetry a pillar of the state.", False),
        ("nick_eir_cow_lord", "the Cow-Lord", "Counted every herd in the kingdom and made the cattle the basis of a state.", False),
        ("nick_eir_abbot_king", "the Abbot-King", "Raised the monastic cities and ruled as friend of the saints.", False),
        ("nick_eir_sea_king", "the Sea-King", "Claimed the Irish Sea for the Gael.", False),
        ("nick_eir_sea_master", "Master of the Western Sea", "Holds every harbour from Dublin to the Hebrides.", False),
        ("nick_eir_gael_father", "Father of the Gael", "Presided over the golden age of the Gaelic peoples.", False),
        ("nick_eir_unifier", "the Unifier", "Ended the age of broken kingdoms and made the high kingship a throne.", False),
        ("nick_eir_celtic_brother", "Brother of the Celtic Peoples", "Called the Welsh, the Cornish, the Bretons and the Gaels of Alba brothers.", False),
        ("nick_eir_high_king", "Ard Rí", "Crowned High King at Tara.", False),
        ("nick_eir_the_crowned", "the Crowned", "Took a crown that Ireland had never seen.", False),
        ("nick_eir_emperor_gael", "Emperor of the Gael", "Raised a throne over every Gaelic land.", False),
        ("nick_eir_tongue_giver", "the Tongue-Giver", "Gave the old speech back to the children of a conquered county.", False),
        ("nick_eir_britain_restorer", "Restorer of Britain", "Stood at the centre when the old island spoke its old languages again.", False),
        ("nick_eir_norse_bane", "Norse-Bane", "Refused the Danegeld and sent the longships home.", False),
    ]
    body = "# Eire Reborn - nicknames\n\n" + "".join("%s = %s\n" % (k, "{ is_bad = yes }" if bad else "{}") for k, _, _, bad in nicks)
    write("common/nicknames/eir_nicknames.txt", body)
    for k, name, desc, _ in nicks:
        L.add(k, name)
        L.add(k + "_desc", desc)
    L.write()
    print("misc loc written")


if __name__ == "__main__":
    build()
