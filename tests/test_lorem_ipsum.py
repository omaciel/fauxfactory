# -*- coding: utf-8 -*-

"""Tests for Lorem Ipsum generator."""

from fauxfactory import gen_iplum
from fauxfactory.constants import LOREM_IPSUM_TEXT

import random
import unittest


class TestLoremIpsum(unittest.TestCase):
    """
    Test lorem ipsum generator
    """

    def test_gen_loremipsum_1(self):
        """
        @Test: Create a complete lorem ipsum string
        @Feature: Lorem Ipsum Generator
        @Assert: Complete lorem ipsum value that starts with 'Lorem ipsum'
        """

        result = gen_iplum()
        self.assertEqual(
            result,
            LOREM_IPSUM_TEXT, "Generated text is not Lorem Ipsum")
        self.assertTrue(
            result.startswith('Lorem ipsum'),
            "Generated string does not start with Lorem Ipsum"
        )

    def test_gen_loremipsum_2(self):
        """
        @Test: Create a lorem ipsum string with fixed number of words
        @Feature: Lorem Ipsum Generator
        @Assert: lorem ipsum value has exact number of words
        """

        for i in range(20):
            length = random.randint(1, 500)
            result = gen_iplum(words=length)
            self.assertEqual(
                len(result.split()),
                length,
                "Generated string does not have the correct number of words")

    def test_gen_loremipsum_3(self):
        """
        @Test: Create a lorem ipsum string with fixed number of paragraphs
        @Feature: Lorem Ipsum Generator
        @Assert: length lorem ipsum value has exact number of paragraphs
        """

        for i in range(20):
            length = random.randint(1, 20)
            result = gen_iplum(paragraphs=length)
            self.assertEqual(
                len(result.split('\n')),
                length,
                "Generated string does not have the correct number"
                " of paragraphs")

    def test_gen_loremipsum_4(self):
        """
        @Test: Create a lorem ipsum string with zero words
        @Feature: Lorem Ipsum Generator
        @Assert: Complete lorem ipsum value is returned
        """

        result = gen_iplum(words=0)
        self.assertEqual(
            result,
            LOREM_IPSUM_TEXT, "Generated text is not Lorem Ipsum")

    def test_gen_loremipsum_5(self):
        """
        @Test: Create a lorem ipsum string with zero paragraphs
        @Feature: Lorem Ipsum Generator
        @Assert: Raises ValueError
        """

        with self.assertRaises(ValueError):
            gen_iplum(paragraphs=0)

    def test_gen_loremipsum_6(self):
        """
        @Test: Create a lorem ipsum string with 1 word and 0 paragragh
        @Feature: Lorem Ipsum Generator
        @Assert: Raise ValueError
        """

        with self.assertRaises(ValueError):
            gen_iplum(words=1, paragraphs=0)

    def test_gen_loremipsum_7(self):
        """
        @Test: Create a lorem ipsum string with 1 word and 1 paragragh
        @Feature: Lorem Ipsum Generator
        @Assert: Generated string has 1 word in 1 paragraph
        """

        result = gen_iplum(words=1, paragraphs=1)
        self.assertEqual(len(result.split()), 1, "String is not 1-word long")
        self.assertEqual(
            len(result.split()), 1, "String is not 1-paragraph long")

    def test_gen_loremipsum_8(self):
        """
        @Test: Create a lorem ipsum string with non-integer words
        @Feature: Lorem Ipsum Generator
        @Assert: Raises ValueError
        """

        with self.assertRaises(ValueError):
            gen_iplum(words='a')

    def test_gen_loremipsum_9(self):
        """
        @Test: Create a lorem ipsum string with non-integer paragraphs
        @Feature: Lorem Ipsum Generator
        @Assert: Raises ValueError
        """

        with self.assertRaises(ValueError):
            gen_iplum(paragraphs='a')

    def test_gen_loremipsum_10(self):
        """
        @Test: Create a lorem ipsum string with random words/paragraphs
        @Feature: Lorem Ipsum Generator
        @Assert: lorem ipsum value has exact number of words/paragraphs
        """

        for i in range(20):
            words = random.randint(1, 500)
            paragraphs = random.randint(1, 500)
            result = gen_iplum(
                words=words, paragraphs=paragraphs)
            self.assertEqual(
                len(result.split('\n')),
                paragraphs,
                ("Generated string does not have the correct number"
                 "of paragraphs"))
            for sentence in result.split('\n'):
                self.assertEqual(
                    len(sentence.split()),
                    words,
                    ("Generated string does not have the correct"
                     "number of words"))
