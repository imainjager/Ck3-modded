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
    for k, n, d in (("dimma", "The Little Gospel", "A pocket gospel book that can be carried in a satchel."),
                    ("bell_shrine", "The Bell Shrine", "A bronze and silver shrine for the iron bell of a saint."),
                    ("lunula", "The Gold Lunula", "A crescent of beaten gold, older than any king."),
                    ("ogham_blade", "The Ogham Blade", "A sword with a line of ogham letters along the spine."),
                    ("chieftain_torc", "The Chieftain's Torc", "A twisted gold collar worn by a line of lesser kings."),
                    ("cathach", "The Cathach", "A battle psalter said to have been copied by a saint, carried around armies before they fought."),
                    ("tara_brooch", "The Great Brooch", "A vast silver-gilt brooch, too big to be practical and too beautiful to leave off."),
                    ("cross_of_cong", "The Processional Cross", "An oak cross covered in bronze and silver, with a crystal at its heart.")):
        L.add("eir_%s_name" % k, n)
        L.add("eir_%s_desc" % k, d)
    L.write()
    print("misc loc written")


if __name__ == "__main__":
    build()
