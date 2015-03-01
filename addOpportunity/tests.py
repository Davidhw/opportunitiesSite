from django.test import TestCase
from addOpportunity.models import Posting
from addOpportunity.forms import PostFilter
from itertools import combinations


def setUp(self):
    # create three posts: marketingIntern, lifeguard, zooVolunteer
    marketingIntern  = Posting.objects.create(position_Type = "I", name = "Marketing Intern", salary = 5000, payment_Type = "Y", organization = "Prescott Media", email = "testemail@test.com", phone = "555-555-5555", description = "Fact check reports, handle social media, summarize other papers coverage", hiring_Criteria  = "3 years experience", key_Words = "journalism",visible=True)
    lifeguard = Posting.objects.create(position_Type = "J", name = "Lifeguard", salary = 15, payment_Type = "H", organization = "YNCA", email = "talentacquisition@ynca.com", phone = "123-123-4567", description = "Maintain Safe Environment, Attend Weekly Meetings", hiring_Criteria  = "two phds in lifeguarding science", key_Words = "")
    zooVolunteer = Posting.objects.create(position_Type = "V", name = "Zoo Volunteer", salary = 0, payment_Type = "U", organization = "The Zoo", email = "zoo@zoo.com", phone = "012-345-6789", description = "Feed the animals and evaluate their health", hiring_Criteria  = "Experience is a plus", key_Words = "animals",visible = False)


# not actually used as a test, used to get app engine to index every possible query
def testAllPossibleIndexes(self):
    fields = ["position_Type","payment_Type", "name", "organization", "key_Words"]
    possibleValue = ["J","H","Python TA", "ncf", "testKey"]
    
    indexes = [x for x in range(len(fields))]
    allFieldCombinations = []
    for x in len(indexes):
        allFieldCombinations+=combinations(indexes,x+1)

    
    for combo in allFieldCombinations:
        postFilterString = ""
        for ind in combo:
            d = {}
            d[fields[ind]] = possibleValue[ind]
        print postFilterString
        Entry.objects.filter()
        print PostFilter(d,queryset = Posting.objects.filter(visible=True)).order_by('-date')




# Create your tests here.
