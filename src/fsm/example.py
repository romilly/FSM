from abc import ABC, abstractmethod

OFF = 'Off'
ON = 'On'


class State(ABC):
    @abstractmethod
    def flip(self):
        pass

    @abstractmethod
    def description(self):
        pass


class LampOn(State):
    def flip(self):
        print('lamp turned off')
        return lamp_off

    def description(self):
        return ON


class LampOff(State):
    def flip(self):
        print('Lamp turned on')
        return lamp_on

    def description(self):
        return OFF


class FSM:
    def __init__(self):
        self._state = lamp_off

    def state(self):
        return self._state

    def flip(self):
        self._state = self._state.flip()

# use variables to make sure we only have one of each state
lamp_on = LampOn()
lamp_off = LampOff()

