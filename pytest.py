# exercise 15 has language ['us','us'] when I believe one should be 'es'


# Using the print function
@pytest.mark.it('Use the print function')
def test_output():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find('print(') > 0



# Testing for a regex in the code
@pytest.mark.it('Create a var name color w the str val red')
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__))+ '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r'color(\s*)=(\s*)[\'"]red[\'"]')
        assert bool(regex.search(content)) == True



# Testing function or var declaration existance
@pytest.mark.it('You should create a var named myVariable')
def test_variable_exists(app):
    try:
        app.myVariable
    except AttributeError:
        raise AttributeError('The var "myVariable" should exist on app.py')

# app.py
def full_name(first, last):
    return first +' '+ last

# test.py
import pytest
@pytest.mark.it('Your func needs to return the full name')
def test_full_name():
    from app import full_name
    assert full_name('Bob', 'Dylan') == 'Bob Dylan'



# Testing function or variable value
@pytest.mark.it('You should create a var named myVariable w val "hello"')
def test_variable_exists(app):
    try:
        assert app.myVariable == 'hello'
    except AttributeError:
        raise AttributeError('The var "myVariable" should exist on app.py')


