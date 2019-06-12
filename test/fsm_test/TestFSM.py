from unittest import TestCase

from fsm.example import FSM, OFF, ON


class FSMTest(TestCase):
    def setUp(self):
        self.fsm = FSM()

    def test_starts_with_lamp_off(self):
        self.assertEqual(self.fsm.state().description(), OFF)

    def test_flip_turns_off_lamp_on(self):
        self.fsm.flip()
        self.assertEqual(self.fsm.state().description(), ON)

    def test_flip_turns_on_lamp_off(self):
        self.fsm.flip()
        self.fsm.flip()
        self.assertEqual(self.fsm.state().description(), OFF)



