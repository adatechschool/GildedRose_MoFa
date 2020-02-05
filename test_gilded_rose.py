# -*- coding: utf-8 -*-
#!/usr/bin/env python

import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_nom_respecter(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_date_expiration(self):
        items = [Item("foo", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)

    def test_qualite(self):
        items = [Item("foo", 1, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(39, items[0].quality)

    def test_3jour(self):
    	items = [
    				Item("sac", 20, 5),
    				Item("Aged Brie", 42, 20),
    				Item("Sulfuras, Hand of Ragnaros", 0, 0),
    				Item("Backstage passes to a TAFKAL80ETC concert", 3, 15),
    				Item("lampe", 10, 10),
    			]
    	days = 3
    	for day in range(days):
    		print("------day %s------" % day)
    		print("name, sell_in, quality")
    		for item in items:
    			print(item)
    		print("")
    		gilded_rose = GildedRose(items)
    		gilded_rose.update_quality()
    	self.assertEquals(17, items[0].sell_in)
    	self.assertEquals(2, items[0].quality)


if __name__ == '__main__':
    unittest.main()
