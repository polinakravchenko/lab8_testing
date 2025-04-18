import re
import pytest

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email) and not email[0] == '+' and not email[1] == '@':
        return True 
    return False

class Params():
    not_valid_emails = ["testgmail", "test@gmail", "gmail@user", "1234..gmailcom", "usernumber@@com"]
    valid_emails = ["test@gmail.com", "user@gmail.com", "firstname.secondname@gmail.com", "123345@gmail.com", "firstname.secondname+1@mail.com"]

class TestClassesEmailsParam():
    @pytest.mark.parametrize("test_input", Params.not_valid_emails)
    def test_failed(self, test_input):
        assert is_valid_email(test_input) == False
    @pytest.mark.parametrize("test_input", Params.valid_emails)
    def test_valid(self, test_input):
        assert is_valid_email(test_input)

@pytest.mark.skip
class TestClassesEmails():
      
    def test_first_failed(self):
        assert is_valid_email("testgmail") == False
    def test_second_failed(self):
        assert is_valid_email("test@com") == False
    def test_third_failed(self):
        assert is_valid_email("gmail@user") == False
    def test_fourth_failed(self):
        assert is_valid_email("1234..gmailcom") == False
    def test_fifth_failed(self):
        assert is_valid_email("usernumber@@com") == False
    
    def test_first_valid(self):
        assert is_valid_email("test@gmail.com")
    def test_second_valid(self):
        assert is_valid_email("firstname.secondname@gmail.com")
    def test_third_valid(self):
        assert is_valid_email("12345@mail.com")
    def test_fourth_valid(self):
        assert is_valid_email("zaraz@gmail.com")
    def test_fifth_valid(self):
        assert is_valid_email("firstname.secondname+1@gmail.com")
