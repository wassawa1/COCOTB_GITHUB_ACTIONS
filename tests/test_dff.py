# test_dff.py
import cocotb
from cocotb.triggers import RisingEdge, Timer

async def clock_gen(clock):
    while True:
        clock.value = 0
        await Timer(10, units="ns")
        clock.value = 1
        await Timer(10, units="ns")

@cocotb.test()
async def test_dff_simple(dut):
    """Test that DFF captures input correctly."""
    cocotb.start_soon(clock_gen(dut.clk))  # Start clock generator
    
    # Apply reset
    dut.reset.value = 1
    await Timer(10, units="ns")
    dut.reset.value = 0
    await Timer(10, units="ns")

    # Apply input and test DFF behavior
    dut.d.value = 1
    await RisingEdge(dut.clk)  # Wait for rising edge
    await Timer(1, units="ns")  # Wait for a short time to ensure the value is captured
    assert dut.q.value == 1, f"Output q was incorrect: {dut.q.value}"
