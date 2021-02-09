from cv import CV


def test_cv():
    cv = CV()

    cv.show()

    cv.to_html("test.html")
