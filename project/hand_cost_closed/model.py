from hand_cost_closed.protocol import ClosedHandCostProtocol
from hand_cost_open.model import OpenHandCostModel
from hand_cost_open.protocol import OpenHandCostProtocol


class ClosedHandCostModel(OpenHandCostModel):
    input_size = ClosedHandCostProtocol.input_size
    output_size = OpenHandCostProtocol.output_size