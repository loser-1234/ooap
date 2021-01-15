from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
    @abstractmethod
    def undo(self) -> None:
        pass
        
class NoCommand(Command):
    def execute(self) -> None:
        pass
        
class LightOnCommand(Command):
    
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.on()
        
    def undo(self) -> None:
        self._light.off()
    
class LightOffCommand(Command):
    
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.off()
        
    def undo(self) -> None:
        self._light.on()

class Light: #получатель
    
    def on(self) -> None:
        print("Light is on")
        
    def off(self) -> None:
        print("Light is off")
        
class GarageDoorOpenCommand(Command):
    
    def __init__(self, garageDoor: GarageDoor) -> None:
        self._garageDoor = garageDoor

    def execute(self) -> None:
        self._garageDoor.up()
        
    def undo(self) -> None:
        self._garageDoor.down()
        
class GarageDoorCloseCommand(Command):
    
    def __init__(self, garageDoor: GarageDoor) -> None:
        self._garageDoor = garageDoor

    def execute(self) -> None:
        self._garageDoor.down()        

    def undo(self) -> None:
        self._garageDoor.up()
        
class GarageDoor: #получатель
    
    def up(self) -> None:
        print("Garage door is open")
        
    def down(self) -> None:
        print("Garage door is close")
class SimpleRemoteControl:
    
    def __init__(self):
        self.commands = list() #стек для отмены команд
    
    def execute(self, command):
        command.execute()
        self.commands.append(command) #добавляет всегда в конец уже существующего стека

    def undo(self):
        if (len(self.commands) != 0):
            self.commands.pop().undo() # функция pop() удаляет всегда с конца стека
        else:
            print('Нет команд для отмены')
            
if __name__ == "__main__":
    
    remoteControl = SimpleRemoteControl()
    light = Light()
    garageDoor = GarageDoor()
    remoteControl.execute(LightOffCommand(light))
    remoteControl.execute(GarageDoorCloseCommand(garageDoor))
    remoteControl.undo()
    remoteControl.undo()
    remoteControl.undo()
