import sys
import unittest

class Evaluator(object):
    VALUES = ['2','3','4','5','6','7','8','9','T', 'J', 'Q', 'K', 'A']
    VALUES_DICT = {
        '2' : '2',
        '3' : '3',
        '4' : '4',
        '5' : '5',
        '6' : '6',
        '7' : '7',
        '8' : '8',
        '9' : '9',
        'T' : '10',
        'J' : '11',
        'Q' : '12',
        'K' : '13',
        'A' : '14'
    }
    SUITS = ['C', 'D', 'H', 'S']
    
    def find_POKER_VALUE(self, hand):
        if self.find_royal_flush(hand):
            return True, "Royal Flush", 10
        elif self.find_straight_flush(hand):
            return True, "Straight Flush", 9
        elif self.find_four_of_a_kind(hand):
            return True, "Four of a Kind", 8
        elif self.find_full_house(hand):
            return True, "Full House", 7
        elif self.find_flush(hand):
            return True, "Flush", 6
        elif self.find_straight(hand):
            return True, "Straight", 5
        elif self.find_three_of_a_kind(hand):
            return True, "Three of a Kind", 4
        elif self.find_two_pair(hand):
            return True, "Two Pair", 3
        elif self.find_one_pair(hand):
            return True, "One Pair", 2
        else:
            return True, "High Card", 1
    
    def is_same_suit(self, hand):
        suit = hand.cards[0].SUIT
        for index in range(1, 5):
            if hand.cards[index].SUIT != suit:
                return False
        return True
    
    def get_cards_dict_value(self, hand):
        dict_value = []
        for card in hand.cards:
            dict_value.append(self.VALUES_DICT[card.VALUE])
        dict_value.sort()
        return dict_value

    def find_royal_flush(self, hand):
        if not self.is_same_suit(hand):
            return False

        sequence = ['A', 'J', 'Q', 'K', 'T']
        for card in hand.cards:
            found = False
            for value in sequence:
                if str(value) == str(card.VALUE):
                    found = True
                    break
            if found == False:
                return False
        return True

    def find_straight_flush(self, hand):
        if not self.is_same_suit(hand):
            return False

        dict_value = self.get_cards_dict_value(hand)
        last_value = dict_value[0]

        for index in range(1, 5):
            if int(dict_value[index]) - int(last_value) != 1:
                return False
            else:
                last_value = dict_value[index]
        return True

    def get_card_values_frequency(self, hand):
        values = [0] * 20
        dict_values = self.get_cards_dict_value(hand)
        
        for value in dict_values:
            values[int(value)] = values[int(value)] + 1
        return values 

    def find_four_of_a_kind(self, hand):
        values = self.get_card_values_frequency(hand)

        found = False
        for value in values:
            if value >= 4:
                found = True
                break
        if found == False:
            return False
        return True
    
    def is_card_values_frequency_three(self, values):
        found = False
        for value in values:
            if value == 3:
                found = True
                break
        if found == False:
            return False
        return True
    
    def is_card_values_frequency_two(self, values):
        found = False
        for value in values:
            if value == 2:
                found = True
                break
        if found == False:
            return False
        return True

    def find_full_house(self, hand):
        values = self.get_card_values_frequency(hand)
        
        if not self.is_card_values_frequency_two(values):
            return False
        
        if not self.is_card_values_frequency_three(values):
            return False

        return True

    def find_flush(self, hand):
        if not self.is_same_suit(hand):
            return False
        return True

    def find_straight(self, hand):
        if self.is_same_suit(hand):
            return False
        
        dict_value = self.get_cards_dict_value(hand)
        last_value = dict_value[0]

        for index in range(1, 5):
            if int(dict_value[index]) - int(last_value) != 1:
                return False
            else:
                last_value = dict_value[index]
        return True

    def find_three_of_a_kind(self, hand):
        values = self.get_card_values_frequency(hand)
        
        if self.is_card_values_frequency_three(values):
            return True
        return False

    def find_two_pair(self, hand):
        values = self.get_card_values_frequency(hand)

        count = 0
        for value in values:
            if value == 2:
                count = count + 1
        if count == 2:
            return True
        return False

    def find_one_pair(self, hand):
        values = self.get_card_values_frequency(hand)
        
        count = 0
        for value in values:
            if value == 2:
                count = count + 1
        if count == 1:
            return True
        return False

    def find_high_card(self, hand):
        return True

class Card(object):
    SUIT = None
    VALUE = None
 
    def __init__(self, str_card):
        self.VALUE = str_card[0]
        self.SUIT = str_card[1]
 
    def __str__(self):
        return "%s%s" % (self.VALUE, self.SUIT)
 
class Hand(object):
    evaluator = Evaluator()
    cards = []
    VALUE = None
    SCORE = None

    def __init__(self, cards=None, value=None, score=None):
        self.cards = cards
        self.VALUE = value
        self.SCORE = score
     
    def __str__(self):
        return "<hand [%s, %s, %s, %s, %s], '%s'>" % (self.cards[0], self.cards[1], self.cards[2], self.cards[3], self.cards[4], self.VALUE)
 
    @classmethod
    def from_string(self, hand_str):
        self.push(hand_str)
        status, self.VALUE, self.SCORE = self.evaluator.find_POKER_VALUE(self)
        return Hand(self.cards, self.VALUE, self.SCORE)
     
    @classmethod
    def push(self, hand_str):
        five_cards = hand_str.split()
        self.push_five_cards(five_cards)
        return self
 
    @classmethod
    def push_five_cards(self, five_cards):
        self.cards = []
        for card_str in five_cards:
            card = Card(card_str)
            self.cards.append(card)
        return self
    
    def __cmp__(self, hand2):
        return cmp(self.SCORE, hand2.SCORE)
 
 
class Hands(object):
    hand_list = []
 
    def __init__(self, hand_str = None):
        if hand_str:
            hand = Hand()
            hand.push(hand_str)
            self.hand_list.append(hand)
 
    def from_string(self, hand_str):
        hand = Hand()
        hand.push(hand_str)
        self.push(hand)
 
    def push(self, hand):
        self.hand_list.append(hand)
 
    def __str__(self):
        hand_list_str = ""
        for hand in self.hand_list:
            hand_list_str += "%s\n" % (hand)
        return "%s" % (hand_list_str)
 
    def sort(self):
        self.hand_list.sort(reverse=True)
        return self.hand_list


class TestPokerMethod(unittest.TestCase):
    def test_royal_flush(self):
        hand = Hand.from_string('TS JS QS KS AS')
        self.assertEqual('Royal Flush', hand.VALUE)

    def test_is_same_suit_false_check(self):
        hand = Hand.from_string('TS JS QS KS AD')
        evaluator = Evaluator()
        self.assertFalse(evaluator.is_same_suit(hand))
    
    def test_is_same_suit_true_check(self):
        hand = Hand.from_string('TS JS QS KS AS')
        evaluator = Evaluator()
        self.assertTrue(evaluator.is_same_suit(hand))
    
    def test_three_of_a_kind(self):
        hand1 = Hand.from_string('4D 4D 4D 7H 5D')
        self.assertEqual('Three of a Kind', hand1.VALUE)

        hand2 = Hand.from_string('4D 4D 4D 7H 2D')
        self.assertEqual('Three of a Kind', hand2.VALUE)

        hand3 = Hand.from_string('4D 4D 4D 7H 3D')
        self.assertEqual('Three of a Kind', hand3.VALUE)

    def test_find_one_pair(self):
        hand1 = Hand.from_string('4D 4D 4D 7H 5D')
        self.assertNotEqual('One Pair', hand1.VALUE)
        
        hand1 = Hand.from_string('4D 4D 5D 7H 5D')
        self.assertNotEqual('One Pair', hand1.VALUE)
        
        hand1 = Hand.from_string('3D 4D 5D 7H 5D')
        self.assertEqual('One Pair', hand1.VALUE)
        
        hand1 = Hand.from_string('3D 4D 5D 7H 5D')
        self.assertEqual('One Pair', hand1.VALUE)

    def test_two_pair(self):
        hand10 = Hand.from_string('5H 5C QD QC QS')
        self.assertNotEqual('Two Pair', hand10.VALUE)

        hand10 = Hand.from_string('5H 5C QD QC 2S')
        self.assertEqual('Two Pair', hand10.VALUE)
    
    def test_one_pair(self):
        hand10 = Hand.from_string('5H 5C QD QC QS')
        self.assertNotEqual('Two Pair', hand10.VALUE)

        hand10 = Hand.from_string('5H 5C 2D QC 3S')
        self.assertEqual('One Pair', hand10.VALUE)

    def test_flush(self):
        hand8 = Hand.from_string('5S 6S 7S 8S TS') 
        self.assertEqual('Flush', hand8.VALUE)
    
    def test_high_card(self):
        hand8 = Hand.from_string('2J QD 8J 7D 4J') 
        self.assertNotEqual('Flush', hand8.VALUE)
        self.assertEqual('High Card', hand8.VALUE)
    
    def test_full_house(self):
        hand8 = Hand.from_string('5S 5S 5S TS TS') 
        self.assertEqual('Full House', hand8.VALUE)
    
    def test_straight_flush(self):
        hand7 = Hand.from_string('5S 6S 7S 8S 9S') 
        self.assertNotEqual('Full House', hand7.VALUE)
        self.assertEqual('Straight Flush', hand7.VALUE)
    
    def test_four_of_a_kind(self):
        hand4 = Hand.from_string('4D 4D 4D 7H 4D')
        self.assertNotEqual('Full House', hand4.VALUE)
        self.assertEqual('Four of a Kind', hand4.VALUE)

    def test_whole_process(self):
        hand1 = Hand.from_string('4D 4D 4D 7H 5D')
        hand2 = Hand.from_string('4D 4D 4D 7H 2D')
        hand3 = Hand.from_string('4D 4D 4D 7H 3D')
        hand4 = Hand.from_string('4D 4D 4D 7H 4D')
        hand5 = Hand.from_string('4D 4D 4D 7H 8D')
        hand6 = Hand.from_string('TS JS QS KS AS') 
        hand7 = Hand.from_string('5S 6S 7S 8S 9S') 
        hand8 = Hand.from_string('5S 6S 7S 8S TS') 
        hand9 = Hand.from_string('7S TC TH TS TD') 
        hand10 = Hand.from_string('5H 5C QD QC QS')
        hand11 = Hand.from_string('2D 3D 7D QD AD')
        hand12 = Hand.from_string('4D 5D 6D 7H 8D')
        hand13 = Hand.from_string('4J 4S 4D 7H 8D')
        hand14 = Hand.from_string('QJ QD 7J 7D 4J')
        hand15 = Hand.from_string('QJ QD 8J 7D 4J')
        hand16 = Hand.from_string('2J QD 8J 7D 4J')
        hand17 = Hand.from_string('4D 3D 3D 7H AD')

        hands = Hands()
        hands.push(hand1)
        hands.push(hand2)
        hands.push(hand3)
        hands.push(hand4)
        hands.push(hand5)
        hands.push(hand7)
        hands.push(hand8)
        hands.push(hand6)
        hands.push(hand9)
        hands.push(hand10)
        hands.push(hand11)
        hands.push(hand12)
        hands.push(hand13)
        hands.push(hand14)
        hands.push(hand15)
        hands.push(hand16)
        hands.push(hand17)
        hands.sort()
        
        print hands 
        

if __name__== '__main__':
    unittest.main()
 
