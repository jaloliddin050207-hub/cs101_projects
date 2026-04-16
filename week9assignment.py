from dataclasses import dataclass,field
@dataclass
class Tool:
    name: str
    rate : float
    hours:int
    def cost(self) ->float:
        return round(self.rate*self.hours,2)
@dataclass
class Workshop:
    name : str
    tools: list[Tool]=field(default_factory=list)
    total_cost:float=field(init=False)
    def __post_init__(self):
        self.refresh()
    
    def refresh(self):
        self.total_cost = round(sum(tool.cost() for tool in self.tools), 2)

    def add_tool(self,tool:Tool) :
        self.tools.append(tool)
        self.refresh()

    def use(self,tool_name:str, hrs:int) ->bool:

        for tool in self.tools:
            if tool.name == tool_name:
                if tool.hours >= hrs:
                    tool.hours -= hrs
                    self.refresh()
                    return True
                return False
        return False

    def extend(self, tool_name: str, hrs: int):
        for tool in self.tools:
            if tool.name == tool_name:
                tool.hours += hrs
                self.refresh()
                return

    def report(self) -> str:
        lines = [f"{self.name} Rentals:"]
        for tool in self.tools:
            lines.append(f"  {tool.name}: {tool.hours} hrs @ ${tool.rate}/hr")
        lines.append(f"Total cost: ${self.total_cost}")
        return "\n".join(lines)
    
t1 = Tool("Drill", 18.50, 12)
t2 = Tool("Saw", 25.99, 8)
t3 = Tool("Sander", 12.75, 20)

w = Workshop("BuildRight")
w.add_tool(t1)
w.add_tool(t2)
w.add_tool(t3)

print(w.total_cost)
print(w.use("Drill", 4))
print(w.use("Drill", 15))
w.extend("Sander", 10)
print(w.report())


    

