from flask import redirect
import json






def simplePlay(tree):
    parent = tree[0]
    left_child = tree[1]
    right_child = tree[2]
    if isLeaf(tree) is False:
        print(parent)
        ans = input("Your answer: ")
        if ans.lower() == "yes":
            return simplePlay(left_child)
        if ans.lower() == "no":
            return simplePlay(right_child)
    else:
        return playLeaf(tree)




# tree = ("Do you want to select a restaurant here?",
#      ("Is it " + a + "?",
#       ('I got it', None, None),
#       ('Need to go a little further?',
#        ('Adjusting distance for you', None, None),
#        ('Need to get a higher rating restaurant?', ('Adjusting rating for you', None, None),
#         ('Want to find a cheaper restaurant?', ('Adjusting price for you', None, None),
#          ('Do you want to deliver the food for you?', ('selecting delivery for you', None, None),
#           ('selecting pickup for you', None, None)))))),
#      (redirect('/form_category_and_user_location'), None, None))

dict_test = {}

def playLeaf(dict):
    parent = list(dict.keys())[0]
    return parent

def isLeaf(dict):
    left_child = dict['left']
    right_child = dict['right']
    if left_child is None and right_child is None:
        return True
    else:
        return False


def simplePlay(dict_test):
    parent = list(dict_test.keys())[0]
    left_child = dict_test.values()
    right_child = dict_test.values()
    print(left_child)
    print(right_child)
    if isLeaf(dict_test) is False:
        print(parent)
        ans = input("Your answer: ")
        if ans.lower() == "yes":
            return simplePlay(left_child)
        if ans.lower() == "no":
            return simplePlay(right_child)
    else:
        return playLeaf(dict)

