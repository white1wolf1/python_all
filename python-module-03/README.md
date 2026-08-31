bu projede oğrenmemiz gerekenler;
1. Kullanıcıdan veri almak 
2. sys
3. list - liste manipulasyonları (len, sum, max ,print)
4. tuple - 




   : List :
are used to  store more than one  items in one variable (Clollections)
List items are ordered, changeable, and allow duplicate values.
list = ["apple", "banana", "cherry"]

list1 = ["abc", 34, True, 40, "male"] 
farklı tupte şeyler tutabilir


-   Tuple 
A tuple is a collection which is ordered and unchangeable.
Tuple items are ordered, unchangeable, and allow duplicate values.
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
you can acsess inside of tuple buy tuple[i]

tuple1 = ("abc", 34, True, 40, "male")
mytuple2 = "ayse",
mytuple = ("apple", "banana", "cherry")
mytuple = ()

-Set 
Set items are unchangeable, but you can remove items and add new items.
Set items are unordered, unchangeable, and do not allow duplicate values.
Once a set is created, you cannot change its items, but you can remove items and add new items.
Sets cannot have two items with the same value.
The values True and 1
The values False  and 0
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns True if all items of this set is present in another set
 	<	Returns True if all items of this set is present in another, larger set
issuperset()	>=	Returns True if all items of another set is present in this set
 	>	Returns True if all items of another, smaller set is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()
 also there are  froze sets you cant add or subtract elements but they act lşke sets 
 boş_set = set() othervise {} is a  dict

-Dictionary 
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}

Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}



