import pytest, io, sys, json

@pytest.mark.it('Sum all three input numbers and print on the console the result')
def test_add_variables(capsys):

    fake_input = [2,3,4] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
      captured = capsys.readouterr()
      assert captured.out == "9\n"

# print('file', __file__)
# print('abspath', os.path.abspath(__file__))
# print('dirname', os.path.dirname(os.path.abspath(__file__)))






# What is bc from bc.json?
''' breathecode '''
# exercise 15 has language ['us','us'] when I believe one should be 'es'