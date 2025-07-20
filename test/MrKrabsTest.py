from ..constants import LocationNames, ItemNames
from . import BfBBTestBase


class MrKrabsSOTest(BfBBTestBase):
    options = {
        "include_purple_so": True
    }

    def test_access_with_so(self):
        rules = [
            (LocationNames.spat_ks_01, 3),  # 1500/500 = 3
            (LocationNames.spat_ks_02, 4),  # 1750/500 = 4 (+250)
            (LocationNames.spat_ks_03, 4),  # 2000/500 = 4 (+250)
            (LocationNames.spat_ks_04, 4),  # 2250/500 = 4 (0)
            (LocationNames.spat_ks_05, 5),  # 2500/500 = 5
            (LocationNames.spat_ks_06, 6),  # 2750/500 = 6 (+250)
            (LocationNames.spat_ks_07, 6),  # 3250/500 = 6 (0)
            (LocationNames.spat_ks_08, 8),  # 3750/500 = 8 (+250)
        ]
        self.collect_by_name(ItemNames.spat)
        item = self.get_item_by_name(ItemNames.so_500)
        amount_sum = 0
        for i in range(-1, 8, 1):
            if i >= 0:
                self.collect(rules[i][1] * [item])
                amount_sum = amount_sum + rules[i][1]
            j = 0
            for loc, _ in rules:
                if i >= 0 and j <= i:
                    self.assertTrue(self.can_reach_location(loc), f"{loc} can't be reached with {amount_sum * 500} SOs")
                else:
                    self.assertFalse(self.can_reach_location(loc), f"{loc} can be reached with {amount_sum * 500} SOs")
                j = j + 1
