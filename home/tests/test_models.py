import pytest

from home.models import FAQ


@pytest.mark.django_db
def test_faq_creation():
    faq_first = FAQ.objects.create(
        question="Why should I use a digital platform for fixed deposits instead of going to a bank?",
        answer="Digital platforms often offer higher interest rates, are more convenient for comparing different options, and have faster processing times. You can manage multiple fixed deposits from different banks in one place without having to visit each bank physically.")

    assert faq_first.question == "Why should I use a digital platform for fixed deposits instead of going to a bank?"
    assert faq_first.answer == "Digital platforms often offer higher interest rates, are more convenient for comparing different options, and have faster processing times. You can manage multiple fixed deposits from different banks in one place without having to visit each bank physically."

    faq_first = FAQ.objects.create(
        question="How can I be sure that my money is safe with your platform?",
        answer="Our platform works with banks that are insured by the Deposit Insurance and Credit Guarantee Corporation (DICGC) for amounts up to ₹5 lakh. We also carefully check the financial stability of our partners.")

    assert faq_first.question == "How can I be sure that my money is safe with your platform?"
    assert faq_first.answer == "Our platform works with banks that are insured by the Deposit Insurance and Credit Guarantee Corporation (DICGC) for amounts up to ₹5 lakh. We also carefully check the financial stability of our partners."

    assert FAQ.objects.count() == 2
