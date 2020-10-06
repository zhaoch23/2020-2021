from main import Pen


def test_pen_init():
     p = Pen("blue")
     assert p.color == "blue"
     assert p.is_activated is False

     p = Pen("green")
     assert p.color == "green"
     assert p.is_activated is False


def test_pen_click_top_button():
     p = Pen("blue")
     assert p.is_activated is False

     # first click
     p.click_top_button()
     assert p.is_activated is True

     # second click
     p.click_top_button()
     assert p.is_activated is False

     # third click
     p.click_top_button()
     assert p.is_activated is True


def test_pen_draw_line_when_properly_activated():
     blue_pen = Pen("blue")

     blue_pen.click_top_button()
    
     line = blue_pen.draw_line(5)
     assert line == "----- (blue)"

     line = blue_pen.draw_line(2)
     assert line == "-- (blue)"

     line = blue_pen.draw_line(10)
     assert line == "---------- (blue)"


     green_pen = Pen("green")
     green_pen.click_top_button()
     line = green_pen.draw_line(5)
     assert line == "----- (green)"


def test_pen_draw_line_not_properly_activated():
     blue_pen = Pen("blue")

     # NOTICE THE PEN BUTTON WAS NOT CLICKED
     line = blue_pen.draw_line(5)
     assert line == ""   #nothing there

     line = blue_pen.draw_line(1000)
     assert line == ""  # nothing there
