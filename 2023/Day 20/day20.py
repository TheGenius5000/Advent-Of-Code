from enum import Enum

class Pulse(Enum):
  LOW = 1
  HIGH = 2

class ModuleCollection():
  modules = {
    "broadcaster": None,
    "button": None
  }
  observed = {
    Pulse.LOW: 0,
    Pulse.HIGH: 0,
  }
  cycle = []

  def send(destination, pulse: Pulse, label):
    print(f"{destination} recieves {pulse}")
    ModuleCollection.cycle.append((destination, pulse))
    ModuleCollection.observed[pulse] += 1
    if isinstance(ModuleCollection.modules[destination], ConjunctionModule):
      ModuleCollection.modules[destination].applyPulse(pulse, label)
    else:
      ModuleCollection.modules[destination].applyPulse(pulse)
  
  def reverberate() -> bool:
    changes_needed = []
    for k, v in ModuleCollection.modules.items():
      if v.internal_pulse:
        changes_needed.append(k)
    for k in changes_needed:
      ModuleCollection.modules[k].sendPulses()
    return bool(changes_needed)
  
  def __repr__(self) -> str:
    return f"{self.modules}"
  
  def initialiseConjunctions():
    for k, v in ModuleCollection.modules.items():
      for destination in v.destinations:
        if isinstance(ModuleCollection.modules[destination], ConjunctionModule):
          ModuleCollection.modules[destination].pulse_history[k] = Pulse.LOW

  def intialiseMissingNodes():
    for k, v in ModuleCollection.modules.items():
      try:
        for destination in v.destinations:
          ModuleCollection.modules[destination]
      except:
        ModuleCollection.modules[destination] = Module([], destination, [])
        break

  def parseInput(lines):
    for label, destinations in lines:
      label = label.strip()
      destinations = [x.strip() for x in destinations.split(",")]
      if label == "broadcaster":
        ModuleCollection.modules["broadcaster"] = Module(destinations, label, [])
      elif label[0] == "%":
        ModuleCollection.modules[label[1:]] = FlipFlopModule(destinations, label[1:], [])
      elif label[0] == "&":
        ModuleCollection.modules[label[1:]] = ConjunctionModule(destinations, label[1:], [], {})

class Module():
  def __init__(self, destinations, label, internal_pulse=[]) -> None:
    self.destinations = destinations
    self.label = label
    self.internal_pulse = internal_pulse
  
  def sendOnePulse(self, pulse) -> None:
    for destination in self.destinations:
      ModuleCollection.send(destination, pulse, self.label)
  
  def sendPulses(self):
    while self.internal_pulse:
      pulse = self.internal_pulse.pop(0)
      self.sendOnePulse(pulse)
  
  def __repr__(self) -> str:
    return f"""Module "{self.label}" with destinations {self.destinations} and {self.internal_pulse}"""
  
  def applyPulse(self, pulse: Pulse):
    self.internal_pulse.append(pulse)

class FlipFlopModule(Module):
  switched_on = False
  
  def sendPulses(self):
    while self.internal_pulse:
      pulse = self.internal_pulse.pop(0)
      if pulse == Pulse.LOW:
        self.switched_on = not self.switched_on
        self.sendOnePulse(pulse)
  
  def sendOnePulse(self, pulse) -> None:
    if pulse == Pulse.LOW:
      if not self.switched_on:
        pulse = Pulse.LOW
        super().sendOnePulse(pulse)
      elif self.switched_on:
        pulse = Pulse.HIGH        
        super().sendOnePulse(pulse)
      else:
        raise NotImplementedError
  
  def __repr__(self) -> str:
    return f"{"ON:" if self.switched_on else "OFF:"} Flip-flop "+super().__repr__()
  
class ConjunctionModule(Module):
  def __init__(self, destinations, label, internal_pulse, pulse_history) -> None:
    self.pulse_history = pulse_history
    super().__init__(destinations, label, internal_pulse)
  
  def sendOnePulse(self, pulse) -> None:
    if Pulse.LOW in self.pulse_history.values():
      pulse = Pulse.HIGH
      super().sendOnePulse(pulse)
    elif Pulse.LOW not in self.pulse_history:
      pulse = Pulse.LOW
      super().sendOnePulse(pulse)
    else:
      raise NotImplementedError
  
  def __repr__(self) -> str:
    return "Conjunction "+super().__repr__()+f" with {self.pulse_history} memory"
  
  def applyPulse(self, pulse: Pulse, label):
    self.pulse_history[label] = pulse
    super().applyPulse(pulse)

class ButtonModule(Module):
  internal_pulse = None
  
  def press(self) -> None:
    super().sendOnePulse(Pulse.LOW)
  
  def __repr__(self) -> str:
    return "Button "+super().__repr__()
  


ModuleCollection.modules["button"] = ButtonModule(["broadcaster"], "button")

lines = [x.split("->") for x in open("D:/GitHub/Advent-Of-Code/2023/Day 20/input.txt").read().splitlines()]
print(lines)

ModuleCollection.parseInput(lines)
ModuleCollection.intialiseMissingNodes()
ModuleCollection.initialiseConjunctions()
observed_cycles = {}

for _ in range(1000):
  ModuleCollection.modules["button"].press()
  while(ModuleCollection.reverberate()):
    continue
  print()
  try:
    observed_cycles[tuple(ModuleCollection.cycle)] += 1
  except:
    observed_cycles[tuple(ModuleCollection.cycle)] = 1
  ModuleCollection.cycle = []

low_pulses = 0
high_pulses = 0
print(ModuleCollection.observed)
for k, v in observed_cycles.items():
  #print(f"{k}\n{v}")
  for _, pulse_type in k:
    if pulse_type == Pulse.LOW:
      low_pulses += v
    elif pulse_type == Pulse.HIGH:
      high_pulses += v
pass
print(low_pulses*high_pulses)
