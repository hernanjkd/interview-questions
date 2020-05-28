# exercise 15 has language ['us','us'] when I believe one should be 'es'

# Using the print function

@pytest.mark.it('Use the print function')
def test_output():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find('print(') > 0

