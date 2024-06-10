#Automating repetitive tests to save time and improve accuracy.

# Using pytest for automated testing
# Save this as test_vacuum_robot.py and run `pytest` in the terminal

import pytest
from robot.vacuum_robot import VacuumRobot

def test_auto_empty_dock_auto_empty_control():
    robot = VacuumRobot()
    robot.auto_empty_dock_auto_empty_control(True)
    assert robot.auto_empty_enabled

def test_auto_empty_dock_manual_trigger():
    robot = VacuumRobot()
    robot.auto_empty_dock_auto_empty_control(True)
    assert robot.auto_empty_dock_manual_trigger() == "Dustbin emptied"
