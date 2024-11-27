module dff (
    input wire clk,
    input wire reset,
    input wire d,
    output reg q = 0
);

always @(posedge clk or posedge reset) begin
    if (reset) begin
        q <= 0;  // Reset value
    end else begin
        q <= d;
    end
end
initial begin
    $dumpfile("dff.vcd");
    $dumpvars(0, dff);
end
endmodule
