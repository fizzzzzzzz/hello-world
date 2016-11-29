from nose.tools import *
from ex49 import game

def test_Sentence():
	sentence = game.Sentence(('noun','bear'),('verb','eat'),('direction','apple'))
	assert_equal(sentence.subject, 'bear')
	assert_equal(sentence.verb, 'eat')
	assert_equal(sentence.object, 'apple')
	
def test_peek():
	p = game.peek([])
	assert_equal(p,None)
	
def test_parse_verb():
	assert_raises(game.ParserError,game.parse_verb,[('noun','apple')])