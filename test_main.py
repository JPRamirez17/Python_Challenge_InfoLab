from main import random_multiply_challenge


def test_random_multiply_challenge(capsys):
    # Call the function
    random_multiply_challenge()

    # Capture printed output
    output = capsys.readouterr().out

    # Assert content of output is correct
    assert "Success!" in output
    lines = output.strip().split("\n")
    assert len(lines) > 2

    # Assert the last values of A and B multiply to 4
    last_result_line = lines[-1]
    a_value = int(last_result_line.split("A = ")[1].split(",")[0])
    b_value = int(last_result_line.split("B = ")[1])
    assert a_value * b_value == 4
