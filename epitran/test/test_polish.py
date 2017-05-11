# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import unicodedata

import epitran


class TestPolish(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('pol-Latn')

    def test_dania(self):
        tr = self.epi.transliterate('dania')
        self.assertEqual(tr, 'daɲa')

    def test_dan(self):
        tr = self.epi.transliterate('dań')
        self.assertEqual(tr, 'daɲ')

    def test_danii(self):
        tr = self.epi.transliterate('Danii')
        self.assertEqual(tr, 'daɲji')

    def test_mania(self):
        tr = self.epi.transliterate('Mania')
        self.assertEqual(tr, 'maɲa')

    def test_mani(self):
        tr = self.epi.transliterate('Mani')
        self.assertEqual(tr, 'maɲi')

    def test_manii(self):
        tr = self.epi.transliterate('manii')
        self.assertEqual(tr, 'maɲji')
