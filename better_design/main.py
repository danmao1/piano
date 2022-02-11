from simple_controller import SimpleController
from piano_lights import LightsFromPiano

lights_controller = SimpleController(5, (244,0,0), (0,0,255))
piano_input = LightsFromPiano(50, (244,0,0),(0,0,255))
piano_input.run()

