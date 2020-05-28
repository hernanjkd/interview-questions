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
