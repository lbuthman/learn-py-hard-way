from nose.tools import *
from ex48 import lexicon
from ex48 import parser


def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                            ('direction', 'south'),
                            ('direction', 'east')])


def test_verbs():
    assert_equal(lexicon.scan("go"), [("verb", "go")])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [("verb", "go"),
                          ("verb", "kill"),
                          ("verb", "eat")])


def test_nouns():
    assert_equal(lexicon.scan("bear"), [("noun", "bear")])
    result = lexicon.scan("bear princess")
    assert_equals(result, [("noun", "bear"),
                           ("noun", "princess")])


def test_numbers():
    assert_equal(lexicon.scan("1234"), [("number", 1234)])
    result = lexicon.scan("3 91234")
    assert_equals(result, [("number", 3),
                           ("number", 91234)])


def test_errors():
    assert_equal(lexicon.scan("ASDFASDF"), [("error", "ASDFASDF")])
    result = lexicon.scan("bear IAS princess")
    assert_equals(result, [("noun", "bear"),
                           ("error", "IAS"),
                           ("noun", "princess")])


def test_peek():
    word_list = lexicon.scan("bear eat beet")
    assert_equal(parser.peek(word_list), "noun")
    assert_equal(parser.peek(None), None)


def test_match():
    word_list = lexicon.scan("bear eat beet")
    assert_equal(parser.match(word_list, 'noun'), ('noun', 'bear'))
    assert_equal(parser.match(word_list, None), None)
    assert_equal(parser.match(None, None), None)


def test_skip():
    word_list = lexicon.scan("the bear eat beet")
    assert_equal(parser.skip(word_list, 'stop'), None)
    assert_equal(parser.skip(None, 'stop'), None)


def test_parse_verb():
    word_list = lexicon.scan("and eat cats")
    assert_equal(parser.parse_verb(word_list), ('verb', 'eat'))
    bad_list = lexicon.scan("bears beets battle star galactica")
    assert_raises(parser.ParserError, parser.parse_verb, bad_list)


def test_parse_object():
    word_list = lexicon.scan("the bear eat beet")
    assert_equal(parser.parse_object(word_list), ('noun', 'bear'))
    word_list = lexicon.scan("south beet")
    assert_equal(parser.parse_object(word_list), ('direction', 'south'))
    bad_list = lexicon.scan("eat beet")
    assert_raises(parser.ParserError, parser.parse_object, bad_list)


def test_parse_subject():
    word_list = lexicon.scan("the bear eat beet")
    assert_equal(parser.parse_subject(word_list), ('noun', 'bear'))
    word_list = lexicon.scan("eat beet")
    assert_equal(parser.parse_subject(word_list), ('noun', 'player'))
    bad_list = lexicon.scan("identity theft is a crime jim")
    assert_raises(parser.ParserError, parser.parse_subject, bad_list)


def test_parse_sentence():
    word_list = lexicon.scan("the bear eat beet")
    sentence = parser.parse_sentence(word_list)
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.object, 'beet')
    word_list = lexicon.scan("eat beet")
    sentence = parser.parse_sentence(word_list)
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.object, 'beet')
    bad_list = lexicon.scan("bear beet eat the make sense none")
    assert_raises(parser.ParserError, parser.parse_sentence, bad_list)
