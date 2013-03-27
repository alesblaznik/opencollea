# coding=utf-8
from django.db import IntegrityError
from django.test import TestCase
from opencollea.models import *

class CourseTests(TestCase):
    def test_title_to_machine_readable_on_insert_with_no_machine_readable_defined(self):
        """
        Pri vnosu novega tečaja se mora naslov tečaja pretvorit
        v strojno berljiv format - v primeru, da ga uporabnik ni sam vnesel.
        """
        course = Course(title=pangram())
        course.save()
        self.assertEqual(course.machine_readable_title, pangram_slugified())

    def test_title_to_machine_readable_on_insert_with_valid_machine_readable_defined(self):
        """
        Pri vnosu novega tečaja lahko uporabnik sam vpiše strojno ime
        za tečaj.
        """
        valid_machine_readable_string = pangram_slugified()
        course = Course(title="Whatever Course Title",
                        machine_readable_title=valid_machine_readable_string)
        course.save()
        self.assertEqual(course.machine_readable_title,
                         valid_machine_readable_string)

    def test_machine_readable_title_must_be_unique(self):
        """
        Machine readable title mora biti unikaten
        """
        title = 'Whatever the Course'
        course1 = Course(title=title)
        course2 = Course(title=title)
        course1.save()
        self.assertRaises(IntegrityError, course2.save)


class TagTests(TestCase):
    def test_title_to_machine_readable_on_insert_with_no_machine_readable_defined(self):
        """
        Pri vnosu novega taga se mora naziv preslikati v strojno berljiv
        format - v primeru, da ga uporabnik in sam navedel.
        """
        title = pangram()
        machine_readable_title = pangram_slugified()
        tag = Tag(title=title)
        tag.save()
        self.assertEqual(tag.machine_readable_title, machine_readable_title)

    def test_title_to_machine_readable_on_insert_with_valid_machine_readable_defined(self):
        """
        Pri vnosu novega taga lahko uporabnik sam vnese poljubno
        veljavno strojno ime.
        """
        title = "My Tag Name"
        machine_readable_title = pangram_slugified()
        tag = Tag(title=title, machine_readable_title=machine_readable_title)
        tag.save()
        self.assertEqual(tag.machine_readable_title, machine_readable_title)

    def test_machine_readable_title_must_be_unique(self):
        """
        Storjno ime za Tag mora biti unikatno.
        """
        title = "My Custom Tag Name"
        tag1 = Tag(title=title)
        tag2 = Tag(title=title)
        tag1.save()
        self.assertRaises(IntegrityError, tag2.save)

def pangram():
    return "  V ko-žu?ščku  hu*do$bne%ga fanta stopiclja mizar. "

def pangram_slugified():
    return "v-ko-zuscku-hudobnega-fanta-stopiclja-mizar"

